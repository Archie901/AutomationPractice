import requests
import json
import random
import time

domain = "https://api.trueqrcode.com"

pathScan = "/api/v1/public/scans/"

headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}

deviceIds = ["8c115a70-4d48-4f47-8245-86ffaffe5d16","2552d0b2-ecfc-4cf1-8378-58646860014c","0f93dd8b-7530-40bc-af78-d3ea5cba77d7","42209e25-daab-4d2e-9a07-7e27eba4076b",
            "4cccc522-c895-4050-becf-a9d652835f4c","fa641144-9ee9-4258-861d-f5508b03cdf5","e7d699f3-fdc8-4bad-8385-5ac6007d4f9d","47aee305-ee67-4140-a719-e43602ed3d7c",
            "52b694d1-824d-4dd9-96c7-8971ef822727","9cb1e2f8-3838-4c10-a9fd-04aa4c5928a7","5d3e90cc-6bbf-4ed7-9eef-ba0fa90fb85c","5303374c-a893-4979-a444-6e12167c7d25",
            "fb616704-34a0-488b-9dc4-e47d31d1d498","ff61d0b4-105b-4757-9da9-c9c8d81a46c0","f99f6959-55c6-4e6b-8f88-739d59aaba0d","0626aee7-e1d4-43b3-91a1-2f9275cab258",
            "d449624c-930a-4cc0-bac7-81bd215e49fe","5fde1645-79b5-4ed1-89c7-6f5b545dd6a0","f0357f62-5144-4fbb-b9ca-5c902fd75379","a470d86f-253c-4ec7-831e-8a146c88be36"]

latitudes = [50.4101, 51.6998, 46.4075, 42.0003, 52.8823, 40.6473, 42.6824, 32.3985, 33.1375, 65.2934]

# additional latitudes which are not typical -32.2499, -20.9614, 23.7252

longitudes = [30.5303, 22.1318, 24.1318, 21.1015, 20.7500, 23.4462, 29.6718, 27.9492, 31.8813, 28.1299]

# additional longitudes which are not typical 02.9882, 12.7441, 17.4462, -33.5820, -33.5820, -104.2382, -100.8984, -64.3359

UkraineLats = [50.4101, 48.3794, 49.1223, 51.2146, 50.0004, 48.0266, 51.0909]

UkraineLngs = [30.5303, 25.9813, 32.8711, 31.9090, 26.7777, 28.7545, 26.9876]

qr_ids = ["3ZHPT5K8","CZNR1FS1"]

def randomizer(x):
    return random.choice(x)

def perform_scan():

    randomDeviceId = randomizer(deviceIds)    
    randomQR_id = randomizer(qr_ids)
    
    randomLat = randomizer(latitudes)
    randomLng = randomizer(longitudes)
    print(randomQR_id, "/ lat:", randomLat, "/ lng:", randomLng)
    
    #randomUkrLat = randomizer(UkraineLats)
    #randomUkrLng = randomizer(UkraineLngs)    
    #print(randomQR_id, "/ lat:", randomUkrLat, "/lng:", randomUkrLng)
     
    payloadScan = {"deviceId": randomDeviceId, "gps": {"lat": 22.3318, "lng": 20.3687, "accuracy": 33}}
    
    #payloadScan = {"deviceId": randomDeviceId, "gps": {"lat": randomUkrLat, "lng": randomUkrLng, "accuracy": 33}}

    json_payloadScan = json.dumps(payloadScan)
    resp_scan = requests.post(url=domain+pathScan+randomQR_id, data=json_payloadScan, headers=headers)
    print(resp_scan.status_code, "/", resp_scan.reason, "/", resp_scan.elapsed)
    #print(resp_scan.json())
    assert resp_scan.status_code == 200, "status code not 200"
    assert resp_scan.headers['Content-Type'] == "application/json", "content type not application/json"
    assert resp_scan.json()['id'] != None
    assert resp_scan.json()['name'] != None
    
iterations = 5

count = 0
while True:
    count += 1
    perform_scan()
    time.sleep(1)
    if count == iterations:
        break