import requests
import json

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportNamne=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-12-06"

response = requests.get(url)
data = response.json()

listOfReports = []

#output data
#print(data)
for i in data["items"]:
    print(i["ResourceName"])
    listOfReports.append(i["ResourceName"])


#save it to a file
file = 'allreports.json'

#write JSON data
f = open(file, 'w')
json.dump(data, f, indent=4)