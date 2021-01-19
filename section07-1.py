# 파이썬 클래스 상세 이해
# Self, 클래스, 인스터스 변수

# 클래스, 인스턴스 차이 중요 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
                # self 인자가 자동으로 넘어간다

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제 1
# snake case 클래스는 앞을 대문자 단어시작마다 대문자를 사용
class UserInfo:
    # 속성, 메소드
    # __ : 매직 메소드, pass 없어도 됨
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스 : 클래스에 인자로 들어감
# 클래스를 사용하여 인스터스화 시켜 사용하고 있다
# 네임스페이스라는 서로 독립적인 창구를 이용
user1 = UserInfo("kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()
    # class에 아무것도 없다면
    # pass가 있어야 에러가 나지 않음
    # pass

# 예제 2
# self의 이해
print('-------------------------------')
class SelfTest:
    # 클래스 메소드
    def function1():
        print('function1 called!')

    # 인스턴스 메소드
    def function2(self):
        print(id(self))
        print('function2 called!')

test1 = SelfTest()
# test1은 SelfTest클래스를 바탕으로 찍어낸 인스턴스
# test1.function() 인자에 self가 없으면 누구의 메소드 인지모르기 때문에
# 오류 발생 
# 즉 클래스 메소드이므로 SelfTest.function1()로 직접 호출해야함
# test1.function1()
SelfTest.function1()
test1.function2()

print(id(test1))
SelfTest.function2(test1)
print('-------------------------------')
# 예제 3
# 클래스 변수(self x), 인스턴스 변수(self o)

class WareHouse:
    # 클래스 변수
    stock_num = 2
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def kdel(self):
        WareHouse.stock_num -= 1
    # def __mul__(self):
    #     WareHouse.stock_num

user1 = WareHouse("kim")
print(user1.stock_num)
print("test : ",user1.stock_num.__mul__(2))
user2 = WareHouse("park")
user3 = WareHouse("lee")


# 인스턴스 네임스페이스 찍어보기
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# 클래스 네임스페이스, 클래스 변수는 (공유)
print('-----------------------')
print("r",WareHouse.__dict__)
print('-----------------------')
# 인스턴스에서 클래스변수를 호출시 안될것 같지만
# 인스턴스 네임스페이스에서 호출시 없다면 클래스 인스턴스에서 호출함
del user1
print(type(user2))
print(WareHouse.__dict__)


