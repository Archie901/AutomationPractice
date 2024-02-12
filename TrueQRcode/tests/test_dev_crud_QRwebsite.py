import requests
import json
import pytest
from data import Requests, QRtemp, General
from fixtures import randomizer, login

def test_create_check_qrcode(login):
    payloadCreate = {
    "codeType": "WEBSITE",
	"name": randomizer(QRtemp.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": randomizer(QRtemp.sizes),
		"frameText": randomizer(QRtemp.frameTexts),		
		"frameTextColor": randomizer(General.mediumColors),
		"frameBackgroundColor": randomizer(General.darkColors),
		"backgroundColor": randomizer(General.lightColors),
		"patternColor": randomizer(General.darkColors),
		"cornerColor": randomizer(General.darkColors),
		"frameType": randomizer(QRtemp.frameTypes),
		"patternType": randomizer(QRtemp.patternTypes),
		"cornerType": randomizer(QRtemp.cornerTypes),
        "libraryId": randomizer(QRtemp.library_ids),
        },
	"website": {
		"url": randomizer(QRtemp.weblinks)
        }
    }
    payload_json = json.dumps(payloadCreate)
    resp_create = requests.post(url=Requests.dev_api_domain+Requests.path_qrCreate, data=payload_json, headers=pytest.headersToken)
    #print(resp_create.text)
    print("create request:", resp_create.status_code, "/", resp_create.reason, "/", resp_create.elapsed)
    assert resp_create.status_code == 200, "status code not 200"
    assert resp_create.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_create.json()['id'] != None, "required id field value empty"
    assert resp_create.json()['name'] != None, "required name field value empty"
    assert resp_create.json()['codeType'] != None, "required codeType field value empty"
    assert resp_create.json()['amountOfScans'] == 0, "initial scans not 0"
    assert resp_create.json()['totalDownloads'] == 0, "initial downloads not 0"
    cre_qr_id = resp_create.json()['id']
    cre_qr_name = resp_create.json()['name']
    cre_qr_type = resp_create.json()['codeType']
    cre_amountOfScans = resp_create.json()['amountOfScans']
    cre_totalDownloads = resp_create.json()['totalDownloads']

    resp_qrcheck = requests.get(url=Requests.dev_api_domain+Requests.path_qrSingle+cre_qr_id, headers=pytest.headersToken)
    print(resp_qrcheck.text)
    print("get qr request:", resp_qrcheck.status_code, "/", resp_qrcheck.reason, "/", resp_qrcheck.elapsed)
    assert resp_qrcheck.status_code == 200, "status code not 200"
    assert resp_qrcheck.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_qrcheck.json()['id'] == cre_qr_id, "qr id does not match"
    assert resp_qrcheck.json()['name'] == cre_qr_name, "qr name does not match"
    assert resp_qrcheck.json()['codeType'] == cre_qr_type, "qr type does not match"
    assert resp_qrcheck.json()['amountOfScans'] == cre_amountOfScans, "initial scans not 0"
    assert resp_qrcheck.json()['totalDownloads'] == cre_totalDownloads, "initial downloads not 0"

'''def test_update_check_qr_code():
    payloadUpdate = {
    "codeType": "WEBSITE",
	"name": randomizer(QRtemp.QRnames),
	"design": {
		"logoSize": 20,
        "frameTextSize": randomizer(QRtemp.sizes),
		"frameText": randomizer(QRtemp.frameTexts),		
		"frameTextColor": randomizer(General.mediumColors),
		"frameBackgroundColor": randomizer(General.darkColors),
		"backgroundColor": randomizer(General.lightColors),
		"patternColor": randomizer(General.darkColors),
		"cornerColor": randomizer(General.darkColors),
		"frameType": randomizer(QRtemp.frameTypes),
		"patternType": randomizer(QRtemp.patternTypes),
		"cornerType": randomizer(QRtemp.cornerTypes),
        "libraryId": randomizer(QRtemp.library_ids),
        },
	"website": {
		"url": randomizer(QRtemp.weblinks)
        }
    }
    payload_json = json.dumps(payloadUpdate)
    headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
           "Connection": "keep-alive", "Authorization": "Bearer " + Requests.access_token}
    resp_update = requests.patch(url=Requests.dev_api_domain+Requests.path_qrSingle+cre_qr_id, data=payload_json, headers=headersToken)
    #print(resp_update.text)
    print("update request:", resp_update.status_code, "/", resp_update.reason, "/", resp_update.elapsed)
    assert resp_update.status_code == 200, "status code not 200"
    assert resp_update.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_update.json()['id'] != None, "required field value empty"
    assert resp_update.json()['name'] != None, "required field value empty"
    assert resp_update.json()['codeType'] != None, "required field value empty"
    global upd_qr_id, upd_qr_name, upd_qr_type
    upd_qr_id = resp_update.json()['id']
    upd_qr_name = resp_update.json()['name']
    upd_qr_type = resp_update.json()['codeType']

    resp_qrcheck = requests.get(url=Requests.dev_api_domain+Requests.path_qrSingle+cre_qr_id, headers=headersToken)
    print("get qr request:", resp_qrcheck.status_code, "/", resp_qrcheck.reason, "/", resp_qrcheck.elapsed)
    #print(resp_qrcheck.text)
    assert resp_qrcheck.status_code == 200, "status code not 200"
    assert resp_qrcheck.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_qrcheck.json()['id'] == upd_qr_id, "qr id does not match"
    assert resp_qrcheck.json()['name'] == upd_qr_name, "qr name does not match"
    assert resp_qrcheck.json()['codeType'] == upd_qr_type, "qr type does not match"

def test_delete_check_qr_code():
    headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
           "Connection": "keep-alive", "Authorization": "Bearer " + Requests.access_token}
    resp_delete = requests.delete(url=Requests.dev_api_domain+Requests.path_qrSingle+upd_qr_id, headers=headersToken)
    #print(resp_delete.text)
    print("delete request:", resp_delete.status_code, "/", resp_delete.reason, "/", resp_delete.elapsed)
    assert resp_delete.status_code == 204, "status code not 204"

    resp_qrcheck = requests.get(url=Requests.dev_api_domain+Requests.path_qrSingle+upd_qr_id, headers=headersToken)
    #print(resp_qrcheck.text)
    print("get qr request:", resp_qrcheck.status_code, "/", resp_qrcheck.reason, "/", resp_qrcheck.elapsed)
    assert resp_qrcheck.status_code == 400, "status code not 400"
    assert resp_qrcheck.json()['errors'][0]['message'] == "Qr code has been deleted", "delete message is different/absent"
    
# cd TrueQRcode/tests
# pytest test_dev_crud_QRwebsite.py -s -vv
# pytest --count=10 test_dev_crud_QRwebsite.py -s -vv'''