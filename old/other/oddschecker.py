import requests
from bs4 import BeautifulSoup

url = 'https://www.oddschecker.com/us/football/nfl/buffalo-bills-vs-cincinnati-bengals'

headers = {"User-Agent": "Chrome/108.0.5359.124"}
# Make the request to the website
try:
	page=requests.get(url,headers=headers)
	page_content = page.content
except:
	print("An error occured")

# Parse the HTML of the website
soup = BeautifulSoup(page.text, 'html.parser')

# Find all div elements with the attribute data-testid set to "bet-odds"
divs = soup.find_all('div', attrs={'data-testid': 'bet-odds'})

# Print the divs
print(divs)
