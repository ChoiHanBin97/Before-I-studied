# print()  기본출력(output) 함수

print(10)  # 10 출력 후 '줄바꿈'(하나의 문자취급) 까지 출력 so 20은 다음줄에서 출력됨
print(20)
print()    # 줄바꿈만 출력
print(10)


# 줄바꿈 없이 출력하는 방법
print(10, 20, 30)   # 한칸씩 떨어져있음
print(10, 20, 30, sep="")     #떨어져있는 것을 사이에 "" -> 즉 공백으로 둠


# end 옵션(parameter)
print('hello', end='')   # hello 다음에 줄바꿈 대신 end='a'에서의 'a'문자 출력
print('Mike')
print(2020, end = '-')
print(2, end = '-',)
print(14)
print(2020, 2, 14, sep = '-')

# 이스케이프 문자(escape character)

# '문자열' 내에서 특수한 문자 출력할때 사용
# \와 조합하여 출력

# 많이 사용되는 이스케이프 코드   -> 이게 문자열 안에서 ㅅ용
#    \n : 줄바꿈
#    \t : 탭
#    \\ : 역슬래시
#    \' : 홀따옴표
#    \" : 쌍따옴표

# He says "I'm fine"  을 출력하려면?
print("""He says "I'm fine" """)
print("He says \"I'm fine\" ")
print("Winter \nis coming")
print("Korea\\Japan")


#-------------------------------
# 문자열 포매팅 (formatting)

# 방법1 % 연산자 사용
# 서식문자(format specifier) 를 포함한 문자열과, 
# 각 '서식문자'에 대응하는 데이터들을 연결하여 문자열 완
# 구문)
#    "서식문자포함문자열" % ( 데이터 튜플 )


myStr = "hello %s, %s is Fun"
print(myStr %("파이썬", "Python"))

myStr = "hello %s, %s is Fun" %("파이썬", "Python")
print(myStr)


myFmt = "Hello %s, %s is Fun"
print(myFmt % ("Java", "자바"))
print(myFmt % ('kotlin', '코틀린'))


# format specifier
#  https://docs.python.org/2/library/string.html
# 우리는 아래 세가지만 기억하자~
# %d   십진수 정수
# %f   실수
# %s   문자열


name = '박수진'
age = 10
myStr = "제 이름은 %s 이고, 나이는 %d입니다." % (name, age)
print(myStr)

pi = 3.141592
print("원주율은", pi , "입니다.")
    #    print("원주율은" + pi + "입니다.") 은 에러뜸(문자열 + 숫자열)
print("원주율은" + str(pi) + "입니다.")
print("원주율은 %f 입니다." %(pi))
print("원주율은 %.1f 입니다." %(pi))  # 소숫점 한자리수까지
print("원주율은 %.2f 입니다." %(pi))  # 소숫점 두자리수까지
print("원주율은 %.3f 입니다." %(pi))  # 소숫점 세자리수까지(이는 반올림됨)


# %d : 자릿수 지정 가능
a, b, c, d = 10, 100, 1000, 10000
print('%d:%d:%d:%d' % (a, b, c, d))
print('%5d:%5d:%5d:%5d' % (a, b, c, d))          # %5d는 5칸에 거쳐서 우측정렬하여 출력해라
print('%-5d:%-5d:%-5d:%-5d' % (a, b, c, d))      # %-5d는 5칸에 거쳐서 좌측정렬하여 출력해라


#방법 2 : format() 함수 사용
myStr = "My name is {}, I'm {} yrs old".format("배트맨", 60)
print(myStr)

myStr = "My name is {}, I'm {} yrs old"
print(myStr.format("배트맨", 60))

myStr = "My name is {name}, I'm {age} yrs old".format(age = 60, name = "배트맨")
print(myStr)

# 방법 3 : f문자열(파이썬 3.6 이상    바깥쪽에 있는 문자 입력 가능
leng = "python"
author = "귀도 반 로썸"

myStr = f'언어:{leng}, 제작자:{author}'
print(myStr)
print(f'언어:{leng}, 제작자:{author}')












