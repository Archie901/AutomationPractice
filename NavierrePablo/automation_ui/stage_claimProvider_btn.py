import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://pablo-dev.vercel.app/for-providers/claim")
claim_button = driver.find_element(By.XPATH, '//button[contains(text(),"Providers")]')
wait.until(expected_conditions.visibility_of((claim_button)))
claim_button.click()
driver.implicitly_wait(2)

npi_input = driver.find_element(By.XPATH, '//input[@placeholder="NPI Number"]')

npi_input.send_keys("1154597581")

time.sleep(1)

search_button = driver.find_element(By.XPATH, '//button[contains(text(), "Search")]')
search_button.click()

time.sleep(2)

yes_button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes")]')
yes_button.click()

time.sleep(3)

add_serv_button = driver.find_element(By.XPATH, '//button[contains(text(), "Add Services")]')
add_serv_button.click()

serv_name_input = driver.find_element(By.XPATH, '//input[@id="service"]')
desc_textarea = driver.find_element(By.XPATH, '//textarea[@id="description"]')

serv_name_input.send_keys("custom service 1")
desc_textarea.send_keys("custom service 1 description")

save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
save_button.click()

time.sleep(2)

serv_name_input.send_keys("custom service 2")
desc_textarea.send_keys("custom service 2 description")
save_button.click()

time.sleep(2)

serv_name_input.send_keys("custom service 3 no desc")
save_button.click()
time.sleep(2)

back_button = driver.find_element(By.XPATH, '//button[contains(text(), "Back")]')
back_button.click()

time.sleep(2)

continue_button1 = driver.find_element(By.XPATH, '//a[contains(text(), "Continue")]')
continue_button1.click()

time.sleep(4)

location1_button = driver.find_element(By.XPATH, '//tbody/tr[1]/td/button[contains(@class, "MuiButtonBase-root")]')
location1_button.click()

continue_button2 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button2.click()

time.sleep(4)

skip_button = driver.find_element(By.XPATH, '//button[contains(text(), "Skip")]') 
skip_button.click()
time.sleep(2)

email_input = driver.find_element(By.XPATH, '//input[@id="email"]')
phone_input = driver.find_element(By.XPATH, '//input[@id="phone-number"]')
fax_input = driver.find_element(By.XPATH, '//input[@id="fax-number"]')

email_input.send_keys("abcergonu@mailinator.com")
phone_input.send_keys("5518239134")
fax_input.send_keys("9805657280")

continue_button2 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button2.click()

time.sleep(2)

pref_email_box = driver.find_element(By.XPATH, '//div/label[1]/span[contains(@class, "MuiButtonBase-root")]')
pref_fax_box = driver.find_element(By.XPATH, '//div/label[2]/span[contains(@class, "MuiButtonBase-root")]')
pref_email_box.click()
pref_fax_box.click()

continue_button3 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button3.click()

time.sleep(2)

continue_button4 = driver.find_element(By.XPATH, '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]')
continue_button4.click()

time.sleep(2)

#verify flow is finished, profile verified, now we go to account creation

create_acc_button = driver.find_element(By.XPATH, '//a[contains(text(), "Create Account")]')
create_acc_button.click()

time.sleep(2)

med_license_input = driver.find_element(By.XPATH, '//input[@id="medical-license-number"]')
state_license_dropdown = driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="New Jersey"]')
dob_input = driver.find_element(By.XPATH, '//input[@name="dateOfBirth"]')

med_license_input.send_keys("123_gfhgf_000")
state_license_dropdown.send_keys("Delaware")
state_license_dropdown.send_keys(Keys.DOWN)
state_license_dropdown.send_keys(Keys.ENTER)
#driver.execute_script("arguments[0].setAttribute('value', 'California')", state_license_dropdown)
dob_input.send_keys("09091990")

time.sleep(2)

next_button1 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button1.click()
time.sleep(2)

acc_password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
acc_password_confirm = driver.find_element(By.XPATH, '//input[@name="passwordConfirmation"]')
acc_password_input.send_keys("Qwerty123!")
acc_password_confirm.send_keys("Qwerty123!")

time.sleep(1)

next_button2 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button2.click()
time.sleep(2)

verify_code_input = driver.find_element(By.XPATH, '//input[@autocomplete="one-time-code"]')
verify_code_input.send_keys("010101")
time.sleep(2)

prac_input = driver.find_element(By.XPATH, '//input[@id="practice-name"]')
prac_email = driver.find_element(By.XPATH, '//input[@id="practice-email"]')

prac_input.send_keys("Autotest Practice")
prac_email.send_keys("auto_practice@maildrop.cc")

next_button3 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button3.click()
time.sleep(3)

login_button = driver.find_element(By.XPATH, '//a[contains(text(), "Log In")]')
login_button.click()

time.sleep(5)

#now we are on web side

accept_button = driver.find_element(By.XPATH, '//button[contains(text(), "I Accept")]')
accept_button.click()
time.sleep(8)

x_button = driver.find_element(By.XPATH, '//h2/button[contains(@class, "MuiButtonBase-root")]')
x_button.click()

time.sleep(3)

profile_selector = driver.find_element(By.XPATH, '//span[contains(text(), "My Profile")]')
profile_selector.click()

time.sleep(3)

insurance_tab = driver.find_element(By.XPATH, '//button[contains(text(), "Insurance")]')
locations_tab = driver.find_element(By.XPATH, '//button[contains(text(), "Locations")]')

insurance_tab.click()
time.sleep(3)

locations_tab.click()
time.sleep(5)


driver.quit()