import requests
from kobis import URLMaker


def get_movie_cd(title, director):
    url_maker = URLMaker('9bda25102558de0a15fdafeacd305593')
    request = url_maker.get_url('movie','searchMovieList')
    payload = {
        'movieNm' : title,
        'directorNm' : director
    }
    response = requests.get(request, params = payload).json() #요청 -> 응답
    try:  #'movieListResult'키의 -> 'movieList'의 키의 '첫 리스트의 moviecd
        code = int(response.get('movieListResult').get('movieList')[0].get('movieCd'))
    except IndexError: #만약 해당 영화가 없다면 리스트가 아예잡히지 않기 때문에 인덱스 에러가 발생
        return 0
    if code >0:
       
        return code
    
        
        

if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색합니다.
    print(get_movie_cd('기생충', '봉준호'))