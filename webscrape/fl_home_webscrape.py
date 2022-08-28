from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from random import randint
from time import sleep


my_url = 'https://www.realtor.com/realestateandhomes-search/Florida'

req = Request(my_url, headers={'User-Agent':'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

#Getting containers for properties
prop_containers = page_soup.findAll("div", {"data-label":"property-card"})

#Creating the csv
filename = "Florida_Homes.csv"
f = open(filename, "w")

headers = "Status, Price, Beds, Bath, Sq_feet, Acre-Sqft_Lot, Address, Second Address, Zip"

f.write(headers + "\n")

for pgNum in range(1,200):
	my_url = 'https://www.realtor.com/realestateandhomes-search/Florida/pg-' + str(pgNum)

	req = Request(my_url, headers={'User-Agent':'Mozilla/5.0'})
	webpage = urlopen(req).read()
	page_soup = soup(webpage, "html.parser")
	#Getting containers for properties

	prop_containers = page_soup.findAll("div", {"data-label":"property-card"})
	for prop_container in prop_containers:
		try:
			container_status = prop_container.findAll("span",{"class":"statusText"})
			container_price = prop_container.findAll("span",{"data-label":"pc-price"})
			container_beds = prop_container.findAll("li",{"data-label":"pc-meta-beds"})
			container_baths = prop_container.findAll("li",{"data-label":"pc-meta-baths"})
			container_sqft = prop_container.findAll("li",{"data-label":"pc-meta-sqft"})
			container_acre_sq_lot = prop_container.findAll("li",{"data-label":"pc-meta-sqftlot"})
			container_full_address = prop_container.findAll("div",{"data-label":"pc-address"})

			#Values that are in the containers, written to csv
			prop_status = container_status[0].getText()
			prop_price = container_price[0].getText()
			prop_beds = container_beds[0].span.getText()
			prop_baths = container_baths[0].span.getText()
			prop_sqft = container_sqft[0].span.getText()
			prop_acre_sq_lot_num = container_acre_sq_lot[0].span.getText()
			prop_acre_sq_lot_val = container_acre_sq_lot[0].findAll("span")[1].getText()
			prop_full_address = container_full_address[0].getText()
			prop_second_address = container_full_address[0].div.getText()
			prop_zip = prop_second_address[-5:]

			#Print Values
			print("Status: " + prop_status)
			print("Price: " + prop_price)
			print("Beds: " + prop_beds)
			print("Bath: "+ prop_baths )
			print("Sq Feet: " + prop_sqft)
			print("Acre/Sqft Lot: " + prop_acre_sq_lot_num + prop_acre_sq_lot_val)
			print("Address: " + prop_full_address)
			print("Second Address: " + prop_second_address)
			print("Zip: " + prop_zip + "\n")

			#Write To file
			f.write(prop_status.replace(",", ";") + "," + prop_price.replace(",", "") + "," + prop_beds + "," + prop_baths + "," + 
				prop_sqft.replace(",", "") + "," + prop_acre_sq_lot_val.replace(",", "") + "," + prop_full_address.replace(",",";") + "," + 
				prop_second_address.replace(",",";")  + "," + prop_zip +"\n")
		except:
			print("no value")

	x = randint(35,120)
	sleep(x)

f.close()