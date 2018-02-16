"""Main."""
from time import sleep
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from ajilog import logger

from .settings import (
    EXECUTABLE_PATH, EXTENSTION_PATH, UID, EMAIL, PASSWORD
)


class Browser:
    """Browser handler."""

    _chats = None
    _friends = None

    def __init__(self):
        """Add LINE chrome extension."""
        chrome_options = Options()
        chrome_options.add_extension(EXTENSTION_PATH)
        self.driver = webdriver.Chrome(
            executable_path=EXECUTABLE_PATH,
            chrome_options=chrome_options,
        )
        self.driver.get(f'chrome-extension://{UID}/index.html')

    def login(self):
        """Login LINE."""
        sleep(0.5)
        self.driver.find_element_by_id('line_login_email').send_keys(EMAIL)
        self.driver.find_element_by_id('line_login_pwd').send_keys(PASSWORD)
        sleep(0.5)
        self.driver.find_element_by_id('login_btn').click()
        sleep(1.5)
        while True:
            verify_code = (
                self.driver
                .find_element_by_css_selector('#login_content div.mdCMN01Code')
                .text
            )
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
