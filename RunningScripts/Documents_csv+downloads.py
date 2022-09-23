import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatienDocumenttDownloadPage import PatientDocumentdownloadclass
from PageObjects.DocumentCsvPage import DocumentClass
from PageObjects.PatientChartSecurityPage import PatientchartSecurityclass
from Utitilities.readProperties import ReadConfig
from Utitilities import XLUtils
import os
from os import path
import shutil
service_obj=Service('H:\Office_Allay\Driver\chromedriver.exe')
driver=webdriver.Chrome(service=service_obj)
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
Path = "H:\\Office_Allay\All_CSV_Files\Incomplete_ids_officeallay_Patients.xlsx"
driver.implicitly_wait(2)
src = 'C:\\Users\HP\Downloads'
ptcd=PatientDocumentdownloadclass(driver)
ptc=PatientChartClass(driver)
dcmcsv=DocumentClass(driver)
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
    ptc.clickbtnchart()
    ptc.clickdrppatientid('PatientID')
    ptc.clickdrpsearchby('1')
    rows = XLUtils.getRowCount(Path, 'Sheet1')
    print("Number of rows in an Excel:", rows)
    for r in range(1,100):
        loop_time = time.time()  # time to strt loop
        patientid = XLUtils.readData(Path, 'Sheet1', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize = ptc.sizeofpatientlist()
        if rowsize == 2:
            print('============================= ' + str(r) + ' =============================')
            print(patientid)
            ptc.clickpatientchrttr()
            ptcd.clickbtnbtnothers()
            ptcd.clicklnkchartdownload()
            rows = ptcd.number_of_rows()
            if rows >= 2:
                dcmcsv.Patient_Document()
                ptcd.clickslcall()
                ptcd.clicklnkdownload()
                clinicksecurity()
                time.sleep(4)
                new_dir = ('D:/Documents/' + str(patientid))
                print(new_dir)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                    dst=str(new_dir)
                    files = [i for i in os.listdir(src)]
                    for f in files:
                        shutil.move(path.join(src,f),dst)
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

                with open('H:\\Office_Allay\\All_CSV_Files\\NoDocuments.csv', 'a') as f:
                    f.write(str(patientid) + "\n")
                    f.close()
                ptc.clickbtnchart()
                ptc.clickdrppatientid('PatientID')
                ptc.clickdrpsearchby('1')
        else:
            print('============================= ' + str(r) + ' =============================')
            print('This patient data not exist..' + str(patientid))
            with open('H:\\Office_Allay\\All_CSV_Files\\NoRecords.csv', 'a') as f:
                f.write(str(patientid) + "\n")
                f.close()
            ptc.cleartxtpatientid()


loginpage_test()
patientchartpage()

