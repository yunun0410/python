# 문자열은 [이뮤터블] - 변경 불가능 / [뮤터블]  - 변경 가능
# 문자열 - 이뮤터블(변경이 불가능)
# +=, -=, *=  할당 연산자 -> 복합 할당 연산자
# x += 2 -> x = x + 2

# x = 'Answer : '
# x += 'Yes'

# print(x) # -> Answer : Yes

# x = ''

# for i in range(100000):
#     x += '*/*-*'

# print(x)

# x = '*/*-*' * 100000
# print(x)

# 문자형 -> 이뮤터블 하면서 시퀀스 성격갖고 있다
# 시퀀스 : 순서가 있는 데이터 타입
#        순서가 있는 자료형에게 부영되는 성격이고 성격을 갖게되면 인덱스를 갖게됨

# () : 소괄호 / {} : 중괄호 / [] : 대괄호
# x = 'hello.txt'
# print(x[5])
# x[5] = '-'

# 'hello'
# x[시작 인덱스 : 종료 인덱스]
# x[0:4] -> x[0:5] : 출력을 원하는 마지막 값의 +1 
# print(x[:5])

# 'txt'
# print(x[6:])

# print(x[-1:])

# 스트라이드(보폭)
# x[데이터 시작 위치, 데이터 끝 위치, 스트라이드(보폭)]
# x = '-H-E-L-L-O'
# print(x[1::2])

# 비교 연산자 -> 같다 '=='
# x = input("거꾸로 해도 동일한 단어인지를 확인하는 서비스. 단어 입력 : ")
# print(x == x[::-1]) # 단어를 거꾸로 했을 때 동일한 언어를 찾는 로직 

# 내장 함수 / 내장 메서드
# print() / x = 'abc' -> x.upper()

# x = 'Python'
# print(x.upper()) # 글자를 대문자로 변경
# print(x.lower()) # 글자를 소문자로 변경

# print(x.startswith('py')) # 찾는 글자가 있는 지 확인
# print(x.lower().startswith('py'))
# print(x.lower().endswith('py'))

# file = 'hello.py'
# replace('바꾸고싶은 값', '원하는 값', '앞에서부터 변경할 개수')
# print(file.replace('py', 'txt'))

# x = 'ababacvada'
# print(x.replace('a', 'A', 3))

# x = 'banana' 
# print(x.count('a'))

# name = 'Guido van Rossum'
# print(name[:5])
# print(name.find(' ')) # 찾는 단어의 첫번째인덱스를 알려줌
# print(name[:name.find(' ')])

name = input("전화 번호를 입력하시요(-도 같이 입력하시요) : ")
print(name[:name.find('-')])

if name.find('*') == -1:
    print("입력한 값 중에 '*'를 찾을  수 없습니다")
