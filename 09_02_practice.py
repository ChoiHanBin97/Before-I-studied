# 연습 : 원에 대한 객체 정의

#  클래스 정의 Circle
#  객체변수(속성) 는 반지름  (radius)

#  생성자 

#  원의 넓이 계산하여 리턴하는 메소드  getArea()
#  원의 둘레 계산하여 리턴하는 메소드  getPerimeter()

# 원주율은 3.141592 로 하자  (후에 math 모듈을 배우면 math.pi 로 사용하면 된다)

#-------------------------------------------
# 클래스 정의,  인스턴스들도 만들고 동작 시켜보기


import math

print(math.pi)

class Circle:
    
    def __init__(self, radius = 0):
        self.radius = radius   # 반지름
        print("Circle() 생성자 호출")
        
    def getArea(self):
        Area = (math.pi)*(self.radius) ** 2
        return Area
    
    def getPerimeter(self):
        Perimeter = 2 * math.pi * self.radius
        return Perimeter


c1 = Circle(10)


print("c1의 area =", c1.getArea())
print("c1의 perimeter =", c1.getPerimeter())

print('-' * 30)


#-----------------------------------------------
# 연습 : 2차원 상의 좌표 객체 정의

#  클래스 정의 Point2D

#  객체변수는 x, y

#  생성자 

#  원점에서 부터 거리 계산 getDistance()

# 파이썬에서 root 구하는 함수는
# import math 후
# math.sqrt(x) 사용   혹은   x ** 0.5


class Point2D:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print("Point20의 생성자 호출")
        
    def getDistance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    

point1 = Point2D(3, 4)
print(point1.getDistance())






























