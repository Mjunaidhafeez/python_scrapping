import configparser
config=configparser.RawConfigParser()
config.read('H:\Office_Allay\Configuration\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicaationURL():
        url=config.get('CommonInfo','baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('CommonInfo','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('CommonInfo','password')
        return password

    @staticmethod
    def getAccountNo():
        account = config.get('CommonInfo', 'account')
        return account

    # WebDriverWait(self.Driver, 60).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".x-body .x-window .x-window-header .x-box-inner .x-box-target .x-tool.x-tool-pressed")))
    # self.Driver.execute_script("arguments[0].click();", WebDriverWait(self.Driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x-body .x-window .x-window-header .x-box-inner .x-box-target .x-tool.x-tool-pressed"))))

    # WebDriverWait(self.Driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".x-body .x-window .x-window-header .x-box-inner .x-box-target .x-tool.x-tool-pressed"))).click()
    # click=self.Driver.find_element(By.CSS_SELECTOR,'.x-body .x-window .x-window-header .x-box-inner .x-box-target .x-tool.x-tool-pressed')
    # self.execute_script("arguments[0].click();", click)

 #         WebDriverWait(self.Driver, self.delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x-body .x-window .x-window-header .x-tool'))).click()
            #         # btnclose2 = self.Driver.find_element(By.CSS_SELECTOR,'.x-body .x-window .x-window-header .x-tool')
            #
            #         # (// span[contains(text(),’odamax’)])[1]
            # # btnclose3 = self.Driver.find_element(By.ID, 'closebutton-1274-btnInnerEl').click()