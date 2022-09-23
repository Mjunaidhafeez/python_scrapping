import time
from selenium.webdriver.common.by import By
class loginpage:
    btn_click_id='nav_Login'
    txtbox_username_name='Login1_UserName'
    txtbox_password_name='Login1_Password'
    btn_login_id='Login1_LoginButton'
    btnEhr_link = 'EHR'

    def __init__(self,driver):
        self.driver=driver

    def clickbtn(self):
        self.driver.find_element(By.ID, self.btn_click_id).click()

    def setUserName(self,username):
        self.driver.find_element(By.NAME, self.txtbox_username_name).clear()
        self.driver.find_element(By.NAME,self.txtbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.txtbox_password_name).clear()
        self.driver.find_element(By.NAME,self.txtbox_password_name).send_keys(password)
    def loginclick(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()
    def clickbtnehr(self):
        self.driver.find_element(By.LINK_TEXT, self.btnEhr_link).click()

