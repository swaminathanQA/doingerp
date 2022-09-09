import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
    if request.param == "firefox":
        firefox_options = Options()
        firefox_options.add_argument('--windows-size=1344, 840')
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH, options=firefox_options)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()
    web_driver.quit()