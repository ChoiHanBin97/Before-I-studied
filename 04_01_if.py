# 제어문 (control)
#    1. 조건문 : if~ else
#    2. 순환문 : while, for



# 조건문, 반복문에 대해 작용
# 조건문 (if ~ elif ~ else)

# if 조건식:             #  조건식은 참 or 거짓인지 판명가능해야함
#    참일때 수행 구문 블록  (블록이란 문장들의 집합,   : 다음에 나옴)
#    거짓일때 수행안하고 넘어감

a = 1
if a > 0 :
     print("변수 A 값은")
     print(a, "는 양수입니다.")                  # 참일 때 수행 o
     
print("if 종료")     

a = 0
if a > 0 :
     print("변수 A 값은")
     print(a, "는 양수입니다.")                  # 거짓일 때 수행 x
     
print("if 종료")    

# if 조건식:
#    참일때 수행 구문 블록
# else:
#    거짓일때 수행 구문 블록

print("*" * 50)

a = 32

if a % 2 == 0:
    print("a는 짝수입니다.")
else:
    print("a는 홀수입니다.")

print("if~else 종료")


a = 33

if a % 2 == 0:
    print("a는 짝수입니다.")
else:
    print("a는 홀수입니다.")

print("if~else 종료")

# if 조건식1:
#    조건식1 참일때 수행 구문 블록    거짓이면 elif 1로 감
# elif 조건식2:
#    조건식2 참일때 수행 구문 블록    거짓이면 elif 2로 감
# elif 조건식3:
#    조건식3 참일때 수행 구문 블록    거짓이면 else로 감 
# else:
#    어떤 조건식도 거짓일때 수행 구문 블록

print("*" * 50)

# 음수, 0, 양수 구분

a = 0

if a > 0:
    print("a는 양수입니다.")       # 양수가 많이 나오면 a > 0을 제일 위에 놔둠  
elif a == 0:                      # 이렇게 해야지 횟수를 줄일 수 있음
    print("a는 0입니다.")
else:
    print("a는 음수입니다.")

print("if ~ elif 종료")


# 각 블록은 반드시 동일한 인덴트로 작성되어야 한다

# 조건식에는 비교연산자와 논리연산자 등을 잘 활용해야 한다
# 비교연산자 <, >, ==, !=, >=, <-
# 논리연산자 and, or, not


# 조건식에 사용가능한 비교연산자, 논리연산자
# 비교연산자 : >, >=, <, <=, !=(다르다), ==
# 논리연산자 : and, or, not, ^ (xor)
          # and : 둘다 '참'일 때 '참'
          # or  : 둘 중 하나만 '참'일 때 '참'
          # not : '참' -> '거짓', '거짓' -> '참'
          # nor : 같으면 '거짓', 다르면 '참' 
          
# 위 연산자들의 결과값은 항상 True / False

print("*" * 50)

d = 10
data = d > 2                         # True
data = d > 10                        # False
data = d <= 100                      # True
data = d <= 10                       # True
data = d == 100 / 10                 # True
data = d != 10                       # False

if data:
    print(data, "참입니다.")
else:
    print(data, "거짓입니다.")


data = True and True                 # Ture
data = True and False                # False
data = False or True                 # True
data = False or False                # False
data = not True                      # False
data = not not not not not True      # False
data = True ^ True                   # False
data = False ^ False                 # False
data = True ^ False                  # True

if data:
    print(data, "참입니다.")
else:
    print(data, "거짓입니다.")

# 논리 연산자와 비교 연산자의 활용
data = d % 2 == 0 and d % 3 == 0     # False
data = d % 2 == 0 or d % 3 == 0      # True
data = d % 2 == 0 ^ d % 3 == 0       # False  -> ^의 연산자가 우선순위임
data = (d % 2 == 0) ^ (d % 3 == 0)   # True
data = not d % 2 == 0                # False

if data:
    print(data, "참입니다.")
else:
    print(data, "거짓입니다.")

print("*" * 50)

# 주어진 숫자가 0 이상 100 이하의 범위인지? 


# 일반적인 언어에서 쓰는 조건문
score = 34
if 0 <= score and score <= 100 :
    print(score, "는 유효한 점수입니다.")
else:
    print(score, "는 유효한 점수가 아닙니다.")


#파이썬은 아래와 같이 범위값 표현 가능
if 0 <= score <= 100:
    print(score, "는 유효한 점수입니다.")
else:
    print(score, "는 유효한 점수가 아닙니다.")


#  in 연산자    -> list, tuple, dict, str에서 활용 -> 이는 T / F로 표시됨
#  in list, in typle, in dict, in set, in str ... ... 
animals = ["dog", "cat", "bird"]
new_animal = "Fish"

if new_animal in animals:
    print("이미 있습니다.")
else:
    print(new_animal, "을 추가합니다.")
    animals.append(new_animal)
    
print(animals)






































