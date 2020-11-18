# READ.ME

[toc]

# API 활용한 데이터 수집

**목표**

1.  필모리스트를 이용하여 카운트 기능

2. 영화 검색기능

3. 특정 정보를 이용한 상세 정보 수집

   부가) NAVER API 활용해보기 



### 1. 필모리스트 정보를 활용한 기능

> 영화인명과 필모리스트를 이용하여 영화인을 검색하고 몇 작품을 출연, 제작등을 하였는지 계산
>
> 활용 API : kobis

1. URL 정보 만들기

   - url, key를 담은 class 만들기 (kobis.py)

2. request 라이브러리를 활용하여 요청한 데이터 조작

   -  요청한 데이터를 .json으로 바꿔주어서 `python`에서 다룰 수 있게 만들어 준다.
   - 원하는 조건에 맞추어 데이터를 찾아서 카운트를 샜다.

3. requests 기능 공부 

   - GET 요청 parameter 전달

     ```python
     params = {'param1': 'value1', 'param2': 'value'} 
     res = requests.get(URL, params=params)
     ```

   - POST요청

     ```python
     data = {'param1': 'value1', 'param2': 'value'}
     res = requests.post(URL, data=data)
     ```

     

### 2. 검색

다양한 방법이 있지만 나는 한번 프로젝트에서 예외처리를 통해서 결과를 만들어 보기로 했다.

```python
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
```

다양한 테스트 케이스를 해보았고 문제가 없었다.



### 3. 상세정보 수집

> 검색 기능을 활용하여 상세 정보를 출력하는 함수를 만들어 보자

**구성**

```python
    response = requests.get(request, params = payload).json() 
    puplic = response['movieInfoResult']['movieInfo']
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
```

### 추가

```python
import requests
#import urllib.request
header = {
    "X-Naver-Client-id" : 'NxX6OVwc3ZRLPCLzoNBH',
    "X-naver-Client-secret" : 'c2h_cuitbg'
}
url ='https://openapi.naver.com/v1/search/movie?query='
text = '기생충'
res = requests.get(url+text, headers = header).json()

main_actor = [] #주연배우들
actors_string = res.get('items')[1].get('actor') 
main_actor = actors_string.split('|') # 
main_actor.pop() # 마지막|제거 
print(main_actor) 

#간단하게 네이버 api활용하여 실습을 해보았다
#네이버는 영화뿐만 아니라 다양한 api를 제공하는 것을 보았기 때문에 다른 프로젝트나 개인적으로 활용도 가능해보여서 나만을 위한 데이터 제공 애플리케이션을 만들어보겠다.

```

