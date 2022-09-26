from selenium.webdriver.common.by import By
import pandas as pd
import  csv
class DocumentClass():

    def __init__(self, driver):
        self.driver=driver
        self.patientID_id = 'ctl00_phFolderContent_myPatientHeader_lblPatientID'
    def Patient_Document(self):
        try:
            patientID = self.driver.find_element(By.ID, self.patientID_id).text
            rowcount = self.driver.find_elements(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr')
            rowsize = len(rowcount)
            strsize = str(rowsize)
            size = int(strsize)
            for i in range(2, rowsize + 1):
                if i <= size:
                    documentid=self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(2)').text
                    document_Date = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(3)').text
                    documenttitle = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7)').text
                    documenttype = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(5)').text
                    mediatype = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(6)').text
                    dateadd=self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7)').text
                    status = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_grdDocuments > tbody > tr:nth-child('+ str(i) +') > td:nth-child(8)').text

                    Table_dict = {'Patient Id': patientID,'documentid':documentid, 'document_Date': document_Date,'documenttitle': documenttitle,'documenttype':documenttype,'mediatype': mediatype,'dateadd':dateadd,'Status':status}
                    i += 1
                    df = pd.DataFrame((Table_dict), index=[0])
                    f=df.to_csv('H:\\Office_Allay\\All_CSV_Files\\Patient_Document.csv', mode='a', index=False, header=False)
        except Exception as e:
            print(e)