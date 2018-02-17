"""Main."""
from time import sleep
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
        NoAlertPresentException,
        NoSuchElementException,
)
from ajilog import logger

from .settings import (
    EXECUTABLE_PATH, EXTENSTION_PATH, UID, EMAIL, PASSWORD
)


class RemotePatch(webdriver.Remote):
    """Patch for webdriver.Remote."""

    def __init__(self, *args, **kwargs):
        """Patch webdriver.Remote.execute."""
        self.reuse_session_id = kwargs.pop('reuse_session_id', None)
        super().__init__(*args, **kwargs)
        if self.reuse_session_id:
            self.session_id = self.reuse_session_id

    def execute(self, command, params=None):
        """Patch for `webdriver.Remote.execute`."""
        if command == 'newSession' and self.reuse_session_id:
            logger.debug(f'reuse session: {self.reuse_session_id}')
            return {'success': 0, 'value': None, 'sessionId': self.session_id}
        else:
            return super().execute(command, params)


class Browser:
    """Browser handler."""

    _chats = None
    _friends = None

    def __init__(self, command_executor=None, reuse_session_id=None):
        """Add LINE chrome extension."""
        chrome_options = Options()
        chrome_options.add_extension(EXTENSTION_PATH)
        if command_executor:
            self.driver = RemotePatch(
                command_executor=command_executor,
                desired_capabilities=chrome_options.to_capabilities(),
                reuse_session_id=reuse_session_id,
            )
        else:
            self.driver = webdriver.Chrome(
                executable_path=EXECUTABLE_PATH,
                chrome_options=chrome_options,
            )
        self.driver.get(f'chrome-extension://{UID}/index.html')
        sleep(0.5)
        # browser may confirm leaving of the current page
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    def login(self):
        """Login LINE."""
        sleep(0.5)
        # get email and password fields
        email_field = self.driver.find_element_by_id('line_login_email')
        pass_field = self.driver.find_element_by_id('line_login_pwd')
        # clear fields
        email_field.clear()
        pass_field.clear()
        # send keys
        email_field.send_keys(EMAIL)
        pass_field.send_keys(PASSWORD)
        sleep(0.5)
        self.driver.find_element_by_id('login_btn').click()
        sleep(1.5)
        while True:
            try:
                verify_code = (
                    self.driver
                    .find_element_by_css_selector(
                        '#login_content div.mdCMN01Code')
                    .text
                )
            except NoSuchElementException:
                logger.debug('no verify code needed.')
                break
            if verify_code:
                logger.debug(f'input verify code: ({verify_code})')
            else:
                logger.info('Loggged in successfully!')
                break
            sleep(1)

    def logout(self):
        """Logout LINE."""
        self.driver.find_element_by_class_name('mdGHD01SettingBtn').click()
        sleep(0.3)
        self.driver.find_element_by_id('setting_logout').click()

    def send_msg(self, message):
        """Send message.

        options
        `message`: strings or text
        """
        chat_box = self.driver.find_element_by_id('_chat_room_input')
        chat_box.click()
        sleep(0.3)
        chat_box.send_keys(f'{message}{Keys.ENTER}')

    def select_friend(self, name_or_id):
        """Select friend.

        options
        `name_or_id`: LINE name of id
        """
        if not re.match(r'[0-9a-z]{33}', name_or_id):
            name_or_id = self.chats[name_or_id]
        (
            self.driver
            .find_element_by_css_selector(f'[data-chatid={name_or_id}]')
            .click()
        )

    @property
    def chats(self):
        """List all firends."""
        if not self._chats:
            (
                self.driver
                .find_element_by_css_selector('li[data-type=chats_list')
                .click()
            )
            es = (
                self.driver
                .find_elements_by_css_selector('#_chat_list_scroll li')
            )
            self._chats = {
                e.get_attribute('title'):
                e.find_element_by_tag_name('div').get_attribute('data-chatid')
                for e in es
            }
        return self._chats

    @property
    def friends(self):
        """Firends."""
        if not self._friends:
            (
                self.driver
                .find_element_by_css_selector('li[data-type=friends_list')
                .click()
            )
            es = (
                self.driver
                .find_elements_by_css_selector('#contact_wrap_friends ul li')
            )
            self._friends = {
                e.get_attribute('title'):
                e.get_attribute('data-mid')
                for e in es
            }
        return self._friends
