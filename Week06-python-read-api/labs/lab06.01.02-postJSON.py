import requests
import json

dataString = {'reg': '09 K 1920', 'make': 'Ford', 'model': 'Focus', 'price': 20000}
url = 'http://127.0.0.1:5000/cars'
response = requests.post(url, json=dataString)
print(response.status_code)


