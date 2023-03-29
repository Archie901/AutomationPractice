from selenium.webdriver.common.by import By

class PageProfile:

    def __init__(self, driver):
        self.driver = driver

    profile_logo = (By.XPATH, "//div[text()='Profile']")

    userName_value_span = (By.XPATH, "//label[@id='userName-value']")

    def profile_logo_fullLocator(self):
        return self.driver.find_element(*self.profile_logo)
    
    def userName_value_text(self):
        return self.driver.find_element(*self.userName_value_span).text