import requests
import json
import random

domain = "https://demoqa.com"
endpoint_login = "/Account/v1/Login"
endpoint_onebookinfo = "/BookStore/v1/Book"
endpoint_addonebook = "/BookStore/v1/Books"
endpoint_deleteallbooks = "/BookStore/v1/Books"

payload_login_creds = {"userName": "archie@mailinator.com","password": "Qwerty123!"}

books_isbns = (9781449325862, 9781449331818, 9781449337711, 9781449365035,
               9781491904244, 9781491950296, 9781593275846, 9781593277574)

def login():
    resp_login = requests.post(url=domain+endpoint_login, data=payload_login_creds)
    global userId, token
    userId = resp_login.json()["userId"]
    token = resp_login.json()["token"]
    username = resp_login.json()["username"]    
    print(resp_login.status_code, resp_login.reason)
    print("Logged-in user:", resp_login.json()["username"], resp_login.json()["userId"])

    assert resp_login.status_code == 200, "status code is not 200"
    assert resp_login.reason == "OK", "status message is not OK"
    assert username == payload_login_creds["userName"], "username is different"

def userinfo():
    endpoint_userinfo = f"/Account/v1/User/{userId}"
    global headers
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    resp_userinfo = requests.get(url=domain+endpoint_userinfo, headers=headers)
    username = resp_userinfo.json()["username"]
    user_id_resp = resp_userinfo.json()["userId"]
    books = []
    for title in resp_userinfo.json()["books"]:
        books.append((title['title'], title['isbn']))
    #books_pretty = json.dumps(books, indent=4)
    print(resp_userinfo.status_code, resp_userinfo.reason)
    print(f"Added books for {username}:", len(books), books)

    assert resp_userinfo.status_code == 200, "status code is not 200"
    assert resp_userinfo.reason == "OK", "status message is not OK"
    assert userId == user_id_resp, "user id is different"

def onebookinfo():
    params = {'ISBN': books_isbns[1]}
    resp_onebookinfo = requests.get(url=domain+endpoint_onebookinfo, headers=headers, params=params)
    resp_pretty = json.dumps(resp_onebookinfo.json(), indent=4)
    print(resp_onebookinfo.status_code, resp_onebookinfo.reason)
    print(resp_pretty)
    
def addonebook():
    randomized_book = random.choice(books_isbns)
    payload_addonebook = {"userId": userId, "collectionOfIsbns": [{"isbn": randomized_book}]}
    payload_changed = json.dumps(payload_addonebook)
    resp_addonebook = requests.post(url=domain+endpoint_addonebook, data=payload_changed, headers=headers)
    print(resp_addonebook.status_code, resp_addonebook.reason)
    print(resp_addonebook.text)

def deleteallbooks():
    params = {'UserId': userId}
    resp_deleteallbooks = requests.delete(url=domain+endpoint_deleteallbooks, headers=headers, params=params)
    print(resp_deleteallbooks.status_code, resp_deleteallbooks.reason)

login()
userinfo()
onebookinfo()
#addonebook()
#deleteallbooks()
#userinfo()

headersing = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Host": "httpbin.org",
    "User-Agent": "A completely unknown user agent"
    }

r = requests.get(url='https://httpbin.org/headers', headers=headersing)

print(r.text)
print(r.headers)