import requests

url = "https://api-dev.vororder.ch/api/auth/login-admin"

payload={'email': 'admin@gmail.com', 'password': 'Password-123'}

files=[]

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjJiY2Q4MzM0NTgyMmJlYzU3YTcxNDM4MTg1MWE3MTU3ZWEyZDEyZmQwNDE3OTMxZmE1YzkxODEwOWRmNWU5MjZmNzY5MGZhMjAxYjNkZjgiLCJpYXQiOjE2Nzg0ODU0NDguMTgzMDU1LCJuYmYiOjE2Nzg0ODU0NDguMTgzMDYsImV4cCI6MTcxMDEwNzg0OC4xNzg4MjMsInN1YiI6IjE1MCIsInNjb3BlcyI6W119.RkTo4kPJotfSmo12GmqZsHOYCG--WZ-Vj9cF_B3tAzZgm17IMuaqYnK8WyTXT6lKLwZ5Y2KnbNacaINVGOtOZdYhm-CQHDYpfyf1wc9IMvo4TRIcCPPGVIiYWPF3Ov6cJpD-QyC3_hiWI0ANlDwliD_rbGPEoOdgz_GBUzIW6gmbzWXG2JxWawo3TdcLecDL6GVTnFMlbIDAeg2tggV5yeObBWVZDuLLAHd5mzK65_QDReVKy9qXj3CTUUNJops6vt58J9xeqsa0WFYMqsXn4Sh3AUMUnqnrPpswAkiE4rFeoHUSxLjaKJ2uMLIeJxOtFuWPZsOCD7pt3iJ7RcymQ1iS8smWtsy6nvuqAo6lnZEbKmkOm9Q1CrYOi6WHFZTC1ZK8U79d27EodcJB2u1tB-74RRFyXP4L2tbeYXzdJkxjcWO9KNa8Joz8iS8_wfcbbrTjd8m6Vwktjl2peV28gJD4Ummu3IS4AmvcE-r8w3KMZ37Q_Pfi06IlrZ7Rmoe50ZoqH4h_atF4MnzwUAPUpXy8LmDq5A1wHsuE7e0uWvpRh9JKyH2C1lpbaBfnex8qbF1C4-ipucXHvtDZrfW3CMwZWx1-GgOpGNjj6bVlV1UX-FvX7bCc8tpPJFrjDJXY51A-lX1tTbYk7LQ4rO_QbHy7f-li_J5gcKp0IMsHXho'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
