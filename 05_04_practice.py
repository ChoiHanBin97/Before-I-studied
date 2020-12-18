# 자연수 n 값에 따라
# 다음과 같이 *을 출력하세요.

"""
n = 5

*
**
***
****
*****
"""

# 내 답
for i in range(1, 6):
    print("*" * i)


# 강사님 답
n = 5
for i in range(1, n + 1):
    print("*" * i)
    



# 자연수 n값에 따라 같이 출력하는 프로그램을 작성하시오.
"""
[예]
n = 3

[출력예]
*
**
***
**
*
"""
print("-" * 50)


# 내 답
n = 3
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)


# 강사님 답     => 나랑 동일함 ㅎㅎ
n = 5
for i in range(1, n + 1):
    print("*" * i)
    
for i in range(n - 1, 0, -1):
    print("*" * i)



