from selenium.webdriver.common.by import By

class PageLogin:

    '''In page objects we may store locators and methods (actions to perform on the page)
    or just locators for the specific page'''

    def __init__(self, driver):
        self.driver = driver

    email_field = (By.XPATH, "//input[@id='userName']")

    password_field = (By.XPATH, "//input[@id='password']")

    login_button = (By.XPATH, "//button[@id='login']")

    def set_email_in_field(self, email):
        self.driver.find_element(*self.email_field).clear()
        self.driver.find_element(*self.email_field).send_keys(email)

    '''(*) is required to make arguments accept keywords, like By.ID, By.XPATH, etc.'''

    def set_password_in_field(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()