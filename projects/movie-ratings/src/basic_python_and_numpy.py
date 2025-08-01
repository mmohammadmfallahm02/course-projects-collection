import numpy as np
import csv

file_path = '../imdb_top_1000.csv'


with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in reader]

data_array = np.array(data)
header = np.array(data[0])
movies = np.array(data[1:])

# Task 1.1: Statistics on Ratings
def calculate_statistics_rating():
    rating_array = movies[:, 6].astype(float)

    print('Mean:', np.mean(rating_array))
    print('Standard deviation:', np.std(rating_array))
    print('Median:', np.median(rating_array))



# Task 1.2: Filtering
def filtered_movie_by_imdb_rating(rating):
    rate_filter = (movies[:, 6]).astype(float) > rating
    filtered_movie = movies[rate_filter]

    print('Filtered by IMDB rating:', filtered_movie)


def filtered_movie_by_year(year):
    year_filter = movies[:, 2].astype(str) == year
    filtered_movie = movies[year_filter]

    print('Filtered by year:', filtered_movie)


def filtered_movie_by_genre(genre):
    genre_filter = np.array([genre in g for g in movies[:, 5]])
    filtered_movie = movies[genre_filter]

    print('Filtered by genre:', filtered_movie)


# Run
calculate_statistics_rating()
filtered_movie_by_imdb_rating(8.0)
filtered_movie_by_year("2010")
filtered_movie_by_genre("Drama")