import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    web_driver = None

    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.set_headless = False
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        firefox_options = Options()
        firefox_options.headless = False
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield

    web_driver.close()
    web_driver.quit()
