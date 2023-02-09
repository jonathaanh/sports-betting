import pandas as pd

# Read in both CSV files into dataframes
df1 = pd.read_csv("output.csv")
df2 = pd.read_csv("output2.csv")

# Merge the two dataframes on a common column (e.g. "GameID")
merged_df = pd.merge(df1, df2)

# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_file_output.csv", index=False)
