# 매직 메소드란? (Magic Method)
# 클래스안에 정의할 수 있는 스페셜 메소드이며 클래스를 int, str, list등의 파이썬의 빌트인 타입(built-in type)과 같은 작동을 하게 해준다.
# +, -, >, < 등의 오퍼레이터에 대해서 각각의 데이터 타입에 맞는 메소드로 오버로딩하여 백그라운드에서 연산을 한다.
# __init__이나 __str__과 같이 메소드 이름 앞뒤에 더블 언더스코어("__")를 붙인다.
"""

연산자     메소드                     설명
─────────────────────────
         <binary operator>
         
 +      __add__(self, other)         덧셈 
 *      __mul__(self, other)         곱셈
 -      __sub__(self, other)         뺄셈 
 /      __truediv__(self, other)     나눗셈
 //     __floordiv__(self, other)
 %       __mod__(self, other)             나머지
 **      __pow__(self, other[, modulo])
 >>      __lshift__(self, other)
 <<      __rshift__(self, other)
 &       __and__(self, other)
 ^      __xor__(self, other)
 |      __or__(self, other)
 
 
             <Extended operator>
+=         __iadd__(self, other)
-=         __isub__(self, other)
*=         __imul__(self, other)
/=         __idiv__(self, other)
//=        __ifloordiv__(self, other)
%=         __imod__(self, other)
**=        __ipow__(self, other)
<<=        __ilshift__(self, other)
>>=        __irshift__(self, other)
&=         __iand__(self, other)
^=         __ixor__(self, other)
|=         __ior__(self, other)

        <unary operators>
-
+
abs()
~
complex()
int()
long()
float()
oct()
hex()
        


 <       __lt__(self, other)         작다(미만) 
 <=      __le__(self, other)         작거나 같다(이하) 
 ==      __eq__(self, other)         같다 
 !=      __ne__(self, other)         같지 않다 
 >      __gt__(self, other)          크다(초과)
 >=     __ge__(self, other)          크거나 같다(이상) 
 [index]   __getitem__(self, index)   인덱스 연산자 
 in       __contains__(self, value)   멤버 확인  
 len     __len__(self)                요소 길이 
 str      __str__(self)                문자열 표현 
 
 
         __init__
         __del__
         __new__
 
         __repr__(self)              representative form
 """


s1 = "Hello"
s2 = "Python"

# 다음 두개(씩)의 결과는 같다. 
# 실제로는 MagicMethod가 동작하고 있던 것이었다.
print(s1 + s2)
print(s1.__add__(s2))      # s1 + s2는 __add__ 호출

print(s1 * 2)
print(s1.__mul__(2))

print("python" > "PYTHON")
print("python".__gt__("PYTHON"))

print(s1[0])
print(s1.__getitem__(0))

print("e" in s1)
print(s1.__contains__("e"))


# __repr__, __str__

# __repr__(),  __str__()
# 공통점 : 객체를 문자열 리턴
# 차이점
#    `__repr__` : out 값
#    `__str__` : str(), print() 등에서 문자열(str) 변환시 호출됨, 
#                 오버라이딩 안되어 있으면 __repr__ 의 값을 리턴한다


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
        
s1 = Student("김수진", 3)
print(s1)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __repr__(self):
        return "이름 %s, 학년 %d" % (self.name, self.grade)
    
s2 = Student("박수진", 4)
print(s2)

myList = [10, 20, 30]
print(myList)
print(myList.__repr__())




# MagicMethod 를 오버라이딩 하면
# 객체 간의 연산도 가능해진다.

class Number:
    def __init__(self, number):
        self.number = number
        
    def __repr__(self):
        return str(self.number)
        
f1 = Number(10)
f2 = Number(20)

print(f1, f2)
# print(f1 + f2) 는 에러
      # f1 + f2 ==> f1.__add__(f2)


class Number:
    def __init__(self, number):
        self.number = number
        
    def __repr__(self):
        return str(self.number)
        
    def __add__(self, other):
        return self.number + other.number

        
f1 = Number(10)
f2 = Number(20)

print(f1 + f2)      #f1.__add__(f2)

f3 = Number(30)
#  print(f1 + f2 + f3)      # 에러 
# 정수 + 정수 + Number의 합임 => number + number + number의 합으로 만들어줘야함
~

class Number:
    def __init__(self, number):
        self.number = number
        
    def __repr__(self):
        return str(self.number)
        
    def __add__(self, other):
        return Number(self.number + other.number)

f1 = Number(10)
f2 = Number(20)
f3 = Number(30)
print(f1 + f2 + f3)




















