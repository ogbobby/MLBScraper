from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#import pandas as pd
import time

#make blank list to append ownership data too
ownership = []

#Create a function to go and grab the projection csv
def grabProjections():
    #make an browser object
    chromeOptions = Options()
    chromeOptions.headless = True
    getPro = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
    getPro.get("https://www.dailyfantasyfuel.com/mlb/projections/")
    #find the dl link and click on it
    getPro.find_element_by_xpath('//span[@class="hov-underline"]').click()
    #getPro.find_element_by_link_text("CSV").click()
    #getPro.find_element_by_css_selector('a.target._blank').click()
    time.sleep(4)
    getPro.quit()

def grabOwnership():
    chromeOptions = Options()
    chromeOptions.headless = True
    browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
    browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
    table = browser.find_elements_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
    for i in table:
        #print(i.text)
        ownership.append(i.text)
        time.sleep(8)


        browser.quit()

grabProjections()
grabOwnership()
print(ownership)