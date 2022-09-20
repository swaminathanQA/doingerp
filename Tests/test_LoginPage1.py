import time
import allure

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.WelcomePage import welcomePage
from Tests.test_base import BaseTest
from selenium.webdriver.chrome.webdriver import WebDriver

class Test_Home(BaseTest):


    def test_launch_url(self):
        self.driver.get(TestData.BASE_URL5)
        time.sleep(5)
        WebDriver.maximize_window(self.driver)
        print(strself.LoginPage.get_browser_title("Sign In"))

    @allure.description("login to the doing erp portal")
    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME5, TestData.PASSWORD5)
        time.sleep(10)
        print("Selected Environment URL : " + TestData.BASE_URL5)
        print("Logged in User Name : " + TestData.USER_NAME5)

    @allure.description("logput to the doing erp portal")
    def test_logout(self):
        self.welcomePage = welcomePage(self.driver)
        self.welcomePage.do_click(welcomePage.ACCOUNT_NAME)
        time.sleep(1)
        self.welcomePage.do_click(welcomePage.SIGN_OUT_LINK)
        print("Selected Environment URL : " + TestData.BASE_URL5)
        print("Logged in User Name : " + TestData.USER_NAME5)

