from selenium.webdriver.common.by import By

class P_profile:

    def __init__(self, driver):
        self.driver = driver

    profile_header = (By.XPATH, "//div[@class='orangehrm-edit-employee-imagesection']//h6")

    profile_input_firstName = (By.XPATH, "//*[@class='oxd-input oxd-input--active orangehrm-firstname']")

    profile_input_driverNum = (By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input")

    profile_button_save1 = (By.XPATH, "(//button[@type='submit'])[1]")

    def profile_header_locator(self):
        return self.driver.find_element(*self.profile_header)
    
    def profile_input_firstName_locator(self):
        return self.driver.find_element(*self.profile_input_firstName)
    
    def profile_input_driverNum_locator(self):
        return self.driver.find_element(*self.profile_input_driverNum)
    
    def profile_button_save1_locator(self):
        return self.driver.find_element(*self.profile_button_save1)