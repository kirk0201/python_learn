# 파이썬 모듈과 패키지
# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1 (클래스 형태)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
# Fibonacci() 형태로 인스턴스화(클래스 생성)를 시켜줘야 __init__ 초기화 가능
print("ex2 : ", Fibonacci().title)

# 사용2(클래스) 권장하진 않음, 메모리를 많이 사용
from pkg.fibonacci import *

# 사용3(클래스) 별명 사용
from pkg.fibonacci import Fibonacci as fb

# 사용4 (함수)
import pkg.calculations as c
print('ex4 : ', c.add(10, 100))

# 사용5 (함수) 함수 선택해서 가져오기 (추천)
from pkg.calculations import div as d
print('ex5 : ', int(d(100, 10)))

# 사용6
import pkg.prints as p
# 빌트인 함수 , 내장함수?
# 빌트인 함수는 내장되어있어서 import를 안해도 사용가능 
import builtins
p.prt1()
p.prt2()

# 빌트인 함수 출력하기
print(dir(builtins))

