# python 개발자의 철학
# import this

import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'
print(type(myName))

# 조건문
if type(myName) == 'str':
    print('ok')
else : 
    print('No!')

# 반복문 구구단
for i in range(1, 10) :
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)

# 함수 선언
def greeting() :
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))

