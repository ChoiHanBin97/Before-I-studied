# 함수 작성 연습

# 반지름을 입력받아
# 원의 둘레를 계산하여 리턴하는 함수를 작성하세요.



def calc_perimeter(radius):
    perimeter = 2 * radius * 3.141592
    return perimeter


# 호출
result = calc_perimeter(10)
print("둘레 =", result)    


# 반지름을 입력받아
# 원의 면적을 계산하여 리턴하는 함수를 작성하세요.

def calc_area(radius):
    area = 3.141592 * (radius ** 2)
    return area

result = calc_area(10)
print("면적 =", result)





# 직사각형의 가로, 세로의 크기를 입력받아
# 직사각형의 넓이를 구하는 함수를 작성하세요
# 정의, 호출


def area(x, y):
    a = x * y
    return a

result = area(15, 10)
print(area(10, 15))
print(result)




# 직각삼각형의 밑변과 높이가 주어졌을때
# 빗변의 길이를 구하는 함수를 작성하세요
# 정의, 호출


def area2(x, y):
    a = (x**2 + y**2)**(1/2)
    return a

print(area2(1, 2))
result = area2(4, 4)
print(result)


