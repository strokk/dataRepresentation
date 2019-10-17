from bs4 import BeautifulSoup
import csv

with open("carviewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
#print (soup.tr)

employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
rows = soup.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    dataList = []
    for col in cols:
        dataList.append(col.text)

    employee_writer.writerow(dataList[:-2])
employee_file.close()