# break
# 순환문 (while, for) 안 에서 순환문을 강제로 종료시키는 키워드
# break 는 감싸고 있는 가장 가까운 순환문을 종료합니다

# continue
# 다시 순환문 처음으로 돌아가기


n = 1
while True:            # 원래는 무한 루프
    print(n)
    
    if n == 100:
        break;         # 순환문 종료! 
    n += 1

print("while 종료!")


n = 1
while True:            # 원래는 무한 루프
    if n == 100:
        break;         # 순환문 종료! 
    print(n)

    n += 1

print("while 종료!")



print("*" * 50)

num = 0
while num <= 10:
    num += 1
    
    if num % 2 == 1: continue    # 순환문 처음으로 돌아감
    
    print(num)

print("while 종료!")


# 정수를 계속해서 입력받다가, 0 이 입력되면
# 그때까지의 정수의 '합' 과 '평균' 을 출력 

"""
[예]
10
20
30
0

합 : 60
평균 : 20.0

"""

# 내 답

n = 0
a = 0
i = 0
while True:
    n = int(input("정수를 입력하세요."))
    if n == 0: break
    a += n
    i += 1
print("합 :", a)
print("평균 :", a/i)


# 강사님 답

total = 0
cnt = 0
while True:
    n = int(input())
    if n == 0: break
    total += n
    cnt += 1
print("합:", total)
print("평균: %.1f"%(total / cnt))

















































