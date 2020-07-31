# READ.ME

### problem_a

- 첫 난관  :  정확한 api 데이터 요청을 이해하지 못했다. 처음에는 영화인(다우니)한명의 데이터를 어떻게 가지고 오는지 고민을 오래했다. 하지만 api제공 사이트를 잘 읽어보고 차근차근 접근해 나가며 문제를 해결했다.



### problem_b

- a번 문제에서 감을 익혔는지 데이터를 가져와서 활용하는 방안이 더 쉽게 느껴졌다.

- 다만, 영화가 없을 때를 어떻게 해볼까 생각해봤다. 

  다양한 방법이 있지만 나는 한번 프로젝트에서 예외처리를 통해서 결과를 만들어 보고 싶었다.

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

  그래서 함수를 이렇게 만들어보았다.

  다양한 테스트 케이스에서 문제가 없다고 느껴져서 좋았다. 



### Problem_c

- C번 문제도 빠르게 풀 수 있었다. 다만 코드를 다짜고 보니 공통부분을 변수처리를 하지 않고 해서 코드가 길어보이고 가독성이 떨어져보였다

- 그래서 완성 후 바로 변수를 만들어서 최대한 간결하게 만들어 볼려고 했다

- 영화 Api를 이용하여 영화 정보를 가져와 다양한 활용도를 구사할 수 있는 토대가 마련되었다고 생각한다.

  => 다음 프로젝트가 기대된다.



### Problem_d

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
actors_string = res.get('items')[0].get('actor') 
main_actor = actors_string.split('|')
main_actor.pop() #마지막 |제거 
print(main_actor)

#간단하게 네이버 api활용하여 실습을 해보았다
#네이버는 영화뿐만 아니라 다양한 api를 제공하는 것을 보았기 때문에 다른 프로젝트나 개인적으로 활용도 가능해보여서 나만을 위한 데이터 제공 애플리케이션을 만들어보겠다.
```

