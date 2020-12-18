# 디폴트 매개변수 (Default Arguments)

# 함수정의시 매개변수에 디폴트 값을 지정해 주면,  호출시 생략가능하다
# 생략된 상태에서 호출되면 디폴트 값으로 작동된다

# 디폴트 매개변수 작성 구문
#    def 함수명(매개변수명=디폴트값)


def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다," % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        print()


say_myself("홍길동", 43, True)
say_myself("홍길동", 43)
say_myself("임향미", 13, False)



print(10, 20, 30)
print(10, 20, 30, sep = ":")
print(2020, 4, 20, sep = "/")

# 디폴트 매개변수 주의 사항들
# 함수 정의시, 디폴트 매개변수 뒤에는 디폴트 매개변수가 아닌 것은 정의할 수 없다.

"""
def say_myself(name, man = True, old):
    print("나의 이름은 %s 입니다," % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        print()

say_myself("박응용", 27)
"""










































