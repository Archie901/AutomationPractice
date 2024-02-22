import requests
import json
import random
import pytest
import _main
import adata as ad

def randomizer(x):
    randomed = random.choice(x)
    return randomed

@pytest.fixture(scope='session')
def login():
    customer_email = ad.Creds.dev_customerCreds[8][0]
    customer_password = ad.Creds.dev_customerCreds[8][1]
    payload_login = {"authType": "TOKEN", "email": customer_email, "password": customer_password}
    payload_json = json.dumps(payload_login)
    resp_login = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_login,
                               data=payload_json, headers=ad.Requests.headers)
    #print(resp_login.text)
    print("login request:", resp_login.status_code, "/", resp_login.reason, "/", resp_login.elapsed)
    print("email from login response:", f"-- {resp_login.json()["email"]} --")
    assert resp_login.status_code == 200, "status code not 200"
    assert resp_login.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_login.json()['email'] == customer_email, "email does not match"
    assert resp_login.json()['id'] != None, "required id field value empty"
    assert resp_login.json()['role'] != None, "required role field value empty"
    pytest.user_id = resp_login.json()['id']
    pytest.user_email = resp_login.json()['email']
    access_token = resp_login.json()["accessToken"]
    pytest.headersToken = {
        "Content-Type": "application/json",
        "Accept-Encoding": "charset=utf-8",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + access_token
    }
    yield pytest.headersToken
    print("Tearing down the login fixture")

@pytest.fixture(scope='module')
def create_check_qrcode(login):
    payloadCreate = {
    "codeType": "WEBSITE",
	"name": randomizer(ad.QRtemp.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": randomizer(ad.QRtemp.sizes),
		"frameText": randomizer(ad.QRtemp.frameTexts),		
		"frameTextColor": randomizer(ad.General.mediumColors),
		"frameBackgroundColor": randomizer(ad.General.darkColors),
		"backgroundColor": randomizer(ad.General.lightColors),
		"patternColor": randomizer(ad.General.darkColors),
		"cornerColor": randomizer(ad.General.darkColors),
		"frameType": randomizer(ad.QRtemp.frameTypes),
		"patternType": randomizer(ad.QRtemp.patternTypes),
		"cornerType": randomizer(ad.QRtemp.cornerTypes),
        "libraryId": randomizer(ad.QRtemp.library_ids),
        },
	"website": {
		"url": randomizer(ad.QRtemp.weblinks)
        }
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_qrCreate,
                                data=payload_json, headers=pytest.headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['name'] != None, "required name field value empty"
    assert resp_create.json()['codeType'] != None, "required codeType field value empty"
    assert resp_create.json()['amountOfScans'] == 0, "initial scans not 0"
    assert resp_create.json()['totalDownloads'] == 0, "initial downloads not 0"
    pytest.cre_qr_id = resp_create.json()['id']
    cre_qr_name = resp_create.json()['name']
    cre_qr_type = resp_create.json()['codeType']
    
    resp_qrcheck = requests.get(url=ad.Requests.dev_api_domain+ad.Requests.path_qrSingle+pytest.cre_qr_id,
                                headers=pytest.headersToken)
    #print(resp_qrcheck.text)
    print("get qr request:", resp_qrcheck.status_code, "/", resp_qrcheck.reason, "/", resp_qrcheck.elapsed)
    assert resp_qrcheck.status_code == 200, "status code not 200"
    assert resp_qrcheck.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_qrcheck.json()['id'] == pytest.cre_qr_id, "qr id does not match"
    assert resp_qrcheck.json()['name'] == cre_qr_name, "qr name does not match"
    assert resp_qrcheck.json()['codeType'] == cre_qr_type, "qr type does not match"