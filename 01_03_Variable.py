# print(100) Inmdentation Error 
#  파이썬은 들여쓰기, 열 맞추어야 한다.

"""
 print(100)
 print(200)
 print(300)
print(400)
print(500)
print(600)

"""
# 변수 (Variable)
# 데이터를 담아두는 공간
# '변수이름(Variable name)'을 정해서 담아둔다.
# 변수 안의 데이터는 언제든지 변경 가능(변할 수 있다!)

# 변수 사용법
# 변수 이름 = 값
 
# = : 대입연산자(assignment operator)
#  프로그래머는 '변수'에 어떠한 '타입'의
#  어떠한 '값'이 담겨 있는지 놓치면 안돼요~!
#  '타입', '값' 놓치면 안됨!!! 완전 중요.



a = 10      # a 라는 변수에 int 10을 대입 -> a는 int 타입
print('a 값은', a, "입니다.")
b = 5
print(a + b)
            # print(c)  NameError : 선언한 적 없는 변수 사용 불가
            # 최초로 변수에 값을 넣는 것을 선언한다라고 함
            # print(A): 변수이름 대소문자 구분!

# 변수명 지켜야 할 규칙
abc2020 = 100  # 변수명으로는 알파벳, 숫자, _ 가능
               # 2020abc = 100와 같이 숫자로는 시작하면 안됨
abc_2020 = 200 # OK
               # aaa bbb = 300과 같이 띄어쓰기 불가
_abc_ = 400    # _로 시작 가능
강아지 = 500   # 한글도 가능은 하나... 하지말자~
               # $aaa = 600와 같이 특수기호 불가
               # class = 700와 같이 예약어들은 변수명 사용 불가

myName = '최한빈'
print("제 이름은", myName, "입니다.")     # ','에는 빈칸이 들어감
print("제 이름은 " + myName + " 입니다.") # '+'에는 빈칸이 안들어감

age = 24
print("제 나이는", age, "살 입니다.")
  # print("제 나이는 " + age + "살 입니다.") 문자열 + 정수열 불가

# 형변환 함수들
# 각 타입별로 형변환 할 수 있는 함수들
#  int(), str(), float() ...
print(age, type(age))
print(str(age), type(str(age)))
print(type(age))
    # int(myName)   ValueError : 형 변형 불가
print("제 나이는", str(age), "살 입니다.")
num1 = "100"
    # print(num1 + 200) 불가
print(int(num1) + 200)
print(int(3.14)) #  소숫점이 잘린 정수로 바뀜    3.14 -> 3
print(type(float(3)))
print("num1", num1)

# del() : 변수 없애기 
del(num1)
         # print(num1) NameError


# ; : 여러 변수를 한줄에 선언
a = 10; b = 20; c = 30 
print(a, b, c)

# 파이썬 다운(?) 한줄에 여러 변수 선언
a, b, c = 100, 200, 300
print(a, b, c)

# 기존의 변수의 값을 일정량 증가, 감소, 변화 시키기
a = 10
print(a)
a = a + 1   # 기존의 a 값에 1 증가  //  오른쪽에 있는 값이 왼쪽으로 대입
print('a=', a)
a = a * 2
print("a=", a)
a = a - 1
print("a=", a)
a = a / 7
print("a=", a)



# 복합 대입 연산자 사용
a, b, c = 100, 10, 7
a += 10       # a= a+10 이라는 의미
b /= 2
c %= 2        # c를 2로 나눈 나머지
print(a, b, c)        


# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a,b)

# 일반적인 프로그래밍 언어에서의 방법
temp = a     # 임시변수 temp 사용
a = b
b = temp
print(a,b)

# 파이썬에서의 방법
a, b = b, a
print(a,b)



