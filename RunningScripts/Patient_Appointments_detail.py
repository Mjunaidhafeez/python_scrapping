import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatienDocumenttDownloadPage import PatientDocumentdownloadclass
from PageObjects.PatientChartDownload import PatientChartdownloadclass
from PageObjects.Upcomingappointment_Page import UpcommingAppointmentsclass
from PageObjects.Pastappointment_Page import PastAppointmentsclass
from Utitilities.readProperties import ReadConfig
from PageObjects.EncounterCsvPage import EncountersClass
from Utitilities import XLUtils
service_obj=Service('H:\\Office_Allay\\Driver\\chromedriver.exe')
driver=webdriver.Chrome(service=service_obj)
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
Path = "H:\\Office_Allay\\ExternalData\\Patient_list_14Sep2022.xlsx"
driver.implicitly_wait(2)
docs=PatientDocumentdownloadclass(driver)
chart=PatientChartdownloadclass(driver)
ptc=PatientChartClass(driver)
enc=EncountersClass(driver)
upcommingappointment=UpcommingAppointmentsclass(driver)
pastappointment=PastAppointmentsclass(driver)

def loginpage_test():
    driver.get(baseURL)
    lp=loginpage(driver)
    lp.clickbtn()
    lp.setUserName(username)
    lp.setPassword(password)
    lp.loginclick()
    driver.maximize_window()
    lp.clickbtnehr()
def patientchartpage():
    timestrt = datetime.now()
    print('Time Start={}'.format(timestrt))  # time to start
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows_sheet = XLUtils.getRowCount(Path, 'Sheet3')
    print("Number of rows in an Excel:", rows_sheet)
    for r in range(1,4210):
        loop_time = time.time()  # time to strt loop
        patientid = XLUtils.readData(Path, 'Sheet3', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize = ptc.sizeofpatientlist()
        if rowsize == 2:
            print('============================= ' + str(r) + ' =============================')
            print(patientid)
            ptc.clickpatientchrttr()
            timetaken = round(time.time() - loop_time)  # time taken to complete a loop
            print('Time taken to complete this patient=' + str(timetaken) + 's')
            upcommingappointment.Patient_UpcommingAppointments()
            pastappointment.PastpatientClickbutton()
            pastappointment.Patient_PastAppointments()
            ptc.clickbtnchart()
            ptc.clickdrppatientid('PatientID')
            ptc.clickdrpsearchby('1')
        else:
            print('============================= ' + str(r) + ' =============================')
            print('This patient data not exist..' + str(patientid))
            with open('H:\\Office_Allay\\No_Record_csv\\No_Patient_Record.csv', 'a') as f:
                f.write(str(patientid) + "\n")
                f.close()
            ptc.cleartxtpatientid()

loginpage_test()
patientchartpage()
