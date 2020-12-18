"""
100 이하의 자연수 n을 입력받고 
n개의 정수를 입력받아 평균을 출력하는 프로그램을 작성하시오.
(평균은 반올림하여 소수 둘째자리까지 출력하도록 한다.)


입력 예]
3
99 65 30

출력 예]
64.67

"""

# 내 답
# abc = map(int, input("100 이하의 자연수를 입력하시오.").split())
# i = len(abc)
# print(i, abc, sep="\n", "평균 : %.1f", (abc/i))


# 강사님 답

n = int(input())
cnt = 0
total = 0

for i in map(int, input().split()):
    if cnt == n: break
    total += i
    cnt += 1

print("{:.2f}", format(total / n))























