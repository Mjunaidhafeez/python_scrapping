from selenium.webdriver.common.by import By
import pandas as pd
import  csv
class EncountersClass():

    def __init__(self, driver):
        self.driver=driver
        self.patientID_id = 'ctl00_phFolderContent_myPatientHeader_lblPatientID'
    def Patient_Encounters(self):
        try:
            patientID = self.driver.find_element(By.ID, self.patientID_id).text
            rowcount = self.driver.find_elements(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr')
            rowsize = len(rowcount)
            strsize = str(rowsize)
            size = int(strsize)
            for i in range(2, rowsize + 1):
                if i <= size:
                    encounterid=self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(2)').text
                    Encounter_Date_Type = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(3)').text
                    chiefcomplaint = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td.wrap').text
                    location = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(5)').text
                    provider = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(6)').text
                    typevisit=self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7)').text
                    status = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdEncounters > tbody > tr:nth-child('+ str(i) +') > td:nth-child(8)').text

                    Table_dict = {'Patient Id': patientID,'Encounter Id':encounterid, 'EncounterDate': Encounter_Date_Type,'Chiefcomplaint': chiefcomplaint,'Location':location,'Provider': provider,'Type of Visit':typevisit,'Status':status}
                    i += 1
                    df = pd.DataFrame((Table_dict), index=[0])
                    f=df.to_csv('Encounters2.csv', mode='a', index=False, header=False)
        except:
            ('Error')