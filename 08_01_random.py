# random 모듈   :  난수 생성
import random

print(random.random())                       # 0.0 <=  x  < 1.0 난수값 리턴

for i in range(10):
    print(random.random())

for i in range(10):
    print(random.randint(1, 10))             # 1 <= x <= 10 정수 난수값 리턴


print("*"*50)
# 주어진 리스트에서 데이터 랜덤으로 추출
data = [1, 2, 3, 4, 5]

def random_pop(d):
    i = random.randint(0, len(d) - 1)
    return d.pop(i)

while data:
    print(random_pop(data))

print()

data = [1, 2, 3, 4, 5]
for i in range(3):
    print(random_pop(data))



# 연습
# 로또 번호 추출
#  1 ~ 45까지의 숫자중 6개 랜덤 추출

data = [i + 1 for  i in range(45)]

print("로또번호")
for i in range(6):
    print(random_pop(data), end=" ")


print()
# random.shuffle()
data = [i + 1 for i in range(10)]
print("data=", data)

random.shuffle(data)
print("data=", data)


# random.choice()
print(random.choice(["dog", "cat", "bird"]))


