#nombre, el año y el rating de las peliculas.
import csv
import json
from operator import itemgetter

def printMovieData():
    with open('movie_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['movie_title'], row['year'], row['rating'])

#rating por default es True, es decir, es Descending
def getMovieByMagicKey(magicKey, rating):
    movieList = []
    
    if rating.upper() == "" or rating.upper() == "TRUE":
        rating = True
    elif rating.upper() == "FALSE":
        rating = False
    else:
        return "Error: Rating must be True or False"

    with open('/src/movies/movie_results.csv', newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['preference_key'] == str(magicKey)):
                movieList.append(row)
    return sorted(movieList, key=itemgetter('rating'), reverse = rating)
    

