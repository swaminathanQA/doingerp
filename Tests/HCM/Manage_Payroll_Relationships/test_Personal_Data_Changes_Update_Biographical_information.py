import time
import allure


from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.WelcomePage import welcomePage
from Tests.test_base import BaseTest
from selenium.webdriver.chrome.webdriver import WebDriver
from resources.utilities.XLUtility import XLutilities


class Test_Home(BaseTest):

    def test_launch_url(self):
        xlurl = XLutilities.readDate(TestData.xlpath, "URL", TestData.xlrow, 2)
        self.driver.get(xlurl)
        time.sleep(10)
        WebDriver.maximize_window(self.driver)
        print("Selected Environment URL : " + xlurl)

    @allure.description("login to the doing erp portal")
    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        uname = XLutilities.readDate(TestData.xlpath, "URL", TestData.xlrow, 3)
        pword = XLutilities.readDate(TestData.xlpath, "URL", TestData.xlrow, 4)
        self.LoginPage.do_login(uname, pword)
        time.sleep(5)
        print("Logged in User Name : " + uname)
        try:
            self.welcomePage = welcomePage(self.driver)
            self.welcomePage.do_click(welcomePage.MENU_BAR)
            time.sleep(1)
            self.welcomePage.do_click(welcomePage.OPTION_HOME)
            time.sleep(5)
            print("Home menu option is clicked")
        except:
            print("Home menu option is not clicked")

    @allure.description("logput to the doing erp portal")
    def test_logout(self):
        self.welcomePage = welcomePage(self.driver)
        time.sleep(2)
        self.welcomePage.do_click(welcomePage.ACCOUNT_NAME)
        self.welcomePage.do_click(welcomePage.SIGN_OUT_LINK)

        uname = XLutilities.readDate(TestData.xlpath, "URL", TestData.xlrow, 3)
        xlurl = XLutilities.readDate(TestData.xlpath, "URL", TestData.xlrow, 2)
        print("Selected Environment URL : " + xlurl)
        print("Logged in User Name : " + uname)

    @allure.description("Clicking confirmation button")
    def test_logout_confirmation(self):
        self.welcomePage = welcomePage(self.driver)
        time.sleep(2)
        self.welcomePage.do_click(welcomePage.CONFIRM_BUTTON)
        if self.welcomePage.test_element_visibility(LoginPage.SIGNIN_BUTTON) == True:
            print("Successfully logout")
