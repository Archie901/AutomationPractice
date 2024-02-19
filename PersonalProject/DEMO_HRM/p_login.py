from selenium.webdriver.common.by import By

class P_login:

    '''In page objects we may store locators and methods (actions to perform on the page)
    or just locators for the specific page'''

    def __init__(self, driver):
        self.driver = driver

    login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    login_field = (By.XPATH, "//input[@name='username']")

    password_field = (By.XPATH, "//input[@name='password']")

    def login_with_all_data_entered(self, login, password):
        self.driver.find_element(*self.login_field).clear()
        self.driver.find_element(*self.login_field).send_keys(login)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.password_field).submit()

    '''(*) is required to make arguments accept keywords, like By.ID, By.XPATH, etc.'''