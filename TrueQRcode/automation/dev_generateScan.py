import requests
import json
import time
from adata import Requests, Scans, Methods

def perform_scan():
    deviceId = Methods.randomizer(Scans.deviceIds)
    lat = Methods.randomizer(Scans.NorthAmerLats)
    lng = Methods.randomizer(Scans.NorthAmerLngs)
    dev_qrId = Methods.randomizer(Scans.dev_qrIds_Newest)
    #dev_qrId = Methods.randomizer(["D8MXM3NE","FBVMWTX4","V59U5YL2"])
    print("lat", lat, "---", "lng", lng)
    #print("device:", deviceId, "---", "qrId:", dev_qrId)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 100}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=Requests.dev_api_domain+Requests.path_scan+dev_qrId, data=payload_json, headers=Requests.headers)
    #print(resp_scan.text)
    print("scan request:", resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None
    assert resp_scan.json()['name'] != None

iterations = 15

count = 0
while True:
    count += 1
    perform_scan()
    if count == iterations:
        break