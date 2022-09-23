from selenium.webdriver.common.by import By
class PatientClinicinfoClass:
    def __init__(self,driver):
        self.driver=driver

    btnothers_xpath = '//*[@id="subMenu"]/ul/li[2]/div/div[1]'
    lnkclinicinfo_id='exportClinicalInformation'
    btnexport_id ='btnExport'

    def clickbtnbtnothers(self):
        self.driver.find_element(By.XPATH, self.btnothers_xpath).click()
    def clicklnkclinicinfo(self):
        self.driver.find_element(By.ID, self.lnkclinicinfo_id).click()
    def clicktpatientexport(self):
        self.driver.find_element(By.ID, self.btnexport_id).click()













