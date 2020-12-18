# set
# 만드는 방법
# 1.set()  함수로 만들수도 있고
# 2. {  } 으로 만들수도 있다.

#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다(index, slice 사용 x),  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.


animals = {"dog", "cat", "bird", "cat", "dog"}
print(animals)  # 중복 허용 x, 순서 x
print(type(animals))
print(len(animals))


                # print(animals[1]) TypeError, subscriptable : index 사용 x
 
# 형변환 함수
# int(), float(), str()  ...           
# list(), tuple(), set() ...
animals = ["dog", "dog", "cat", "bird", "cat"]
print(animals)





# 중복된 데이터를 제거하고 싶다면?
print(list(set(animals)))










































