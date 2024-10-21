from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login:

    username_text_name="username"
    password_text_name="password"
    login_button_Xpath="//button[normalize-space()='Login']"

    def __init__(self,driver,wait):
        self.driver=driver
        self.wait = wait

    def logo(self):
        a=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='company-branding']"))).is_displayed()



    def SetUsername(self,username):
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.username_text_name))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.username_text_name))).clear()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.username_text_name))).send_keys(username)


    def SetPassword(self,password):
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.password_text_name))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.password_text_name))).clear()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.password_text_name))).send_keys(password)

    def ClickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.login_button_Xpath))).click()

