#this is how i had to install bs4 for python 3.9.1:  python3 -m pip install bs4
#that is the version of python that is set for the working dir, pandas required a high version of python
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import requests
import re

projectionHeader = []
projectionColumn = []
#i need to create some variables or some way to just change the year and week on the url
#2017,2018,2019,2020,2021,2022
#week 1-17
#this whole thing needs to be wrapped inside a function
def grabData():
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    url = "https://www.footballdb.com/fantasy-football/index.html?pos=OFF&yr=2017&wk=8&key=48ca46aa7d721af4d58dccc0c249a1c4"
    page = requests.get(url, headers=HEADERS)
    page = page.text
    # html = page.read().decode("utf-8")
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find('table', attrs={'class':'statistics scrollable'})
    #need to grab the headers of the table
    table_header = table.find('tr', attrs={'class':'header right'})
    for i in table_header:
        #print(i.text)
        projectionHeader.append(i.text)

    #need to remove empty elements from list
    while("\n" in projectionHeader):
        projectionHeader.remove("\n")

    #grab the stat data
    table_body = table.find('tbody')
    rows = table_body.findAll('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        projectionColumn.append(cols)
    #this is where we need to clean up the player names in our list before we make the dataframe, this is our regex /[A-Z]\W.[a-z][a-z](.+?)'
    #or this /[A-Z]\W\S[A-Z].+
    #regex = re.compile("/[A-Z]\W.[a-z][a-z](.+?)'$")
    regex = re.compile("[A-Z]\W.[A-Z].+")
    # for a in projectionColumn:
    #     newNames = [a[0]]
    #     #filtered = [i for i in newNames if not regex.match(i)]
    #     filtered = filter(None, [re.sub(regex, r"", i) for i in newNames])
    #     for b in filtered:
    #         print(b)
    for a in projectionColumn:
        new_name = a[0]
        filtered = re.sub(regex, "", new_name)
        if filtered:
            print(filtered)  
grabData()
#print(projectionColumn)
#after we get the headers and the table data we will put it into a pandas dataframe
#df = pd.DataFrame(projectionColumn, columns=projectionHeader)
#print(df)