import requests
import time

N = 10000

def update_token():
    response = requests.get('http://localhost:5000/token/')
    if response.status_code == 200:
        token = response.json()['token']
        print('New token:', token)
        check_token(token)
    else:
        print('Failed to get token:', response.status_code)

def check_token(token):
    response = requests.post('http://localhost:5000/token/', json={'token': token})
    if response.status_code == 200:
        print('Token is valid')
    else:
        print('Token is invalid:', response.status_code)

while True:
    update_token()
    time.sleep(N / 5000)