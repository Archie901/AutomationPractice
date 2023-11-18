import requests
import json
import time
from data import Requests, Scans, Functions

def perform_scan():
    random_deviceId = Functions.randomizer(Scans.deviceIds)
    random_qrId = Functions.randomizer(Scans.dev_qrIds)
    print(random_qrId)
    #randomLat = Functions.randomizer(Scans.latitudes)
    #randomLng = Functions.randomizer(Scans.longitudes)
    #print("lat:", randomLat, "lng:", randomLng)    
    #randomUkrLat = Functions.randomizer(Scans.UkraineLats)
    #randomUkrLng = Functions.randomizer(Scans.UkraineLngs)
    #print("lat:", randomUkrLat, "lng:", randomUkrLng)
    payload_scan = {"deviceId": random_deviceId, "gps": {"lat": 26.1597, "lng": -6.1603, "accuracy": 33}}
    #payloadScan = {"deviceId": random_deviceId, "gps": {"lat": randomUkrLat, "lng": randomUkrLng, "accuracy": 33}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=Requests.dev_api_domain+Requests.path_scan+random_qrId, data=payload_json, headers=Requests.headers)
    print(resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None
    assert resp_scan.json()['name'] != None
    #print(resp_scan.text)

iterations = 1

count = 0
while True:
    count += 1
    perform_scan()
    time.sleep(1)
    if count == iterations:
        break