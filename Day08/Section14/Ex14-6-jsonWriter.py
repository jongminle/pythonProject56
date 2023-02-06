'''

JSON (JavaScript Object Notation)
    - 딕셔너리 비슷하다
    - 구조 { k : v }

'''

import  json

# 첫 번째 방법
'''
dict_list = [
    {
        'name':'james',
        'age':28,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'alice',
        'age':21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
json_string = json.dumps(dict_list)
with open('dictlist.json', 'w') as file:
    file.write(json_string)
print('dictlist.json 파일이 생성되었습니다.')
'''

# 두 번째 방법

dict_list = [
    {
        'name':'james',
        'age':28,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'홍길동',
        'age':21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
# indent 들여쓰기, ensure_ascii=False 한글읽기
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
with open('dictlist.json', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictlist.json 파일이 생성되었습니다.')













