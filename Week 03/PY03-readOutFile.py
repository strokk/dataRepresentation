from bs4 import BeautifulSoup

with open("carviewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print(soup.tr)

rows = soup.find_all("tr")
for row in rows:
    print("-----")
    #print(row)
    cols = row.find_all("td")
    for col in cols:
        print(col.text)


dataList = []
for col in cols:
    dataList.append(col.text)

print(dataList)