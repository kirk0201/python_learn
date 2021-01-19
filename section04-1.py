# 데이터 타입

str = 'Niceman'
# 앞에 대문자 사용 
bool = True
str2 = 'Goodboy'
float1 = 10.3
int1 = 7
# key와 value의 형태
dict = {
    "name" : "kim",
    "age" : 25
}

list = [3, 5, 7]
tuple = 3, 5, 7
# set은 집합이라 함
set = {7, 8, 9}

i1 = 39
i2 = 939
int1 = 999999999999999
int2 = 777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(int1 * int2)
print(f1 ** f2)
result = i2 + f3
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
# 1
test = print(int('3'))
# 3
print(complex(False))

# 단항 연산자
y = 100
y = y + 100
print(y)

z = 100
z += 100
print(z)

# 수치 연산 함수

# 절대값
print(abs(-7))
n, m = 10, 20

# 몫은 n 나머지 m
n, m = divmod(100, 9)
print("몫 : %d 나머지 : %d" % (n, m))

import math
# ceil은 5.1보다 크면서 가장 작은 정수를 찾음
print(math.ceil(5.1))
# 6
# floor보다 이하 인 수 중에 가장 작은 정수
print(math.floor(3.874))
# 3