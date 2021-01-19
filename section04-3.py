# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)

# 선언 방법
a = []
b = list()

c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱

# d에서 Banana를 꺼낼때
print(d[3]) # Banana
print(d[-2]) # Banana
print(d[0] + d[1]) # 110

# e에서 Banana 꺼내기
print(e[2][1]) # Banana
print(e[-1][-2]) # Banana

# 슬라이싱
print("e[0:2] ",d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)
# 슬라이싱을 처리를 하면 하나의 리스트에 원소가 그대로 들어감
c[1:2] = 100, 1000, 10000
print(c)
# 하나의 인덱스를 잡고 추가하면 리스트가 중첩되어 들어감
c[1] = ['a','b','c']
print(c)

# 삭제 del()
del(c[1])
print("del :",c)
del c[-1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
# append() 끝에 원소 추가
y.append(6)
print(y)
# sort() 원소 정렬
y.sort()
print(y)
# reverse() 반대로 정렬
y.reverse()
print("reverse :", y)
# insert() 첫번째 인자 인덱스에 추가

y.insert(2, 7)
print("insert() : ",y)
# remove() 해당하는 원소를 지움
# del과 remove 차이
# del은 인덱스를 지우고 remove는 원소를 찾아서 삭제
y.remove(2)
y.remove(7)
print(y)
y.pop() # LIFO stack 먼저들어간게 나중에 나온다
print(y)
ex = [88, 77]
ex.extend([105])
print('extend : ', ex)
ex.append(106)
print("append : ", ex)
# extend() : 끝 부분에 연장
# append로 ex추가시 배열 자체가 추가
# extend로 추가시 원소만 추가
# y.append(ex)
# y.extend(ex)
print(y)

# 삭제 : del, remove. pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)
# 뒤에 ,로 끝내야함
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a','b','c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2])
print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

# 튜플 함수
z = (5, 2 ,1 , 3, 4, 2, 2)
print(z)
# in 존재하는지
print(3 in z)
# index() 몇번째 인덱스에 있ㄴ느지
print(z.index(1))
# count()튜플안에 원소가 몇개 있는지
print("count : ",z.count(2))

a = [1, 2, 3, 4]
b = [10, 100, ['Pen', 'Banana', 'Orange']]

print(a * 3)
family = ['mother', 'farther', 'gentlemen', 'sexy lady']
print(len(family))

a = [1, 2, 3, 4, 5]

while a:
    l = a.pop()
    print(2 is l)