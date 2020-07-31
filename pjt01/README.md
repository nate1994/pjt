# README

- `problem_a`는 간단하게 해결했다.

- `problem_b`는 (리스트 안에 있는 딕셔너리)와 (리스트 안에 있는 인덱스)를 어떻게 매치시키는지에 대한 고민이 필요했고, 딕셔너리 안에 있는 리스트에 접근하여 값을 수정하는 것을 해야했다.

  - 이러한 과정을 통해 데이터 저장을 잘 파악하는 것에 대한 중요성을 느꼈다.

    ```python
    for num in movie_detail['genre_name']: #무비 디테일의 리스트를 하나식 받지여 -> 80 
            for genre in genres:
                if num == genre['id']:
                    movie_detail['genre_name'][idx] = genre['name']
                    idx += 1
    ```

  - 더 간단하게 하는 방법이 있을 거 같은데 고민과 공부가 필요할 것 같다.

- `problem_c` : so easy ; 리스트에 딕셔너리를 집어넣는 방법에 대해 복기 할 수 있었다.

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

​	이게 요구한 사항인지는 모르겠지만 결과는 잘나왔다 :)