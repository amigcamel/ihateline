"""Main."""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .settings import (
    EXECUTABLE_PATH, EXTENSTION_PATH, UID, EMAIL, PASSWORD
)


class Browser:
    """Browser handler."""

    _chats = []

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

    def logout(self):
        """Logout LINE."""
        self.driver.find_element_by_class_name('mdGHD01SettingBtn').click()
        sleep(0.3)
        self.driver.find_element_by_id('setting_logout').click()

    def send_msg(self):
        """Send message."""

    def select_friend(self):
        """Select friend."""

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
