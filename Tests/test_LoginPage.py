import time
import allure

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from selenium.webdriver.chrome.webdriver import WebDriver

class Test_Home(BaseTest):
    @allure.description("login to the doing erp portal")
    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        WebDriver.maximize_window(self.driver)
        time.sleep(5)
        print("Selected Environment URL : " + TestData.BASE_URL)
        print("Logged in User Name : " + TestData.USER_NAME)

