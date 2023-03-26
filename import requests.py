import requests

url = "https://api-dev.vororder.ch/api/auth/login-user"

payload={'email': 'nogapi@mailinator.com', 'password': 'Password-123'}

files=[]

headers = {
    'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)