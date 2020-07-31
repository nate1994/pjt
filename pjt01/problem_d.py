import json

# movies의 for문을 돌려서 -> 각 영화의 id를 통해 json파일을 연다. id 당 수익과 타이틀을 저장한다. 
# ->최종 리턴은 타이틀

def max_revenue(movies):
    result = [] #movies는 리스트 안에 딕셔너리 
    max_revenue = -1
    revenue_result = { }
    for movie in movies:
        movie_detail = {}
        movie_detail['id'] = movie['id']
        movie_detail['title'] = movie['title']
        result = result + [movie_detail]
    for search in result:
        mov_id = search['id']
        file_name = 'data/movies/'+ str(mov_id) +'.json'
        json_file = open(file_name, encoding= 'UTF8')
        js = json.load(json_file)
        if js['revenue'] > max_revenue:
            max_revenue = js['revenue']
            revenue_result['title'] = js['title']
            print(js['id'])
    return revenue_result['title']


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))