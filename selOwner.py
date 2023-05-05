
from selenium import webdriver

playas = []

driver = webdriver.Firefox()
driver.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
#table = driver.find_element_by_xpath('//td[@data-testid="ownershipPlayer"]')
table = driver.find_element_by_xpath('//tr[@data-testid="ownershipPlayerRow"]')
print(table)
# for p in range(len(table)):
#     playas.append(table[p].text)
#     print(playas)
#driver.quit()