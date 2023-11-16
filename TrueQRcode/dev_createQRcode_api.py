import requests
import json
import random
import time
import dev_authorization

token = dev_authorization.access_token

domain = "https://api-dev.trueqrcode.com"

pathCreate = "/api/v1/private/qr-code"

headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive", "Authorization": "Bearer " + token}

QRnames = ["John O'Grady)_@#:<66", "(Great feeling-123)", "Beware_OF_mad_DOG909"]

frameTexts = ["JUST DO IT", "COMING IS NOW","ANGER TO GO"]

patternColors = ["#EB0000", "#128501", "#0119B9"]

frameTypes = ["BORDER", "BORDER_INTERRUPTION", "NO_BORDER"]

patternTypes = ["SQUARE", "CLASSY_ROUNDED", "EXTRA_ROUNDED"]

cornerTypes = ["SQUARE", "FULL_CIRCLE", "ROUNDED"]

targetURLs = ["https://www.englishgrammar.org", "https://wordcounter.net/character-count", "https://advice.writing.utoronto.ca"]

def randomizer(x):
    return random.choice(x)

def create_qr_code():

    randomQRname = randomizer(QRnames)
    randomFrameText = randomizer(frameTexts)
    randomPatternColor = randomizer(patternColors)
    randomFrameType = randomizer(frameTypes)
    randomPatternType = randomizer(patternTypes)
    randomCornerType = randomizer(cornerTypes)
    randomTargetURL = randomizer(targetURLs)

    payloadCreate = {

	"codeType": "WEBSITE",
	"name": randomQRname,
	"design": {
		"logoSize": 20,
		"frameText": randomFrameText,
		"frameTextSize": 12,
		"frameTextColor": "#000000",
		"frameBackgroundColor": "#000000",
		"backgroundColor": "#FFFFFF",
		"patternColor": randomPatternColor,
		"cornerColor": "#000000",
		"frameType": randomFrameType,
		"patternType": randomPatternType,
		"cornerType": randomCornerType
	},
	"website": {
		"url": randomTargetURL
	}
}

    json_paylodCreate = json.dumps(payloadCreate)

    resp_create = requests.post(url=domain+pathCreate, data=json_paylodCreate, headers=headers)
    print(resp_create.json())
    print(resp_create.status_code, resp_create.reason, resp_create.elapsed)
    assert resp_create.status_code == 200, "status code is not 200"
    assert resp_create.reason == "OK", "status message is not OK"

iterations = 2

count = 0
while True:
    count += 1
    create_qr_code()
    time.sleep(1)
    if count == iterations:
        break