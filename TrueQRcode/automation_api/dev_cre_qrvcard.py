import requests
import json
import time
import _main
import adata as ad
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def create_qrcode():
    socialLinks = [
    	{"linkType": "FACEBOOK", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	{"linkType": "LINKEDIN", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	#{"linkType": "TIKTOK", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	{"linkType": "TELEGRAM", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	#{"linkType": "WHATSAPP", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	#{"linkType": "INSTAGRAM", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	{"linkType": "YOUTUBE", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"},
    	{"linkType": "TWITTER", "url": ad.Methods.randomizer(ad.QRtemp.weblinks), "title": "social"}
    ]
    payloadCreate = {
    "codeType": "V_CARD",
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
        "libraryId": ad.Methods.randomizer(ad.QRtemp.library_ids),
        },
	"vcard": {
		"designPrimaryColor": ad.Methods.randomizer(ad.General.darkColors),
		"designSecondaryColor": ad.Methods.randomizer(ad.General.lightColors),
		"designNameColor": ad.Methods.randomizer(ad.General.lightColors),
		"designTextColor": ad.Methods.randomizer(ad.General.darkColors),
		"designIconColor": ad.Methods.randomizer(ad.General.mediumColors),
		"designTextHoverColor": ad.Methods.randomizer(ad.General.mediumColors),
		"designTitleColor": ad.Methods.randomizer(ad.General.darkColors),
		"buttonText": ad.Methods.randomizer(ad.General.words),
		"buttonSize": ad.Methods.randomizer(ad.QRtemp.sizes),
		"buttonBgColor": ad.Methods.randomizer(ad.General.lightColors),
		"buttonTextColor": ad.Methods.randomizer(ad.General.darkColors),
		"buttonHoverColor": ad.Methods.randomizer(ad.General.mediumColors),
		"buttonBorderColor": ad.Methods.randomizer(ad.General.darkColors),
		"fullName": ad.Methods.randomizer(ad.General.persons),
		"phoneNumber": ad.Methods.randomizer(ad.General.telNumbers),
		"alternativePhoneNumber": ad.Methods.randomizer(ad.General.telNumbers),
		"email": ad.Methods.randomizer(ad.General.emails),
		"website": ad.Methods.randomizer(ad.QRtemp.weblinks),
		"companyName": ad.Methods.randomizer(ad.General.companies),
		"jobPosition": ad.Methods.randomizer(ad.General.positions),
		"street": ad.Methods.randomizer(ad.General.words),
		"postalCode": ad.Methods.randomizer(ad.General.postalCodes),
		"city": ad.Methods.randomizer(ad.General.cities),
		"state": ad.Methods.randomizer(ad.General.words),
		"country": ad.Methods.randomizer(ad.General.countries),
		"links": socialLinks,
		"libraryId": ad.Methods.randomizer(ad.QRtemp.library_ids),
        },
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_qrCreate,
                                data=payload_json, headers=headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['name'] != None, "required name field value empty"
    assert resp_create.json()['codeType'] != None, "required codeType field value empty"

iterations = 5

count = 0
while True:
    count += 1
    create_qrcode()
    if count == iterations:
        break