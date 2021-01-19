# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 힘수명(parameter)
# code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(w):
    val = "Hello " + str(w)
    return val

str1 = hello_return("world!")
print(str1)

# 예제3 (다중 리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3
# 튜플형식
ans = func_mul(2)
# 개별 
val1, val2, val3 = func_mul(2)
print("튜플 형식 : ",ans)
print("개별 : ", val1, val2, val3)

# 예제4
# *args, *kwargs

def args_func(*args):
    # print(args)

    # enumerate
    for i, v in enumerate(args):
        print(i, v)

args_func("kim")
args_func("kim", "Park")
args_func("Kim", "Park", "Lee")

# kwargs
def kwargs_func(**k):
    print(k)

kwargs_func(name1 = 'kim', name2 = 'jung', name3 = 'choi')

# 혼합 형태
def example_mul(arg1, arg2, *arg, **kwargs):
    print(arg1, arg2, arg, kwargs)

example_mul(11, 22, '포트번호','엔드포인트', name1 = "kim", name2 = "park")

# 중첩함수 (클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제 6
# Hint : 힌트를 어길시 오류가 생기지는 않음'
def func_mul4(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul4(1))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int ) -> int:
    return num * 10

var_func = mul_10
print(var_func(1))

# 람다식을 많이 사용하면 가독성이 오히려
# 떨어질수 있다
lambda_mul_10 = lambda num: num * 10
print('>>>1', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

func_lambda = lambda num: num * 10
print('>>>', func_lambda(10))

def func2(x, y, func3):
	print(x * y * func3(10))

func2(1, 2, func_lambda)