from selenium import webdriver 
import time
import re


#launch url/maybe ask about this later? 
url = "https://grailed.com/krist__offer"

# set options
 

#   create new Chrome session
browser = webdriver.Chrome()
browser.set_window_position(0, 0)
browser.set_window_size(300, 400)


#   go to url
browser.get(url)
time.sleep(3)

#   fetch number of listings and convert to text
data = browser.find_element_by_xpath("//*[@id=\"wardrobe\"]/div/div[2]/div[1]/div[1]/a")
string = ''.join(data.text)

print(string)

# extract numbers
num = re.findall('\d+', string)
num = int(num[0])

if num > 1:
    print("The user has some new listings.")


# if there are new listings, update the current listing value and send me the designer, item name and price.

