import requests
import json
import time
from adata import Requests, Scans

def perform_scan():
    deviceId = Scans.randomDeviceId()
    lat = Scans.randomLat()
    lng = Scans.randomLng()
    qrId = Scans.dev_randomQRid()
    print("lat:", lat, "lng:", lng)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 33}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=Requests.dev_api_domain+Requests.path_scan+qrId, data=payload_json, headers=Requests.headers)
    print(resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None
    assert resp_scan.json()['name'] != None
    #print(resp_scan.text)

iterations = 13

count = 0
while True:
    count += 1
    perform_scan()
    if count == iterations:
        break