# tuple : 튜플
# 콤마 , 로 구분된 집합 데이터 타입

#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.



animals = ("dog", "cat", "bird", "fish", "tiger")
print(animals)
print(type(animals))

animal  = "dog", "cat", "fish" 
print(type(animal))      # ()가 없어도 튜플! / 튜플의 본질은 ,에 있음

student = "김이박"
print(type(student))     # str
student = ("김이박")
print(type(student))     # str


# 원소 하나짜리 tuple을 만드려면? 
# 첫 원소 뒤에 콤마 하나 붙여주세요~~~~~~~~~~~~~~~
student = "김이박",
print(type(student))     # tuple
student = ("김이박",)
print(type(student))     # tuple

# index / slice / step 가능 ~~~~
print(animals[0:3], animals[4])
print(animals[::-1])

# in 연산자 가능
print("bird" in animals)
print("bird" not in animals)
print("whale" not in animals)


# tuple 은 immutable 하다!
# 원소 값 변경 불가!!!!!!!!!
                 # animals[0] = "puppy"      TypeError
                 # animals.append("puppy")   AttributeError

# + 연산자로 tuple에 추가(새로운 tuple 생성)
animals = animals + ("eagle", "bear")
print(animals)

animals = animals * 2
print(animals)


# tuple 은 언제 사용하나?
# 1. 주로 변경되지 말아야 할 데이터들
# 2. 복수의 값 '전달' 목적으로.       ex) a, b, c = 1, 2, 3 // a, b = b, a

# ex) 사각형 : [가로, 세로] 값

# 1. list의 경우
rec = [100, 200]
width = rec[0]
height = rec[1]
print(width, height)

# 2. tuple의 경우
rec = (100, 200)
width, height = rec             # 한번에 여러값 대입
print(width, height)

width, height = [200, 300]      # 왼쪽에 있는게 tuple이어야지 가능함!
print(width, height)





























