
# join() 메소드
s = '-'.join('python')   # 지정한 문자가 join문자열 사이사이에 들어간다
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = '+'.join('abcde')
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()   #  띄어쓰기를 기준으로 []리스트를 만든다.
print(result)


s = '010-1234-5678'
result = s.split('-')  #  -를 기준으로 []리스트를 만든다.
print(result)

data = '이종민|23|프로그래머'
result = data.split('|')
print(result)
print('이름 : {}'.format(result[0]))

# replace() 메소드  ->  문자열 치환
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)


# strip(), lstrip(), restrip() 공백제거

s = '           apple'
print(s)
result = s.lstrip() # 왼쪽 공백 제거
print(result)


s = 'apple          '
print(s)
result = s.rstrip() # 오른쪽 공백 제거
print(result)


s = '       apple          '
print(s)
result = s.strip() # 양쪽 공백 제거
print(result)


s = ' a p p l e '
print(s)
result = s.strip()
print(result)

# 전체 공백(띄어쓰기) 제거
result = s.replace(' ', '')
print(result)






