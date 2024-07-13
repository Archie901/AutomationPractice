import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import locators as el
import testvalues as tv

service = Service()
options = webdriver.ChromeOptions()
options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get(tv.Requests.devstage_pablo_url_domain + "/for-providers/claim")

driver.implicitly_wait(3)

prov_claim_button = driver.find_element(By.XPATH, f'{el.ProvMainPage.prov_claim_button}')

wait.until(expected_conditions.visibility_of((prov_claim_button)))

prov_claim_button.click()
time.sleep(2)

npi_input = driver.find_element(By.XPATH, f'{el.ProvMainPage.npi_input}')

npi_input.send_keys(tv.General.npi)

time.sleep(1)

print("Main page, prov NPI entered: --", npi_input.get_attribute("value"))

search_button = driver.find_element(By.XPATH, f'{el.ProvMainPage.search_button}')
search_button.click()

time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/1_npi_found_provider.png')

yes_button = driver.find_element(By.XPATH, f'{el.ProvMainPage.yes_button}')
yes_button.click()

time.sleep(3)

add_serv_button = driver.find_element(By.XPATH, f'{el.ProvServicesPage.add_serv_button}')
add_serv_button.click()

serv_name_input = driver.find_element(By.XPATH, f'{el.ProvServicesPage.serv_name_input}')
desc_textarea = driver.find_element(By.XPATH, f'{el.ProvServicesPage.desc_textarea}')

s1 = serv_name_input.send_keys(tv.Methods.randomizer(tv.General.serviceNames))
d1 = desc_textarea.send_keys(tv.Methods.randomizer(tv.General.serviceDescs))

save_button = driver.find_element(By.XPATH, f'{el.ProvServicesPage.save_button}')
save_button.click()
time.sleep(2)

s2 = serv_name_input.send_keys(tv.Methods.randomizer(tv.General.serviceNames))
d2 = desc_textarea.send_keys(tv.Methods.randomizer(tv.General.serviceDescs))
save_button.click()
time.sleep(2)

s3 = serv_name_input.send_keys(tv.Methods.randomizer(tv.General.serviceNames))
save_button.click()
time.sleep(2)

back_button = driver.find_element(By.XPATH, f'{el.ProvServicesPage.back_button}')
back_button.click()

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/2_entered_services.png')

continue_button1 = driver.find_element(By.XPATH, f'{el.ProvServicesPage.continue_button1}')
continue_button1.click()

time.sleep(4)

location1_button = driver.find_element(By.XPATH, f'{el.LocInsurPages.location1_button}')
location1_button.click()

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/3_selected_locations.png')

continue_button2 = driver.find_element(By.XPATH, f'{el.LocInsurPages.continue_button2}')
continue_button2.click()

time.sleep(4)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/4_list_of_insurances.png')

skip_button = driver.find_element(By.XPATH, f'{el.LocInsurPages.skip_button}') 
skip_button.click()
time.sleep(2)

contact_email_input = driver.find_element(By.XPATH, f'{el.LocInsurPages.contact_email_input}')
contact_phone_input = driver.find_element(By.XPATH, f'{el.LocInsurPages.contact_phone_input}')
contact_fax_input = driver.find_element(By.XPATH, f'{el.LocInsurPages.contact_fax_input}')

contact_email_input.send_keys(tv.General.unique_email)
contact_phone_input.send_keys(tv.Methods.randomizer(tv.General.usPhoneNums))
contact_fax_input.send_keys(tv.Methods.randomizer(tv.General.usPhoneNums))

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/5_contact_information.png')

print("Contact info form, contact email entered: --", contact_email_input.get_attribute("value"))
print("Contact info form, contact phone entered: --", contact_phone_input.get_attribute("value"))
print("Contact info form, contact fax entered: --", contact_fax_input.get_attribute("value"))

continue_button3 = driver.find_element(By.XPATH, f'{el.LocInsurPages.continue_button3}')
continue_button3.click()

time.sleep(2)

pref_email_box = driver.find_element(By.XPATH, f'{el.LocInsurPages.pref_email_box}')
pref_fax_box = driver.find_element(By.XPATH, f'{el.LocInsurPages.pref_fax_box}')
pref_email_box.click()
pref_fax_box.click()

continue_button4 = driver.find_element(By.XPATH, f'{el.LocInsurPages.continue_button4}')
continue_button4.click()

time.sleep(3)

continue_button5 = driver.find_element(By.XPATH, f'{el.LocInsurPages.continue_button5}')
continue_button5.click()

time.sleep(2)

#verify flow is finished, profile verified, now we go to provount creation

create_prov_button = driver.find_element(By.XPATH, f'{el.VerifyIdentityPage.create_prov_button}')
create_prov_button.click()

time.sleep(2)

prov_med_license_input = driver.find_element(By.XPATH, f'{el.VerifyIdentityPage.prov_med_license_input}')
prov_state_license_dropdown = driver.find_element(By.CSS_SELECTOR, f'{el.VerifyIdentityPage.prov_state_license_dropdown}')
prov_dob_input = driver.find_element(By.XPATH, f'{el.VerifyIdentityPage.prov_dob_input}')

prov_med_license_input.send_keys(tv.Methods.randomizer(tv.General.diff_values))
prov_state_license_dropdown.send_keys(tv.Methods.randomizer(tv.General.usStates))
prov_state_license_dropdown.send_keys(Keys.DOWN)
prov_state_license_dropdown.send_keys(Keys.ENTER)
#driver.execute_script("arguments[0].setAttribute('value', 'California')", state_license_dropdown)
prov_dob_input.send_keys(tv.Methods.randomizer(tv.General.datesOfBirth))

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/6_verify_identity_info.png')

print("Verify Identity, med license entered: --", prov_med_license_input.get_attribute("value"))
print("Verify Identity, state of license selected: --", prov_state_license_dropdown.get_attribute("value"))
print("Verify Identity, DOB entered: --", prov_dob_input.get_attribute("value"))

next_button1 = driver.find_element(By.XPATH, f'{el.VerifyIdentityPage.next_button1}')
next_button1.click()
time.sleep(2)

prov_password_input = driver.find_element(By.XPATH, f'{el.CreatePasswordPage.prov_password_input}')
prov_password_confirm = driver.find_element(By.XPATH, f'{el.CreatePasswordPage.prov_password_confirm}')
prov_password_input.send_keys("Qwerty123!")
prov_password_confirm.send_keys("Qwerty123!")

time.sleep(1)

next_button2 = driver.find_element(By.XPATH, f'{el.CreatePasswordPage.next_button2}')
next_button2.click()
time.sleep(2)

verify_code_input = driver.find_element(By.XPATH, f'{el.CreatePasswordPage.verify_code_input}')
verify_code_input.send_keys("010101")
time.sleep(2)

prac_input = driver.find_element(By.XPATH, f'{el.WorkInfoPage.prac_input}')
prac_email = driver.find_element(By.XPATH, f'{el.WorkInfoPage.prac_email}')

prac_input.send_keys(tv.Methods.randomizer(tv.General.practiceNames))
prac_email.send_keys(tv.Methods.randomizer(tv.General.practiceEmails))
time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/7_practice_info.png')

print("Work Info, prac name entered: --", prac_input.get_attribute("value"))
print("Work Info, prac email entered: --", prac_email.get_attribute("value"))

next_button3 = driver.find_element(By.XPATH, f'{el.WorkInfoPage.next_button3}')
next_button3.click()
time.sleep(8)

login_button = driver.find_element(By.XPATH, f'{el.WorkInfoPage.login_button}')
login_button.click()

time.sleep(5)

# print browser console messages (not working for Firefox)
for entry in driver.get_log('browser'):
    print(entry)

#now we are on web side

accept_button = driver.find_element(By.XPATH, f'{el.WebProvPages.accept_button}')
accept_button.click()
time.sleep(8)

x_button = driver.find_element(By.XPATH, f'{el.WebProvPages.x_button}')
x_button.click()

time.sleep(3)

profile_selector = driver.find_element(By.XPATH, f'{el.WebProvPages.profile_selector}')
profile_selector.click()

time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/8_created_provider_profile.png')

insurance_tab = driver.find_element(By.XPATH, f'{el.WebProvPages.insurance_tab}')
locations_tab = driver.find_element(By.XPATH, f'{el.WebProvPages.locations_tab}')

insurance_tab.click()
time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/9_created_insurances.png')

locations_tab.click()
time.sleep(5)

driver.save_screenshot('C:/Users/overk/Downloads/ClaimProvider/10_created_locations.png')

driver.quit()