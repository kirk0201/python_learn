# Section05-3
# 파이썬 흐름제어(제어문)


# 1 ~ 5 문제 for나 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
ch = "가을"
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for a1 in q1.keys():
    if a1 == "가을":
        print(f"{ch} 값 ", q1[a1])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k2, v2 in q2.items():
    if v2 == '사과':
        print(k2, v2)
        break
else:
    print("사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 11

if score >= 81:
    print('A학점', score)
elif score >= 61:
    print('B학점', score)
elif score >= 41:
    print('C학점', score)
elif score >= 21:
    print('D학점', score)
else:
    print('E학점', score)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
li = [12, 6, 18]

for ele in li:
    if type(ele) is int:
        print("가장 큰 수 : ", max(li))
print()
print()
print()
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

# if num[:1] == "1" or num[:1] == "3":
#     print("넌 남자")
# elif num[:1] == "2" or num[:1] == "4":
#     print("넌 여자")
# else:
#     print("잘못된 주민번호")

num = "489456123"

if num[0] in ["1", "3"]:
    print("넌 남자")
elif num[0] in ["2", "4"]:
    print("넌 여자")
else:
    print("잘못된 주민번호")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for ele in q3:
    if ele == "정":
        continue
    print("정 제외 출력 : ", ele, end=', ')

q4 = [x for x in q3 if x != '정']
print(q4)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1, 101, 2):
    print("홀수 : ", n)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for ele4 in q4:
    if len(ele4) >= 5:
        print('5글자 이상의 단어 : ', ele4)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for ele5 in q5:
    if ele5.islower():
        print("소문자 출력 : ", ele5)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

ans = ""
for ele6 in q6:
    if ele6.islower():
        ans += ele6.upper()
        print("소문자 -> 대문자 : ", ele6.upper())
    else:
        ans += ele6.lower()
        print("대문자 -> 소문자 : ", ele6.lower())
else:
    print(ans)

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)

print("numbers : ", numbers)

# 리스트 컴프리헨션 (List Comprehension)
numbers2 = [x for x in range(1, 101)]
