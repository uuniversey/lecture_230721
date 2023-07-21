

API_KEY = '96c426ee230a53b0799861a32e91762b'

lat = 37.56
lon = 126.97
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

import requests
# API 요청 보내기
response = requests.get(url).json()
print(response)

## 온도만 출력
temp = response['main']['temp']
temp -= 273.15
print(temp)

# 날씨만 description
description = response['weather'][0]['description']
print(f'날씨 설명: {description}')