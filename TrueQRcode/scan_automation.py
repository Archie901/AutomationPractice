import time
from selenium import webdriver


qr_id1 = 'FFWATS9Z'

qr_id2 = 'KF2P98ZB'

iterations = 30

driver = webdriver.Firefox()

count = 0
while True:
    count += 1
    driver.get("https://trueqrcode-dev.osdb.io/qr/" + qr_id1)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()