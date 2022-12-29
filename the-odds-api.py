import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

API_KEY = os.getenv('api_key')

SPORT = 'upcoming' # use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au

MARKETS = 'h2h,spreads,totals' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'american' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

sports = []
sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports', 
    params={
        'api_key': API_KEY
    }
)
if sports_response.status_code != 200:
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')
else:
    for sport in sports_response.json():
        sports.append(sport['key'])
    # print('List of in season sports:', sports_response.json())

for sport in sports:
	odds_response = requests.get(
		f'https://api.the-odds-api.com/v4/sports/{sport}/odds',
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
		print('Number of events:', len(odds_json))
		print(odds_json)
		with open("{}.json".format(sport), "w") as f:
			json.dump(odds_json,f)
		# Check the usage quota
		print('Remaining requests', odds_response.headers['x-requests-remaining'])
		print('Used requests', odds_response.headers['x-requests-used'])