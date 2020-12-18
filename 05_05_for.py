# for 와 tuple

a = [(1, 2), (3, 4), (5, 6)]
print(len(a))


for x in a:
    print(x)
    
print()

for x in a:
    print(x[0], x[1])


print()

for x in a:
    print(x[0], x[1], sep = "", end ="")

print("\n")

# 파이썬스러운(pythonic) 한 방법
for x, y in a:
    print(x, y)



# 예제 연습
# 학생들의 점수가 아래와 같이 주어졌다고 하자
# 총점과 평균을 출력해보세요
# 예시)
# 학생수: 5 명
# 총점: 327 점
# 평균: 65.4 점

total = 0
avg = 0.0
scores = [88, 34, 98, 74, 33]  


# 내 답
for x in scores:
    total += x
avg = total/5
print("총점:", total, "평균", avg)


# 강사님 답

for score in scores:
    total = total + score
    
print("학생수 : ", len(scores), "명")
print("총점 :", total, "점")
print("평균 : ", total / len(scores), "명")




print("-" * 50)

# for 와 dict

student = {
        "name" : "홍반장",
        "email" : "hong@gmail.com",
        "address" : "역삼역"
            }

for key in student:
    print(key, ":", student[key])

print()

# dict.items() : (k, v) 쌍을 tuple로 iterate 한다.

# ('name', '홍반장') 
# ('email', 'hong@gmail.com') 
# ('address', '역삼역')

for val in student.items():
    print(val, type(val))


for key, val in student.items():
    print(key, ":", val)




