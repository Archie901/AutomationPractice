import requests
import json
import time
import _main
import adata as ad

def scan():
    deviceId = ad.Methods.randomizer(ad.Scans.deviceIds)
    lat = ad.Methods.randomizer(ad.Scans.NorthAmerLats)
    lng = ad.Methods.randomizer(ad.Scans.NorthAmerLngs)
    dev_qrId = ad.Methods.randomizer(ad.QRids.prod_qrIds_Mykemo)
    #dev_qrId = ad.Methods.randomizer(["D8MXM3NE","FBVMWTX4","V59U5YL2"])
    print("lat", lat, "---", "lng", lng)
    #print("device:", deviceId, "---", "qrId:", dev_qrId)
    payload_scan = {"deviceId": deviceId, "gps": {"lat": lat, "lng": lng, "accuracy": 100}}
    payload_json = json.dumps(payload_scan)
    resp_scan = requests.post(url=ad.Requests.prod_api_domain+ad.Requests.path_scan+dev_qrId,
                              data=payload_json, headers=ad.Requests.headers)
    #print(resp_scan.text)
    print("scan request:", resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)    
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None, "required id field value empty"
    assert resp_scan.json()['name'] != None, "required name field value empty"

iterations = 10

count = 0
while True:
    count += 1
    scan()
    if count == iterations:
        break