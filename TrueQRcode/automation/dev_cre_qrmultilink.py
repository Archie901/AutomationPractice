import requests
import json
import time
from adata import Methods, Requests, QRtemp, General
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def create_qrcode():
    socialLinks = [
    	#{"linkType": "FACEBOOK", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "LINKEDIN", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "TIKTOK", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "TELEGRAM", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "WHATSAPP", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "INSTAGRAM", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "YOUTUBE", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "TWITTER", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"}
    ]
    customLinks = [
        {"library": {}, "libraryId": Methods.randomizer(QRtemp.library_ids),
         "url": Methods.randomizer(QRtemp.weblinks), "title": Methods.randomizer(General.words), "linkType": "CUSTOM"},
        {"library": {}, "libraryId": Methods.randomizer(QRtemp.library_ids),
         "url": Methods.randomizer(QRtemp.weblinks), "title": Methods.randomizer(General.words), "linkType": "CUSTOM"},
        {"library": {}, "libraryId": Methods.randomizer(QRtemp.library_ids),
         "url": Methods.randomizer(QRtemp.weblinks), "title": Methods.randomizer(General.words), "linkType": "CUSTOM"},
        ]
    payloadCreate = {
    "codeType": "MULTILINK",
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
    "multilink": {
        "socialLinks": socialLinks,
        "customLinks": customLinks,
        "buttonBgColor": Methods.randomizer(General.lightColors),
		"buttonTextColor": Methods.randomizer(General.darkColors),
		"buttonHoverColor": Methods.randomizer(General.mediumColors),
		"buttonBorderColor": Methods.randomizer(General.darkColors),
		"designDescriptionColor": Methods.randomizer(General.lightColors),
		"designTitleColor": Methods.randomizer(General.lightColors),
		"designBgColor": Methods.randomizer(General.darkColors),
		"libraryId": Methods.randomizer(QRtemp.library_ids),
		"description": Methods.randomizer(General.words),
		"title": Methods.randomizer(General.persons),
        },
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_qrCreate, data=payload_json, headers=headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)    
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required field value empty"
    assert resp_create.json()['name'] != None, "required field value empty"
    assert resp_create.json()['codeType'] != None, "required field value empty"

iterations = 2

count = 0
while True:
    count += 1
    create_qrcode()
    if count == iterations:
        break