from bs4 import BeautifulSoup
#import pandas as pd
from urllib.request import urlopen

url = "https://fantasyteamadvice.com/dfs/mlb/ownership"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
table = soup.find('table', attrs={'class':'table-container'})
print(table)
# table_body = table.find('tbody')
# rows = table_body.find('tr', attrs={'class':'playerRow'})
# tdata = rows.find_all('td')
# print(tdata)
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     #data.append([ele for ele in cols if ele])
#     print(cols)
