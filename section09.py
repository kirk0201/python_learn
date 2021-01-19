# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드 (기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제1
f = open("./resource/review.txt", 'r')
content = f.read()
print(content)
# 메서드 확인하기
# print(dir(f))

# 외부 리소스를 사용할 때는 반드시
# 반드시 close 리소스 반환
f.close()
print('--------------------------------------')
# 예제2
# close()가 자동으로 호출?
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

print('--------------------------------------')
# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # 한 줄 단위로 끊어서 출력
        # print(c)
        # 해결 방법
        print(c.strip())

print('--------------------------------------')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    
    # 출력이 되지 않는 이유는 한번 위에서 읽고 커서가 맨끝으로 갔기 때문에
    content = f.read()
    print(">", content)

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end = "####")
        line = f.readline()

print('--------------------------------------')
print('--------------------------------------')
# 예제6 readlines() 모든 문장을 리스트형태로 출력
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end = ' ***** ')

print('--------------------------------------')
print('--------------------------------------')

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
# string format{:6.3} : 6자리고 소수점 3째자리 까지 나와라 
print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제 1 'w' : 새 파일 생성
with open('./resource/text1.txt', 'w') as f:
    # 줄바꿈을 추가하려면 \n 추가하면 가능
    f.write('Niceman!')

# 예제 2 'a' : 기존 파일에 내용 추가
with open('./resource/text1.txt', 'a') as f:
    # 줄바꿈을 추가하려면 \n 추가하면 가능
    f.write('Goodman!')

# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for n in range(5):
        f.write(str(randint(0, 50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n','Park\n','Cho\n']
    f.writelines(list)

# 예제 5
# 콘솔에 찍히지 않고 파일에 로그 내용을 저장할때
with open('./resource/text4.txt', 'w') as f:
    print('Test Contest1!', file = f)
    print('Test Contest2!', file = f)