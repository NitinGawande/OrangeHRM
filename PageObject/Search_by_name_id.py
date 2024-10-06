from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Search_name_id:

    lnkpim_xpath="//span[normalize-space()='PIM']"
    employeename_text_xpath="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    employeeid_text_xpath="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    search_button_xpath="//button[normalize-space()='Search']"
    names_results_namo="//div[@role='table']//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']//div[3]"
    ids_results_namo = "//div[@role='table']//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']//div[2]"

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def clickpim(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.lnkpim_xpath))).click()

    def search_by_name(self,name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeename_text_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeename_text_xpath))).clear()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeename_text_xpath))).send_keys(name)

    def search_by_id(self,id):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeeid_text_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeeid_text_xpath))).clear()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employeeid_text_xpath))).send_keys(id)

    def ClickSearch(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.search_button_xpath))).click()

    def nameofemp(self,name):
        names=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.names_results_namo)))
        flag=False
        for nameo in names:
            if nameo.text==name:
                flag=True
                break
        return flag
