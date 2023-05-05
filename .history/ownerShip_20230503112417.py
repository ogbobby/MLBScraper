from bs4 import BeautifulSoup
#import pandas as pd
from urllib.request import urlopen

url = "https://www.linestarapp.com/Ownership/Sport/MLB/Site/DraftKings"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', attrs={'class':'ownershipTable table table-striped table-condensed table-responsive sortable'})
table_body = table.find_all('tbody')
print(table_body)
rows = table_body.find('tr', attrs={'class':'playerRow'})
# tdata = rows.find_all('td')
# print(tdata)
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     #data.append([ele for ele in cols if ele])
#     print(cols)
#print(soup.get_text())
