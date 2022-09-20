from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class welcomePage(BasePage):

    MENU_BAR = (By.XPATH, "(//*[name()='path'][@class='svg-outline'])")
    OPTION_HOME = (By.XPATH, "(//span[normalize-space()='Home'])")
    SIGNIN_BUTTON = (By.XPATH, "(//button[normalize-space()='Sign In'])")
    ACCOUNT_NAME = (By.XPATH, "//img[@id='pt1:_UIScmil2u']")
    SIGN_OUT_LINK = (By.XPATH, "//a[@id='pt1:_UISlg1']")


    def __int__(self, driver):
        super().__init__(driver)