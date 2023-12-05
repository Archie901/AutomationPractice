import requests
import json
from tdata import Requests, Scans, Methods

def test_perform_scan():
    deviceId = Methods.randomizer(Scans.deviceIds)
    lat = Methods.randomizer(Scans.EuropeLats)
    lng = Methods.randomizer(Scans.EuropeLngs)
    dev_qrId = Methods.randomizer(Scans.dev_qrIds)
    #print("lat", lat, "---", "lng", lng)
    #print("device:", deviceId, "---", "qrId:", dev_qrId)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 33}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=Requests.dev_api_domain+Requests.path_scan+dev_qrId, data=payload_json, headers=Requests.headers)
    #print(resp_scan.text)
    print("scan request:", resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None
    assert resp_scan.json()['name'] != None

# cd TrueQRcode/tests
# pytest test_dev_genScan.py -s -vv
# pytest --count=10 test_dev_genScan.py -s -vv