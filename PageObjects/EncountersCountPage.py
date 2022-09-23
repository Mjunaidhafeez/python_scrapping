from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import DictWriter
import pandas as pd
import  csv
class EncountersCountClass():

    def __init__(self, driver):
        self.driver=driver
        self.patientID_id = 'ctl00_phFolderContent_myPatientHeader_lblPatientID'
    def Patient_Encounters(self):
        try:
            patientID = self.driver.find_element(By.ID, self.patientID_id).text
            rowcount = self.driver.find_elements(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl06_grdSection > tbody > tr')
            rowsize = len(rowcount)
            strsize = str(rowsize)
            size = int(strsize)
            if size>=2:
                Table_dict = {'Patient Id': patientID}
                df = pd.DataFrame((Table_dict), index=[0])
                f=df.to_csv('EncountersCountIds.csv', mode='a', index=False, header=False)
        except:
            ('Error')