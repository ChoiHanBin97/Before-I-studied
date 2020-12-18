# 조건식의 참 / 거짓 판정 

# 조건문,  순환문 등에 사용되는  '조건식' 은 참, 거짓이 판정되어야 하는데
# 파이썬에서는 bool 타입 외에도 조건식에서 참, 거짓 판정이 된다.

#               │     참     │   거짓
# ───────────────────
# bool 타입 :      True      │    False
# 숫자 타입 :    0 아닌 숫자  │    0
# str  타입 :      "abc"     │   ""   빈문자열
# list 타입 :    [1, 2, 3]   │   []
# tuple 타입 :   (1, 2, 3)   │   ()
# dic 타입 : {"name":"john"} │   {}
# None 타입 :   무조건 거짓

data = 0.001                              # True
data = -100                               # True
data = 10 - 10                            # False
data = "python"                           # True
data = ""                                 # False
data = " "                                # True   -> 공백도 문자!
data = [1, 2, 3]                          # True
data = []                                 # False
data = ()                                 # False
data = (1, )                              # True   -> tuple이 되기 위해 , 넣어야함
data = {}                                 # False
data = {"a" : 200}                        # True
data = None                               # False

if data:
    print(type(data), data, "'참'입니다.")
else:
    print(type(data), data, "'거짓'입니다.")

print("*" * 50)


#논리 연산자 and, or 표현식과의 관계
#참, 거짓 판정에 이어 논리연산자의 결과는 
# expression 값
# short-circuit evalutaiton 혹은 
# lazy evalutation 이라 한다.

print("SCE: hort-circuit evalutaiton")



# or
# 왼쪽이 참인 경우 '왼쪽'값 리턴
# 왼쪽이 거짓인 경우 '오른쪽' 값 리턴

data = True or False          # True (왼쪽 값)
data = False or True          # True (오른쪽 값)

if data:
    print(type(data), data, "'참'입니다.")
else:
    print(type(data), data, "'거짓'입니다.")



# and 
# 왼쪽이 참인 경우 '오른쪽' 값 리턴
# 왼쪽이 거짓인 경우 '왼쪽' 값 리턴

data = True and False         # False(오른쪽 값)
data = False and True         # False (왼쪽 값)

data = 0 or 100               # 100(오른쪽 값)
data = "Hello" or "Python"    # "Hello"(왼쪽 값)
data = "Hello" and "Python"   # "Python"(오른쪽 값)
data = [] and "Python"        # []

if data:
    print(type(data), data, "'참'입니다.")
else:
    print(type(data), data, "'거짓'입니다.")




# 활용한 문장!
n = 10
(n % 5 == 0) and print(n, "은 5의 배수입니다.")
(n % 5 == 0) or print(n, "은 5의 배수가 아닙니다.")

n = 9
(n % 5 == 0) and print(n, "은 5의 배수입니다.")
(n % 5 == 0) or print(n, "은 5의 배수가 아닙니다.")


print("*" * 50)


# is : 타입 확인 
a = 10
print(type(a))

if type(a) is int:
    print("int 타입입니다.")
else:
    print("int 타입이 아닙니다.")


print("*" * 50)


# pass
# 아무일도 하지 않는 블럭

myList = ["a", "b", "c"]
if "a" in myList:
    pass                   # 아무 문장도 없는 블럭 만드려면 반드시 pass !!!!!!
else:
    print("없습니다.")





























