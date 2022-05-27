#nombre, el año y el rating de las peliculas.
import csv
import json

def printMovieData():
    with open('movie_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['movie_title'], row['year'], row['rating'])


def getMovieByMagicKey(magicKey, sorting):
    movieList = []
    with open('/src/movies/movie_results.csv', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['preference_key'] == str(magicKey)):
                movieList.append(row)
    return movieList


