# Selenuim imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selexcept

import csv



# Time and date-time (mainly for using delays between clicks)
import time

from bs4 import BeautifulSoup
  
# This will open the Chrome window and add options to prevent expeida from blocking scraper
options = Options()
options.add_argument("--disable-extensions")
options.add_argument('--no-sandbox')
options.add_argument("disable-infobars")
options.add_argument('--single-process')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options)
browser.get("https://www.expedia.com/Flights-Search?leg1=from%3AAtlanta%20%28ATL%20-%20Hartsfield-Jackson%20Atlanta%20Intl.%29%2Cto%3ACancun%20%28CUN%20-%20Cancun%20Intl.%29%2Cdeparture%3A4%2F3%2F2024TANYT&mode=search&options=carrier%3A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A2%2Cchildren%3A0%2Cinfantinlap%3AN&trip=oneway")
time.sleep(7)
resp = browser.page_source
soup=BeautifulSoup(resp,'html.parser')


# departure times
dep_times = browser.find_elements(By.XPATH,"//span[@data-test-id='departure-time']")
dep_times_list = [value.text for value in dep_times]
# airline name
airlines = browser.find_elements(By.XPATH,"//div[@data-stid='airline-info']")
airlines_list = [value.text for value in airlines]
# durations
durations = browser.find_elements(By.XPATH,"//div[@data-test-id='journey-duration']")
durations_list = [value.text for value in durations]

# price
price = browser.find_elements(By.XPATH, '//span[@class = "uitk-lockup-price"]')
price_list = [value.text for value in price]

# Prepare data for CSV
data = zip(dep_times_list, airlines_list, durations_list, price_list)

# Writes data to CSV with title
with open('CancunTrip.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Departure Time', 'Airline', 'Duration','Price'])
    writer.writerows(data)





