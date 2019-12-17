import requests
import json   


apiKey = '8c0e5202752a9f00b139b7d0f36bd79f75741975'
url = 'https://api.github.com/datarepresentationstudent/aPrivateOne'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print(response.json())

#file = open("filename.txt", 'w')
#json.dummp(repoJSON, file, indent=4)

file = 'datarep.json'
with open(file, 'w') as f:
    json.dump(repoJSON, f, indent=4)