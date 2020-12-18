# self

class Foo:
    def __init__(self, name = "noname"):
        self.name = name
        
        
    def setName(self, name):
        print("이름변경:", self.name, "->", name)
        self.name = name


f1 = Foo()
f2 = Foo()

# id(객체)
# 인스턴스 고유 식별번호 ( 주소 )
print(id(f1), id(f2))
print(id(f1) == id(f2))         # 다른 인스턴스다!
print(type(f1) == type(f2))     # 같은 타입이다!

print(f1.name, f2.name)

f1.setName("John")
f2.setName("Susan")
print(f1.name, f2.name)


# -----------------------------------------------------------
# self

f1.setName("John")
#        실제로는 이렇게 호출된다!
Foo.setName(f1, "John")     # self 값에 f1를 전달~

# 아래의 두 코드는 동일한 동작
f2.setName("Susan")
Foo.setName(f2, "Susan")    # self 값에 f2를 전달~




































