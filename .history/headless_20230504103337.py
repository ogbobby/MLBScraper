from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
nameList = browser.find_elements_by_css_selector('div.table-container table.ownershipTablelb tbody tr.odd')
print(nameList)
# for i in nameList:
#     print(i)
#table = browser.find_element_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
#print(nameList.text)
#print("Title: %s" % browser.title)
browser.quit()