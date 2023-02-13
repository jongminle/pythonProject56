'''

모듈 설치 requests
pip install requests
pip install chardet
pip install brotli

conda install requests

https://movie.naver.com/movie/bi/mi/basic.naver?code=10016
'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param = {'code': 10016}
response = requests.get(url, params=param)
print(response.text)

















