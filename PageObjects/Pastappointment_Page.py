from selenium.webdriver.common.by import By
import pandas as pd
class PastAppointmentsclass():

    def __init__(self, driver):
        self.driver = driver
        self.clickpastbuttn_css = '#ctl00_phFolderContent_panelView_ctl02_tabs_nav > ul > li.unselected > a'
        self.patientID_id = 'ctl00_phFolderContent_myPatientHeader_lblPatientID'

    def PastpatientClickbutton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clickpastbuttn_css).click()

    def Patient_PastAppointments(self):

        patientID = self.driver.find_element(By.ID, self.patientID_id).text
        rowcount = self.driver.find_elements(By.CSS_SELECTOR, '#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr')
        rowsize = len(rowcount)
        strsize = str(rowsize)
        size = int(strsize)
        if size >= 2:
            for i in range(2,size+1):
                date = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1) > table > tbody > tr > td').text
                time = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str( i) + ') > td:nth-child(2) > table > tbody > tr > td').text
                length = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > table > tbody > tr > td').text
                staff_provider = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(4)> table > tbody > tr > td').text
                office = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5) > table > tbody > tr > td').text
                reasonforvisit = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(6) > table > tbody > tr > td').text
                status = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_panelView_ctl02_grdPastAppointment > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(7) > table > tbody > tr > td').text
                Table_dict = {'Patient_id': patientID, 'Date': date, 'Time': time, 'Length': length,
                              'Staff_provider': staff_provider, 'Office': office,
                              'Reason For Visit': reasonforvisit, 'Status': status}

                df = pd.DataFrame((Table_dict), index=[0])
                df.to_csv('H:\\Office_Allay\\All_CSV_Files\\Past_Patient_Appointment.csv', mode='a', index=False, header=False)
                i += 1
        else:
            with open('H:\\Office_Allay\\Incomplete_Record_csv\\NoPast_Appointment.csv', 'a') as f:
                f.write(str(patientID) + "\n")
                f.close()

