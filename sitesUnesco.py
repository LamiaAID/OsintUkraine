import string
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import urllib.parse


req = requests.get(url='https://www.unesco.org/fr/articles/sites-culturels-endommages-en-ukraine-confirmes-par-lunesco')
soup = BeautifulSoup(req.text, 'html.parser')
#data = soup.find_all("div",{"class":"field__item"})[0]
data = soup.find_all("ol")
#print(data)
liste = []
for row in data: 
    liste.append(row.get_text().split('\n'))


liste_emplty = [string for string in liste if string != ""]
liste_emplty = pd.DataFrame(liste_emplty)
liste_emplty.to_csv('siteBrut.csv',encoding='utf-8-sig')