import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import _main
import adata as ad
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

service = Service()
options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Edge()
driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://dev.trueqrcode.com/auth/sign-in")
time.sleep(1)
email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
time.sleep(1)
email_input.send_keys("newest@mailinator.com")
password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
driver.implicitly_wait(2)
password_input.send_keys("Qwerty123!")
time.sleep(1)
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()
time.sleep(1)
dashboard_side = driver.find_element(By.XPATH, '//span[contains(text(),"Dashboard")]')
print(dashboard_side.text)
create_qr_button = driver.find_element(By.XPATH, '//span[contains(text(), "Create")]')
create_qr_button.click()
time.sleep(1)
next_button = driver.find_element(By.XPATH, '//button//span[1][contains(text(), "Next")]')
next_button.click()
time.sleep(1)
website_input = driver.find_element(By.XPATH, '//input[@name="websiteUrl"]')
website_input.send_keys("http://example.com/")
next_button.click()
time.sleep(1)

frame_button = driver.find_element(By.XPATH, '//div[contains(text(), "Frame")]')
frame_button.click()
time.sleep(1)

#frame_container1 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[1]//div[1][contains(@class, "FrameContainer_container")]')
frame_container2 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[2]//div[1][contains(@class, "FrameContainer_container")]')
frame_container3 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[3]//div[1][contains(@class, "FrameContainer_container")]')
frame_container4 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[4]//div[1][contains(@class, "FrameContainer_container")]')
frame_container5 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[5]//div[1][contains(@class, "FrameContainer_container")]')
frame_container6 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[6]//div[1][contains(@class, "FrameContainer_container")]')

frame_containers = []
frame_containers.extend((frame_container2, frame_container3, frame_container4, frame_container5, frame_container6))

randomed = ad.Methods.randomizer(frame_containers)
randomed.click()
time.sleep(2)

scanme_input = driver.find_element(By.XPATH, '//input[@placeholder="SCAN ME"]')
frame_size_input = driver.find_element(By.XPATH, '//input[@name="frameTextSize"]')

scanme_input.send_keys(Keys.CONTROL + "a")
scanme_input.send_keys(Keys.BACKSPACE)
frame_size_input.send_keys(Keys.CONTROL + "a")
frame_size_input.send_keys(Keys.BACKSPACE)

scanme_input.send_keys(ad.Methods.randomizer(ad.QRtemp.frameTexts))
frame_size_input.send_keys(ad.Methods.randomizer(ad.QRtemp.sizes))
time.sleep(2)

pattern_button = driver.find_element(By.XPATH, '//div[contains(text(), "Pattern")]')
pattern_button.click()
time.sleep(1)

pattern_con1 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][1]')
pattern_con2 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][2]')
pattern_con3 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][3]')
pattern_con4 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][4]')
pattern_con5 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][5]')
pattern_con6 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][1]//div[contains(@class, "Pattern_root__cGft9")][6]')

pattern_cons = []
pattern_cons.extend((pattern_con1, pattern_con2, pattern_con3, pattern_con4, pattern_con5, pattern_con6))

randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
randomess = ad.Methods.randomizer(pattern_cons)
randomess.click()
time.sleep(2)

corner_type1 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][2]//div[contains(@class, "Pattern_root__cGft9")][1]')
corner_type2 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][2]//div[contains(@class, "Pattern_root__cGft9")][2]')
corner_type3 = driver.find_element(By.XPATH, '//div[contains(@class, "grid")][2]//div[contains(@class, "Pattern_root__cGft9")][3]')

corner_types = []
corner_types.extend((corner_type1, corner_type2, corner_type3))

randomik = ad.Methods.randomizer(corner_types)
randomik.click()
randomik = ad.Methods.randomizer(corner_types)
randomik.click()
randomik = ad.Methods.randomizer(corner_types)
randomik.click()
randomik = ad.Methods.randomizer(corner_types)
randomik.click()
randomik = ad.Methods.randomizer(corner_types)
randomik.click()
randomik = ad.Methods.randomizer(corner_types)
randomik.click()
time.sleep(2)


next_button.click()
time.sleep(2)

qrname_input = driver.find_element(By.XPATH, '//input[@value="QR code"]')

qrname_input.send_keys(Keys.CONTROL + "a")
qrname_input.send_keys(Keys.BACKSPACE)

qrname_input.send_keys(ad.Methods.randomizer(ad.QRtemp.QRnames))
time.sleep(2)


confirm_save_button = driver.find_element(By.XPATH, '//button//span[1][contains(text(), "Confirm")]')
confirm_save_button.click()
time.sleep(4)
website_of_code_created = driver.find_element(By.XPATH, '//span[contains(text(), "http://example.com/")]')
print(website_of_code_created.text)
time.sleep(4)

driver.quit()