


# 서버에 정보 요청

# import requests

# url = 'https://fakestoreapi.com/carts'
# response = requests.get(url)
# print (response.json())



# json

# import json # 내장 모듈

# json_data = '''
# {
#     "name" : "김싸피",
#     "age" : 28,
#     "hobbies" : [
#         "공부하기",
#         "복습하기"
#     ]
# }
# '''

# data = json.loads(json_data) # 문자열을 딕셔너리로 변화시켜준다. (Parsing)

# name = data.get('name') # JSON 데이터에서 원하는 데이터만 가져오기

# print(name)


