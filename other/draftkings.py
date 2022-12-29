import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


urls = 'https://sportsbook.draftkings.com/leagues/football/nfl'
driver = webdriver.Chrome('Users/jonathanhsu/Downloads/chromedriver')
driver.get(urls)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

nfl_teams = []
teams = soup.find_all("div", {"class": 'event-cell__name-text'})
line = soup.find_all("span", {"class": 'sportsbook-outcome-cell__line'})
odds = soup.find_all("span", {"class": 'sportsbook-odds american default-color'})

for team in teams:	
	print(team.text)

nfl_odds_lines = []

