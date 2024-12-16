# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
# Load the CSV file into a DataFrame
netflix_df = pd.read_csv('netflix_data.csv')

print(netflix_df.head())


# Filter the data to remove TV shows and store as netflix_subset
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Create netflix_movies DataFrame with specific columns
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Filter netflix_movies to find movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Display the short_movies DataFrame and inspect factors contributing to shorter movies
print(short_movies.head())

# List to store colors based on genre groups
colors = []

# Assigning colors based on genre groups for each row in netflix_movies
for index, row in netflix_movies.iterrows():
    if 'Children' in row['genre']:
        colors.append('blue')  # Assign blue for Children genre
    elif 'Documentaries' in row['genre']:
        colors.append('green')  # Assign green for Documentaries genre
    elif 'Stand-Up' in row['genre']:
        colors.append('orange')  # Assign orange for Stand-Up genre
    else:
        colors.append('red')  # Assign red for other genres

# Create a scatter plot for movie duration by release year using the assigned colors
fig, ax = plt.subplots()
ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)


# Set labels and title for the plot
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')

# Show the plot
plt.show()



# Grouping by genre and plotting distribution of movie durations
plt.figure(figsize=(10, 6))
genre_duration = netflix_movies.groupby('genre')['duration'].plot(kind='hist', alpha=0.7, legend=True)
plt.xlabel('Duration (min)')
plt.ylabel('Frequency')
plt.title('Movie Duration Distribution by Genre')
plt.show()



# Grouping movies by country and counting occurrences
top_countries = netflix_movies['country'].value_counts().head(10)  # Assuming you want the top 10 countries

print("Top Countries Contributing to Netflix's Movie Library:")
print(top_countries)




import matplotlib.pyplot as plt
import seaborn as sns

# Filter out genres and release year
genre_year_duration = netflix_movies.groupby(['genre', 'release_year'])['duration'].mean().reset_index()

# Plotting the temporal analysis for each genre
plt.figure(figsize=(12, 8))
sns.lineplot(data=genre_year_duration, x='release_year', y='duration', hue='genre', ci=None)
plt.xlabel('Release Year')
plt.ylabel('Average Duration (min)')
plt.title('Temporal Analysis of Movie Durations by Genre Over Years')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()