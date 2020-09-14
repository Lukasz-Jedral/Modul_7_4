from Models import Movie, Series
from DataBase import Data_Base
import random

def get_movies(data_base):
    movies = []
    for item in data_base:
        if isinstance(item, Movie):
            movies.append(item)
    return movies

def get_series(data_base):
    series = []
    for item in data_base:
        if isinstance(item, Series):
            series.append(item)
    return series

def search(title,data_base):
    for item in data_base:
        if title == item.title:
            return item.title

    return print("brak filmu lub serialu w bazie")

def generate_views(How_many_times,data_base):
    db = data_base
    for conter in range(1,How_many_times):
        rnd_Data_Base_entry = random.choice(db)
        rnd_Data_Base_entry.views_number(random.randint(1,100))
        for counter in range(len(db)):
            if db[counter].title == rnd_Data_Base_entry.title:
                db[counter] = rnd_Data_Base_entry
    return db



def top_titles(how_many, data_base, content_type = ''):
    if content_type == 'movies':
        movies = get_movies(data_base)
        by_popularity = sorted(movies, key=lambda item: item._views)
        result = []
        for counter in range(0, how_many):
            result.append(by_popularity[counter])
        return result
    elif content_type == 'series':
        series = get_series(data_base)
        by_popularity = sorted(series, key=lambda item: item._views)
        result = []
        for counter in range(0, how_many):
            result.append(by_popularity[counter])
        return result
    else:
        by_popularity = sorted(data_base, key = lambda item: item._views)
        result=[]
        for counter in range(0,how_many):
            result.append(by_popularity[counter])
        return result

updated_db = generate_views(10, Data_Base)
print(top_titles(10,updated_db))
print(top_titles(5,updated_db, "movies"))
print(top_titles(5,updated_db, "series"))
"""
movies = get_movies(Data_Base)
for movie in movies:
    print(movie)

series = get_series(Data_Base)
for serie in series:
    print(serie)

print(search("The Shawshank Redemption",Data_Base))
print(search("ABC",Data_Base))
"""
