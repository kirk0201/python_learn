# 파이썬 흐름 제어

print(type(True))
print(type(False))

# ex1
if True:
    print("yes")

# ex2
if False:
    print("No")
else:
    print("yes2")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)

# 참 거짓 종류(True, False)
# 참 : "내용",[내용], (내용), {내용}, 1
city = ""

if city:
    print(">>>True")
else:
    print(">>>False")

# 논리 연산자
# and or not
a = 100
b = 60
c = 15

print("------------------------")
print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = "A"

if score1 >= 90 and score2 == "A":
    print("합격하셨습니다")
else:
    print("죄송합니다. 불합격하셨습니다")

# 다중 조건문
num = 9

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)    
elif num >= 70:
    print("num 등급 C", num)
else :
    print("num 등급 D", num)

# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height>= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")