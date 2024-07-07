import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import elements_locators as el
import testvalues as tv

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get(tv.Requests.devstage_pablo_url_domain + "/for-providers/claim")

driver.implicitly_wait(3)

busi_claim_button = driver.find_element(By.XPATH, f'{el.BusiMainPage.busi_claim_button}')

wait.until(expected_conditions.visibility_of((busi_claim_button)))

busi_claim_button.click()
time.sleep(2)

inpatient_button = driver.find_element(By.XPATH, f'{el.BusiMainPage.inpatient_button}')
inpatient_button.click()
time.sleep(1)

random_lvl3_type1 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type2 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type3 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type4 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type5 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type6 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type7 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.lvl3_typesInp)}')
random_lvl3_type1.click()
random_lvl3_type2.click()
random_lvl3_type3.click()
random_lvl3_type4.click()
random_lvl3_type5.click()
random_lvl3_type6.click()
random_lvl3_type7.click()

time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/2_selected_lvl3_types.png')

continue_button1 = driver.find_element(By.XPATH, f'{el.BusiMainPage.continue_button1}')
continue_button1.click()
time.sleep(2)

continue_button2 = driver.find_element(By.XPATH, f'{el.BusiMainPage.continue_button2}')
continue_button2.click()
time.sleep(2)

search_input = driver.find_element(By.XPATH, f'{el.BusiMainPage.search_input}')
search_input.send_keys(tv.Methods.randomizer(tv.General.practice_search))
time.sleep(2)

random_prac = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.BusiMainPage.found_pracs)}')
random_prac.click()
time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/3_choose_your_practice.png')

continue_button3 = driver.find_element(By.XPATH, f'{el.BusiMainPage.continue_button3}')
continue_button3.click()
time.sleep(4)

ein_input = driver.find_element(By.XPATH, f'{el.ConfirmIdentityPage.ein_input}')
email_input = driver.find_element(By.XPATH, f'{el.ConfirmIdentityPage.email_input}')
fax_input = driver.find_element(By.XPATH, f'{el.ConfirmIdentityPage.fax_input}')

ein_input.send_keys(tv.Methods.randomizer(tv.General.diff_values))
email_input.send_keys(tv.Methods.randomizer(tv.General.emails))
fax_input.send_keys(tv.Methods.randomizer(tv.General.usPhoneNums))

time.sleep(5)

driver.save_screenshot('C:/Users/overk/Downloads/4_confirm_identity_data.png')

next_button1 = driver.find_element(By.XPATH, f'{el.ConfirmIdentityPage.next_button1}')
next_button1.click()
time.sleep(2)

random_serv1 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.SelectServicesPage.services_list)}')
random_serv2 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.SelectServicesPage.services_list)}')
random_serv3 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.SelectServicesPage.services_list)}')
random_serv4 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.SelectServicesPage.services_list)}')
random_serv5 = driver.find_element(By.XPATH, f'{tv.Methods.randomizer(el.SelectServicesPage.services_list)}')
random_serv1.click()
random_serv2.click()
random_serv3.click()
random_serv4.click()
random_serv5.click()

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/5_selected_services.png')

next_button2 = driver.find_element(By.XPATH, f'{el.SelectServicesPage.next_button2}')
next_button2.click()
time.sleep(2)

continue_button4 = driver.find_element(By.XPATH, f'{el.SelectServicesPage.continue_button4}')
continue_button4.click()
time.sleep(2)

#verify flow finished, not account creation starts

create_acc_button = driver.find_element(By.XPATH, f'{el.CreateAccountPage.create_acc_button}')
create_acc_button.click()

time.sleep(2)

firstName_input = driver.find_element(By.XPATH, f'{el.CreateAccountPage.firstName_input}')
lastName_input = driver.find_element(By.XPATH, f'{el.CreateAccountPage.lastName_input}')
dob_input = driver.find_element(By.XPATH, f'{el.CreateAccountPage.dob_input}')
phone_input = driver.find_element(By.XPATH, f'{el.CreateAccountPage.phone_input}')

firstName_input.send_keys(tv.Methods.randomizer(tv.General.firstNames))
lastName_input.send_keys(tv.Methods.randomizer(tv.General.lastNames))
dob_input.send_keys(tv.Methods.randomizer(tv.General.datesOfBirth))
phone_input.send_keys(tv.Methods.randomizer(tv.General.usPhoneNums))

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/6_admin_account_data.png')

next_button3 = driver.find_element(By.XPATH, f'{el.CreateAccountPage.next_button3}')
next_button3.click()
time.sleep(2)

acc_email_input = driver.find_element(By.XPATH, f'{el.SetPasswordPage.acc_email_input}')
acc_password_input = driver.find_element(By.XPATH, f'{el.SetPasswordPage.acc_password_input}')

acc_email_input.send_keys(tv.Methods.randomizer(tv.General.emails))

acc_password_input.send_keys("Qwerty123!")

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/7_admin_email.png')

create_button = driver.find_element(By.XPATH, f'{el.SetPasswordPage.create_button}')
create_button.click()
time.sleep(1)

verify_code_input = driver.find_element(By.XPATH, f'{el.SetPasswordPage.verify_code_input}')
verify_code_input.send_keys("010101")
time.sleep(2)

login_button = driver.find_element(By.XPATH, f'{el.SetPasswordPage.login_button}')
login_button.click()

time.sleep(5)

#now we are on web side

accept_button = driver.find_element(By.XPATH, f'{el.WebSidePages.accept_button}')
accept_button.click()
time.sleep(8)

continue_button5 = driver.find_element(By.XPATH, f'{el.WebSidePages.continue_button5}')
continue_button5.click()
time.sleep(2)

skip_button = driver.find_element(By.XPATH, f'{el.WebSidePages.skip_button}')
skip_button.click()
time.sleep(2)

pm_selector = driver.find_element(By.XPATH, f'{el.WebSidePages.pm_selector}')
pm_selector.click()

locations_selector = driver.find_element(By.XPATH, f'{el.WebSidePages.locations_selector}')
locations_selector.click()

time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/8_web_created_locs.png')

driver.quit()