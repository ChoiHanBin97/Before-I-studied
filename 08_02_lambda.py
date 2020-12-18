# 가령 다음과 같은 기능을 하는 함수들를 만드려고 한다

#      (입력)        (리턴)
# 1. [1, 2, 3] => [1, 4, 9]        <-- 제곱을 하는 함수

# 2. [-1, 2, -3] => [1, 2, 3]      <--  절대값을 구하는 함수


# 즉, 집합데이터형을 입력 받아서 '각 원소'들에게 '무언가 적용' 한 결과를 만드는 함수!!







data = [1, 2, 3]
# print(data**2)       # 불가능

def get_square_list(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

result = get_square_list(data)
print(result)



# 내 답
data = [1, -2, 3, -9]
def get_absolute_list(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
        else:
            result.append(-number)
    return result

print(get_absolute_list(data))

# 강사님 답

def get_absolute_list(numbers):
    result = []
    for number in numbers:
        result.append(number if number >= 0 else -number)
    return result

print(get_absolute_list(data))



# 함수도 데이터 타입이다!
print(type(get_absolute_list))

# 함수도 데이터처럼 주고 받을 수 있다.
a = get_absolute_list                 #지금부터 a는 함수
print(a([-4, -5, 10]))


# 함수를 매개변수 값으로 넘겨줄수도 있는 것이다.

def square(x):
    return x**2

def absolute(x):
    return (x if x>0 else -x)

def apply_func_to_list(numbers, func):   # 함수 func을 받아서
    result = []
    for number in numbers:
        result.append(func(number))      # func 호출
    return result


print(apply_func_to_list([3, 2, 7], square))
print(apply_func_to_list([-1, 2, -3], absolute))


#------------------------------------------------------
# 람다 표현식(Lambda expression)
# '이름이 없는' 함수 정의 

# lambda 표현식 구문
# lambda 매개변수: 표현식,  (값인 경우 리턴)


f = lambda x : x * 2

# 같은 구문
def func(x):
    return x * 2

print(func(20))
print(func(100))
print(func(5))


(lambda : print("hello"))()

print((lambda x, y : x + y)(10, 20))

print(apply_func_to_list([10, 20, 30, 40], lambda x : x / 2))
print(apply_func_to_list([10, 20, 30, 40], lambda x : x + 2))


