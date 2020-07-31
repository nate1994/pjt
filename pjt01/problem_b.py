import json
from pprint import pprint


def movie_info(movie, genres):
    movie_detail = {}
    movie_detail['genre_name'] = movie['genre_ids']
    movie_detail['id'] = movie['id']
    idx = 0
    #genre ids(리스트)를 for문 돌려서 무비 디테일의 키값과 같다면 , movie_detail['genre_name']의 인덱스에 벨류값저장
    for num in movie_detail['genre_name']: #무비 디테일의 리스트를 하나식 받지여 -> 80 
        for genre in genres:
            if num == genre['id']:
                movie_detail['genre_name'][idx] = genre['name']
                idx += 1
    movie_detail['overview'] = movie['overview'] 
    movie_detail['poster_path'] = movie['poster_path']
    movie_detail['title'] = movie['title']
    movie_detail['vote_average'] = movie['vote_average'] 
    return movie_detail
        

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))