from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class PatientChartClass:
    def __init__(self,driver):
        self.driver=driver

    btnchart_xpath = '//*[@id="patient-charts_tab"]/span'
    drppatientid_xpath='//*[@id="ctl00_phFolderContent_ucSearch_lstSearchBy"]'
    drpsearchby_xpath ='//*[@id="ctl00_phFolderContent_ucSearch_lstSearchCondition"]'
    txtsearch_id='ctl00_phFolderContent_ucSearch_txtSearch'
    btnsearch_id='ctl00_phFolderContent_ucSearch_btnSearch'
    patientdatalist_xpath='/html/body/form/div[5]/div[2]/div[5]/div/div[3]/div[3]/div/table/tbody/tr'
    patientchartTr_xpath='/html/body/form/div[5]/div[2]/div[5]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[17]'
    patienteditdemo_xpath = '/html/body/form/div[5]/div[2]/div[5]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[15]'

    def clickbtnchart(self):
        self.driver.find_element(By.XPATH, self.btnchart_xpath).click()
    def clickdrppatientid(self,value):
        drppatientid=Select(self.driver.find_element(By.XPATH, self.drppatientid_xpath))
        drppatientid.select_by_value(value)
    def clickdrpsearchby(self,value):
        drpsearchby=Select(self.driver.find_element(By.XPATH, self.drpsearchby_xpath))
        drpsearchby.select_by_value(value)
    def setpatientid(self,patientid):
        self.driver.find_element(By.ID, self.txtsearch_id).clear()
        self.driver.find_element(By.ID, self.txtsearch_id).send_keys(patientid)
    def clickbtnsearch(self):
        self.driver.find_element(By.ID,self.btnsearch_id).click()
        time.sleep(2)
    def sizeofpatientlist(self):
        rows=self.driver.find_elements(By.XPATH,self.patientdatalist_xpath)
        rowsize=len(rows)
        return rowsize
    def clickpatientchrttr(self):
        self.driver.find_element(By.XPATH, self.patientchartTr_xpath).click()
    def clickpatienteditdemo(self):
        self.driver.find_element(By.XPATH, self.patienteditdemo_xpath).click()
    def cleartxtpatientid(self):
        self.driver.find_element(By.ID, self.txtsearch_id).clear()













