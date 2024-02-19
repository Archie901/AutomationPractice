from selenium.webdriver.common.by import By

class P_addEmployee:

    def __init__(self, driver):
        self.driver = driver

    addEmployee_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"

    input_firstName = (By.XPATH, "//*[@class='oxd-input oxd-input--active orangehrm-firstname']")

    input_middleName = (By.XPATH, "//*[@class='oxd-input oxd-input--active orangehrm-middlename']")

    input_lastName = (By.XPATH, "//*[@class='oxd-input oxd-input--active orangehrm-lastname']")

    button_save = (By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    def input_firstName_locator(self):
        return self.driver.find_element(*self.input_firstName)
    
    def input_middleName_locator(self):
        return self.driver.find_element(*self.input_middleName)
    
    def input_lastName_locator(self):
        return self.driver.find_element(*self.input_lastName)
    
    def button_save_locator(self):
        return self.driver.find_element(*self.button_save)