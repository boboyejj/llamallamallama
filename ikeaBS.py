import urllib.request, urllib.parse, urllib.error
import re
import datetime
from bs4 import BeautifulSoup
import json

import ssl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://www.ikea.com/us/en/catalog/categories/departments/decoration/10759/'
ssl._create_default_https_context = ssl._create_unverified_context
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
names = soup.find_all(class_="productTitle floatLeft")
des = soup.find_all(class_="productDesp")
prices = soup.find_all(class_="price regularPrice")
#special = soup.find_all(class_= "floatLeft prodPrice")
length = len(names)
inventory = {}

#find the date
d = datetime.date.today()
d = re.findall('[0-9]+', str(d))
time = d[0]+'.'+d[1]+'.'+d[2]


for i in range(0,length):
	name = names[i].get_text() + ' ' + des[i+1].get_text()

	price = prices[i].get_text()	
	price = re.findall('[0-9]+.[0-9]+', price)
	data = {}
	data[time] = price[0]
	inventory[name] = data

dates = ['2017.10.16', '2017.09.13', '2017.08.28', '2017.07.22', '2017.07.05', '2017.06.10',
'2017.05.25', '2017.04.15']

snofsa = 'SNOFSA table clock'
pugg = 'PUGG wall clock'
slip = 'SLIPSTEN wall clock'
bondis = 'BONDIS wall clock'
klocki = 'KLOCKIS clock/thermometer/alarm/timer'
bravur = 'BRAVUR wall clock'
viki = 'VIKIS alarm clock'
dekad = 'DEKAD alarm clock'
braller = 'BRALLER alarm clock'
tjalla = 'TJALLA wall clock'
sondrum = 'SÖNDRUM wall clock'

for key, value in inventory.items():
	if(key == snofsa):
		for d in dates:
			if(d == '2017.07.22'):
				break
			value[d] = 12.99
	elif(key == pugg):
		for d in dates:
			value[d] = 12.99
	elif(key == slip):
		for d in dates:
			if(d == '2017.07.22'):
				break
			value[d] = 9.99
	elif(key == bondis):
		for d in dates:
			value[d] = 19.99
	elif(key == klocki):
		for d in dates:
			value[d] = 4.99
	elif(key == bravur):
		for d in dates:
			value[d] = 49.99
	elif(key == viki):
		for d in dates:
			if (d >= '2017.07.22'):
				value[d] = 9.99
			else:
				value[d] = 8.99
	elif(key == dekad):
		for d in dates:
			value[d] = 6.99
	elif(key == braller):
		for d in dates:
			value[d] = 5.99
	elif(key == tjalla):
		for d in dates:
			if(d == '2017.07.22'):
				break
			value[d] = 9.99
	elif(key == sondrum):
		for d in dates:
			value[d] = 49.99


	print(value)


with open('data.json','w', encoding='utf8') as outfile:
	json.dump(inventory, outfile, ensure_ascii=False)
	