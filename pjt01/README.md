# README

[toc]

## Python을 통한 데이터 수집



### 1. 제공되는 영화 데이터  주요 내용수집

- `movie.json` 파일에 있는 영화 정보를 가지고 `python`에 맞게 출력 결과를 확인을 해보았다.

  ```python
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
  ```

  

### 2. 영화 데이터 내용 수정 

 (리스트 안에 있는 딕셔너리)와 (리스트 안에 있는 인덱스)를 어떻게 매치시키는지에 대한 고민이 필요했고, 딕셔너리 안에 있는 리스트에 접근하여 값을 수정하는 것을 해야했다.

- 이러한 과정을 통해 데이터 저장을 잘 파악하는 것에 대한 중요성을 느꼈다.

  ```python
  for num in movie_detail['genre_name']: #무비 디테일의 리스트를 하나식 받는다. -> 80 
          for genre in genres:
              if num == genre['id']:
                  movie_detail['genre_name'][idx] = genre['name']
                  idx += 1
  ```

- 더 간단하게 하는 방법이 있을 거 같은데 고민과 공부가 필요할 것 같다.



### 3.  영화 데이터 평점 순으로 놓고 필요한 정보만 반환.

```python
def movie_info(movies, genres):
		....
                    idx += 1
        movie_detail['overview'] = movie['overview'] 
        movie_detail['poster_path'] = movie['poster_path']
        movie_detail['title'] = movie['title']
        movie_detail['vote_average'] = movie['vote_average'] 
        result = result + [movie_detail] # 이전과 다른점 하나 -> 리스트에 딕셔너리 하나씩 추가
    return result

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
	....
```



### 4. 데이터 출력

- 영화 정보를 통해 가장 높은 수익을 낸 영화를 출력해보는 것을 목적으로 알고리즘 작성

- `problem_d`: '처음 여러 파일을 어떻게 접근할까 ?' 라는 고민으로 시작하게 되었고, 파일 이름을 변수로 저장해서 돌리자는 접근으로 문제를 풀게 되었다.

  ```python
  				 ......
          file_name = 'data/movies/'+ str(mov_id) +'.json'
          json_file = open(file_name, encoding= 'UTF8')
          js = json.load(json_file)
                   ......
  
  ```

  

### 추가)

- json 파일 변환

```python
from collections import OrderedDict
    
     ......
        
file_data = OrderedDict()
    file_data = movie_info(movies_list, genres_list)
    with open('problem_c.json','w', encoding='UTF8') as make_file:
        json.dump(file_data,make_file, ensure_ascii=False,indent ='\t')
```

---

### 끝 마치며.

>데이터를 다루는 것을 처음 해보기로 해서 여러 작업들을 해보았다. `json파일`도 처음 다루어봤고 python을 통해 데이터를 다루는 것 또한 처음이었다. 문법을 알고 알고리즘을 푸는 것과 또 다른 어려움이 있었고 더 많은 공부가 필요하다는 것을 느꼈습니다.

