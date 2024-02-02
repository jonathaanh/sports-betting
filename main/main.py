import requests
import urllib
from datetime import datetime
import os 

BASE_URL = 'https://api.prop-odds.com'
# API_KEY = os.getenv('api_key')
API_KEY = '1D71BLVDFQFWDjmMOKejfhYBrCtjxhnxukMcNcY'


def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    print('Request failed with status:', response.status_code)
    return {}


def get_nba_games():
    now = datetime.now()
    print(now.strftime('%Y-%m-%d'))
    query_params = {
        'date': '2024-02-01',
        'tz': 'America/New_York',
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/games/nba?' + params
    return get_request(url)


def get_game_info(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/game/' + game_id + '?' + params
    return get_request(url)


def get_markets(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/markets/' + game_id + '?' + params
    return get_request(url)


def get_most_recent_odds(game_id, market):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/odds/' + game_id + '/' + market + '?' + params
    return get_request(url)


def prizepicks():
    #points, rebounds, PRA, assists, 3PM, steals, blocks, turnovers, pts+reb, pts+ast, reb+ast, blks+stls
    return 

def underdog():
    
    return


def main():

    #get nba games
    games = get_nba_games()
    if len(games['games']) == 0:
        print('No games scheduled for today.')
        return

    #get first game
    first_game = games['games'][0]
    game_id = first_game['game_id']
    print(first_game)


    eligible_markets = ['player_points_over_under']
    # , 'player_rebounds_over_under', 'player_assists_points_rebounds_over_under', 
    #                     'player_assists_over_under', 'player_threes_over_under', 'player_steals_over_under', 'player_blocks_over_under', 'player_turnovers_over_under', 
    #                     'player_points_rebounds_over_under', 'player_assists_points_over_under', 'player_assists_rebounds_over_under', 'player_blocks_steals_over_under']

    markets = get_markets(game_id)
    print(markets)

    for markets in markets['markets']:
        print(markets)
        if markets['name'] in eligible_markets:
            print('eligible market')
        else:
            print('not eligible market')


    # if len(markets['markets']) == 0:
    #     print('No markets found.')
    #     return



    for market in eligible_markets:
        print("market" + market)
        # Assuming get_most_recent_odds takes game_id and market name to fetch odds
        odds = get_most_recent_odds(game_id, market['name'])
        print(odds)

    # first_market = markets['markets'][0]
    # print(first_market)
    # odds = get_most_recent_odds(game_id, first_market['name'])
    # print(odds)


if __name__ == '__main__':
    main()