import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')


#listings = soup.find("div", class_="PropertyListingCard")
#price = listings.find(class_="PropertyListingCard__Price").text
#address = listings.find(class_="PropertyListingCard__Address").text
#print(price, address)

listings = soup.find_all("div", class_="PropertyListingCard")

for listing in listings:
    entry = []
    price = listing.find(class_="PropertyListingCard__Price").text
    address = listing.find(class_="PropertyListingCard__Address").text
    entry.append(price)
    entry.append(address)

print(entry)

import csv
home_file = open('week')