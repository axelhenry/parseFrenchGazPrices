from urllib.request import urlopen
import bs4 as BeautifulSoup
import re
import json
import os
import sys

html = urlopen('http://www.carbeo.com/index.php/prixmoyens')
soup = BeautifulSoup.BeautifulSoup(html)
pricePattern = re.compile(r'(^\d+([,.]\d{1,3})?)')

tdOddTags = soup.findAll('tr',attrs={"class":u"officialPriceBe_odd"})

dict = {}
for elem in tdOddTags:
	name = elem.find('td', attrs={"class":u"officialPriceBe_col1"}).text
	price = elem.find('td',attrs={'class':None}).text
	# print(name," : ",price)
	regexedPrice = (pricePattern.search(price).groups()[0]).replace(',','.')
	# print(regexedPrice)
	dict[name] = regexedPrice
	# print("dict[",name,"]:",dict[name])

# print(json.dumps(dict,indent=4))
fileName = sys.argv[1]
with open(fileName,'w', encoding='utf-8') as f:
	json.dump(dict,f,indent=4)
