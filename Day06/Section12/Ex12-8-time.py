'''

time 모듈
    시간 처리에 관련된 time 모듈

'''

import time
# 1970년 1월 1일 0시 0분 0초 부터 현재 까지 견과 시간을 반환
# 마이크로초 까지 표현
print(time.time())


# ctime() 함수 - 인수로 전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
# 날짜 데이터를 문자로 반환
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y년-%m월-%d일 %H시 %M분 %S초'))

print(
    time.strftime(
        '%Y년 %m월 %d일'
        .encode('unicode-escape')
        .decode()
    ).encode().decode('unicode-escape')
)

# 인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1










