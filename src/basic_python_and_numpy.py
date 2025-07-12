import numpy as np
import csv

file_path = '../imdb_top_1000.csv'


with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in reader]

data_array = np.array(data)

# header = data_array[0]
# print('Header: ', header)


rating_array = data_array[1:, 6].astype(float)

# print('Rating array: ', rating_array)
print('Mean:', np.mean(rating_array))
print('Standard deviation:', np.std(rating_array))
print('Median:', np.median(rating_array))


