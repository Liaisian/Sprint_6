import pytest
from selenium import webdriver
from url import URL_MAIN

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920,1080')
    driver.get(URL_MAIN)
    yield driver
    driver.quit()






