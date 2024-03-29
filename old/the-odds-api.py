import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import time


class Team:
	def __init__(self, name, value):
		self.name = name
		self.value = value

initial_spread_team = []
initial_spread_names = []


THRESHOLD = int(input("Input a threshold you want to check for between all NBA games."))

while(True):
	API_KEY = os.getenv('api_key')
	API_KEY = '6ed046c94f7627b7df3a69b3bd487d62'

	SPORT = 'basketball_nba' # use 'upcoming' to see the next 8 games across all sports

	REGIONS = 'us' # uk | us | eu | au

	MARKETS = 'spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

	ODDS_FORMAT = 'american' # decimal | american

	DATE_FORMAT = 'iso' # iso | unix

	# sports = []
	# sports_response = requests.get(
	#     'https://api.the-odds-api.com/v4/sports', 
	#     params={
	#         'api_key': API_KEY
	#     }
	# )
	# if sports_response.status_code != 200:
	#     print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')
	# else:
	#     for sport in sports_response.json():
	#         sports.append(sport['key'])
		# print('List of in season sports:', sports_response.json())

	# for sport in sports:
	odds_response = requests.get(
		f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
		params={
			'api_key': API_KEY,
			'regions': REGIONS,
			'markets': MARKETS,
			'oddsFormat': ODDS_FORMAT,
			'dateFormat': DATE_FORMAT,
		}
	)

	if odds_response.status_code != 200:
		print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')
	else:
		odds_json = odds_response.json()
		# print('Number of events:', len(odds_json))
		# print(odds_json)
		with open("{}.json".format(SPORT), "w") as f:
			json.dump(odds_json,f)
		# Check the usage quota
		print('Remaining requests', odds_response.headers['x-requests-remaining'])
		print('Used requests', odds_response.headers['x-requests-used'])


	def notify(title, text):
		os.system("""
				osascript -e 'display notification "{}" with title "{}"'
				""".format(text, title))

	with open("americanfootball_nfl.json", "r") as f:
		data = json.load(f)

	df = pd.DataFrame(columns=['Team', 'Bookie', 'Price', 'Points'])

	bookies = []
	names = []
	prices = []
	points = []

	for match in data:
		# df['Home Team'] = match['home_team']
		# df['Away Team'] = match['away_team']
			for bookie in match['bookmakers']:
				# df['bookie'] = bookie['title']
				for markets in bookie['markets']:
					# df['key'] = markets['key']
					for outcomes in markets['outcomes']:
						bookies.append(bookie['title'])
						names.append(outcomes['name'])
						prices.append(outcomes['price'])
						points.append(outcomes['point'])
						# prices += outcomes['price']

	# print(len(bookies))
	# print(len(names))
	# print(len(prices))
	# print(len(points))

	df['Team'] = names
	df['Bookie'] = bookies
	df['Price'] = prices
	df['Points'] = points

	print(df)
	
	

	for index, row in df.iterrows():
		if row['Team'] not in initial_spread_names:
			newTeam = Team(row['Team'], row['Points'])
			initial_spread_team.append(newTeam)
			initial_spread_names.append(newTeam.name)
		for team in initial_spread_team:
			if row['Team'] == team.name:
				if abs(row['Points'] - team.value) > THRESHOLD:
					notify("Bet", "{}: {}, Book: {}, Spread: {}".format(team.name, THRESHOLD, row['Bookie'], row['Points']))
					break
					#notify("The spread difference has changed: {}".format((row['Points'] - team.value)))


time.sleep(60)
