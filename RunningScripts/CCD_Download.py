import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatientClinicleInfPage import PatientClinicinfoClass
from PageObjects.Clinicledatasecuritypage import ClinicleSecurityclass
from Utitilities.readProperties import ReadConfig
from Utitilities import XLUtils

service_obj=Service('H:\Office_Allay\Driver\chromedriver.exe')
driver=webdriver.Chrome(service=service_obj)
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
path = "H:\Office_Allay\ExternalData\Incomplete_ids_officeallay_ccda.xlsx"

def loginpage_test():
    driver.get(baseURL)
    lp=loginpage(driver)
    lp.clickbtn()
    lp.setUserName(username)
    lp.setPassword(password)
    lp.loginclick()
    driver.maximize_window()
    lp.clickbtnehr()
def patientclinickinfo_test():
    ptci=PatientClinicinfoClass(driver)
    ptci.clickbtnbtnothers()
    ptci.clicklnkclinicinfo()
    ptci.clicktpatientexport()
def clinicksecurity_test():
    sec=ClinicleSecurityclass(driver)
    sec.setPassword('1234')
    sec.setconfirmPassword('1234')
    sec.clickok()
def patientchartpage_test():
    timestrt = datetime.now()
    print('Time Start={}'.format(timestrt))  # time to start
    ptc=PatientChartClass(driver)
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows = XLUtils.getRowCount(path, 'Sheet1')
    print("Number of rows in an Excel:", rows)
    for r in range(1,86):
        loop_time = time.time()  # time to strt loop
        patientid = XLUtils.readData(path, 'Sheet1', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize=ptc.sizeofpatientlist()
        if rowsize==2:
            print('============================= ' + str(r) + ' =============================')
            print(patientid)
            ptc.clickpatientchrttr()
            patientclinickinfo_test()
            clinicksecurity_test()
            ptc.clickbtnchart()
            ptc.clickdrppatientid('PatientID')
            ptc.clickdrpsearchby('1')
            timetaken = round(time.time() - loop_time)  # time taken to complete a loop
            print('Time taken to complete this patient=' + str(timetaken) + 's')
            if r % 100 == 0:
                print('==============' + 'Patient Completed = {}'.format(r) + '===========================')
                print('Time Start={}'.format(timestrt))  # time to start
                timeend = datetime.now()
                print('Time End={}'.format(timeend))  # end to start
                timetakentocomplete = timeend - timestrt
                print('Time Taken={}'.format(timetakentocomplete))
        else:
            print('============================= ' + str(r) + ' =============================')
            print('This patient data not exist..' + str(patientid))
            with open('H:\Office_Allay\All_CSV_Files\Incompleteids.csv', 'a') as f:
                f.write(str(patientid) + "\n")
                f.close()
            ptc.cleartxtpatientid()

loginpage_test()
patientchartpage_test()



