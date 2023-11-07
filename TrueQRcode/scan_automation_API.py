import requests
import json
import random

domain = "https://api-trueqrcode-dev.osdb.io"

pathScan = "/api/v1/public/scans/"

headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}

deviceIds = ["adcd9ea5-071e-461e-b2e6-f7daa05f3ce5","3cc9cdfa-2d9d-4a53-b888-4163b3c7dfcc","9b9771b0-6951-4baf-bf27-9b4e50b9595a","274b3982-3f59-49e9-828c-f375dc4f4401",
            "afa6a281-aa61-4645-a873-e0714eebd956","e8706f40-786b-4b50-8d41-8f67d2d18207","a8a6458b-57db-4955-9385-2d841501a7a1","839d2dea-fd2c-45fb-aac1-6c24653096c2",
            "b2686576-f03d-4613-af13-e67382b7bb07","2b3574f3-36f9-4437-ba79-6194aa064577","0b5f8f40-154e-43e1-bbd1-443f87c0253a","0cd33c0e-0e08-4f1f-af95-3efc2a609405",
            "db539ce9-7214-440e-8cdf-4597641b1748","9d23030b-f710-4827-ae1b-15d58e996023","8fe55a98-5b84-43a5-bd21-dbe46ff8c42d","c529d496-87e9-430b-91c9-c64ce344f617",
            "2c9dbe98-2fc7-41a6-8efc-68eae04dacb5","87f2eebc-a6bd-4ed4-9255-eb03f26fb605","43d5afbb-685e-4de3-ba02-ff968e66c853","0ae323fa-cce0-461a-8232-e6dba77590b0"]

latitudes = [50.4101, 51.6998, 46.4075, 42.0003, 52.8823, 40.6473, 23.7252, 42.6824, 32.3985, 33.1375, -32.2499, -20.9614, 65.2934]

longitudes = [30.5303, 12.7441, 17.4462, 0.1318, -1.5820, 34.1015, 78.7500, -104.2382, -100.8984, 2.9882, -64.3359, 128.6718, 27.9492]

qr_ids = ["VFRRH3BR","8Q42EABK","5X5TAGX3","RE7A9F26","8JRQR839"]

def randomizer(x):
    return random.choice(x)

def perform_scan():

    randomDeviceId = randomizer(deviceIds)    
    randomQR_id = randomizer(qr_ids)
    randomLat = randomizer(latitudes)
    randomLng = randomizer(longitudes)
    #print(randomDeviceId)
    #print(randomQR_id)
    #print(randomLat, randomLng)

    payloadScan = {"deviceId": randomDeviceId, "gps": {"lat": randomLat, "lng": randomLng, "accuracy": 33}}

    json_paylodScan = json.dumps(payloadScan)

    resp_scan = requests.post(url=domain+pathScan+randomQR_id, data=json_paylodScan, headers=headers)
    #response from request must be received at this moment
    print(resp_scan.status_code, resp_scan.reason, resp_scan.elapsed)
    resp_qr_id = resp_scan.json()["id"]
    assert resp_scan.status_code == 200, "status code is not 200"
    assert resp_scan.reason == "OK", "status message is not OK"
    assert resp_qr_id == randomQR_id, "id is different"

iterations = 55

if __name__ == "__main__":
    count = 0
    while True:
        count += 1
        perform_scan()
        if count == iterations:
            break