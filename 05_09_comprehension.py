# list comprehension
# set comprehension
# dict comprehension
# ...


# List Comprehension 구문
# ->> list (아래와 같이) 생성 
# [표현식 for 항목 in 반복가능객체 (if 조건)]

# 주어진 리스트의 원소 데이터를 각각 * 3 적용한
# 새로운 리스트를 작성하기 

# [1, 2, 3, 4,] -> [3, 6, 9, 12]

a = [1, 2, 3, 4]

print(a * 3)                                # 리스트가 3번 나옴

result = []
for num in a:
    result.append(num * 3)

print(result)


result = [num * 3  for num in a]           # 굉장히 많이 쓰이는 구문
print(result)

# 0 으로만 20개 채워진 list 작성
print()
result = [ 0  for i in range(20)]
print(result)



#  [1, 2, 3, 4]
# 짝수에만 3을 곱하여 담은 새로운 리스트 생성
#    ↓    ↓
#    [6, 12]

print()
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)
print(result)
        

print()

result = [ num * 3  for num in a if num % 2 == 0 ]
# 순환문이 먼저 해석 -> 조건식을 확인 -> 참이면 num*3에 넣음
print(result)


print()

result = [
          num * 3
          for num in a
          if num % 2 == 0
          ]

print(result)



# ["1월, "2월", .... , "12월"]
# list comprehension 만들기

result = [
         str(i + 1) + "월"
         for i in range(12)
         ]
print(result)


# for문 2개 이상 사용도 가능

# [표현식 for 항목1 in 반복가능객체1 if 조건1
#         for 항목2 in 반복가능객체2 if 조건2
#         ...
#         for 항목n in 반복가능객체n if 조건n]


result = [
        dan
        for dan in range(2, 10)
        ]

print(result)

result = [
        mul
        for mul in range(1, 10)
        ]

print(result)


result = [
        "%d * %d = %d" % (dan, mul, dan * mul)
        for dan in range(2, 10)
        for mul in range(1, 10)
        ]

print(result)

result = [
        "%d * %d = %d" % (dan, mul, dan * mul)
        for dan in range(2, 10)
        if dan % 2 == 0
        for mul in range(1, 10)
        ]

print(result)


result = [
        "%d * %d = %d" % (dan, mul, dan * mul)
        for dan in range(2, 10)
        if dan % 2 == 1
        for mul in range(1, 10)
        ]

print(result)

