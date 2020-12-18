# list의 원소는 '어떠한 타입'의 데이터도 가능!
myList = [100, 200, "John", 0.29, False, None]
print(myList)

# 리스트의 원소로 리스트를 가질 수 있다.
animals = [
        ["dog", "cat", "tiger", "bear", "wolf"],
        ["eagle", "pelican"],
        ["tuna", "shark", "salmon"]
        ]
print(animals)
print(len(animals))    # animals의 원소는 3개의 리스트이기에 3이 나옴
print(animals[0], type(animals[0]))
print(animals[0][2])   # animals 0번째 원소의 3번째!
print(animals[0][4])   # wolf
print(animals[2][0])   # tuna
print(animals[1][1])   # pelican

# list를 원소로 하는 list : 2차원 list라고 함
# [][] <-- index 2개 사용
# [] 쓰는 리스트 <-- 1차원 list
# [][][] 쓰는 리스트 <-- 3차원 list ......

myList = [[[10, 20, 30], 
         [40, 50, 60],
         ],
        [
        [100, 200, 300],
        [400, 500, 600]
        ]
        ,
        [
        [1000, 2000, 3000],
        [2000, 3000, 4000]
        ],
        ]
print(myList[2][1][2])    # 4000



# slicing : 데이터의 일부분을 잘라냄(:)
animals = ["dog", "cat", "bird", "tiger", "wolf"]
print(animals[0:3])  # 0부터 3 전까지의 list (3은 포함이 안됨)  #dog, cat, bird
print(animals[1:4])
print(animals[:2])   # [:2] 처음부터 2 전까지의 list
print(animals[2:])   # [2:] 2부터 끝까지의 list

# 문자열(str)도 index, slice 가능
myStr = "This is SPARTAAA!"
print(len(myStr))
print(myStr[2])         # i
print(myStr[8:14])      # SPARTA

# index vs slice
print(animals)                   #길이는 5
animals[2] = ["Shark", "Fish"]   #길이는 5(변함없음)   such as, extend
print(animals)
animals = ["dog", "cat", "bird", "tiger", "wolf"]
animals[2:3] = ["Shark", "Fish"] # slice 한 뒤에 추가 시키면 리스트의 원소가 들어감    such as, append
print(animals)                  
# 데이터 값으로 인덱스 찾기
# list.index(value)
 
print(animals.index("tiger"))     # tiger의 위치가 어디인지!
          #print(animals.index("turtle"))     # 없는 값은 에러
          # a = [1, 1, 2, 3, 4]
          # print(a.index(1))                 # 중복 값이 여러 개면 오류

# in 연산자 사용한 원소 존재 여부       # true / false로 나옴
print("tiger" in animals)             
print("turtle" in animals)


# pop()
# list 맨 뒤의 원소 추출, 리스트에서는 제거됨!  
a = animals.pop()      # 추출한 결과를 리턴함!
print(a)
print(animals)

# pop(n) : n번째 원소 추출
print(animals.pop(1))     # print 상에서 입력하더라도 추출됨
print(animals)

# list sort() : 데이터 정렬
animals.sort()                  # 오름차순으로 정렬
print(animals)
animals.sort(reverse = True)    # 내림차순 정렬
print(animals) 
animals.reverse()               # 역순 (뒤집기)

aaa = [1, 3, 12, 232, 12, 231, 3412341, 34123411242454]
aaa.reverse()
print(aaa)


# slice의 step 값  (::)
# [start:end:step]
print(aaa[1:6])   # step 값의 디폴트 값은 1
print(aaa[1:6:2]) # step은 두번씩 건너 뜀 R에서의 from, to, 'by' 개념
print(aaa[::3])
print(aaa[::-1])  # 파이썬에서 데이터를 뒤집는 가장 기본적인 방법   # 음수 step 값
print(myStr)
print(myStr[::-1])







