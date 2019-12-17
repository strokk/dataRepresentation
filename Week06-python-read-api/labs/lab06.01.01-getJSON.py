#gets all the cars from the server

import requests

url = 'http://127.0.0.1:5000/cars'

response = requests.get(url)
data = response.json()

#print data
for car in data['cars']:
    print(car)


#other code
import json

#save it to a file
file = 'cars.json'
if file:
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

#save it to excel file
from xlwt import *
w = Workbook()
ws = w.add_sheet('cars')
row = 0
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1
for car in data['cars']:
    ws.write(row,0,car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1
w.save('cars.xls')