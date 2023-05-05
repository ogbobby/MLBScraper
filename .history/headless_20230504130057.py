from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#Create a function to go and grab the projection csv
def grabProjections():
    #make an browser object
    chromeOptions = Options()
    chromeOptions.headless = True
    getPro = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
    getPro.get("https://www.dailyfantasyfuel.com/mlb/projections/")
    #find the dl link and click on it
    getPro.find_element(by.linkText("Download")).click()
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
# #nameList = browser.find_elements_by_css_selector('div.table-container table.ownershipTablelb tbody tr.odd')
# # for i in nameList:
# #     print(i)
# table = browser.find_elements_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
# for i in table:
#     print(i.text)

grabProjections()
#print(nameList.text)
browser.quit()