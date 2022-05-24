import csv

# Uso del principio de Single Responsibility al hacer otro módulo dedicado a la conversión de los datos
def store_csv_movie_data(file_name):
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})
