from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.LoginPage import Login
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username="Admin"
    password = "admin123"

    @allure.feature('Checking logo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logo(self,setup):
        self.driver,self.wait=setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        a=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='company-branding']"))).is_displayed()
        if a==True:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_list(self):
        pytest.skip("Skipping test..Will try later")

    @allure.story('Valid credntials')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_employees(self,setup):
        self.driver, self.wait = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver,self.wait)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name='Testlogin',attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
