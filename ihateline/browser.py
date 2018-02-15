"""Main."""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .settings import (
    EXECUTABLE_PATH, EXTENSTION_PATH, UID, EMAIL, PASSWORD
)

class Browser:

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

    def send_msg(self):
        """Send message."""

    def select_friend(self):
        """Select friend."""

    @property
    def friends(self):
        """List all firends."""
