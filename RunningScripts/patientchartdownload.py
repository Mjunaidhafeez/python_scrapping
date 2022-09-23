import time
from selenium import webdriver

from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatientChartDownload import PatientChartdownloadclass
from PageObjects.PatientChartSecurityPage import PatientchartSecurityclass
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
src = 'C:\\Users\HP\Downloads'


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
    ptc=PatientChartClass(driver)
    ptcd = PatientChartdownloadclass(driver)
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows = XLUtils.getRowCount(Path, 'Sheet2')
    print("Number of rows in an Excel:", rows)
    for r in range(7, rows + 1):
        print(r)
        patientid = XLUtils.readData(Path, 'Sheet2', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize=ptc.sizeofpatientlist()
        if rowsize==2:
            ptc.clickpatientchrttr()
            ptcd.clickbtnbtnothers()
            ptcd.clicklnkchartdownload()
            rows = ptcd.number_of_rows()
            if rows >= 2:
                ptcd.clickslcall()
                ptcd.clicklnkdownload()
                clinicksecurity()
                time.sleep(30)
                new_dir = ('D:/Encounters2/' + str(patientid))
                print(new_dir)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                    dst=str(new_dir)
                    files = [i for i in os.listdir(src)]
                    for f in files:
                        shutil.move(path.join(src, f),dst)
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

