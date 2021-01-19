# 문자열, 문자열 연산, 슬라이싱

str1 = "Hello world"
str2 = 'Bye python'
str3 = '  '  # 1
str4 = str() # 0
# 문자열 길이 len()
# 공백도 메모리에 할당됨
print(len(str1), len(str2), len(str3), len(str4))

# 이스케이프 문자
escape_str1 = "그가 말했다 \"넌 안돼\""
print(escape_str1)
escape_str2 = "tab\ttab\ttab"
print(escape_str2)

# Raw String : 원문 그대로 출력
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티 라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77))
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참고 w3schools.com
a = 'niceman'
b = 'orange'

# islower() : 모두 소문자인지 찾는 함수
print("islower() ",a.islower())
# endswith() : 끝 글자가 어떤 문자로 끝나는지 확인하는 함수
print("endswith() ",a.endswith('s'))
# capitalize() : 첫 글자로 대문자로 치환
print("capitalize() ",a.capitalize())
# replace() : 첫번째 인자를 두번째 인자로 치환
print(a.replace('nice', 'good'))
# reversed() : 문자열을 거꾸로 배열화 시킴
# list()를 하지 않으면 메모리값으로 나온다?
print("reversed() ",list(reversed(b)))

# 문자열 슬라이싱 중요!
print(a[0:3]) # nic
print(a[0:len(a)]) # niceman
print(a[:4]) # nice
print(a[:]) # niceman
# [ : : ?] ?에는 몇칸씩 건너뛸지
print(b[0:4:2]) # oa
print(b[1:-2]) # ran
print(b[::-1]) #egnaro

num = 77
ischange = str(num)
# print(type(str(num)))
if type(ischange) is str:
    print("형변환이 되었습니다")