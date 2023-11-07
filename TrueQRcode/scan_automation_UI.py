import time
from selenium import webdriver


qr_id1 = '8HQS6UR6'

qr_id2 = 'LMF24NHS'

qr_id3 = 'H1JDGC4A'

qr_id4 = 'JJZXVUZD'

iterations = 2

driver = webdriver.Firefox()

count = 0
while True:
    count += 1
    driver.get("https://trueqrcode-dev.osdb.io/qr/" + qr_id1)
    time.sleep(6)
    if count == iterations:
        break

driver.quit()