"""
년도를 입력받아 윤년(leap year)인지 평년(common year)인지 판단하는 프로그램을 작성하시오.


400으로 나누어떨어지면 윤년이다. 
    또는 
4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다. 

나머지는 모두 평년이다.

"""

# 내 답
year = int(input("연도를 입력하세요:"))

a = "leap year" if year % 400 == 0 else ("leaf year" if year % 4 == 0 else ( "common year" if year % 100 == 0 else "leap year"))
print(a)

# 강사님 답
year = int(input("연도를 입력하세요"))

if year % 400 == 0:
    print("leaf year")
elif year % 4 == 0 and not year % 100 == 0:
    print("leaf year")
else:
    print("common year")













































