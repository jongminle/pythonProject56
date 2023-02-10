'''

모듈 설치 requests
pip install requests
conda install requests


'''

import requests

url = 'https://n.news.naver.com/article/469/0000722807?cds=news_media_pc&type=editn'
param = {'code': 161967}
response = requests.get(url, param=param)
print(response.text)

















