
# 내가 설명 넣기
'''

try:
    raise Exception('강제로 발생시킨 예외')
except Exception:
    print('강제로 발생시킨 예외')
'''

# Exception에서 나오는 설명

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print('강제로 발생시킨 예외메세지는 다음과 같습니다')
    print(e)




















