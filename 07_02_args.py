# 가변 매개변수 *args
# 가변매개변수(various arguments) 함수 구문

# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

# 함수 호출시 전달된 복수개의 매개변수는 tuple 의 형태로 다루어진다
# args <-- arguments


def var_args(*args):
    print(type(args), ":", len(args), args)


var_args(10, 20, 30)
var_args()
var_args([10, 20], [30, 40], [50, 60])




def sum_many(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_many(10, 20, 30))
print(sum_many(10, 20, 30, 40, 50))
print(sum_many(0.1, 40.4, 3.14, -432,1))

#  print(sum_many("a", "b", "c"))                     # TypeError

# 가변매개변수는 다른 (고정) 매개변수와 혼합 사용가능
# 그러나! 가변  매개변수는 다른 매개변수 뒤에 정의하는 것을 추천

# def sum_mul(operator, *args)
# def sum_mul(a, b, *args, operator)                  # *args값 뒤로 판단 불가
# deg sum_mul(a, b, *args, *args)                     # 가변변수 두개 이상 불가


def sum_mul(operator, *args):
    result = None
    
    if operator == "sum":
        result = 0
        for i in args:
            result += i
            
    elif operator == "mul":
        result = 1
        for i in args:
            result = result * i
            
    return result

print(sum_mul("sum", 10, 25, 31, 52))
print(sum_mul("mul", 10, 25))
print(sum_mul(10, 225, 10, "mul"))                      # None



def sum_mul(*args, operator):
    print(args, operator)


# print(sum_mul(10, 20, 30, "sum"))                     # 불가
print(sum_mul(10, 20, 30, operator = "sum"))            # 가능 but 비추

#-------------------------------------------------------------------
# 키워드 매개변수  **kwargs
# kwargs : keyword argument 약자

# 함수호출시 함수의 인수로 key = value 형태로 주어지면
# 함수에선 kwargs 가 '딕셔너리' 형태로 받아옴


def func(**kwargs):
    print(type(kwargs), len(kwargs), kwargs)

func(name = "john")
func(name = "john", age = 32)
func()
func(a = 1, b = 2, c = 3, d = 4)


# *args, **kwargs 혼용 가능
def func(*args, **kwargs):
    print(len(args), args)
    print(len(kwargs), kwargs)
    
func(1, 2, 3, name = "pooh", age = 4)
# func(1, 2, 3, name = "pooh", age = 4, 5, 6)          # syntaxError


# 키워드 형태의 매개변수 뒤에 키워드 형태가 아닌 매개변수는 올 수 없다.

# def func(**kwargs, **args):                          # 불가능
#     print(len(args), args)
#     print(len(kwargs), kwargs)



