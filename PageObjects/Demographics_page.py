import time
from selenium.webdriver.common.by import By


class Demographicsclass:

    def __init__(self, driver):
        self.driver = driver

    def patient_overall_detail(self):
        Patient_id = self.driver.find_element(By.XPATH,'//*[@id="ctl00_phFolderContent_ucPatient_lblPatientID"]').text
        Last_Name = self.driver.find_element(By.XPATH, '//*[@id="ctl00_phFolderContent_ucPatient_lblLastName"]').text
        First_Name = self.driver.find_element(By.XPATH,'//*[@id="ctl00_phFolderContent_ucPatient_lblFirstName"]').text
        Middle_Name = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[1]/td[8]').text
        AlternateId = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[2]/td[2]').text
        Language = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[3]/td[2]').text
        Smoke = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[3]/td[4]').text
        Race = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[3]/td[6]').text
        Ethnicity = self.driver.find_element(By.CSS_SELECTOR,'#Table3 > tbody > tr:nth-child(3) > td:nth-child(8)').text
        SSN = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[2]/td[8]').text
        Dob = self.driver.find_element(By.XPATH, '//*[@id="ctl00_phFolderContent_ucPatient_lblDOB"]').text
        Sex = self.driver.find_element(By.XPATH, '//*[@id="ctl00_phFolderContent_ucPatient_lblGender"]').text
        Type = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_ucPatient_lstAccountType option[selected]').text
        Status = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_ucPatient_lstAccountStatus option[selected]').text
        primary_care_Provider = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_ucPatient_tbxPrimaryProvider').text
        Referring_Provide = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_tbxReferringProvider').get_attribute('value')
        Api_Token = self.driver.find_element(By.ID, 'txtPatientApiToken').text
        Favourit_Pharmacy = self.driver.find_element(By.CSS_SELECTOR,'#ctl00_phFolderContent_ucPatient_ddlPharmacy option[selected]').text

        Table_dict = {'Patient_id': Patient_id, 'Last_Name': Last_Name, 'First_Name': First_Name, 'Middle_Name': Middle_Name, 'AlternateId': AlternateId, 'Language': Language, 'Smoke': Smoke,
                      'Race': Race,
                      'SSN': SSN, 'Date Of Birth': Dob, 'Gender': Sex, 'Account Type': Type, 'Status': Status, 'primary_care_Provider': primary_care_Provider, 'Referring_Provider': Referring_Provide,
                      'ApiToken': Api_Token, 'Favpurit Pharmacy': Favourit_Pharmacy}

    def patient_demographics(self):
        lastname1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_LastName').get_attribute('value')
        First_Name1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_FirstName').get_attribute('value')
        Middlename1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_MiddleName').get_attribute('value')
        SSN_D1 = self.driver.find_element(By.ID, 'ssnBox1').get_attribute('value')
        SSN_D2 = self.driver.find_element(By.ID, 'ssnBox2').get_attribute('value')
        SSN_D3 = self.driver.find_element(By.ID, 'ssnBox3').get_attribute('value')
        Dob_Month = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_DOB_Month').get_attribute('value')
        Dob_Day = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_DOB_Day').get_attribute('value')
        Dob_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_DOB_Year').get_attribute('value')
        demo_sex = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstGender option[selected]').text
        Weight = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Weight').get_attribute('value')
        Height = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Height').get_attribute('value')
        Suffix = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstNameSuffix option[selected]').text
        MeterialStatus = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstMaritalStatus option[selected]').text
        EmployementStatus = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstEmploymentStatus option[selected]').text
        Professional_Status = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ProfessionalTitle').get_attribute('value')
        Preferd_Language = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlLanguage option[selected]').text
        RaceDemo = self.driver.find_element(By.XPATH, '//*[@id="Table3"]/tbody/tr[3]/td[6]').text
        EthenticityDemo = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_lblEthnicity').text
        Sexual_Orientaial = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlSexualOrientation option[selected]').text
        Gender_Identity = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlGenderIdentity option[selected]').text
        Relegion = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlReligion option[selected]').text
        Motherlastname = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_MothersMaidenLastName').get_attribute('value')
        Motherfirstname = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_MothersMaidenFirstName').get_attribute('value')
        advance_directives = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlAdvancedDirectiveType option[selected]').text
        AdvanceDirectiveReview_Month = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_AdvanceDirectiveReviewedDate_Month').get_attribute('value')
        AdvanceDirectiveReview_Day = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_AdvanceDirectiveReviewedDate_Day').get_attribute('value')
        AdvanceDirectiveReview_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_AdvanceDirectiveReviewedDate_Year').get_attribute('value')

    def patient_contact_info(self):
        Adress1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_AddressLine1').get_attribute('value')
        Adress2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_AddressLine2').get_attribute('value')
        City = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_City').get_attribute('value')
        State = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstState option[selected]').text
        Zipcod = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Zip').get_attribute('value')
        Home_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_AreaCode').get_attribute('value')
        Home_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_Prefix').get_attribute('value')
        Home_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_Number').get_attribute('value')
        Work_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_WorkPhone_AreaCode').get_attribute('value')
        Work_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_WorkPhone_Prefix').get_attribute('value')
        Work_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_WorkPhone_Number').get_attribute('value')
        Work_PhoneEx = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_WorkPhone_Extension').get_attribute('value')
        Cell_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_CellPhone_AreaCode').get_attribute('value')
        Cell_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_CellPhone_Prefix').get_attribute('value')
        Cell_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_CellPhone_Number').get_attribute('value')
        Fax_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Fax_AreaCode').get_attribute('value')
        Fax_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Fax_Prefix').get_attribute('value')
        Fax_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Fax_Number').get_attribute('value')
        Phonepreffered = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstPreferredPhone option[selected]').text
        Email = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_Email').get_attribute('value')
        CommunicationPrefrence = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlPatientReminder option[selected]').text

    def patient_smoking_history(self):
        Smoking = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlSmokingStatus option[selected]').text
        SmokingFrequency = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlSmokingFrequency option[selected]').text
        Smoking_strt = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlSmokingStartDateType option[selected]').text
        Strt_year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_SmokingStartDate_Year').get_attribute('value')
        Smoking_End = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlSmokingEndDateType option[selected]').text
        End_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_SmokingEndDate_Year').get_attribute('value')
        OtherTobaco = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlTobaccoSNOMEDCode option[selected]').text
        Tobaco_strt = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlTobaccoStartDateType option[selected]').text
        TobacoStrt_year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_TobaccoStartDate_Year').get_attribute('value')
        Tobaco_End = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlTobaccoEndDateType option[selected]').text
        TobacoEnd_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_TobaccoEndDate_Year').get_attribute('value')
        TobacoFrequncy = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_PatientSmoking_ddlTobaccoFrequency option[selected]').text
        TobacoLastReview_Month = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_LastTobaccoUseReviewDate_Month').get_attribute('value')
        TobacoLastReview_Day = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_LastTobaccoUseReviewDate_Day').get_attribute('value')
        TobacoLastReview_Year = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_LastTobaccoUseReviewDate_Year').get_attribute('value')
        SmokingComments = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientSmoking_SmokingComments').get_attribute('value')
    def patient_employe_history(self):
        EmployerName = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerName').get_attribute('value')
        Employer_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerPhone_AreaCode').get_attribute('value')
        Employer_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerPhone_Prefix').get_attribute('value')
        Employer_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerPhone_Number').get_attribute('value')
        EmployerAdress1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerAddrLine1').get_attribute('value')
        EmployerAdress2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerAddrLine2').get_attribute('value')
        EmployerZip = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerZip').get_attribute('value')
        EmployerState = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstEmployerState option[selected]').text
        EmployerCity = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmployerCity').get_attribute('value')

    def patient_emergency_contact(self):
    ##=========================================Emergency======================================================
        EmergencyContactName = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactName').get_attribute('value')
        RelationtoPatient = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactRelation').get_attribute('value')
        EmergencyAdress1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactAddrLine1').get_attribute('value')
        EmergencyAdress2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactAddrLine2').get_attribute('value')
        Emergencystate = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstEmergencyContactState option[selected]').text
        EmergencyZip = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactZip').get_attribute('value')
        EmergecyCity = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactCity').get_attribute('value')
        EmergencyHome_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_AreaCode').get_attribute('value')
        EmergencyHome_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_Prefix').get_attribute('value')
        EmergencyHome_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactHomePhone_Number').get_attribute('value')
        EmergencyCell_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactCellPhone_AreaCode').get_attribute('value')
        EmergencyCell_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactCellPhone_Prefix').get_attribute('value')
        EmergencyCell_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactCellPhone_Number').get_attribute('value')
        EmergencyWork_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactWorkPhone_AreaCode').get_attribute('value')
        EmergencyWork_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactWorkPhone_Prefix').get_attribute('value')
        EmergencyWork_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_EmergencyContactWorkPhone_Number').get_attribute('value')
        FamilyId = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_FamilyID').get_attribute('value')
    ##====================================================NxtOF Kin===========================================
    def patient_nextofkin(self):
        NextofkinContactName = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinContactName').get_attribute('value')
        NextofkinRelationtoPatient = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstNextKinRelation option[selected]').text
        NextofkinAdress1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinContactAddrLine1').get_attribute('value')
        NextofkinAdress2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinContactAddrLine2').get_attribute('value')
        Nextofkinstate = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_lstEmergencyContactState option[selected]').text
        NextofkinZip = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinContactZip').get_attribute('value')
        NextofkinCity = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinContactCity').get_attribute('value')
        NextOfKinHome_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinHomePhone_AreaCode').get_attribute('value')
        NextOfKinHome_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinHomePhone_Prefix').get_attribute('value')
        NextOfKinHome_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinHomePhone_Number').get_attribute('value')
        NextOfKinCell_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinCellPhone_AreaCode').get_attribute('value')
        NextOfKinCell_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinCellPhone_Prefix').get_attribute('value')
        NextOfKinCell_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinCellPhone_Number').get_attribute('value')
        NextOfKinWork_Phone1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinWorkPhone_AreaCode').get_attribute('value')
        NextOfKinWork_Phone2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinWorkPhone_Prefix').get_attribute('value')
        NextOfKinWork_Phone3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_NextKinWorkPhone_Number').get_attribute('value')
    ##=========================================UserdefineFeilds======================================================
    def patient_user_defines(self):
        Field1 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined1').get_attribute('value')
        Field2 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined2').get_attribute('value')
        Field3 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined3').get_attribute('value')
        Field4 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined4').get_attribute('value')
        Field5 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined5').get_attribute('value')
        Field6 = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_UserDefined6').get_attribute('value')
        Notes = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_ucPatientNotes_txtAddNotes').get_attribute('value')
    ##=========================================RegistryInfo======================================================
    def patient_registory_info(self):
        OccupationCode = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_txtOccupationCode').get_attribute('value')
        OccupationDescription = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_txtOccupationDescription').get_attribute('value')
        IndustoryCode = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_txtIndustryCode').get_attribute('value')
        IndustoryOccupation = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_txtIndustryDescription').get_attribute('value')
    ##=========================================ImmunizitionRegistory======================================================
    def patient_imunization_history(self):
        State_Eligibility_Status = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlEligibilityStatus').get_attribute('text')
        Immunization_Funding_Source = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlImmunizationFunding').get_attribute('text')
        mmunization_Reminde = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlImmunizationReminder').get_attribute('text')
        Lock_Immunization_Data = self.driver.find_element(By.CSS_SELECTOR, '#ctl00_phFolderContent_ucPatient_ddlProtectData').get_attribute('text')

    # =========================================================Account Status=================================================================
    def patient_account_history(self):
        patientstatusstrt_Month = self.driver.find_element(By.ID, 'ctl00_phFolderContent_ucPatient_PatientStartDate_Month').get_attribute('value')
        patientstatusstrt_Day = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_PatientStartDate_Day').get_attribute('value')
        patientstatusstrt_Year = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_PatientStartDate_Year').get_attribute('value')
        patientstatusend_Month = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_PatientEndDate_Month').get_attribute('value')
        patientstatusend_Day = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_PatientEndDate_Day').get_attribute('value')
        patientstatusend_Year = self.driver.find_element(By.ID,'ctl00_phFolderContent_ucPatient_PatientEndDate_Year').get_attribute('value')

