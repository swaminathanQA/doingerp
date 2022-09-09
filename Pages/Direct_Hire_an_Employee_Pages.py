from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData

class Direct_Hire_an_Employee_Pages(BasePage):
    MY_CLIENT_GROUPS = (By.LINK_TEXT, "My Client Groups")
    HIRE_AN_EMPLOYEE = (By.LINK_TEXT, "Hire an Employee")