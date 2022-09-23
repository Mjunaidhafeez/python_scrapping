import time
from selenium import webdriver
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.EncountersCountPage import EncountersCountClass
from Utitilities.readProperties import ReadConfig
from Utitilities import XLUtils
import os
from os import path
import shutil
driver=webdriver.Chrome(executable_path='D:\\NewEthizoProject\Driver\Chrome\chromedriver.exe')
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
Path = "D:\\NewEthizoProject\ExternalData\ListofPatientIds.xlsx"

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
    ptc=PatientChartClass(driver)
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows = XLUtils.getRowCount(Path, 'Sheet1')
    print("Number of rows in an Excel:", rows)
    for r in range(1, rows + 1):
        print(r)
        patientid = XLUtils.readData(Path, 'Sheet1', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize=ptc.sizeofpatientlist()
        if rowsize==2:
            ptc.clickpatientchrttr()
            encounters=EncountersCountClass(driver)
            encounters.Patient_Encounters()
            ptc.clickbtnchart()
            ptc.clickdrppatientid('PatientID')
            ptc.clickdrpsearchby('1')
        else:
            ptc.cleartxtpatientid()


loginpage_test()
patientchartpage()

