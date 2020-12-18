# 여러개의 데이터를 담는 집합 데이터 타입들..
#1. list   :  순서있다.(입력한 순서 외움)  중복허용(같은 데이터 입력 가능),  mutable(리스트 안에 있는 값을 변화가능)
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

"""
list

# list 는   [   ]  으로 만든다
# 데이터(원소) 들은 , 콤마로 구분한다
# 각 데이터(원소) 들은 어떠한 타입도 가능하다
"""

animals = ["dog", 'dog', 'cat', 'bird']
print(animals)
print(type(animals))
animals = ["dog",
           'dog',
           'cat',
           'bird']

# 인덱싱(indexing) : [순서] -> 리스트에서 첫번째는 0, 두번째는 1 ....
print(animals[0])       # 0 부터 시작! 첫번째 원소
print(animals[3])
       # print(animals[4]) Inderxerror   :   리스트의 인덱스의 범위를 벗어남 

# 음수 인텍싱 가능
print(animals[-1])      # 거꾸로 감 -> 이건 -1번부터 인식
       # print(animals[-5]) Inderxerror

# len() 함수 : 리스트 안의 데이터 원소의 개수
print(len(animals))     # len(list)  :  리스트 원소의 개수
print(len("Hello"))     # len(str)   :  문자열 안의 문자 개수


# append()  :  데이터 (원소) 추가  뒤에
animals.append("tiger")
print(animals)


# del()  :  데이터 원소 삭제 
del(animals[1])         # 두번째꺼 삭제
print(animals) 


# 데이터 원소 변경
# 리스트는 값을 변경할 수 있다. : mutable
animals[1] = "냥아치"
print(animals)


#리스트 연산 : +, *
colors = []
print(len(colors))
colors.append("white")
colors.append("blue")
colors.append("red")
print(colors)

# list + list => list

print(animals + colors)
print(colors * 2)


# list.extend()
animals.extend(colors)    
print(animals)
# ['dog', '냥아치', 'bird', 'tiger', 'white', 'blue', 'red']
        # 리스트의 원소가 추가됨

animals.append(colors)
print(animals)
# ['dog', '냥아치', 'bird', 'tiger', ['white', 'blue', 'red']]
        # 리스트 하나 자체가 추가가 됨

print(colors)
colors.append("orange")
colors.extend(["orange"])    # append와 결과는 같으나 속도는 더 빠름
print(colors)


# list의 원소 타입은 어떠한 타입도 가능하다. (list의 원소가 list 타입일수도 있음)



