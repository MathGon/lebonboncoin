import urllib
from BeautifulSoup import BeautifulSoup

def leboncoin_request(produit): 
	result_list = []
	url = "http://www.leboncoin.fr/annonces/offres/?f=a&th=1&q=kobo+mini"
	data = urllib.urlopen(url).read()
	soup = BeautifulSoup(data)
	soup = soup.prettify()
	line = soup.split("\n")
	for i in range(len(line)):
		chaine_a_chercher = "<div class=\"date\">"
		token = chaine_a_chercher in line[i]
		#print i, line [i]
		while token == True:
			lien = line[i-2].split("\"")[1]
			
			date = line[i+2].replace("  ", "")
			heure = line[i+5].replace("  ", "")
			
			desc = line[i+23].replace("  ", "")
			desc = desc.replace(" 6&quot;", "")
			desc = desc.replace("&#45;", "")
			
			ville = line[i+29].replace("  ", "")
			
			departement = line[i+34].replace("  ", "")
			
			prix = line[i+37].replace(" ", "")
			prix = prix.replace("&nbsp;&euro;", "")
			result = date, heure, ville, departement, desc, prix, lien
			result_list.append(result)
			token = False
		i += 37
	return result_list

print leboncoin_request("kobo+mini")
