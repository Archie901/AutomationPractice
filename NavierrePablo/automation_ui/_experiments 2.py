import requests
import json
import csv

headers = {"Content-Type": "application/json",
            "Accept-Encoding": "charset=utf-8",
            "Connection": "keep-alive"}

providers_list= requests.get(url="https://api-synergyhealth-dev.osdb.io/api/v1/public/ribbon-health/providers?gender=FEMALE&minRating=5",
                             headers=headers)

resp = providers_list.json()['result']

print(resp)

provider_info = []

npi = resp[0]['npi']

firstName = resp[0]['firstName']

lastName = resp[0]['lastName']

print(npi, firstName, lastName)

provider_info.insert(0, npi)

provider_info.insert(1, firstName)

provider_info.insert(2, lastName)

print(provider_info)

for each in providers_list.json()['result']:
    provider_info.insert(0, each['npi'])

print(provider_info)

'''with open('C:/Users/overk/Downloads/NPIs.csv', 'w', newline='') as file:
    for each in all_NPIs:
        stringed = str(each)
        file.write(stringed)
        file.write('\n')'''

'''for each in all_firstNames:
    print(each)'''

'''with open('C:/Users/overk/Downloads/NPIs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for each in all_firstNames:
        print(each)'''