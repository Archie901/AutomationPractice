import time
import random
from selenium import webdriver


domain = "https://dev.trueqrcode.com/qr/"

qr_ids = ["8Q42EABK", "8JRQR839", "LMF24NHS"]

#qr_id1 = 

def randomizer(x):
    return random.choice(x)

iterations = 10

driver = webdriver.Firefox()

count = 0
while True:
    randomQR_id = randomizer(qr_ids)
    print(randomQR_id)
    count += 1
    driver.get(domain + randomQR_id)
    time.sleep(5)
    if count == iterations:
        break

driver.quit()