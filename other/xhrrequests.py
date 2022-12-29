import requests
import pandas as pd
from pandas.io.json import json_normalize
from functools import reduce

def parse_data(jsonData):
    results_df = pd.DataFrame()
    return jsonData
# for alpha in jsonData['eventGroup']:
    #     print ('Gathering %s data: %s @ %s' %(alpha['sportname'],alpha['participantname_away'],alpha['participantname_home']))
    #     alpha_df = json_normalize(alpha).drop('markets',axis=1)
    #     for beta in alpha['markets']:
    #         beta_df = json_normalize(beta).drop('selections',axis=1)
    #         beta_df.columns = [str(col) + '.markets' for col in beta_df.columns]
    #         for theta in beta['selections']:
    #             theta_df = json_normalize(theta)
    #             theta_df.columns = [str(col) + '.selections' for col in theta_df.columns]

    #             temp_df = reduce(lambda left,right: pd.merge(left,right, left_index=True, right_index=True), [alpha_df, beta_df, theta_df])
    #             results_df = results_df.append(temp_df, sort=True).reset_index(drop=True)

    # return results_df

# nfl = parse_data(jsonData_draftkings_nfl)
# print(nfl)

headers = {"User-Agent": "Chrome/108.0.5359.124"}
try:
	jsonData_draftkings_nfl = requests.get('https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/88808/categories/492/subcategories/4518?').json()
	print(jsonData_draftkings_nfl)
except:
	print("An error")