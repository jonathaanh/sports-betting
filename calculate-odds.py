import pandas as pd
import json

with open("json/americanfootball_nfl.json", "r") as f:
	data = json.load(f)

df = pd.DataFrame(['Home Team', 'Away Team', 'bookie', 'key', 'Name', 'price'])

home_team = []
away_team = []
bookies = []
keys = []
names = []
prices = []

for match in data:
	# df['Home Team'] = match['home_team']
	# df['Away Team'] = match['away_team']
	for bookie in match['bookmakers']:
		# df['bookie'] = bookie['title']
		for markets in bookie['markets']:
			# df['key'] = markets['key']
			for outcomes in markets['outcomes']:
				home_team += match['home_team']
				away_team += match['away_team']
				bookies = bookie['title']
				keys += markets['key']
				names += outcomes['name']
				# prices += outcomes['price']

print(df)