import requests
import json
import time
from adata import Requests, QRtemp, General, Methods
import dev_authorization

token = dev_authorization.access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + token}

def create_qr_code():
    socialLinks = [
    	{"linkType": "FACEBOOK", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "LINKEDIN", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "TIKTOK", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "TELEGRAM", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "WHATSAPP", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	#{"linkType": "INSTAGRAM", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "YOUTUBE", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"},
    	{"linkType": "TWITTER", "url": Methods.randomizer(QRtemp.weblinks), "title": "social"}
    ]
    payloadCreate = {
    "codeType": "V_CARD",
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
	"vcard": {
		"designPrimaryColor": Methods.randomizer(General.darkColors),
		"designSecondaryColor": Methods.randomizer(General.lightColors),
		"designNameColor": Methods.randomizer(General.lightColors),
		"designTextColor": Methods.randomizer(General.darkColors),
		"designIconColor": Methods.randomizer(General.mediumColors),
		"designTextHoverColor": Methods.randomizer(General.mediumColors),
		"designTitleColor": Methods.randomizer(General.darkColors),
		"buttonText": Methods.randomizer(General.words),
		"buttonSize": Methods.randomizer(QRtemp.sizes),
		"buttonBgColor": Methods.randomizer(General.lightColors),
		"buttonTextColor": Methods.randomizer(General.darkColors),
		"buttonHoverColor": Methods.randomizer(General.mediumColors),
		"buttonBorderColor": Methods.randomizer(General.darkColors),
		"fullName": Methods.randomizer(General.persons),
		"phoneNumber": Methods.randomizer(General.telNumbers),
		"alternativePhoneNumber": Methods.randomizer(General.telNumbers),
		"email": Methods.randomizer(General.emails),
		"website": Methods.randomizer(QRtemp.weblinks),
		"companyName": Methods.randomizer(General.companies),
		"jobPosition": Methods.randomizer(General.positions),
		"street": Methods.randomizer(General.words),
		"postalCode": Methods.randomizer(General.postalCodes),
		"city": Methods.randomizer(General.cities),
		"state": Methods.randomizer(General.words),
		"country": Methods.randomizer(General.countries),
		"links": socialLinks,
		"libraryId": Methods.randomizer(QRtemp.library_ids),
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

iterations = 5

count = 0
while True:
    count += 1
    create_qr_code()
    if count == iterations:
        break