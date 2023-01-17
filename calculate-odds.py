import pandas as pd
import json
import os

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
	if match['home_team'] == 'Tampa Bay Buccaneers':
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

# print(df)

for index, row in df.iterrows():
	if(row['Team'] == 'Dallas Cowboys'):
		if(row['Points'] >= 3):
			notify("Bet", "Cowboys +3")
			break
	if(row['Team'] == 'Tampa Bay Buccaneers'):
		if(row['Points'] >= 8):
			notify("Bet", "TB +8")
			break