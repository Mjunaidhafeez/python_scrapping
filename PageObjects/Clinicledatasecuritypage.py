import time

from selenium.webdriver.common.by import By
class ClinicleSecurityclass:

    txtpassword_id='dlgPW'
    txtconfimpassword_id='dlgPWConfirm'
    btn_ok_id='ok'
    def __init__(self,driver):
        self.driver=driver

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.txtpassword_id).clear()
        self.driver.find_element(By.ID,self.txtpassword_id).send_keys(password)

    def setconfirmPassword(self,confirmpassword):
        self.driver.find_element(By.ID, self.txtconfimpassword_id).clear()
        self.driver.find_element(By.ID,self.txtconfimpassword_id).send_keys(confirmpassword)
    def clickok(self):
        self.driver.find_element(By.ID,self.btn_ok_id).click()
        time.sleep(2)


