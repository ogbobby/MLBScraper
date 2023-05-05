from bs4 import BeautifulSoup
#import pandas as pd
from urllib.request import urlopen

url = "https://www.linestarapp.com/Ownership/Sport/MLB/Site/DraftKings"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', attrs={'class':'ownershipTable table table-condensed table-responsive sortable'})
print(table)
#print(soup.get_text())
