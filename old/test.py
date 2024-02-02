import requests
import time
from plyer import notification

# Set the API endpoint
url = 'https://api.theoddsapi.com/v3/odds'

# Set the API key
api_key = 'c4dd4ffcdec88e0fd40ddd5836b98fd1'

# Set the parameters for the API request
params = {
    'sport': 'basketball_nba',
    'region': 'us',
    'mkt': 'spreads'
}

# Get the threshold spread difference from user input
threshold = float(input("Enter the threshold spread difference: "))

# Get the game id from user input
game_id = input("Enter the game id: ")

# Initialize the initial spread
initial_spread = None

while True:
    # Send the GET request to the API
    response = requests.get(url, params=params, headers={'x-api-key': api_key})

    # Get the lines for all NBA games
    games = response.json()

    # Iterate through all games
    for game in games:
        if game['home_team']['team_id'] == game_id or game['away_team']['team_id'] == game_id:
            # Get the current spread
            current_spread = game['sites'][0]['odds']['spreads'][0]['spread']
            if initial_spread is None:
                initial_spread = current_spread
            # Check if the current spread is greater than the initial spread by the threshold
            if current_spread - initial_spread >= threshold:
                # Display a popup notification
                notification.notify(
                    title = "Spread Alert",
                    message = f"The spread for the game between {game['home_team']['team_name']} and {game['away_team']['team_name']} has reached {current_spread} which is {current_spread - initial_spread} greater than the initial spread of {initial_spread}.",
                    timeout = 10
                )
                break
    time.sleep(60) #refresh the data after 60 sec
