import csv
from movie_fetcher import list
# Storing the movie information
# in a csv file

# Uso del principio de Single Responsibility al hacer otro módulo dedicado a la conversión de los datos
def store_csv_movie_data(list):
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})
    

store_csv_movie_data(list)
