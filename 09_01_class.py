# 프로그래밍은 함수중심, 동작 중심이었음
# but 프로그래밍이 커지면 커질수록 관리하기가 어려워짐 
# 객체 지향 프로그래밍을 만듦 -> 발전과정

# 클래스 (class)

# 지금까지의 프로그래밍은 '함수 중심'

# ex) 아래와 같이 goto() 함수 안에 필요한 인자를 넘겨준다

# goto("이길자", "집(논현동 188)")
# goto("김해성", "집(서초동 333)")
# 함수 중심이라는 것은 곧 '동작' 중심이라는 거다.
# 그러나 이는 '실세계'를 표현하는데는 한계가 있다.


# 사람이 인지하는 세상은 '객체 중심' 이기 때문이다

# '객체 중심' 프로그래밍은 다음과 같다.

# 예시]
# Person 클래스(class) 안에 다음의 '틀' 을 정의
#     - 이름 : 이름 정보 담는 '속성'
#     - 집주소 : 주소 정보 담는 '속성'
#     - goHome() : 집으로 가는 '동작' 수행
# 속성은 객체 변수를 통해서 만들것임 
# 동작은 함수를 통해 진행!


# 사람객체(object)들 생성
# lee = Person("이길자", "논현동 188") <- 이름, 집주소 등에 대한 정보가 객체에 담김
# kim = Person("김해성", "서초동 333") <- 이름, 집수소 등에 대한 정보가 객체에 담김

# lee.goHome()
# kim.goHome()

# 프로그래밍의 중심이 '함수' 중심이 아니라, 각각의 객체 중심( lee, kim )..


# 객체는 클래스로 정의를 하고
# 클래스를 통하여 객체를 생성한다   생성된 객체를 인스턴스(instance) 라 한다

# 흔히 클래스(Class ) 를 '붕어빵 틀'이라 하고
# 객체(object) 를 Class 로 찍어낸 '붕어빵'에 비유하곤 한다


# 파이썬에선 다음 순서대로 클래스를 사용한 객체중심 프로그래밍을 한다
#     ① 클래스 정의, class 키워드 사용
#     ② 객체 생성 (생성자 사용), 생성된 객체를 '인스턴스(instance)' 라 한다 
#     ③ 객체 사용 (객체의 변수, 메소드)

# 클래스 이름은 
# 변수나 함수 이름 정의하는 규칙과 거의 동일하나
# 관례적으로 첫글자는 대문자로 한다




# 1. 클래스 정의 (객체 정의[쿠키 객체])   -> 붕어빵 틀을 만든 것이다!
class cookie:
    pass

# 2. 객체 생성, 붕어빵 찍어내기
a = cookie()        # cookie 객체 생성, cookie 인스턴스 생성, 변수 a에 대입
b = cookie()
c = cookie()

print(type(a))      # cookie 타입!
print(type(b))
print(type(c))



# is
print(type(a) is cookie)
print(a == b)       # a와 b는 타입만 같을 뿐 다른 인스턴스다!


# 클래스를 통해 만들어진 객체를 인스턴스(instance)라고도 한다
# 객체와 인스턴스는 다소 혼용되어 표현되기도 한다.
# "a 는 Cookie 의 객체" 다
# "a 는 Cookie 의 인스턴스" 다

#----------------------------------------------------------

# 객체의 '속성' --> 객체변수로 정의
# 객체의 '동작' --> 객체함수(메소드)로 정의


# 클래스 가 가져야 하는 변수를 '객체변수(instance variable)', 혹은 속성값 (attribute value) 혹은 멤버변수(member variable) 이라고도 함
# 어떠한 메소드에서도 self. 키워드를 사용하여 정의 가능하고
# 인스턴스를 통해 생성도 가능.

# 객체변수 사용구문   . 사용
#   객체.객체변수

# 생성자 (Constructor)  __init__()
# 객체가 생성될때 자동으로 호출되는 특별한 메소드
# 주로 객체변수를 정의하고 초기화 하는 역할 수행

# 클래스 안에서 정의된 함수를 메소드(method) 라 함
# 메소드 호출 구문    . 사용
#    객체.메소드()
# 메소드가 호출될때는 해당 '객체' 에 대해서 동작하게 됨

# 모든 메소드는 기본적으로 첫번째 매개변수가 self 이다.



#----------------------------------------------------------
#사각형이란 객체에 대해 설계해보자
#사각형 클래스를 정의해보자!

# 사각형의 속성은? -> 가로(width), 세로(height)
# 사각형의 동작은? -> ??

# rectangle 객체 정의 (클래스 정의, 붕어빵 틀을 제작)
class Rectangle:
    
    def __init__(self):
        print("Rectangle() 생성자 호출")
        # 객체변수들
        self.width = 0      # 객체변수 width 선언, 초기값 0
        self.height = 0     # 객체변수 height 선언, 초기값 0
        
# 각각 객체변수들이 각각의 인스턴스에 할당
        
# Rectangle 객체 생성 (인스턴스 생성, 붕어빵 찍어내기)
r1 = Rectangle()
r2 = Rectangle()
print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r2.width =", r2.width)
print("r2.height =", r2.height)


# 객체가 생성될때 자동으로 호출됨 -> 생성자 ->>print("Rectangle() 생성자 호출")
# 객체 변수를 정의하고 초기화하는 역할 수행


r1.width, r1.height = 100, 200
r2.width, r2.height = 50, 30

print(r1.width, r1.height)
print(r2.width, r2.height)

print("-"*50)
# --------------------------------------------------------------
# 사각형의 동작?   ->>> 객체의 메소드(함수)로 정의
# 사각형의 넓이 구하기
# 사각형의 둘레를 구하기

class Rectangle:
    
    def __init__(self):
        print("Rectangle() 생성자 호출")
        self.width = 0      
        self.height = 0     
        
# 사각형의 넓이를 구하기
    def getArea(self):
        area = self.width * self.height
        return area

# 사격형의 둘레를 구하기
    def getperimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter


print("**메소드**")
r1 = Rectangle()
r2 = Rectangle()
r1.height, r1.width = 10, 20     # 가로 10, 세로 20

print("r1의 넓이 = ", r1.getArea())
print("r1의 둘레 = ", r1.getperimeter())

print("r2의 넓이 = ", r2.getArea())
print("r2의 둘레 = ", r2.getperimeter())


print("-" * 50)

# --------------------------------------------------------------
print("** 생성자 매개변수 **")

class Rectangle:
    # 생성자 매개변수
    # 객체변수 초기하에 사용된ㄷ,
    # 디폴트 매개변수 가능!
    
    def __init__(self, width, height):
        print("Rectangle() 생성자 호출")
        self.width = width       # 생성자 매개변수로 객체변수 초기화    
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area

    def getperimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter


# r1 = Rectangle()               # 에러 : 매개변수 2개 필요
r1 = Rectangle(30, 20)         

print("r1의 넓이 =", r1.getArea())
print(r1.width, r1.height)

# r2 = Rectangle(100)            # 에러 : 매개변수 1개 더 필요


class Rectangle:
    # 생성자 매개변수
    # 객체변수 초기하에 사용된ㄷ,
    # 디폴트 매개변수 가능!
    
    def __init__(self, width = 0, height = 0):
        print("Rectangle(width, height) 생성자 호출")
        self.width = width       # 생성자 매개변수로 객체변수 초기화    
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area

    def getperimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

r1 = Rectangle()
r2 = Rectangle(100)
r3 = Rectangle(20, 30)
print(r2.width, r2.height)




