import time
import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from PageObject.Search_by_name_id import Search_name_id

try:

    class Test_002_Search_By_Name:
        baseurl="https://opensource-demo.orangehrmlive.com/auth/login"
        username="Admin"
        password = "admin123"
        id="testuser1"
        # name="Harish Naidu"

        #
        # def test_searchbyname(self,setup):
        #
        #     self.driver, self.wait = setup
        #     self.driver.maximize_window()
        #     self.driver.get(self.baseurl)
        #     self.lp = Login(self.driver, self.wait)
        #     self.lp.SetUsername(self.username)
        #     self.lp.SetPassword(self.password)
        #     self.lp.ClickLogin()
        #     self.searchid=Search_name_id(self.driver,self.wait)
        #     self.searchid.clickpim()
        #     self.searchid.search_by_name("Dan Brent Mitchell")
        #     self.searchid.ClickSearch()
        #     status=self.searchid.nameofemp("Dan Brent Mitchell")
        #     assert True == status
        #     self.driver.close()
        #
        #




        # @pytest.mark.sanity
        def test_searchbyid(self,setup):
            self.driver,self.wait=setup
            self.driver.maximize_window()
            self.driver.get(self.baseurl)

            self.lp = Login(self.driver, self.wait)
            self.lp.SetUsername(self.username)
            self.lp.SetPassword(self.password)
            self.lp.ClickLogin()
            self.searchid=Search_name_id(self.driver,self.wait)
            self.searchid.clickpim()
            self.searchid.ClickSearch()
            id_status=self.searchid.idofemp('1243')
            assert True==id_status
            self.driver.close()



except Exception as e:
    print(e)


