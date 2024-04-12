import requests
import json
import random

def randomizer(x):
        randomed = random.choice(x)
        return randomed

headers = {"Content-Type": "application/json",
            "Accept-Encoding": "charset=utf-8",
            "Connection": "keep-alive"}

def requester():
    
    resp_lvl1 = requests.get(url="https://api-synergyhealth-dev.osdb.io/api/v1/public/pablo/services?level=1",
                             headers=headers)

    list_lvl1 = []

    for each in resp_lvl1.json()['pabloServices']['result']:
        list_lvl1.append(each)

    global random_lvl1

    random_lvl1 = randomizer(list_lvl1)

    print(random_lvl1)

    resp_lvl2 = requests.get(url=f"https://api-synergyhealth-dev.osdb.io/api/v1/public/pablo/services?level=2&groupIds={random_lvl1['id']}",
                             headers=headers)
    
    list_lvl2 = []

    for each in resp_lvl2.json()['pabloServices']['result']:
        list_lvl2.append(each)

    global random_lvl2

    random_lvl2 = randomizer(list_lvl2)

    print(random_lvl2)
    
    resp_lvl3 = requests.get(url=f"https://api-synergyhealth-dev.osdb.io/api/v1/public/pablo/services?level=3&groupIds={random_lvl2['id']}",
                             headers=headers)
    
    list_lvl3 = []

    for each in resp_lvl3.json()['pabloServices']['result']:
        list_lvl3.append(each)

    global random_lvl3_1
    global random_lvl3_2
    global random_lvl3_3

    random_lvl3_1 = randomizer(list_lvl3)
    random_lvl3_2 = randomizer(list_lvl3)
    random_lvl3_3 = randomizer(list_lvl3)

    print(random_lvl3_1['title'])
    print(random_lvl3_2['title'])
    print(random_lvl3_3['title'])

requester()