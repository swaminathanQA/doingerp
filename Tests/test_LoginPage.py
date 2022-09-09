import time

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from selenium.webdriver.chrome.webdriver import WebDriver

class Test_Home(BaseTest):

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        WebDriver.maximize_window(self.driver)
        time.sleep(2)
        print("Selected Environment URL : " + TestData.BASE_URL)
        print("Logged in User Name : " + TestData.USER_NAME)

