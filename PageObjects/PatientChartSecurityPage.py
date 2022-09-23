import time

from selenium.webdriver.common.by import By
class PatientchartSecurityclass:

    txtpassword_xpath='//*[@id="ui-id-11"]/div[1]/input[1]'
    txtconfimpassword_xpath='//*[@id="ui-id-11"]/div[1]/input[2]'
    btn_ok_xpath='//*[@id="ui-id-11"]/div[2]/input[1]'
    def __init__(self,driver):
        self.driver=driver
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtpassword_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtpassword_xpath).send_keys(password)
    def setconfirmPassword(self,confirmpassword):
        self.driver.find_element(By.XPATH, self.txtconfimpassword_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtconfimpassword_xpath).send_keys(confirmpassword)
    def clickok(self):
        self.driver.find_element(By.XPATH,self.btn_ok_xpath).click()
        time.sleep(2)


