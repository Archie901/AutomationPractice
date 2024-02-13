import requests
import json
import time
from adata import Methods, Requests, QRtemp, General
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def update_qrcode():
    payloadUpdate = {
    "codeType": "WEBSITE",
	"name": Methods.randomizer(QRtemp.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": Methods.randomizer(QRtemp.sizes),
		"frameText": Methods.randomizer(QRtemp.frameTexts),		
		"frameTextColor": Methods.randomizer(General.mediumColors),
		"frameBackgroundColor": Methods.randomizer(General.darkColors),
		"backgroundColor": Methods.randomizer(General.lightColors),
		"patternColor": Methods.randomizer(General.darkColors),
		"cornerColor": Methods.randomizer(General.darkColors),
		"frameType": Methods.randomizer(QRtemp.frameTypes),
		"patternType": Methods.randomizer(QRtemp.patternTypes),
		"cornerType": Methods.randomizer(QRtemp.cornerTypes),
        "libraryId": Methods.randomizer(QRtemp.library_ids),
        },
	"website": {
		"url": Methods.randomizer(QRtemp.weblinks)
        }
    }
    payload_json = json.dumps(payloadUpdate)
    resp_update = requests.patch(url=Requests.dev_api_domain+Requests.path_qrSingle+"G5JLJRSC", data=payload_json, headers=headersToken)
    #print(resp_update.text)
    print("update request:", resp_update.status_code, "/", resp_update.reason, "/", resp_update.elapsed)
    assert resp_update.status_code == 200, "status code not 200"
    assert resp_update.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_update.json()['id'] != None, "required id field value empty"
    assert resp_update.json()['name'] != None, "required name field value empty"
    assert resp_update.json()['codeType'] != None, "required codeType field value empty"

iterations = 1

count = 0
while True:
    count += 1
    update_qrcode()
    if count == iterations:
        break