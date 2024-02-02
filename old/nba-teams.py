import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players
import requests


url = 'https://stats.nba.com/stats/boxscorescoringv2'


response = requests.get('https://stats.nba.com/stats/boxscorescoringv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0')