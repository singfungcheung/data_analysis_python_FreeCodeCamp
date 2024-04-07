# Import numpy, pandas, and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Print the pandas version and the configuration.
# print(pd.__version__)

"""
DataFrame creation
"""
# Create an empty pandas DataFrame.
# df = pd.DataFrame(data=[None],
#                   index=[None],
#                   columns=[None])
# print(df)

# Create a marvel_df pandas DataFrame with the given marvel data.
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]
marvel_df = pd.DataFrame(data=marvel_data)

# Add column names to the marvel_df.
col_names = ['name', 'sex', 'first_appearance']
marvel_df.columns = col_names

# Add index names to the marvel_df (use the character name as index).
marvel_df.index = marvel_df['name']

# Drop the name column as it's now the index.
marvel_df = marvel_df.drop(['name'], axis=1)

# Drop 'Namor' and 'Hank Pym' rows
marvel_df.drop(['Namor', 'Hank Pym'], axis=0, inplace=True)

# show the first 5 elements of marvel_df.
# print(marvel_df.iloc[:5])

# Show the last 5 elements of marvel_df.
# print(marvel_df.iloc[-5:])

# Show just the sex of the first 5 elements on marvel_df.
# print(marvel_df.iloc[:5]['sex'])

# print(marvel_df.iloc[:5].sex.to_frame())

# Show the first_appearance of all middle elements on marvel_df
# print(marvel_df)
# print(marvel_df.iloc[1:-1].first_appearance.to_frame())

# Show the first and last elements on marvel_df
# print(marvel_df.iloc[[0, -1]])

"""
DataFrame manipulation and operations.
"""

# Modify the first_appearance of 'Vision' to year 1964.
marvel_df.loc['Vision', 'first_appearance'] = 1964

# Add a new column called 'years_since' with the years since first_appearance.
marvel_df['years_since'] = 2024 - marvel_df['first_appearance']

# Make a mask showing female characters.
mask = marvel_df['sex'] == 'female'
# print(mask)

# Get the male characters.
# print(marvel_df[marvel_df['sex'] == 'male'])

# Get characters with first_appearance after 1970
# print(marvel_df[marvel_df['first_appearance'] > 1970])

# Get female characters with first appearance after 1970
# print(marvel_df[(marvel_df['first_appearance'] > 1970) & (marvel_df['sex'] == 'female')])

"""
DataFrame summary statistics.
"""

# Show basic statistics of marvel_df.
# print(marvel_df.describe())

# show mean value of first appearance.
# print(marvel_df['first_appearance'].mean())

# Show min value of first appearance.
# print(marvel_df['first_appearance'].min())

# Get characters with min value of first_appearance.
# print(marvel_df[marvel_df['first_appearance'] == marvel_df['first_appearance'].min()])

"""
DataFrame basic plottings.
"""

# Reset index names of marvel_df
# print(marvel_df.reset_index())

# Plot values of first_appearance.
marvel_df['first_appearance'].plot()

# Plot a histogram (plot.hist) with values of first_appearance.
plt.hist(marvel_df['first_appearance'])
