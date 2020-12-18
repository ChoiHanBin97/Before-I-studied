"""
1부터 전달받은 수까지의 합을 출력하는 함수를 작성하고 
1000 이하의 자연수를 입력받아 작성한 함수로 전달하여 출력하는 프로그램을 작성하시오. 
(함수를 작성하세요)
입력예]
100

출력예]
5050
"""

def abc1(*args):
    sum = 0
    for i in args:
        sum += i + 1
    return sum

print(abc1(2))



"""
n개의 정수를 입력받아 각 정수의 절대값의 합을 출력하는 프로그램을 작성하시오. 
(함수를 작성하세요)

입력예]
35 -20 10 0 55

출력예]
120
"""

def abc2(*args):
    sum = 0
    for i in args:
        if (i>0):
            sum += i
        elif (i<0):
            sum += -i
    return sum

print(abc2(1, 2, 3, 4, -4100))






"""
자연수를 입력받아 아래와 같은 사각형을 화면에 출력하는 프로그램을 작성하시오. 
주어지는 수는 100이하의 자연수이다.
(함수를 작성하시오.) 

입력예]
3

출력예]
1 2 3
2 4 6
3 6 9

"""

"""
def abc3(a):
    squared = a ** 2
    j = 1
    for i in range(squared):
        if (j<a)
            print(i, end = "")
            j += 1
        elif (j = a):
            print(end = "/n")
            print(i, end = "")
            j = 1
    print()
"""

# 강사님 답

def draw_cub(n):
    for i in range(1, n + 1):
        for j in range(n):
            print(i + j * i, end =" ")
        print()

draw_cub(3)
draw_cub(5)









