'''


'''
member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄 제거 목적
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"') # 회원명의 ""제거
        member[2] = member[2].strip('\n') # 등록일 뒤에 \n (줄바꿈) 제거

        member_list.append(member)

print(member_list)