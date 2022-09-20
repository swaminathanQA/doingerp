import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData

class LoginPage(BasePage):

    EMAIL = (By.ID, "userid")
    PASSWORD = (By.ID, "password")
    SIGNIN_BUTTON = (By.XPATH, "(//button[normalize-space()='Sign In'])")

    def __int__(self, driver):
        super().__init__(driver)

    """This is used to login to application"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)