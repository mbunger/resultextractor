from bs4 import BeautifulSoup

import requests
print "Extrator starting"



r = requests.get("http://www.resultat.dk/fodbold/danmark/superliga/resultater")

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('div'):
	if link.get('id') == 'fs-results':
		print 'found one'
		

table = soup.find('table', {'class' : 'soccer'})

for row in table.findAll('td'):
	print 'found many'
