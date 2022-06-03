import random 
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from time import sleep 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# sleep(random.randiint(12, 18))

target_page = "https://shopee.ph/search?category=11021712&keyword=xda%20keycaps"
driver.get(target_page)
driver.maximize_window() 

options = Options() 
options.add_argument("--headless")
options.add_argument("--start-maximized") 
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
sleep(3)



# results = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div/div[2]/div/div[2]/div')
results = driver.find_elements(By.CSS_SELECTOR, '#main > div > div.dYFPlI > div > div > div.ZgwlcK > div.shopee-search-item-result > div.row.shopee-search-item-result__items > div:nth-child(1) > a > div > div > div.KMyn8J > div.dpiR4u > div.FDn--\+ > div')

#results = driver.find_elements(By.CSS_SELECTOR, '#main > div > div.dYFPlI > div._9dX3ZL > div > div.ZgwlcK > div > div.row.shopee-search-item-result__items > div:nth-child(2) > a > div > div > div.KMyn8J > div.dpiR4u > div.FDn--\+ > div')
print(len(results))

for result in results: 
    print(result.text)
    # item = result.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]')
    #print(item.text)
    
    # print(result.text)
    # item_name = result.text.split('\n')[2]
    # if item_name and item_name == 'OFF': 
    #     print(result.text)
        # print(result.text.split('\n')[0])
    # elif item_name != 'OFF':
    #     print(item_name)
    # print(item_name)
    

    

    
