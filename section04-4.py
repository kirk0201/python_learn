# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 딕셔너리 특징
# 딕셔너리 추가
# 집합 특징
# 집합 자료형 함수
# 자료형 변환

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key,Value (Json) -> MongoDB
# 선언
a = {'name': 'kim', 'phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello python', 1: "Hello coding"}
c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
# get()메소드 이용하기
print(a.get('name'))
print(c['arr'][1:3])
a = {'name': 'kim', 'phone':'01011112222', 'birth': 900101
}
print("g",a['phone'][1:4])

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

# keys, values, items
print("---------------------------------------")
print("a.keys() : ",a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
# 튜플 형태로 나온다
print(list(a.items()))
# key 값이 있는지 확인
print(2 in b)
# key 값이 없는지 확인
print('name2' not in a)

# 집합(sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([5, 6, 7, 7, 8, 8])

print(type(a))
# 중복이 되지 않기 떄문에
print("set(c) :",c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

# s1, s2 교집합
print("교집합 : ", s1.intersection(s2))
print(type(s1.intersection(s2)))
print(s1 & s2)

# 합집합 
# 중복을 허용하지 않기 때문에
# 중복은 사라진 상태로 합해짐
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([1, 2, 3, 4])

s3.add(5)
print(s3)

s3.remove(1)
print(s3)

a = {'name': 'kim', 'phone':'01011112222', 'birth': 900101
}

temp = list(a.items())

print(type(temp[0]))