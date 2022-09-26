import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import loginpage
from PageObjects.PatientChartPage import PatientChartClass
from PageObjects.PatienDocumenttDownloadPage import PatientDocumentdownloadclass
from PageObjects.PatientChartDownload import PatientChartdownloadclass
from PageObjects.PatientChartSecurityPage import PatientchartSecurityclass
from Utitilities.readProperties import ReadConfig
from PageObjects.EncounterCsvPage import EncountersClass
from Utitilities import XLUtils
import os
from os import path
import shutil
service_obj=Service('C:\\Users\mkhawer\PycharmProjects\Office_Allay\Driver\chromedriver.exe')
driver=webdriver.Chrome(service=service_obj)
baseURL = ReadConfig.getApplicaationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()
Path = "C:\\Users\mkhawer\PycharmProjects\Office_Allay\ExternalData\Patient_list_14Sep2022.xlsx"
driver.implicitly_wait(2)
src = 'C:\\Users\mkhawer\Downloads'
docs=PatientDocumentdownloadclass(driver)
chart=PatientChartdownloadclass(driver)
ptc=PatientChartClass(driver)
enc=EncountersClass(driver)

def loginpage_test():
    driver.get(baseURL)
    lp=loginpage(driver)
    lp.clickbtn()
    lp.setUserName(username)
    lp.setPassword(password)
    lp.loginclick()
    driver.maximize_window()
    lp.clickbtnehr()
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
    rows_sheet = XLUtils.getRowCount(Path, 'Sheet3')
    print("Number of rows in an Excel:", rows_sheet)
    for r in range(3967,4210):
        loop_time = time.time()  # time to strt loop
        patientid = XLUtils.readData(Path, 'Sheet3', r, 1)
        ptc.setpatientid(patientid)
        ptc.clickbtnsearch()
        rowsize = ptc.sizeofpatientlist()
        if rowsize == 2:
            print('============================= ' + str(r) + ' =============================')
            print(patientid)
            ptc.clickpatientchrttr()
            docs.clickbtnbtnothers()
            docs.clicklnkchartdownload()
            rows_chart=chart.number_of_rows()
            if rows_chart >= 2:
                enc.Patient_Encounters()
                chart.clickslcall()
                chart.clicklnkdownload()
                clinicksecurity()
                time.sleep(5)
                new_dir = ('D:/Encounters/' + str(patientid))
                print(new_dir)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                    dst=str(new_dir)
                    files = [i for i in os.listdir(src)]
                    for f in files:
                        shutil.move(path.join(src,f),dst)
                timetaken = round(time.time() - loop_time)  # time taken to complete a loop
                print('Time taken to complete this patient=' + str(timetaken) + 's')
                ptc.clickbtnchart()
                ptc.clickdrppatientid('PatientID')
                ptc.clickdrpsearchby('1')
            else:
                with open('H:\\Office_Allay\\Incomplete_Record_csv\\NoEncounters.csv', 'a') as f:
                    f.write(str(patientid) + "\n")
                    f.close()
                ptc.clickbtnchart()
                ptc.clickdrppatientid('PatientID')
                ptc.clickdrpsearchby('1')
        else:
            print('============================= ' + str(r) + ' =============================')
            print('This patient data not exist..' + str(patientid))
            with open('H:\\Office_Allay\\No_Record_csv\\No_Record.csv', 'a') as f:
                f.write(str(patientid) + "\n")
                f.close()
            ptc.cleartxtpatientid()


loginpage_test()
patientchartpage()
