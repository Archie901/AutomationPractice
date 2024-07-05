import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#service = Service()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://pablo-dev.vercel.app/for-providers/claim")
claim_button = driver.find_element(By.XPATH, '//button[contains(text(),"Businesses")]')
wait.until(expected_conditions.visibility_of((claim_button)))
claim_button.click()
driver.implicitly_wait(2)

outpatient_button = driver.find_element(By.XPATH, '//button/div/p[contains(text(),"Outpatient")]')

time.sleep(1)
outpatient_button.click()
time.sleep(1)
lvl2_option1 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][1]/div/p')
lvl2_option2 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][2]/div/p')
lvl2_option3 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][3]/div/p')
lvl2_option4 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][4]/div/p')
lvl2_option5 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][5]/div/p')
lvl2_option7 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][7]/div/p')
lvl2_subcats = []
lvl2_subcats.extend((lvl2_option1, lvl2_option2, lvl2_option3, lvl2_option4, lvl2_option5, lvl2_option7))
def randomizer(x):
    randomed = random.choice(x)
    return randomed

random_lvl2 = randomizer(lvl2_subcats)
random_lvl2.click()
time.sleep(1)

lvl3_option1 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][1]/div/p')
lvl3_option2 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][2]/div/p')
lvl3_option3 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][3]/div/p')
lvl3_option4 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][4]/div/p')
lvl3_types = []
lvl3_types.extend((lvl3_option1, lvl3_option2, lvl3_option3, lvl3_option4))
random_lvl3 = randomizer(lvl3_types)
random_lvl3.click()
random_lvl3 = randomizer(lvl3_types)
random_lvl3.click()
random_lvl3 = randomizer(lvl3_types)
random_lvl3.click()
random_lvl3 = randomizer(lvl3_types)
random_lvl3.click()

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/2_selected_lvl3_types.png')

continue_button1 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button1.click()
time.sleep(2)
continue_button2 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button2.click()
time.sleep(1)
search_input = driver.find_element(By.XPATH, '//input[@placeholder="Practice Name"]')
search_input.send_keys("Medical Clinic Center")
time.sleep(2)

found_prac1 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][1]/div/p')
found_prac2 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][2]/div/p')
found_prac3 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][3]/div/p')
found_prac4 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][4]/div/p')
found_prac5 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][5]/div/p')
found_prac6 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][6]/div/p')
found_prac7 = driver.find_element(By.XPATH, '//button[contains(@class, "MuiButtonBase-root")][7]/div/p')

practice_list = []
practice_list.extend((found_prac1, found_prac2, found_prac3, found_prac4, found_prac5, found_prac6, found_prac7))

random_prac = randomizer(practice_list)
random_prac.click()

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/3_choose_your_practice.png')

continue_button3 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button3.click()
time.sleep(3)

ein_input = driver.find_element(By.XPATH, '//input[@placeholder="EIN"]')
email_input = driver.find_element(By.XPATH, '//input[@placeholder="mail@mail.com"]')
fax_input = driver.find_element(By.XPATH, '//input[@name="faxNumber"]')
ein_input.send_keys("123-iokl-0980")
email_input.send_keys("autotest1@mailinator.com")
fax_input.send_keys("1728322251")

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/4_confirm_identity_data.png')

next_button1 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button1.click()
time.sleep(2)

found_serv1 = driver.find_element(By.XPATH, '//ul/li[1]/span[contains(@class, "MuiButtonBase-root")]')
found_serv2 = driver.find_element(By.XPATH, '//ul/li[2]/span[contains(@class, "MuiButtonBase-root")]')
found_serv3 = driver.find_element(By.XPATH, '//ul/li[3]/span[contains(@class, "MuiButtonBase-root")]')
found_serv4 = driver.find_element(By.XPATH, '//ul/li[4]/span[contains(@class, "MuiButtonBase-root")]')
found_serv5 = driver.find_element(By.XPATH, '//ul/li[5]/span[contains(@class, "MuiButtonBase-root")]')

services_list = []
services_list.extend((found_serv1, found_serv2, found_serv3, found_serv4, found_serv5))

random_serv = randomizer(services_list)
random_serv.click()
random_serv = randomizer(services_list)
random_serv.click()
random_serv = randomizer(services_list)
random_serv.click()
random_serv = randomizer(services_list)
random_serv.click()
random_serv = randomizer(services_list)
random_serv.click()
random_serv = randomizer(services_list)
random_serv.click()

time.sleep(2)

driver.save_screenshot('C:/Users/overk/Downloads/5_selected_services.png')

next_button2 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button2.click()
time.sleep(2)

continue_button4 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button4.click()
time.sleep(2)

#verify flow finished, not account creation starts

create_acc_button = driver.find_element(By.XPATH, '//a[contains(text(), "Create Account")]')
create_acc_button.click()

time.sleep(2)

firstName_input = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
lastName_input = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
dob_input = driver.find_element(By.XPATH, '//input[@name="dateOfBirth"]')
phone_input = driver.find_element(By.XPATH, '//input[@name="phone"]')

firstName_input.send_keys("Scott")
lastName_input.send_keys("Chapman")
dob_input.send_keys("09091990")
phone_input.send_keys("4208245870")

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/6_admin_account_data.png')

next_button3 = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
next_button3.click()
time.sleep(2)

acc_email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
acc_password_input = driver.find_element(By.XPATH, '//input[@name="password"]')

acc_email_input.send_keys("somuchac@mailinator.com")

acc_password_input.send_keys("Qwerty123!")

time.sleep(1)

driver.save_screenshot('C:/Users/overk/Downloads/7_admin_email.png')

create_button = driver.find_element(By.XPATH, '//button[contains(text(), "Create")]')
create_button.click()
time.sleep(1)

verify_code_input = driver.find_element(By.XPATH, '//input[@autocomplete="one-time-code"]')
verify_code_input.send_keys("010101")
time.sleep(2)

login_button = driver.find_element(By.XPATH, '//a[contains(text(), "Log In")]')
login_button.click()

time.sleep(2)

#now we are on web side

accept_button = driver.find_element(By.XPATH, '//button[contains(text(), "I Accept")]')
accept_button.click()
time.sleep(7)

continue_button5 = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
continue_button5.click()
time.sleep(2)

skip_button = driver.find_element(By.XPATH, '//button[contains(text(), "Skip")]') 
skip_button.click()
time.sleep(2)

PM_selector = driver.find_element(By.XPATH, '//span[contains(text(), "Practice Management")]')
PM_selector.click()

Locations_selector = driver.find_element(By.XPATH, '//span[contains(text(), "Locations")]')
Locations_selector.click()

time.sleep(3)

driver.save_screenshot('C:/Users/overk/Downloads/8_web_created_locs.png')

driver.quit()