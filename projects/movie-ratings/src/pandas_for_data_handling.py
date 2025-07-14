import pandas as pd

file_path = '../imdb_top_1000.csv'
dataset = pd.read_csv(file_path)

dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)

dataset.rename(columns={
    'Series_Title': 'Title',
    'IMDB_Rating': 'Ratings',
    'Released_Year': 'Year'
}, inplace=True)


# Task 2.1: Sort movies by ratings
def sort_by_ratings(data):
    selected = data[['Title', 'Ratings', 'Genre']].copy()
    sorted_data = selected.sort_values(by='Ratings', ascending=False)
    print(sorted_data)


# Task 2.2: Group movies by year and calculate average ratings
def group_movies_by_year(data):
    selected = data[['Ratings', 'Year']].copy()
    avg_ratings = selected.groupby('Year')['Ratings'].mean().sort_index()
    print(avg_ratings)


# Run
sort_by_ratings(dataset)
group_movies_by_year(dataset)