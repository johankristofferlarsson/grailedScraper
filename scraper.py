from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import requests
import time
import re

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("http://grailed.com/len")

file = open("listings.txt", "w")


time.sleep(1.5)
int num = 0

for listing in driver.find_elements_by_class_name('feed-item'):
	designer = listing.find_element_by_class_name('listing-designer').text
	name = listing.find_element_by_class_name('listing-title').text
	price = listing.find_element_by_class_name('listing-price').text
	price = re.findall("\d+", price.split("$")[1])
	print(designer, ',', name, ': $', price[0])
	print(designer, ',', name, ': $', price[0], file=file)
	

file.close()
driver.quit()