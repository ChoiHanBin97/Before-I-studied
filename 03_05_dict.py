# dict : 딕셔너리

# dictionary 데이터 타입은  key-value 쌍으로 저장되는 데이터 집합이다.
#  내 생각 : key는 factor로 생각하자. but 1대 1 대응

# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# "이름" = "홍길동", "생일" = "몇 월 몇 일"   과 같은 자료형 담음

# 기존의 list, tuple 등은 value 중심
# 그러나 이 또한 알고 보면 key-value 쌍으로 구성

# 순서는 고정이 안된다

student = {}
print(type(student))    # {}의 기본은 dict임

student = {
           "name" : "최현진",       # key1:value1 와 key2:value2 사이에는 ,넣자!
           "e-mail" : "choi@mail.com"
}
print(student)

# value (값) 사용
print(student["name"])        # 방법 1
print(student.get("name"))    # 방법 2  :  get(key)

# 차이점 -> 존재하지 않는 key의 경우
            # print(student["age"]          KeyError
            # print(student.get("age"))     None
            
# get()을 사용하면 예외적인 상황에서도
# 동작 가능하게 처리가능            
 
print(student.get("age", 20))         # "age" 키가 없으면 20을 리턴





# 수정하기
student["name"] = "이민규"
print(student)

# 추가하기
student["address"] = "역삼동"
print(student)

# 삭제하기
del(student["e-mail"])
print(student)


