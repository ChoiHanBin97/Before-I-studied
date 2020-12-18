# dict
# value는 어떠한 타입이라도 가능 
# key :  hash 가능한 타입만 가능  (중복 key 값 불가)



a = []          # 빈 list
a = ()          # 빈 tuple
a = ""          # 빈 str
dict1 = {}      # 빈 dict

dict1 = {
        1 : "HAHA",
        "two" : {
                3.14 : "pi",
                "pi" : 3.14,
                "score" : [100, 200, 300]
                },
        False : [10, 20, 30, 40]
        # [1, 2] : "hello  TypeError         unhashable type
        }

print(dict1)                             # dict에서는 key를 입력해야하는 개념 
print(dict1["two"]["score"][1])          # 리스트에서는 순서를 입력해야하는 개념


# keys(), values()

student = {
        "name" : "김민호",
        "email" : "kim@mail.com",
        "age" : 23,
        "addr" : "서울"
        }

print(student.keys())
print(student.values())



"""
student = {
        "name" : "김민호",
        "email" : "kim@mail.com",
        "age" : 23,
        "addr" : "서울"
        "addr" : "경기도"    # 실행은 가능한데, 덮어쓰는 것임... 하지말자
        }
"""

student = {
        "name" : "김민호",
        "email" : "kim@mail.com",
        "age" : 23,
        "addr" : "서울",
        "home" : "서울"      # values 값은 중복 가능
        }


print(list(student.keys()))
print(list(student.values()))


# dict의 in 연산자 
# key의 존재 여부 확인


print("name" in student)
print("name" not in student)
print("email" in student)
print("서울" in student)        # 서울은 values



