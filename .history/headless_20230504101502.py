from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://fantasyteamadvice.com/dfs/mlb/ownership")
print("Title: %s" % browser.title)
browser.quit()