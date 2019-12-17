import requests
import json
from xlwt import *

url = "https://prodapi.metweb.ie/observations/valentia/yesterday"

response = requests.get(url)
data = response.json()

#creating a workbook
w = Workbook()
ws = w.add_sheet('weather')
rowNumber = 0;
ws.write(rowNumber,0,"name")
ws.write(rowNumber,1,"temperature")
ws.write(rowNumber,2,"weather")
ws.write(rowNumber,3,"wind speed")
ws.write(rowNumber,4,"date")
rowNumber += 1

#adding data into rows
for i in data:
    #print(i["name"])
    #print(i["temperature"])
    #print(i["weatherDescription"])
    #print(i["windSpeed"])
    #print(i["date"])
    ws.write(rowNumber,0,i["name"])
    ws.write(rowNumber,1,i["temperature"])
    ws.write(rowNumber,2,i["weatherDescription"])
    ws.write(rowNumber,3,i["windSpeed"])
    ws.write(rowNumber,4,i["date"])

    rowNumber += 1    
    
w.save('weather.xls')



#save it to a file
#file = 'weatherReport.json'

#write JSON data
#f = open(file, 'w')
#json.dump(data, f, indent=4)