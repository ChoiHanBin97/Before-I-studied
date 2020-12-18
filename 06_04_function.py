print("안녕하세요")
print("제 이름은 최한빈입니다.")

print("안녕하세요")
print("제 이름은 이승원입니다.")

print("안녕하세요")
print("제 이름은 김기현입니다.")

print("안녕하세요")
print("제 이름은 김유진입니다.")



# 함수 (function)
# 프로그래밍에서 동일한(혹은 거의 비슷한) 내용의 코드가 반복될때가 있다.
# 바로 이러한 코드 낭비를 없애기 위해
# 반복되는 코드를 묶어서 하나의 함수로 정의해 놓고 사용하는 것이다

# 즉, 반복되는 부분이 있을 경우 "반복적으로 사용되는 가치 있는 부분"을 
# 한 뭉치로 묶어서 
# "1. 어떤 입력값(매개변수)을 주었을 때, 
#  2. 어떠한 일을 수행하고, 
#  3. 어떤 결과값(리턴값)을 돌려준다" 라는식의 
# 함수로 작성하는 것이 현명하다.
#----------------------------------------------------------
# 함수 만들기 (함수 정의 : Function Definition)

# def 키워드로 작성  (define)

# def 함수이름( 매개변수 들):
#     함수 본체 <수행할 문장1>
#     함수 본체 <수행할 문장2>
#     ...

# 함수의 동작 정의
#   입력(매개변수) -> 본체 수행 -> 결과(리턴)

# 함수이름은 변수 이름 작성과 거의 동일한 규칙
#----------------------------------------------------------
# 함수 호출 (함수 사용 )  Function call, invoke
# 함수호출시 넘겨지는 인자(parameter) 값들은
# 함수의 매개변수(argument)들이 받습니다.
# 매개변수는 0개, 한개, 여러개 있을수 있을수 있습니다

# 함수에는 리턴값이 있다.
# 리턴값은 함수를 호출(call) 한쪽에 돌려준다
# return 키워드로 리턴값을
# 함수 본체 수행중 return 을 만나면 함수를 종료 하게 됩니다
# 어떠한 타입도 리턴할수 있다.
# 리턴값은 없을수도 있다.

print()


# 함수 정의   -> 수행한단느 의미는 아님
# 함수 이름 : sayAnthem
def sayAnthem():
    print("동해물과 백두산이")
    print("마르고 닳도록")
    print("하나님이 보우하사")
    print("우리나라 만세")


# 함수 호출
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()


print()

# 함수 정의
# 매개변수 지정
def sayHello(name):
    print("안녕하세요")
    print("제 이름은", name, "입니다.")

# 매개변수 지정된 함수는 호출 시 반드시 매개변수에 넘겨줄 값(인자)있어야 한다.
# sayHello(인자값들...[arguments])
# sayHello()   # TypeError
    
sayHello("이윤지")
sayHello("강송희")


# 함수 정의
def sayAge(age):
    print("제 나이는요....")
    print(age, "살 입니다.")

sayAge(100)
sayAge(23)
sayAge(77)



# 함수가 다른 함수 호출 가능합니다.
# 함수 호출 -> 정의된 함수로 감 -> 다시 돌아옴 : 리턴
def sayName(name, age):
    print("---" * 10)
    sayHello(name)
    sayAge(age)
    print("---" * 10)
#   return 생략되어있음 


# sayName("김오영")        # typeError
sayName("김오영", 24)
sayName("한병인", 58)
sayName("토르", 100)


# 함수 호출 시 매개 변수 명시 가능!
# 순서가 바뀌어도 동작 가능!

sayName(name = "정승희", age =25)
sayName(age =25, name = "정승희")


# return
# -- 함수 종료
# -- 호출한 쪽으로 '값'을 돌려준다.

def codeEveryday():
    print("파이썬 열공중")
    print("Life is short")
    print("You need python")
    return

codeEveryday()
print("종료")

print()

# 동일 이름의 함수 정의하면 이전 함수의 정의는 사라짐 -> 덮어쓰기
def codeEveryday():
    print("You need python")
    print("파이썬 열공중")
    return                           # return None 이 생략
    print("Life is short")


codeEveryday()


print()

#

def sum(num1, num2, num3):
    result = num1 + num2 + num3
    return result                   # 값을 리턴할 수 있다.

print(sum(10, 20, 30))

result = sum(20, 20, 20) + sum(30, 30, 30)
print("result =", result)


a = sum(1, 1, 1)
b = sum(2, 2, 2)
c = sum(3, 3, 3)

print(a, b, c)


