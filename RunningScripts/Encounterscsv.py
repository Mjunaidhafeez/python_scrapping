import time
from datetime import datetime

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatientChartDownload import PatientChartdownloadclass
from PageObjects.PatientChartSecurityPage import PatientchartSecurityclass
from PageObjects.EncounterCsvPage import EncountersClass
from Utitilities.readProperties import ReadConfig
from Utitilities import XLUtils
service_obj=Service('H:\Office_Allay\Driver\chromedriver.exe')
driver=webdriver.Chrome(service=service_obj)
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
Path = "H:\Office_Allay\ExternalData\Patient_list_14Sep2022.xlsx"
def loginpage_test():
    driver.get(baseURL)
    lp=loginpage(driver)
    lp.clickbtn()
    lp.setUserName(username)
    lp.setPassword(password)
    lp.loginclick()
    driver.maximize_window()
    lp.clickbtnehr()
def patienchartdownload():
    ptcd=PatientChartdownloadclass(driver)
    ptcd.clickbtnbtnothers()
    ptcd.clicklnkchartdownload()
    rows=ptcd.number_of_rows()
    if rows>=2:
        ptcd.clickslcall()
        ptcd.clicklnkdownload()
    else:
        ptcd.clickbtnchart()
def clinicksecurity():
    sec=PatientchartSecurityclass(driver)
    sec.setPassword('admin123')
    sec.setconfirmPassword('admin123')
    sec.clickok()
def patientchartpage():
    timestrt = datetime.now()
    print('Time Start={}'.format(timestrt))  # time to start
    ptc=PatientChartClass(driver)
    ptcd = PatientChartdownloadclass(driver)
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows = XLUtils.getRowCount(Path, 'Sheet3')
    print("Number of rows in an Excel:", rows)
    for r in range(1, rows + 1):
        loop_time = time.time()  # time to strt loop
        patientid = XLUtils.readData(Path, 'Sheet3', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize=ptc.sizeofpatientlist()
        if rowsize==2:
            ptc.clickpatientchrttr()
            ptcd.clickbtnbtnothers()
            ptcd.clicklnkchartdownload()
            rows = ptcd.number_of_rows()
            if rows >= 2:
                enc=EncountersClass(driver)
                enc.Patient_Encounters()
                ptc.clickbtnchart()
                ptc.clickdrppatientid('PatientID')
                ptc.clickdrpsearchby('1')
            else:
                ptc.clickbtnchart()
                ptc.clickdrppatientid('PatientID')
                ptc.clickdrpsearchby('1')
        else:
            ptc.cleartxtpatientid()


loginpage_test()
patientchartpage()

