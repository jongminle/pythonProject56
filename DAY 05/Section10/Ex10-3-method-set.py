
# 교집합 intersection()
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2) # 중복되는 값 도출

result = s1.intersection(s2)
print(result)


# 합집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 | s2) # 중복값을 제외하면서 모든 값 도출
result = s1.union(s2)
print(result)


# 차집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 - s2)  # s1에서 s2와 중복되는 값을 제외한 s1의 값
result = s1.difference(s2)
print(result)
























