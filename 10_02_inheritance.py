# 클래스의 상속 (inheritance)


# 기존의 만들어진 클래스를 상속받아 새로운 클래스 정의 가능

# 상속받아 만들어진 클래스는 기존의 클래스의 메소드, 객체변수 를 그대로 가지고 있다.
# 상속받은뒤, 새로운 객체변수, 메소드 추가 할수 있다.
# 상속받은뒤, 상속받은 메소드 재정의 가능 (오버라이딩)

# 상속의 장점: 
#    기존의 코드를 다시 재작성 할 필요 없이. 새로이 변경 추가 되는 코드에만 집중할수 있기 때문에 생산성 향상

# 기존의 클래스 상속하여 새로운 클래스 정의하는 구문
#    class 새클래스명(기존의 클래스명)

# 기존의 클래스를 '부모클래스(parent class)' 라고 하고  (혹은 super class,  base class ...)
# 상속받은 클래스를 '자식클래스(child class) 라고 한다  (혹은 sub class, derived class ...)


#-------------------------------------------------------------
class BasicTV:
    
    def __init__(self):
        self.power = False   # 전원
        self.channel = 1     # 채널
        self.volume = 1      # 볼륨 
        
    def display_info(self):
        print("전원 :", self.power)
        print("채널 :", self.channel)
        print("볼륨 :", self.volume)


tv1 = BasicTV()
tv1.power = True
tv1.channel = 24
tv1.volume = 14

print(tv1.display_info())

class SmartTV:
    
    def __init__(self):
        self.power = False       # 전원
        self.channel = 1         # 채널
        self.volume = 1          # 볼륨
        self.IP = "192.168.0.1"  # IP
        
    def display_info(self):
        print("전원 :", self.volume)
        print("채널 :", self.channel)
        print("볼륨 :", self.volume)
        print("IP :", self.IP)


tv2 = SmartTV()
tv2.display_info()


print("*" * 50)
#------------------------------------------------------
# 상속을 사용한 SmartTv 정의

class SmartTV(BasicTV):
    def __init__(self):
        super().__init__()
        self.IP = "192.168.0.1"   # 추가되는 것만 수행
        
    # 부모(BasicTV)가 원래 가지고 있던
    # display_info()를 변경                            # 오버라이딩
    def display_info(self):
        super().display_info()
        print("IP", self.IP)

tv2 = SmartTV()
print(tv2.__dict__)
tv2.display_info()




# -------------------------------------------------------
print("*" * 50)

# 2차원 원 Circle 객체 정의

import math


class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
        
    def getArea(self):        # 면적
        return math.pi * self.radius ** 2
    
    def getParameter(self):   # 둘레
        return 2 * math.pi * self.radius


c1 = Circle(10)
print(c1.getArea())
print(c1.getParameter())


print("*" * 50)
# Circle을 상속받아서 Sphere(구) 객체를 만들기

class Sphere(Circle):
    # 추가되는 메소드 : 부피 구하기
    def getVolume(self):
        return (4 / 3) * math.pi * self.radius ** 3
    
    
    
s1 = Sphere(10)
print("부피 :", s1.getVolume())
print("둘레 :", s1.getParameter())
print("면적 :", s1.getArea())
# 원의 면적과 구의 넓이는 구하는 공식이 다름
# -> 새로이 바꿔야함

# 메소드 오버라이딩 (overriding)
# 부모로부터 상속받은 메소드 재정의

# 클래스가 상속관계에 있을때, 
# 클래스의 메소드와 동일한 이름으로 자식 클래스 쪽에서 재작성 하는 것을 
# 메소드 오버라이딩 이라 한다


print(Circle.__dict__)
print("*" * 50)
print(Sphere.__dict__)

# Sphere에는 상속받은 걸 제외하고 getVolume만 있음


class Sphere(Circle):
    # 추가되는 메소드 : 부피 구하기
    def getVolume(self):
        return (4 / 3) * math.pi * self.radius ** 3
    
    def getArea(self):   #메소드 오버라이딩
        return 4 * math.pi * self.radius ** 2


    
s1 = Sphere(10)
print("부피 :", s1.getVolume())
print("둘레 :", s1.getParameter())
print("면적 :", s1.getArea())



print(Circle.__dict__)
print("*" * 50)
print(Sphere.__dict__)



















