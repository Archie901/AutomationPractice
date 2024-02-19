import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
from p_login import P_login
from p_main import P_main
from p_addEmployee import P_addEmployee
from p_profile import P_profile
from tt_testdata import TT_tesdata

@ddt
class Testing(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        #cls.driver.maximize_window()
        cls.driver.get(P_login.login_url)
    
    def test1_login_with_valid_creds(self):
        login_driver = P_login(self.driver)
        login_driver.login_with_all_data_entered\
            (TT_tesdata.login, TT_tesdata.password)
        time.sleep(2)
        main_driver = P_main(self.driver)
        PIM_clickable = main_driver.PIM_sidebar_locator()
        try:
            self.assertTrue(PIM_clickable.is_displayed)
            print("PIM clickable is found")
        except NoSuchElementException:
            print("PIM clickable is NOT found")

    @data(*TT_tesdata.get_dataCSV(TT_tesdata.data_file))
    @unpack
    def test2_creating(self, firstname, middlename, lastname, changedfirstname, drivernum):

        #Creating a new employee
        time.sleep(2)
        main_driver = P_main(self.driver)
        main_driver.PIM_sidebar_locator().click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((P_main.button_add)))
        main_driver.button_add_locator().click()
        time.sleep(2)
        addEmployee_driver = P_addEmployee(self.driver)
        addEmployee_driver.input_firstName_locator().send_keys(firstname)
        addEmployee_driver.input_middleName_locator().send_keys(middlename)
        addEmployee_driver.input_lastName_locator().send_keys(lastname)
        addEmployee_driver.button_save_locator().click()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)

        #Asserting that a new employee with correcet data is saved (in both profile and list)

        profile_driver = P_profile(self.driver)
        profile_text = profile_driver.profile_header_locator().text
        print("Employee first+last name: " + profile_text)
        self.assertEqual(firstname+" "+lastname, profile_text, "text is not equal")
        main_driver.PIM_sidebar_locator().click()
        time.sleep(4)
        created_emp_inList = main_driver.created_employee_inList_locator(firstname, middlename)
        print("Employee first+middle name in list: " + created_emp_inList.text)
        self.assertEqual(firstname+" "+middlename, created_emp_inList.text)
        time.sleep(2)

    @data(*TT_tesdata.get_dataCSV(TT_tesdata.data_file))
    @unpack
    def test3_opening_and_editing(self, firstname, middlename, lastname, changedfirstname, drivernum):

        #Opening created employee and editing information + adding new information

        main_driver = P_main(self.driver)
        created_emp_inList = main_driver.created_employee_inList_locator(firstname, middlename)
        created_emp_inList.click()
        time.sleep(2)
        profile_driver = P_profile(self.driver)
        input_firstName = profile_driver.profile_input_firstName_locator()
        input_firstName.send_keys(changedfirstname)
        input_drivernum = profile_driver.profile_input_driverNum_locator()
        input_drivernum.send_keys(drivernum)
        time.sleep(2)
        button_save1 = profile_driver.profile_button_save1_locator()
        button_save1.click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        profile_text = profile_driver.profile_header_locator().text
        print("Employee first+last name after changing: " + profile_text)
        self.assertEqual(firstname+changedfirstname+" "+lastname, profile_text)
        main_driver = P_main(self.driver)
        main_driver.PIM_sidebar_locator().click()
        updated_emp_inList = main_driver.updated_employee_inList_locator(firstname, middlename, changedfirstname)
        updated_emp_inList_text = updated_emp_inList.text
        print("Employee first+middle name in list after changing: " + updated_emp_inList_text)
        self.assertEqual(firstname+changedfirstname+" "+middlename, updated_emp_inList_text)

    @data(*TT_tesdata.get_dataCSV(TT_tesdata.data_file))
    @unpack
    def test4_deleting(self, firstname, middlename, lastname, changedfirstname, drivernum):

        #Deleting already saved/edited employees from the list

        main_driver = P_main(self.driver)
        main_driver.PIM_sidebar_locator().click()
        time.sleep(2)
        delete_icon = main_driver.employee_delete_icon_locator(firstname, middlename, changedfirstname)
        delete_icon.click()
        time.sleep(2)
        button_delete_confirm = main_driver.button_delete_confirm_locator()
        button_delete_confirm.click()
        wait = WebDriverWait(self.driver, 5)
        assert wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, "//div[contains(text(), '"+firstname+changedfirstname+" "+middlename+"')]")))
        time.sleep(3)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ =="__main__":
    unittest.main(verbosity=2)