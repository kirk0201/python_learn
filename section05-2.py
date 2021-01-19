# 파이썬 흐름제어(반복문)
# 반복문 실습

# 기본 반복문 :for, while

v1 = 1
while v1 < 5:
    print("v1 : ", v1)
    v1 += 1

for x in range(5):
    print("x : ", x)

for x in range(1, 5):
    print("x : ", x)

# 1 ~ 100 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1, 101)))
print('1 ~ 100 : ', sum(range(1, 101, 2)))
print(sum(range(2, 10, 2)))

# 시퀀스 (순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집할, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip
color = ["blue", "green", "red", "purple", "black"]
for c in color:
    print("color : ", c)

word = "python"

for s in word:
    print("Word : ", s)

my_info = {
    "name": "kim",
    "age" : 33,
    "city" : "Seoul"
}

# 기본 값은 키
for e in my_info:
    print("e : ", e)
print("----------------------------")
# 키
for dic in my_info.keys():
    print("my_info : ", dic)

print("------------------------")

# 값
for dic in my_info.values():
    print(">>> e : ", dic)

# 키 and 값
for v, c in my_info.items():
    print(">>> info : ", v, c)

name = "KennRY"
ans = ""
for ch in name:
    if ch.islower():
       ans += ch.upper()
    elif ch.isupper():
        ans += ch.lower()
print(ans)

# break
numbers = [2, 1, 6, 7, 8]

# for num in numbers:
#     if num == 33:
#         print("found : 33!")
#         break
#     else:
#         print("not found : 33!")

# for - else 구문(반복문이 정상적으로 수행된 경우 else블럭 수행)
for num in numbers:
    if num == 6:
        print("found : 6!")
        break
    else:
        print("not found : 6!")
else:
    print("Not found 6......")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for ele in lt:
    if type(ele) is str:
        print("데이터 타입이 str인 원소 : {}, ele의 인덱스 : {}".format(ele, lt.index(ele)))
    
# 만약 실수형일때를 제외하고 출력하고 싶다면
for ele in lt:
    if type(ele) is bool:
        continue
    print(">>> 데이터 타입 : ", type(ele))

word = "python"
answer = ""
print(''.join(list(reversed(word))))
