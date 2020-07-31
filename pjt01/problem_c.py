import json
from pprint import pprint
from collections import OrderedDict

def movie_info(movies, genres):
    result = [] #movies는 리스트 안에 딕셔너리 
    for movie in movies:
        movie_detail = {}
        movie_detail['genre_name'] = movie['genre_ids']
        movie_detail['id'] = movie['id']
        idx = 0
        for num in movie_detail['genre_name']: #무비 디테일의 리스트를 하나식 받지여 -> 80 
            for genre in genres:
                if num == genre['id']:
                    movie_detail['genre_name'][idx] = genre['name']
                    idx += 1
        movie_detail['overview'] = movie['overview'] 
        movie_detail['poster_path'] = movie['poster_path']
        movie_detail['title'] = movie['title']
        movie_detail['vote_average'] = movie['vote_average'] 
        result = result + [movie_detail] # b번이랑 다른게 그냥 이거 하나 -> 리스트에 딕셔너리 하나씩 붙이는거
    return result

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

    file_data = OrderedDict()
    file_data = movie_info(movies_list, genres_list)
    with open('problem_c.json','w', encoding='UTF8') as make_file:
        json.dump(file_data,make_file, ensure_ascii=False,indent ='\t')