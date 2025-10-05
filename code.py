# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

nineties_movies = netflix_df.loc[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999)]
plt.hist(nineties_movies['duration'],bins= 20)
plt.show
duration = 100
# Filter for action movies in the 90s
action_movies_90s = nineties_movies[nineties_movies['genre'] == 'Action']

short_movie_count = 0

for label, row in action_movies_90s.iterrows():
    if row['duration'] < 90:
        short_movie_count = short_movie_count + 1

print(short_movie_count)
