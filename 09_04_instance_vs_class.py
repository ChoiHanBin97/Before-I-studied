# 클래스 메소드 vs 인스턴스 메소드
# 클래스 변수 vs 인스턴스 변수 


#-------------------------------------------
print("** 클래스 메소드 vs 인스턴스 메소드 **")

# 클래스 메소드 (class method)
# self 가 안붙은 메소드, '클래스 이름' 으로 사용

# 인스턴스 메소드 (instance method)        
# self 가 붙은 메소드 ,  '인스턴스 생성' 하여 사용 


class Foo:
    #클래스 메소드
    def func1():      # self 없다!
        print("function1")


    # 인스턴스 메소드
    def func2(self):  # self 있다!
        print("function2")



f1 = Foo()            # f1은 Foo 인스턴스
# f1.fuc1()           # ->> Foo.func1(f1)  Error
f1.func2()

Foo.func1()           # 클래스 메소드는 클래스 이름으로 호출
                      # 인스턴스 없어도 사용 가능!!  


print('*' * 30)
print("** 클래스 변수 vs 인스턴스 변수 **")
# self.변수이름  : <-- 인스턴스 변수
#       인스턴스 변수는 '인스턴스 마다' 생성       
# 클래스 내부에서 선언된변수 <-- 클래스 변수  (self 가 안 붙음)
#        사용하려면 클래스이름.변수이름  으로 사용해야 함
#        클래스 변수는 '클래스에 딱 하나' 생성


# 계좌 객체 정의
class Account:
    
    
    rate = 0.02              # 클래스 변수
    num_accounts = 0         # 클래스 변수
    
    def __init__(self, name):
        print("Account({}) 생성".format(name))
        self.name = name     # self.name 은 인스턴스 변수
        Account.num_accounts += 1
        
    # 소멸자 (Destructor)  클래스 인스턴스가 소멸될때 자동 호출
    def __del__(self):
        print("Account({}) 삭제".format(self.name))
        Account.num_accounts -= 1

print("Account.num_accounts =", Account.num_accounts)

acc1 = Account("회사")
acc2 = Account("홍길동")
acc3 = Account("아이언맨")


print(acc1.name, "의 이율 =", acc1.rate)
print(acc3.name, "의 이율 =", acc2.rate)
print(acc2.name, "의 이율 =", acc3.rate)

print("Account.num_accounts =", Account.num_accounts)


# 인스턴스 삭제는??
del(acc1)       # 삭제됨!
# print(id(acc1))            # Error

print("Account.num_accounts =", Account.num_accounts)

print(acc2.num_accounts)   # 클래스 변수는 인스턴스 변수로도 접근 가능
                           # 클래스변수는 모든 인스턴스가 공유한다.

del(acc2)
del(acc3)


























