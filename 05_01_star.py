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

n = 5
i = 1
while i <= n:
    print("*" * i)
    i += 1


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
i = 1
while i <= n:
    print("*" * i)
    i += 1
i = n - 1
while i >= 1:
    print("*" * i)
    i -= 1

# 강사님 답

n = 3
i = 1
while i <= n:
    print("*" * i)
    i += 1
    
i = n - 1
while i >= 1:
    print("*" * i)
    i -= 1




