import csv
import  pandas as pd
from selenium.webdriver.common.by import By
class InsuranceClass:

    def __init__(self, driver):
        self.driver = driver

    def patient_Insurance(self):
            # ==================================================InsuranceEligibility=============================================
            Patient_id = self.driver.find_element(By.XPATH, '//*[@id="ctl00_phFolderContent_ucPatient_lblPatientID"]').text
            LastChekedOn = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_txtProcessedDate').get_attribute('value')
            Elig_Check_Frequency = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlBECheckFreq option[selected]').text
            Health_Plan_Elig_Benefit_Co_ID = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_BatchEligibilityPayerID').get_attribute('value')
            Health_Plan_Elig_Benefit_Co_Name = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_BatchEligibilityPayerName').get_attribute('value')
            # ==================================================Primary Insurance:=================================================

            Insurance_Co = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceID').get_attribute('value')
            Insurance_Name = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceName').get_attribute('value')
            Caption = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstCapitation option[selected]').text
            Primary_Insured = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuredID').get_attribute('value')
            LastName = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuredLastName').get_attribute('value')
            First_Name = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuredFirstName').get_attribute('value')
            MI = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuredMiddleName').get_attribute('value')
            Patient_RelationshipToPrimaryIssued = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstRelationshipToInsuredID option[selected]').text
            SubscribeIDr = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceSubscriberID').get_attribute('value')
            GroupNo = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceGroupNo').get_attribute('value')
            PlanName = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsurancePlanName').get_attribute('value')
            Insured_Authorization = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstInsuredAuthorization option[selected]').text
            Deductible = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceDeductible').get_attribute('value')
            CoPayment = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_InsuranceVisitCopay').get_attribute('value')
            ReleaseOfInformation = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstSignatureOnFile option[selected]').text
            SignatureMonth = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SignatureOnFileDate_Month').get_attribute('value')
            SignatureDay = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SignatureOnFileDate_Day').get_attribute('value')
            SignatureYear = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SignatureOnFileDate_Year').get_attribute('value')
            ##=========================================Authorization by Insurance Co======================================================
            AuthorizationNo = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_PriorAuthorizationNumber2').get_attribute('value')
            VisitAuthorized = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_NumberOfVisitsAuthorized').get_attribute('value')
            VisitUsed = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_NumberOfVisitsUsed').get_attribute('value')
            NoOfVisits = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_NumberOfVisitsLeft').get_attribute('value')
            VisitLeft = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_NumberOfVisitsLeft').get_attribute('value')
            EffStrtMonth = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStartDate_Month').get_attribute('value')
            EffStrtDay = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStartDate_Day').get_attribute('value')
            EffStrtYear = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStartDate_Year').get_attribute('value')
            EffEndMonth = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStopDate_Month').get_attribute('value')
            EffEndDay = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStopDate_Day').get_attribute('value')
            EffEndYear = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Authorization_AuthorizedStopDate_Year').get_attribute('value')

            ##=========================================Secondary Insurance======================================================
            Insurance_Co_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceID').get_attribute('value')
            Insurance_Name_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceName').get_attribute('value')
            Secondory_Insured = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuredID').get_attribute('value')
            LastName_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuredLastName').get_attribute('value')
            First_Name_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuredFirstName').get_attribute('value')
            MI_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuredMiddleName').get_attribute('value')
            Patient_RelationshipToPrimaryIssued_s = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstRelationshipToSecondaryInsuredID option[selected]').text
            SubscribeIDr_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceSubscriberID').get_attribute('value')
            GroupNo_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceGroupNo').get_attribute('value')
            PlanName_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsurancePlanName').get_attribute('value')
            Insured_Authorization_s = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstSecondaryInsuredAuthorization option[selected]').text
            Deductible_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceDeductible').get_attribute('value')
            CoPayment_s = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondaryInsuranceVisitCopay').get_attribute('value')
            ReleaseOfInformation_s = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstSecondarySignatureOnFile option[selected]').text
            Signature_2nd_Month = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondarySignatureOnFileDate_Month').get_attribute('value')
            Signature_2nd_Day = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondarySignatureOnFileDate_Day').get_attribute('value')
            Signature_2nd_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_SecondarySignatureOnFileDate_Year').get_attribute('value')

            # ==============================================================Third========================================================================
            Insurance_Co_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceID').get_attribute('value')
            Insurance_Name_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceName').get_attribute('value')
            Third_Insured = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuredID').get_attribute('value')
            LastName_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuredLastName').get_attribute('value')
            First_Name_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuredFirstName').get_attribute('value')
            MI_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuredMiddleName').get_attribute('value')
            Patient_RelationshipToPrimaryIssued_T = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstRelationshipToThirdInsuredID option[selected]').text
            SubscribeIDr_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceSubscriberID').get_attribute('value')
            GroupNo_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceGroupNo').get_attribute('value')
            PlanName_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsurancePlanName').get_attribute('value')
            Deductible_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceDeductible').get_attribute('value')
            CoPayment_T = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ThirdInsuranceVisitCopay').get_attribute('value')
            Grauntor=self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_GuarantorID').get_attribute('value')
            Grauntor_lastnmae = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_GuarantorLastName').get_attribute('value')
            Grauntor_firstname = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_GuarantorFirstName').get_attribute('value')
            Grauntor_mi = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_GuarantorMiddleName').get_attribute('value')
            dob=self.driver.find_element(By.XPATH,'//*[@id="dependentTable"]/tbody/tr[2]/td[4]').text
            Table_dict = {'Patient ID': Patient_id, 'LastChekedOn': LastChekedOn, 'Elig_Check_Frequency': Elig_Check_Frequency, 'Health_Plan_Elig_Benefit_Co_ID': Health_Plan_Elig_Benefit_Co_ID,
                          'Health_Plan_Elig_Benefit_Co_Name': Health_Plan_Elig_Benefit_Co_Name, 'Insurance_Co': Insurance_Co, 'Insurance_Name': Insurance_Name, 'Caption': Caption,
                          'Primary_Insured': Primary_Insured,
                          'LastName': LastName, 'FirstName': First_Name, 'MI': MI,
                          'Patient_RelationshipToPrimaryIssued': Patient_RelationshipToPrimaryIssued, 'SubscribeIDr': SubscribeIDr, 'GroupNo': GroupNo, 'PlanName': PlanName,
                          'Insured_Authorization': Insured_Authorization, 'Deductible': Deductible, 'CoPayment': CoPayment, 'ReleaseOfInformation': ReleaseOfInformation,
                          'SignatureDate': SignatureMonth + SignatureDay + SignatureYear, 'AuthorizationNo': AuthorizationNo, 'VisitAuthorized': VisitAuthorized,
                          'VisitUsed': VisitUsed, 'NoOfVisits': NoOfVisits, 'VisitLeft': VisitLeft, 'EffStrtDate': EffStrtMonth + EffStrtDay + EffStrtYear,
                          'EffEndDate': EffEndMonth + EffEndDay + EffEndYear, 'Insurance_Co_s': Insurance_Co_s, 'Insurance_Name_s': Insurance_Name_s, 'Secondory_Insured': Secondory_Insured,
                          'LastName_s': LastName_s, 'First_Name_s': First_Name_s, 'MI_s': MI_s, 'Patient_RelationshipToPrimaryIssued_s': Patient_RelationshipToPrimaryIssued_s,
                          'SubscribeIDr_s': SubscribeIDr_s, 'GroupNo_s': GroupNo_s,'PlanName_s':PlanName_s, 'Insured_Authorization_s': Insured_Authorization_s,
                          'Deductible_s': Deductible_s, 'CoPayment_s': CoPayment_s, 'ReleaseOfInformation_s': ReleaseOfInformation_s,'Signature_date_secondory':Signature_2nd_Month+Signature_2nd_Day+Signature_2nd_Year,'Insurance_Co_T': Insurance_Co_T,
                          'Insurance_Name_T': Insurance_Name_T, 'Third_Insured': Third_Insured, 'LastName_T': LastName_T, 'First_Name_T': First_Name_T, 'MI_T': MI_T,
                          'Patient_RelationshipToPrimaryIssued_T': Patient_RelationshipToPrimaryIssued_T, 'SubscribeIDr_T': SubscribeIDr_T, 'GroupNo_T': GroupNo_T, 'PlanName_T': PlanName_T,
                          'Deductible_T': Deductible_T, 'CoPayment_T': CoPayment_T,'Grauntor':Grauntor,'Grauntor_lastnmae':Grauntor_lastnmae,'Grauntor_firstname':Grauntor_firstname,'Grauntor_mi':Grauntor_mi,'dob':dob}
            df = pd.DataFrame((Table_dict), index=[0])
            df.to_csv('H:\\Office_Allay\\All_CSV_Files\\PatientInsurrance.csv', mode='a', index=False, header=False)


