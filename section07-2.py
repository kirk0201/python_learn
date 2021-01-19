# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

    # 부모에도 존재하는 메소드
    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # sub
print(model1.show()) # Super
print(model1.show_model()) # sub

# model1 네임스페이스 보기
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# depth가 깊을때 확인 할 수 있는 메소드 : Inheritance(상속) Info
print(BmwCar.mro())

# 예제2 
# 다중 상속

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

# 다중 상속을 확인 가능
print(M.mro())