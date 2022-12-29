from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# store results in a dataframe
# automate the scraping function on repeat
# Visualize and calculate arb opportunities

#List of sites to web scrape 
url = 'https://sports.ny.betmgm.com/en/sports?wm=&btag=&tdpeh=&pid='
#url = 'https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/88808?format=json'
# 'https://sportsbook.fanduel.com/'
# , 'https://www.williamhill.com/us/ny/bet/', 'https://ny.betrivers.com/?page=sportsbook&feed=featured#home', ]

headers = {"User-Agent": "Chrome/108.0.5359.124"}

try:
	page=requests.get(url,headers=headers)
	page_content = page.content
except:
	print("An error occured")

soup = BeautifulSoup(page_content)
print(soup)

tabl = soup.find_all("span", {"class": 's x il im in io hh hi hj hz ip h ev dw iq bg'})
print(tabl)

