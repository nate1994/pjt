import requests
from kobis import URLMaker


def filmo_count(people, movie):
    #http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json
    url_maker = URLMaker('9bda25102558de0a15fdafeacd305593')
    request = url_maker.get_url('people','searchPeopleList')
    payload = {
        'peopleNm' : people,
        'filoNames' : movie
    }
    response = requests.get(request, params = payload).json() #요청 -> 응답
    # print(response)
    people_list = response.get('peopleListResult').get('peopleList')
    for people in people_list: # 각 사람 정보 리스트 탐색 
        if people['filmoNames'].find('아이언맨')> 0:
            mov = people['filmoNames'].split('|')
            cnt = len(mov)        
    return cnt

if __name__ == '__main__':
    # 배우 이름과 작품을 이용하여 총 해당 배우가 몇 작품에 출연했는지 출력합니다.
    print(filmo_count('다우니', '아이언맨'))