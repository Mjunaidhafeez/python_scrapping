from selenium.webdriver.common.by import By
import getpass
class PatientChartdownloadclass:
    def __init__(self,driver):
        self.driver=driver

    btnothers_xpath = '//*[@id="subMenu"]/ul/li[2]/div/div[1]'
    lnkchartdownload_id='chartDownload'
    lnkslcall_id='ctl00_phFolderContent_lnkSelectAll'
    lnkdownload_xpath='//*[@id="Table1"]/tbody/tr[1]/td[3]/div/ul/li[1]/a'
    rows_xpath='// *[ @ id = "ctl00_phFolderContent_grdEncounters"] / tbody / tr'

    def clickbtnbtnothers(self):
        self.driver.find_element(By.XPATH, self.btnothers_xpath).click()
    def clicklnkchartdownload(self):
        self.driver.find_element(By.ID, self.lnkchartdownload_id).click()
    def clickslcall(self):
        self.driver.find_element(By.ID,self.lnkslcall_id).click()
    def clicklnkdownload(self):
        self.driver.find_element(By.XPATH,self.lnkdownload_xpath).click()
    def number_of_rows(self):
        rows = self.driver.find_elements(By.XPATH, self.rows_xpath)
        rowsize = len(rows)
        return rowsize


