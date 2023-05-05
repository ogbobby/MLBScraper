from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
#nameList = browser.find_elements_by_css_selector('div.table-container table.ownershipTablelb tbody tr.odd')
# for i in nameList:
#     print(i)
table = browser.find_element_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
for i in table:
    print(i.text)
#print(nameList.text)
browser.quit()