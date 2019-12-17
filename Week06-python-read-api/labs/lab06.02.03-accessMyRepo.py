import requests
import json   


apiKey = '046409310a8a704d763485cae89de603be03876f'
url = 'https://api.github.com/repos/strokk/datarep_private'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print(response.json())

#file = open("filename.txt", 'w')
#json.dummp(repoJSON, file, indent=4)

file = 'myrepo.json'
with open(file, 'w') as f:
    json.dump(repoJSON, f, indent=4)

    