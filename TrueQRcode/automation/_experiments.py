import requests
import json
import time
from dev_authorization import access_token

headersToken = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8",
                "Connection": "keep-alive", "Authorization": "Bearer " + access_token}

def some_request():
    resp_request = requests.get(
        url="https://api-dev.trueqrcode.com/api/v1/private/library?libraryType=DESIGN_LOGO",
        headers=headersToken)
    print("request:", resp_request.status_code, "/", resp_request.reason, "/", resp_request.elapsed)
    formatted = resp_request.json()['result']
    #print(formatted)
    library_ids = []
    for value in formatted:
        library_ids.append(value['id'])
    print(library_ids)

some_request()