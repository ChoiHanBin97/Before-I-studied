# 주석 : 한줄 주석(line comment)
# 프로그램의 실행과는 관계없이
# 코드에 메모등을 남길때 사용
# '#'으로 시작. 우측 끝까지 주석처리됨
# 모든 함수 값 출력은 F5 / 지정 열 출력은 F9 or Ctrl + Enter

# 숫자 (정수, 실수)
# 소숫점이 없으면 '정수' (int 타입)
# 소숫점이 있으면 '실수' (float 타입)

# tiobe -> 매주마다 프로그래밍 언어의 랭킹 순위 나옴
# 프로그래밍을 하고자 하면 java, c, python을 배워야함
# 자바는 20년 가까이 정점을 찍었었음
# c언어는 70년대에 나온 언어 but 많이 쓰임
# python은 java보다 먼저 쓰임 -> 2010년 이후 급부상
# - 번역기가 계속 돌아감 -> 속도가 느림(근데 빨리 만들수는 있음)
# but 하드웨어 성능 향상 + 딥러닝 등장과 인공지능 각광 / 배우기도 쉬움

print(10)
print(10.0)
print(10.) # 10.0
print(.1)  # 0.1

# 10과 10.0은 다름 
# 10.은 10.0으로 인식 -> 실수
# .1은 0.1로 인식

print(4 * 5)  # '정수'와 '정수' 연산 결과는 '정수'
print(4 * 5.0)  # '실수'와의 연산 결과는 어떤 결과든지 간에 '실수'
print(4 / 2) # 나눗셈 연산 결과는 언제나 '실수'!!
# // : 나눗셈 후 소숫점 이하 버리는 연산자 
print(4 // 2) # '정수'까리 하면 '정수'로 나옴
print(4 // 2.0) # '정수'와 '실수'와의 연산이면 '실수'가 나옴
print(3.4 / 1.1) # 실수
print(3.4 // 1.1) # 실수
                  # print(5 / 0)  -> zeroDivisionError(에러 이름) 
                  # division by zero (에러 메시지) ->>>>> 틀릴 때 이거 읽자!!!
print("과연 실행이 될까!? 두근두근...")

# % : 나머지 연산자  
print(13 % 3)
print(12.5 % 4.1)
     # 컴퓨터에서는 실수를 영원히 정확하게 표현하지 못함 -> 어느 선까지만 정확
     # 항상 오차가 존재함 
     
# ** : 제곱연산자   
print(2 ** 4)
print(-3 ** 3)
print(2 ** -1)
print(10 ** -2)
print(2 ** (1/2))
print(27 ** (1/3)) 

# """ : 블럭 주석
"""

이 안의 내용은 주석으로 처리됩니다.

"""    

# 문자열 타입 : str   (string)
# 문자열 만드는 방법
# 1. 쌍 따옴표
# 2. 홀 따옴표
# 3. 쌍 따옴표 3개
# 4. 홀 따옴표 3개


print("Python is fun")
print('Python is fun')
print("""Python is fun""")
print('''Python is fun''')

# She's gone 치고싶을 때 ''에서는 불가능 -> ""같은 걸로 활용
print("She's gone")
# He says "Hi!" 치고싶을 떄는 ""에서는 불가능 -> ''같은 걸로 활용
print('He says "Hi!"')
# He says "It's Okay!" 치고싶을 떄는 ''나 ""에서는 불가능 -> '''나 """ 활용
print('''He says "It's Okay"''') # 이때 """치고싶을 때는 앞뒤로 띄어쓰기하자



# + : 문자열 연산 
print("Hello" + "Python")  #문자열 '연결' 연산
print("Hello" + " " + "Anaconda")
                          # print( 12 + "monkeys")  TypeError 
                          # 문자와 숫자 연산 불가능
print( "12" + "monkeys")                          
# * : 문자열 연산                          
print('-' * 20)

# 문자열의 길이 Length (문자열 안의 문자개수)
# Len(문자열) 함수 or 명령어 
print(len("파이썬"))
print(len('hello python')) # 공백도 문자에 포함=> 12글자가 나옴                     
                         
# type() 함수
print(10, type(10))
print(10.0, type(10.0))
print("10.0", type("10.0")) # 화면에 찍힌 값이 같다고 같은 타입은 아님

# bool 타입
# True (참) 혹은 False(거짓) 값만 갖는 타입
print(True)
print(False)
print(type(True))  # 중요한 부분은 앞에 대문자!
                   # print(true)는 error
                   
# NoneType 타입
# 아무런 값도 없는 타입   -> 아무것도 존재하지 않는다는 것을 나타낼 때 사용                
print(type(None))                   







