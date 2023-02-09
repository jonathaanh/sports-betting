import csv
import pandas as pd
import numpy as np

POINT_SPREAD = 7.0
POINT_FACTOR = 2.0
QUARTERS = 2
SECOND_HALF_THRESHOLD = -1.5

game1 = pd.read_csv("data/FantasyOdds.2022/Game.2020.csv")
game2 = pd.read_csv("data/FantasyOdds.2022/Game.2021.csv")
game3 = pd.read_csv("data/FantasyOdds.2022/Game.2022.csv")
game4 = pd.read_csv("data/FantasyOdds.2022/Game.2023.csv")
# gameMerge = pd.merge(game1, game2)
# gameMerge = pd.merge(gameMerge, game3)
# gameMerge = pd.merge(gameMerge, game4)

quarter1 = pd.read_csv("data/FantasyOdds.2022/Quarter.2020.csv")
quarter2 = pd.read_csv("data/FantasyOdds.2022/Quarter.2021.csv")
quarter3 = pd.read_csv("data/FantasyOdds.2022/Quarter.2022.csv")
quarter4 = pd.read_csv("data/FantasyOdds.2022/Quarter.2023.csv")
# quarterMerge = pd.merge(quarter1, quarter2)
# quarterMerge = pd.merge(quarterMerge, quarter3)
# quarterMerge = pd.merge(quarterMerge, quarter4)


merged_df = pd.merge(game4, quarter4, on='GameID')

# Filter rows based on the date being after 1/01/2023 12:00:00 AM
# filter_date = pd.Timestamp("1/1/2023 00:00:00")
# merged_df["Day"] = pd.to_datetime(merged_df["Day"])
# merged_df = merged_df[merged_df["Day"] >= filter_date]
print(merged_df)

merged_df = merged_df[merged_df['Number'] <= QUARTERS]

# point spread negative => favored for the home team
grouped_df_home = merged_df[(merged_df['PointSpread'] < -POINT_SPREAD)]

# point spread positive => favored for the away team
#grouped_df_away = merged_df[(merged_df['PointSpread'] > POINT_SPREAD)]

grouped_df_home = grouped_df_home.groupby("GameID").agg({"PointSpread":"mean", "HomeScore": "sum", "AwayScore": "sum","HomeTeamScore": "mean","AwayTeamScore": "mean"})
#grouped_df_away = grouped_df_away.groupby("GameID").agg({"PointSpread":"mean", "HomeScore": "sum", "AwayScore": "sum","HomeTeamScore": "mean","AwayTeamScore": "mean"})


grouped_df_home['Home Team halftime up'] = grouped_df_home['HomeScore'] - grouped_df_home['AwayScore'] 
#grouped_df_away['Away Team halftime up'] = grouped_df_away['AwayScore'] - grouped_df_away['HomeScore'] 

grouped_df_home['Home Team final up'] = grouped_df_home['HomeTeamScore'] - grouped_df_home['AwayTeamScore'] 
#grouped_df_away['Away Team final up'] = grouped_df_away['AwayTeamScore'] - grouped_df_away['HomeTeamScore'] 

grouped_df_home['2H Home Team up'] = grouped_df_home['Home Team final up'] - grouped_df_home['Home Team halftime up'] 
#grouped_df_away['2H Away Team up'] = grouped_df_away['Away Team final up'] - grouped_df_away['Away Team halftime up'] 


# grouped_df_away = grouped_df_away[grouped_df_away['AwayScore'] + grouped_df_away['PointSpread'] >= grouped_df_away['HomeScore']]

# grouped_df_away = grouped_df_away[(grouped_df_away['AwayScore'] <= (grouped_df_away['HomeScore']))]

# grouped_df_home = grouped_df_home[grouped_df_home['HomeScore'] - grouped_df_home['PointSpread'] <= grouped_df_home['AwayScore']]

grouped_df_home = grouped_df_home[(grouped_df_home['HomeScore'] + (grouped_df_home['PointSpread']*POINT_FACTOR) >= (grouped_df_home['AwayScore']))]

print("Home Team Favored")
print(grouped_df_home)

print("Away Team Favored")
#print(grouped_df_away)

# print(grouped_df_home['second half diff'])


print(grouped_df_home['2H Home Team up'].describe())
#print("Away Mean", grouped_df_away['Away Team halftime up'].mean())

#print("Home 2H Median", grouped_df_home['2H Home Team up'].median())
#print("Away Median", grouped_df_away['2H Away Team up'].median())

#away_win =  len(grouped_df_away[grouped_df_away['2H Away Team up'] > SECOND_HALF_THRESHOLD]) / len(grouped_df_away.index)

#print("Away Percentage Win", away_win)

home_win =  len(grouped_df_home[grouped_df_home['2H Home Team up'] > SECOND_HALF_THRESHOLD]) / len(grouped_df_home.index)

print("Home Percentage Win", home_win)
print("Number of points", len(grouped_df_home[grouped_df_home['2H Home Team up'] > SECOND_HALF_THRESHOLD]))


# GameID = []
# spreads = []
# with open('data/FantasyOdds.2022/Game.2022.csv', 'r') as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     for row in reader:
#         GameID.append(row[0])
#         spreads.append(row[13])
# print(GameID)
# print(spreads)