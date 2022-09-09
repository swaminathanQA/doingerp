from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class WelcomePage(BasePage):

    MENU_BAR = (By.XPATH, "(//*[name()='path'][@class='svg-outline'])")
    OPTION_HOME = (By.XPATH, "(//span[normalize-space()='Home'])")
    SIGNIN_BUTTON = (By.XPATH, "(//button[normalize-space()='Sign In'])")

    def __int__(self, driver):
        super().__init__(driver)