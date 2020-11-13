import requests
#import urllib.request
header = {
    "X-Naver-Client-id" : 'NxX6OVwc3ZRLPCLzoNBH',
    "X-naver-Client-secret" : 'c2h_cuitbg'
}
url ='https://openapi.naver.com/v1/search/movie?query='
text = '기생충'
res = requests.get(url+text, headers = header).json()
# print(res)
main_actor = [] #주연배우들 
actors_string = res.get('items')[1].get('actor') 
main_actor = actors_string.split('|')
main_actor.pop() #마지막 |제거 
print(main_actor)