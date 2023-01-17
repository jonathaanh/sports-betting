import pandas as pd
import json

with open("americanfootball_nfl.json", "r") as f:
	data = json.load(f)

df = pd.DataFrame(['Team', 'Bookie', 'Price', 'Point'])

bookies = []
names = []
prices = []
points = []

for match in data:
	# df['Home Team'] = match['home_team']
	# df['Away Team'] = match['away_team']
	if match['home_team'] == 'Tampa Bay Buccaneers':
		for bookie in match['bookmakers']:
			# df['bookie'] = bookie['title']
			for markets in bookie['markets']:
				# df['key'] = markets['key']
				for outcomes in markets['outcomes']:
					bookies.append(bookie['title'])
					names.append(outcomes['name'])
					prices.append(str(outcomes['price']))
					points.append(str(outcomes['point']))
					# prices += outcomes['price']

print(len(bookies))
print(len(names))
print(len(prices))
print(len(points))

df['Team'] = names
df['Bookie'] = bookies
df['Price'] = prices
df['Points'] = points

print(df)