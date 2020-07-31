import requests
from kobis import URLMaker
from problem_b import get_movie_cd


def search_movie_info(movie_cd):
    url_maker = URLMaker('9bda25102558de0a15fdafeacd305593')
    request = url_maker.get_url('movie','searchMovieInfo')
    payload = {
        'movieCd' : movie_cd
    }
    response = requests.get(request, params = payload).json() 
    puplic = response['movieInfoResult']['movieInfo'] #공통 부분
    name = puplic['movieNm']
    y = puplic['openDt']

    gr = []
    for i in puplic['genres']: # 리스트 
        gr.append(i['genreNm'])
    
    if len(puplic['actors']) >= 1:
        actor =  puplic['actors'][0]['peopleNm']
    else:
        actor = 'noActor'
    result = dict(movieNm = name , openDt= y, genres = gr, actor = actor)
    return result


if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색하여 변수 movie_cd에 저장합니다.
    movie_cd = get_movie_cd('기생충', '봉준호')
    # movie_cd를 이용하여 상세정보를 조회하여 출력합니다.
    #print(movie_cd)
    print(search_movie_info(movie_cd)) # 코드를 입력받음...
