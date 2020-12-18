# 파이썬 함수는 여러 개의 값을 리턴할 수 있다!?!?

# 결론적으로 말하자면 함수의 리턴 값은 오직 '하나' 다
# 그런데 파이썬에선 여러개의 값도 리턴이 가능했다!  어떻게 가능?  tuple 로 리턴하면 가능하다.
# 기술적으로는 tuple 하나 만 리턴했지만, tuple 안에 값이 여러개 있기 때문에
# 여러개의 값을 리턴한것과 같은 효과를 보는것이다

def sum_and_mul(a, b):
    return a + b, a * b                  # 두개의 값을 담은 하나의 'tuple'을 리턴

result = sum_and_mul(3, 4)               # (7, 12)
print(result, type(result))
print(result[0], result[1])

s, m = sum_and_mul(3, 4)
print(s, m)


# 리턴 값을 tuple로 하는 기본함수(내장함수)도 많다.
result = divmod(10, 3)                            # 몫과 나머지 두개를 리턴
print(result)

quatient, remainder = divmod(10, 3)
print(quatient, remainder)



# 반지름을 입력받아
# 원의 둘레와 면적을 계산하여 리턴하는 함수를 작성하세요.
# 정의, 호출

import math
print(math.pi)     # 원주율 값   이 전에 import math해야함
print(math.e)


def calc_circle(radius):
    parameter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return parameter, area

a, b = calc_circle(10)
print(a, b)

























