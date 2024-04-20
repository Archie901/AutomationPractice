import requests
import json
import time
import _main
import adata as ad
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def update_qrcode():
    payloadUpdate = {
    "codeType": "WEBSITE",
	"name": ad.Methods.randomizer(ad.QRtemp.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": ad.Methods.randomizer(ad.QRtemp.sizes),
		"frameText": ad.Methods.randomizer(ad.QRtemp.frameTexts),		
		"frameTextColor": ad.Methods.randomizer(ad.General.mediumColors),
		"frameBackgroundColor": ad.Methods.randomizer(ad.General.darkColors),
		"backgroundColor": ad.Methods.randomizer(ad.General.lightColors),
		"patternColor": ad.Methods.randomizer(ad.General.darkColors),
		"cornerColor": ad.Methods.randomizer(ad.General.darkColors),
		"frameType": ad.Methods.randomizer(ad.QRtemp.frameTypes),
		"patternType": ad.Methods.randomizer(ad.QRtemp.patternTypes),
		"cornerType": ad.Methods.randomizer(ad.QRtemp.cornerTypes),
        #"libraryId": ad.Methods.randomizer(ad.QRtemp.library_ids),
        },
	"website": {
		"url": ad.Methods.randomizer(ad.QRtemp.weblinks)
        }
    }
    payload_json = json.dumps(payloadUpdate)
    resp_update = requests.patch(url=ad.Requests.dev_api_domain+ad.Requests.path_qrSingle+"PS24VGMY",
                                 data=payload_json, headers=headersToken)
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