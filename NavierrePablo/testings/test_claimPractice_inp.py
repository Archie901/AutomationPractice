import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import _mainus
import atestus as at
import pytest

@pytest.fixture(scope='session')
def setupTeardown():
    service = Service()
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})
    global driver
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Edge()
    #driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver, 10)
    yield
    driver.quit()

def test_initiation(setupTeardown):
    driver.maximize_window()
    driver.get(at.Requests.devstage_pablo_weburl + "/for-providers/claim")
    driver.implicitly_wait(3)
    busi_claim_button = driver.find_element(By.XPATH, f'{at.BusiMainPage.busi_claim_button}')
    wait.until(expected_conditions.visibility_of((busi_claim_button)))
    busi_claim_button.click()
    time.sleep(2)
    inpatient_button = driver.find_element(By.XPATH, f'{at.BusiMainPage.inpatient_button}')
    inpatient_button.click()
    time.sleep(1)

def test_select_lvl3_types(setupTeardown):
    random_lvl3_type1 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type2 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type3 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type4 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type5 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type6 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type7 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.lvl3_typesInp)}')
    random_lvl3_type1.click()
    random_lvl3_type2.click()
    random_lvl3_type3.click()
    random_lvl3_type4.click()
    random_lvl3_type5.click()
    random_lvl3_type6.click()
    random_lvl3_type7.click()
    time.sleep(3)
    #driver.save_screenshot('C:/Users/overk/Downloads/1_selected_lvl3_types.png')
    continue_button1 = driver.find_element(By.XPATH, f'{at.BusiMainPage.continue_button1}')
    continue_button1.click()
    time.sleep(2)
    continue_button2 = driver.find_element(By.XPATH, f'{at.BusiMainPage.continue_button2}')
    continue_button2.click()
    time.sleep(2)

def test_practice_search(setupTeardown):
    search_input = driver.find_element(By.XPATH, f'{at.BusiMainPage.search_input}')
    search_input.send_keys(at.Methods.randomizer(at.General.practice_search))
    time.sleep(2)
    random_prac = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.BusiMainPage.found_pracs)}')
    random_prac.click()
    time.sleep(2)
    #driver.save_screenshot('C:/Users/overk/Downloads/2_choose_your_practice.png')
    continue_button3 = driver.find_element(By.XPATH, f'{at.BusiMainPage.continue_button3}')
    continue_button3.click()
    time.sleep(4)

def test_confirm_identity(setupTeardown):
    prac_name_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_name_input}')
    prac_ein_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_ein_input}')
    prac_address_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_address_input}')
    prac_phone_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_phone_input}')
    prac_email_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_email_input}')
    prac_fax_input = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.prac_fax_input}')
    prac_ein_input.send_keys(at.Methods.randomizer(at.General.diff_values))
    prac_phone_input.send_keys(Keys.CONTROL, "a")
    prac_phone_input.send_keys(Keys.DELETE)
    prac_phone_input.send_keys(at.Methods.randomizer(at.General.usPhoneNums))
    prac_email_input.send_keys(at.Methods.randomizer(at.General.practiceEmails))
    prac_fax_input.send_keys(at.Methods.randomizer(at.General.usPhoneNums))
    time.sleep(2)
    print("Confirm Identity, prac name retrieved: --", prac_name_input.get_attribute("value"))
    print("Confirm Identity, prac ein entered: --", prac_ein_input.get_attribute("value"))
    print("Confirm Identity, prac address retrieved: --", prac_address_input.get_attribute("value"))
    print("Confirm Identity, prac phone entered: --", prac_phone_input.get_attribute("value"))
    print("Confirm Identity, prac email entered: --", prac_email_input.get_attribute("value"))
    print("Confirm Identity, prac fax entered: --", prac_fax_input.get_attribute("value"))
    #driver.save_screenshot('C:/Users/overk/Downloads/3_confirm_identity_data.png')
    next_button1 = driver.find_element(By.XPATH, f'{at.ConfirmIdentityPage.next_button1}')
    next_button1.click()
    time.sleep(2)

def test_select_services(setupTeardown):
    random_serv1 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.SelectServicesPage.services_list)}')
    random_serv2 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.SelectServicesPage.services_list)}')
    random_serv3 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.SelectServicesPage.services_list)}')
    random_serv4 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.SelectServicesPage.services_list)}')
    random_serv5 = driver.find_element(By.XPATH, f'{at.Methods.randomizer(at.SelectServicesPage.services_list)}')
    random_serv1.click()
    random_serv2.click()
    random_serv3.click()
    random_serv4.click()
    random_serv5.click()
    time.sleep(2)
    #driver.save_screenshot('C:/Users/overk/Downloads/4_selected_services.png')
    next_button2 = driver.find_element(By.XPATH, f'{at.SelectServicesPage.next_button2}')
    next_button2.click()
    time.sleep(2)
    continue_button4 = driver.find_element(By.XPATH, f'{at.SelectServicesPage.continue_button4}')
    continue_button4.click()
    time.sleep(2)

#verify flow finished, not account creation starts

def test_create_account(setupTeardown):
    create_acc_button = driver.find_element(By.XPATH, f'{at.CreateAccountPage.create_acc_button}')
    create_acc_button.click()
    time.sleep(2)
    pa_firstName_input = driver.find_element(By.XPATH, f'{at.CreateAccountPage.pa_firstName_input}')
    pa_lastName_input = driver.find_element(By.XPATH, f'{at.CreateAccountPage.pa_lastName_input}')
    pa_dob_input = driver.find_element(By.XPATH, f'{at.CreateAccountPage.pa_dob_input}')
    pa_phone_input = driver.find_element(By.XPATH, f'{at.CreateAccountPage.pa_phone_input}')
    pa_firstName_input.send_keys(at.Methods.randomizer(at.General.firstNames))
    pa_lastName_input.send_keys(at.Methods.randomizer(at.General.lastNames))
    pa_dob_input.send_keys(at.Methods.randomizer(at.General.datesOfBirth))
    pa_phone_input.send_keys(at.Methods.randomizer(at.General.usPhoneNums))
    time.sleep(4)
    print("Create Account, pa firstName entered: --", pa_firstName_input.get_attribute("value"))
    print("Create Account, pa lastName entered: --", pa_lastName_input.get_attribute("value"))
    print("Create Account, pa DOB entered: --", pa_dob_input.get_attribute("value"))
    print("Create Account, pa phone entered: --", pa_phone_input.get_attribute("value"))
    driver.save_screenshot('C:/Users/overk/Downloads/5_pa_personal_data.png')
    next_button3 = driver.find_element(By.XPATH, f'{at.CreateAccountPage.next_button3}')
    next_button3.click()
    time.sleep(2)
    pa_email_input = driver.find_element(By.XPATH, f'{at.SetPasswordPage.pa_email_input}')
    pa_password_input = driver.find_element(By.XPATH, f'{at.SetPasswordPage.pa_password_input}')
    pa_email_input.send_keys(at.General.unique_email)
    pa_password_input.send_keys("Qwerty123!")
    time.sleep(1)
    print("Set Email/Password, pa email entered: --", pa_email_input.get_attribute("value"))
    print("Set Email/Password, pa password entered: --", pa_password_input.get_attribute("value"))
    #driver.save_screenshot('C:/Users/overk/Downloads/6_pa_email-password.png')

def test_set_password(setupTeardown):
    create_button = driver.find_element(By.XPATH, f'{at.SetPasswordPage.create_button}')
    create_button.click()
    time.sleep(2)
    # print browser console messages (not working for Firefox)
    for entry in driver.get_log('browser'):
        print(entry)
    verify_code_input = driver.find_element(By.XPATH, f'{at.SetPasswordPage.verify_code_input}')
    verify_code_input.send_keys("010101")
    time.sleep(2)
    # print browser console messages (not working for Firefox)
    for entry in driver.get_log('browser'):
        print(entry)
    login_button = driver.find_element(By.XPATH, f'{at.SetPasswordPage.login_button}')
    login_button.click()
    time.sleep(5)

#now we are on web side

def test_webside_checks(setupTeardown):
    accept_button = driver.find_element(By.XPATH, f'{at.WebSidePages.accept_button}')
    accept_button.click()
    time.sleep(8)
    continue_button5 = driver.find_element(By.XPATH, f'{at.WebSidePages.continue_button5}')
    continue_button5.click()
    time.sleep(2)
    skip_button = driver.find_element(By.XPATH, f'{at.WebSidePages.skip_button}')
    skip_button.click()
    time.sleep(2)
    pm_selector = driver.find_element(By.XPATH, f'{at.WebSidePages.pm_selector}')
    pm_selector.click()
    locations_selector = driver.find_element(By.XPATH, f'{at.WebSidePages.locations_selector}')
    locations_selector.click()
    time.sleep(3)
    #driver.save_screenshot('C:/Users/overk/Downloads/7_created_practice.png')
    location_details = driver.find_element(By.XPATH, f'{at.WebSidePages.location_details}')
    location_details.click()
    time.sleep(3)
    #driver.save_screenshot('C:/Users/overk/Downloads/8_created_location.png')
    services_tab = driver.find_element(By.XPATH, f'{at.WebSidePages.services_tab}')
    services_tab.click()
    time.sleep(3)
    #driver.save_screenshot('C:/Users/overk/Downloads/9_created_services.png')
    profile_selector = driver.find_element(By.XPATH, f'{at.WebSidePages.profile_selector}')
    profile_selector.click()
    time.sleep(3)
    #driver.save_screenshot('C:/Users/overk/Downloads/10_pa_created_account.png')
    # print browser console messages (not working for Firefox)
    for entry in driver.get_log('browser'):
        print(entry)

# cd NavierrePablo/testings
# pytest -s -vv test_claimPractice_inp.py
# pytest -s -vv --setup-show test_claimPractice_inp.py
# pytest -s -vv --count=5 test_claimPractice_inp.py
    
if __name__ == '__main__':
    pytest.main(["-s", "-v", "--setup-show", "NavierrePablo/testings/test_claimPractice_inp.py"])