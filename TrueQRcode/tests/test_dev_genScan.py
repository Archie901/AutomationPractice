import requests
import json
import pytest
import _main
import adata as ad
from fixtures import randomizer

def test_scan1():
    deviceId = randomizer(ad.Scans.deviceIds)
    lat = randomizer(ad.Scans.EuropeLats)
    lng = randomizer(ad.Scans.EuropeLngs)
    dev_qrId = randomizer(ad.QRids.dev_qrIds_Selovi)
    #print("lat", lat, "---", "lng", lng)
    #print("device:", deviceId, "---", "qrId:", dev_qrId)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 33}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_scan+dev_qrId,
                              data=payload_json, headers=ad.Requests.headers)
    #print(resp_scan.text)
    print("scan request:", resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None, "required id field value empty"
    assert resp_scan.json()['name'] != None, "required name field value empty"

def test_scan2():
    deviceId = randomizer(ad.Scans.deviceIds)
    lat = randomizer(ad.Scans.AsiaLats)
    lng = randomizer(ad.Scans.AsiaLngs)
    dev_qrId = randomizer(ad.QRids.dev_qrIds_Selovi)
    #print("lat", lat, "---", "lng", lng)
    #print("device:", deviceId, "---", "qrId:", dev_qrId)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 33}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=ad.Requests.dev_api_domain+ad.Requests.path_scan+dev_qrId,
                              data=payload_json, headers=ad.Requests.headers)
    #print(resp_scan.text)
    print("scan request:", resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None, "required id field value empty"
    assert resp_scan.json()['name'] != None, "required name field value empty"

# cd Trueqrcode/tests
# pytest -s -vv test_dev_genScan.py
# pytest -s -vv --setup-show test_dev_genScan.py
    
if __name__ == '__main__':
    pytest.main(["-s", "-vv", "Trueqrcode/tests/test_dev_genScan.py"])