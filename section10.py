# 예외처리의 이해
# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# print('Test)
# if True
    # pass

# NameError : 참조변수 없음
a = 10
b = 15

# NameError
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])

# 예외발생
# print(x[3])

# KeyError :
dic = {
    'name': 'kim',
    'age': 33,
    'city': 'seoul'
}

# 키 에러
# print(dic['hobby'])

# 추천방법
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 이용시 예외
import time
print(time.time())

# 예외 발생 : month()라는 속성이 없다
# print(time.month())

# ValueError : 참조 값이 없을 떄 발생
x = [1, 5, 9]

# valueError
# x.remove(10)
# x.index(10)

# FileNotFoundError

# 예외 발생
# f = open('test.txt', 'r')

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# 예외 : 타입 에러, 리스트와 튜플은 결합할수 없다
# print(x + y)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1
name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    # print('{} Found it! in name'.format(z, x + 1))
except ValueError:
    print("Not Found it! - Occurred ValueError!")
else:
    print("Ok! else!")

# 예제 2
try:
    z = 'jin'
    x = name.index(z)
    # print('{} Found it! in name'.format(z, x + 1))
# 어떤 에러가 발생할지 모를때는  except그대로 둠
# except: 은 except Exception: 같다
except:
    print("Not Found it! - Occurred Error!")
else:
    print("Ok! else!")
# 예외가 발생하든 발생하지 않든 무조건 실행
finally:
    print('finally ok!')

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok finally!')

# 예제 5
try:
    z = 'jin'
    x = name.index(z)
    # print('{} Found it! in name'.format(z, x + 1))

# 여러 예외 처리를 할 때 순서가 중요
# Exception은 모든 에러를 포함하기에 가장 마지막
except ValueError:
    print("Not Found it! - ValueError Error!")
except IndexError:
    print("Not Found it! - IndexError Error!")
except Exception:
    print("Not Found it! - Occurred Error!")
else:
    print("Ok! else!")
finally:
    print('finally ok!')

# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'kim3'
    if a == 'kim':
        print('ok! 허가')
    # 직접 문제를 발생시켜서 활용 가능함
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')

List = [1, 1, 0, 1, 1, 1]
class Solution:
    count = 0
    mostn = 0
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        for n in nums:
            if n == 1:
                Solution.count += 1
            elif n != 1:
                if Solution.mostn <= Solution.count:
                    Solution.mostn = Solution.count
                Solution.count = 0
        return Solution.mostn

ins1 = Solution()
print(ins1.findMaxConsecutiveOnes([1, 1, 0, 1]))
print((-4)**2)
ls = [16, 1, 0, 9, 100]
print(ls)