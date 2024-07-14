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
    driver.get(at.Requests.devstage_pablo_url_domain + "/for-providers/claim")
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
    pass

def test_set_password(setupTeardown):
    pass

#now we are on web side

def test_webside_checks(setupTeardown):
    pass



# cd NavierrePablo/testings
# pytest -s -vv test_claimPractice_inp.py
# pytest -s -vv --setup-show test_claimPractice_inp.py
# pytest -s -vv --count=5 test_claimPractice_inp.py
    
if __name__ == '__main__':
    pytest.main(["-s", "-v", "--setup-show", "NavierrePablo/testings/test_claimPractice_inp.py"])