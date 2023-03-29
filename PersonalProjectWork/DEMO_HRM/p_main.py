from selenium.webdriver.common.by import By

class P_main:

    def __init__(self, driver):
        self.driver = driver

    main_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    employeeList_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

    PIM_sidebar = (By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[2]/a")

    button_add = (By.XPATH, "//button[@type='button' and text()=' Add ']")

    button_delete_confirm = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")

    def PIM_sidebar_locator(self):
        return self.driver.find_element(*self.PIM_sidebar)

    def button_add_locator(self):
        return self.driver.find_element(*self.button_add)
    
    def created_employee_inList_locator(self, firstname, middlename):
        return self.driver.find_element(By.XPATH, "//div[contains(text(), '"+firstname+" "+middlename+"')]")
    
    def updated_employee_inList_locator(self, firstname, middlename, changedfirstname):
        return self.driver.find_element(By.XPATH, "//div[contains(text(), '"+firstname+changedfirstname+" "+middlename+"')]")
    
    def employee_delete_icon_locator(self, firstname, middlename, changedfirstname):
        return self.driver.find_element(By.XPATH, "//div//div[contains(text(), '"+firstname+changedfirstname+" "+middlename+"')]//following::i[1]")
    
    def button_delete_confirm_locator(self):
        return self.driver.find_element(*self.button_delete_confirm)