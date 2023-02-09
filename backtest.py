import csv
import pandas as pd
import numpy as np

POINT_SPREAD = 6.5
QUARTERS = 2
SECOND_HALF_THRESHOLD = -1.5

df1 = pd.read_csv("data/FantasyOdds.2022/Game.2022.csv")
df2 = pd.read_csv("data/FantasyOdds.2022/Quarter.2022.csv")

merged_df = pd.merge(df1, df2, on='GameID')

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

grouped_df_home = grouped_df_home[(grouped_df_home['HomeScore'] - (POINT_SPREAD*2) >= (grouped_df_home['AwayScore']))]

print("Home Team Favored")
print(grouped_df_home)

print("Away Team Favored")
#print(grouped_df_away)

# print(grouped_df_home['second half diff'])


print("2H Comeback Mean", grouped_df_home['2H Home Team up'].mean())
#print("Away Mean", grouped_df_away['Away Team halftime up'].mean())

#print("Home 2H Median", grouped_df_home['2H Home Team up'].median())
#print("Away Median", grouped_df_away['2H Away Team up'].median())

#away_win =  len(grouped_df_away[grouped_df_away['2H Away Team up'] > SECOND_HALF_THRESHOLD]) / len(grouped_df_away.index)

#print("Away Percentage Win", away_win)

home_win =  len(grouped_df_home[grouped_df_home['2H Home Team up'] > SECOND_HALF_THRESHOLD]) / len(grouped_df_home.index)

print("Home Percentage Win", home_win)


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