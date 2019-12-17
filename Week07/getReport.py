from xlwt import *
import requests
import json

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportNamne=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10<=2019-11-11"

response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page=" + str(pageNumber)
    data = requests.get(pageUrl).json()
    for i in data["items"]:
        print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])
    pageNumber +=1

w = Workbook()
ws = w.add_sheet('reports')
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1

for ReportName in listOfReports:
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName
    response = requests.get(url)
    aReport = response.json()
    for row in aReport["rows"]:
        #print(row["ImbalancePrice"])
        ws.write(rowNumber,0,row["StartTime"])
        ws.write(rowNumber,1,row["EndTime"])
        if "ImbalanceVolume" in row:
            ws.write(rowNumber,2,row["ImbalanceVolume"])
        if "ImbalanceVolume" in row:
            ws.write(rowNumber,3,row["ImbalancePrice"])
        if "ImbalanceVolume" in row:
            ws.write(rowNumber,4,row["ImbalanceCost"])
        rowNumber += 1    
w.save('balance.xls')

#save it to a file
#file = 'allreports.json'
#
##write JSON data
#f = open(file, 'w')
#json.dump(data, f, indent=4)