import requests
from bs4 import BeautifulSoup
from helper import ev, arb
import re

H2H_NUM_OF_TEAMS = 2
NUM_OF_BOOKMAKERS = 8

EV_THRESHOLD = 0


url_nfl = "https://www.vegasinsider.com/nfl/odds/las-vegas/"
url_nba = 'https://www.vegasinsider.com/nba/odds/las-vegas/'
url_nhl = 'https://www.vegasinsider.com/nhl/odds/las-vegas/'
url_ncaab = 'https://www.vegasinsider.com/college-basketball/odds/las-vegas/'

urls = ["https://www.vegasinsider.com/nfl/odds/las-vegas/", 'https://www.vegasinsider.com/nba/odds/las-vegas/'
, 'https://www.vegasinsider.com/nhl/odds/las-vegas/','https://www.vegasinsider.com/college-basketball/odds/las-vegas/']

# Make a GET request to the website
response = requests.get(url_nfl)
bookmakers = ['FanDuel', 'BetMGM', 'Caesars', 'WynnBet', 'BetRivers', 'PointsBet', 'SI', 'UniBet']

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

lines = []
odds = []
teams = []
moneyline_odds = []
NA_all = []

# Find all div elements with the classes below
for line in soup.find_all("div", class_='d-flex flex-row pr-2 pr-lg-0 px-1'):
	str = line.text.strip()
	str = str.replace('Bet Now', '')
	lines.append(str.split())

print(lines)
# print(len(lines))

all_odds = []
rows =len(lines)
columns=8
for i in range(0,rows,2):
	for j in range(columns):
		odd = []
		odd.append(lines[i][j])
		odd.append(lines[i+1][j])
	all_odds.append(odd)

print(all_odds)
for team in soup.find_all("a", class_='d-flex flex-column justify-content-start text-align-left text-decoration-none'):
	teams.append(team.text.strip())

matchups = []
for i in range(0, len(teams), H2H_NUM_OF_TEAMS):
	matchups.append(teams[i] + ' vs. '+ teams[i+1])
print(matchups)

# for line in soup.find_all("div", class_="font-weight-bold pt-2 regular-text text-center"):
# 	lines.append(line.text.strip())
# for odd in soup.find_all("div", class_="pt-1 regular-text text-center text-muted"):
# 	odds.append(odd.text.strip())
# for moneyline_odd in soup.find_all("div", class_="font-weight-bold pt-3 regular-text text-center"):
# 	moneyline_odds.append(moneyline_odd.text.strip())


# # Print the text content of each div element
# print("NA", NA_all)
# print("lines", lines)
# print("odds", odds)
# print("teams",teams)
# print("ML", moneyline_odds)
# print(len(lines))
# print(len(odds))
# print(len(teams))
# print(len(moneyline_odds))

# num_of_games = len(teams)/H2H_NUM_OF_TEAMS
# all_odds = {}
# Counter_end = 1
# Counter_start = 0
# Counter_end_ml = 1
# Counter_start_ml = 0
# for match in matchups:
# 	all_odds[match] = []
# 	shift = 0
# 	for bookie in bookmakers:
# 		book = {}
# 		book_data = []
# 		for i in range((int)(shift+Counter_start),Counter_end*(int)(len(lines)/num_of_games), NUM_OF_BOOKMAKERS):
# 			book_data.append(lines[i])
# 			book_data.append(odds[i])
# 		# print("Start", (int)(shift+Counter_start_ml))
# 		# print("End",Counter_end_ml*(int)(len(moneyline_odds)/num_of_games))
# 		for i in range((int)(shift+Counter_start_ml),Counter_end_ml*(int)(len(moneyline_odds)/num_of_games), NUM_OF_BOOKMAKERS):
# 			book_data.append(moneyline_odds[i])
# 		book[bookie] = book_data
# 		all_odds[match].append(book)
# 		shift += 1
# 	Counter_end+= 1
# 	Counter_start += len(lines)/num_of_games
# 	Counter_end_ml+= 1
# 	Counter_start_ml += len(moneyline_odds)/num_of_games
	
# print(all_odds)

# for match in all_odds:
# 	i = 0
# 	print(match)
# 	for bookie in bookmakers:
# 		print(bookie)
# 		print(all_odds[match][i][bookie])
# 		i += 1