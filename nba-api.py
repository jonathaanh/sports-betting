import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players

player_name = 'Giannis Antetokounmpo'
team = 'MIL'
versus = 'POR'

nba_player = next((x for x in players.get_players() if x.get("full_name") == player_name), None).get("id")

gamelog = pd.concat(playergamelog.PlayerGameLog(player_id=nba_player, season=SeasonAll.all).get_data_frames())
gamelog["GAME_DATE"] = pd.to_datetime(gamelog["GAME_DATE"], format="%b %d, %Y")
# print(gamelog_luka)
gamelog = gamelog.query("GAME_DATE.dt.year in [2020,2021,2022,2023]")
# gamelog = gamelog.query("GAME_DATE.dt.year in [2022, 2023]")
gamelog = gamelog[(gamelog['MATCHUP'] == '{} vs. {}'.format(team,versus)) | (gamelog['MATCHUP'] == '{} @ {}'.format(team,versus))]
pts_avg = gamelog['PTS'].mean()

reb_avg = len(gamelog[gamelog['REB'] > 14.5])
print(gamelog)
print('PTS', pts_avg)
print('reb')
print(gamelog.columns.values)
print(reb_avg/len(gamelog.index))
