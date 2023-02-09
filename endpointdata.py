import os
import requests
import json
import pandas as pd

# API endpoint
endpoint = "https://api.sportsdata.io/api/nba/odds/json/GameOddsByDate/{}?key=96fd2d2f9c194b7caa75fddfdc2a154f"

# Date range of the games (start and end dates of the NBA 2020 season)
start_date = "2021-10-22"
end_date = "2022-07-15"

# Create the directory to store the .json files
if not os.path.exists("NBA 2021 Season JSONS"):
    os.makedirs("NBA 2021 Season JSONS")
if not os.path.exists("NBA 2021 Season OUTPUTS"):
    os.makedirs("NBA 2021 Season OUTPUTS")

# Loop through the date range
date = start_date
while date <= end_date:
    # Construct the URL with the date
    url = endpoint.format(date)

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data from the response
        data = response.json()
        # Dump the JSON data into a .json file in the directory
        filename = "nba_odds_{}.json".format(date)
        file_path = os.path.join("NBA 2021 Season JSONS", filename)
        with open(file_path, "w") as file:
            json.dump(data, file)
        print("Data saved to file:", filename)
    else:
        # Print an error message if the request was not successful
        print("Failed to load data for date:", date, "Status code:", response.status_code)



    # Load the .json file into a pandas dataframe
    df = pd.read_json('NBA 2021 Season JSONS/{}'.format(filename))
    df = df[["GameId", "PregameOdds", "AwayTeamName" ,"HomeTeamName", "HomeTeamScore", "AwayTeamScore"]]

    # Extract the "PregameOdds" column into a separate variable
    pregame_odds = df["PregameOdds"]

    # Create an empty list to store the HomePointSpread values
    home_point_spread = []

    # Loop through the "PregameOdds" column
    for odds in pregame_odds:
        # Check if the odds are not empty
        if odds:
            # Extract the "HomePointSpread" value
            spread = odds[0]['HomePointSpread']
            # Append the spread to the list
            home_point_spread.append(spread)
        # If the odds are empty, append None to the list
        else:
            home_point_spread.append(None)

    # Add the new "HomePointSpread" column to the dataframe
    df["HomePointSpread"] = home_point_spread
    df = df[["GameId", "AwayTeamName" ,"HomeTeamName", "HomeTeamScore", "AwayTeamScore", "HomePointSpread"]]
    df.rename(columns = {"GameId":"GameID"}, inplace = True)


    print(df)

    # Write the dataframe to a .csv file
    output_filename = "nba_odds_{}_output.json".format(date)

    df.to_csv('NBA 2021 Season OUTPUTS/{}.csv'.format(output_filename), index=False)

        # Increment the date by one day
    date = (pd.to_datetime(date) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
        
