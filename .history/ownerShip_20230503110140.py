from bs4 import BeautifulSoup
#import pandas as pd
from urllib.request import urlopen

url = "https://www.linestarapp.com/Ownership/Sport/MLB/Site/DraftKings"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
soup.find_all("table")
#print(soup.get_text())
