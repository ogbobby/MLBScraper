from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
nameList = browser.find_elements_by_css_selector('div.table-container table.ownershipTablelb tbody')
table = browser.find_element_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
print(table)
#print("Title: %s" % browser.title)
browser.quit()