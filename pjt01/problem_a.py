import json
from pprint import pprint



def movie_info(movie):
    movie_detail = {}
    movie_detail['genre_ids'] = movie['genre_ids']
    movie_detail['id'] = movie['id']
    movie_detail['overview'] = movie['overview'] 
    movie_detail['poster_path'] = movie['poster_path']
    movie_detail['title'] = movie['title']
    movie_detail['vote_average'] = movie['vote_average'] 
    return movie_detail


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))

