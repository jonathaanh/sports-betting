import requests
import json
import pandas as pd

# API endpoint
endpoint = "https://api.sportsdata.io/api/nba/odds/json/GamesByDate/{}?key=96fd2d2f9c194b7caa75fddfdc2a154f"

# Date of the game(s)
date = "2022-01-01"

# Construct the URL with the date
url = endpoint.format(date)

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data from the response
    data = response.json()
    # Dump the JSON data into a .json file
    with open("nba_games_2022-01-01.json", "w") as file:
        json.dump(data, file)
    print("Data saved to file.")
else:
    # Print an error message if the request was not successful
    print("Failed to load data. Status code:", response.status_code)

# Load the .json file into a pandas dataframe
df = pd.read_json('nba_games_2022-01-01.json')
df = df[["GameID", "AwayTeam", "HomeTeam", "AwayTeamScore", "HomeTeamScore", "PointSpread", "Quarters"]]
data = df["Quarters"]
awayScoreArray = []
homeScoreArray = []

for i in range(len(data)): 
    awayScore = 0
    homeScore = 0
    print("new data")
    for j in range(2):
        awayScore = data[i][j]['AwayScore'] + awayScore
        homeScore = data[i][j]['HomeScore'] + homeScore
    awayScoreArray.append(awayScore)
    homeScoreArray.append(homeScore)


df["HomeFirstHalf"] = homeScoreArray
df['AwayFirstHalf'] = awayScoreArray
df = df[["GameID", "AwayTeam", "HomeTeam", "HomeTeamScore",  "AwayTeamScore", "PointSpread", "HomeFirstHalf", "AwayFirstHalf" ]]
df.rename(columns = {"AwayTeam": "AwayTeamName", "HomeTeam": "HomeTeamName", "PointSpread": "HomePointSpread2"}, inplace = True)

print(df)


df.to_csv('output2.csv', index=False)
