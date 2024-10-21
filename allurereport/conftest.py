from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver,10)
    return driver,wait
