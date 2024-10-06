from selenium import webdriver
from PageObject.LoginPage import Login



class Test_001_loginpage:
    baseurl="https://opensource-demo.orangehrmlive.com/auth/login"
    username="Admin"
    password = "admin123"

    def test_homepage(self,setup):
        self.driver,self.wait=setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        act_title=self.driver.title

        if act_title=="OrangeHRM":
            assert True
        else:
            assert False
        self.driver.close()

    def test_login(self,setup):
        self.driver, self.wait = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver,self.wait)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
        else:
            assert False
        self.driver.close()




