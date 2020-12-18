# 10 + 2  # 피연산자(10, 2) 2개 필요 --> 이항연산자 (binary operator)
# -10 ,  not True  # 피연산자 1개 필요 --> 단항연산자 (unary operator)

# 피연산자 3개 필요 --> 삼항연산자 (ternary operator)
# ( 참일때의 값 ) if (조건식) else (거짓일때의 값)

n = 3
result = "짝수" if n % 2 == 0 else "홀수"
print(result)





# 퀴즈
# 삼항연산자 사용.
# 주어진 정가수 => 양수 / 음수 / 0인지 구분하는 코드 작성  ?????

n = 0
result = "양수" if n > 0 else ("음수" if n < 0 else 0)
print(result)



a = 1
result = "양수" if a > 0 else ("음수" if a < 0 else 0)
print(result)

# 두 수간의 차 (difference)

a = 72
b = 50
diff = (a - b) if a > b else (b - a)
print("diff:", diff)




































