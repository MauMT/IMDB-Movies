import requests
import re
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup

#### -- Dependency Inversion & Interface Segregation --
# Removed: from models import get_postgres_uri
# to avoid dependency movie_fetcher --> models
# Created UriInterface.py and can only access the method get_postgres_uri
from UriInterface import UriInterface

from movie_to_dictionary import SimpleExporterFactory


#from movie_to_dictionary import store_csv_movie_data

# DEFAULT_SESSION_FACTORY = sessionmaker(
#     bind=create_engine(
#         UriInterface.get_postgres_uri(),
#         isolation_level="REPEATABLE READ",
#     )
# )
# session = DEFAULT_SESSION_FACTORY()

def __init__(self, u : UriInterface, factory : SimpleExporterFactory):
    self.UriInterface = u
    self.factory = factory


def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    # create a empty list for storing
    # movie information
    list = []

    # Iterating over movies to extract
    # each movie's details
    for index in range(0, len(movies)):
        # Separating movie into: 'place',
        # 'title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]

        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index],
                "preference_key": index % 4 + 1}
        list.append(data)

    exporter = SimpleExporterFactory.createExporter('csv')
    exporter.save(list)

if __name__ == '__main__':
    main()
