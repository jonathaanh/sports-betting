import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players
import string



player_name = 'LeBron James'
team = 'LAL'
versus = 'OKC'
pts_line = 32.5
ast_line = 7.5
reb_line = 8.5
get_matchup_data = False

nba_player = next((x for x in players.get_players() if x.get("full_name") == player_name), None).get("id")

gamelog = pd.concat(playergamelog.PlayerGameLog(player_id=nba_player, season=SeasonAll.all).get_data_frames())
gamelog["GAME_DATE"] = pd.to_datetime(gamelog["GAME_DATE"], format="%b %d, %Y")
# print(gamelog_luka)

#gamelog = gamelog.query("GAME_DATE.dt.year in [2020,2021,2022,2023]")
gamelog = gamelog.query("GAME_DATE.dt.year in [2022,2023]")

if (get_matchup_data):
	gamelog = gamelog[(gamelog['MATCHUP'] == '{} vs. {}'.format(team,versus)) | (gamelog['MATCHUP'] == '{} @ {}'.format(team,versus))]

gamelog = gamelog[(gamelog['MATCHUP'].str.contains('vs.'))]
print(gamelog)

pts_count = len(gamelog[gamelog['PTS'] > pts_line])
print(gamelog[gamelog['PTS'] > pts_line])
pts_avg = gamelog['PTS'].mean()
print('PTS AVG', pts_avg)
print('Percentage above PTS', pts_count/len(gamelog.index))

reb_count = len(gamelog[gamelog['REB'] > reb_line])
print(gamelog[gamelog['REB'] > reb_line])
reb_avg = gamelog['REB'].mean()
print('REB AVG', reb_avg)
print('Percentage above REB', reb_count/len(gamelog.index))


ast_count = len(gamelog[gamelog['AST'] > ast_line])
print(gamelog[gamelog['AST'] > ast_line])
ast_avg = gamelog['AST'].mean()
print('AST AVG', ast_avg)
print('Percentage above AST', ast_count/len(gamelog.index))

pra_count = len(gamelog[(gamelog['AST'] + gamelog['PTS'] + gamelog['REB']) > 49.5])
print(gamelog[(gamelog['AST'] + gamelog['PTS'] + gamelog['REB']) > 49.5])
pra_avg = (gamelog['AST'] + gamelog['PTS'] + gamelog['REB']).mean()
print('PRA AVG', pra_avg)
print('Percentage above PRA', pra_count/len(gamelog.index))

