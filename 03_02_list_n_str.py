# list 와 str

# str.join()   :   list를 하나의 str로 만들어줌
animals = ["dog", "cat", "bird", "fish", "wolf"]
print(animals)
result = "-".join(animals)
print(result)    # list가 문자열이 되었기 때문에 len은 1

myList = ["2020", "04", "08"]
print("/".join(myList))

# str.split() : str   :   list로 쪼갬
myStr = "Hello python 2020"
result2 = myStr.split()    # str.split()은 매개변수 없이 쓰이면 공백단위로 쪼개어 list 생성
print(result2)

myStr = "20:16:40"
print(myStr.split(":"))    # split() 에서 ()사이에 있는 타입은 문자이기에 "" 필수!
print("-".join(myStr.split(":")))
print(myStr)

# 내 답
myStr = "2020-04-08 20:17:20"
a = myStr.split()
print(a)
a = "-".join(a)
print(a)
a = myStr.split("-")
print(a)
a = ":".join(a)
print(a)
a = a.split(":")
print(a)


# 강사님 답

print(myStr.split()[0].split('-') + myStr.split()[1].split(":"))

print(myStr.split()[0].split("-") + myStr.split()[1].split(":"))








































