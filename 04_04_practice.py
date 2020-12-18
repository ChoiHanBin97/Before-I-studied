# 국어, 영어, 수학  3개의 점수(정수)로 입력받아서
# 총점 출력
# 평균 출력 (소숫점 1자리까지)
# 등급 출력
#   평균이
#     90이상이면 'A'
#     80이상이면 'B'
#     70이상이면 'C'
#     60이상이면 'D'
#     60미만이면 'F'

# if ~ elif ~ ..  ~ else  사용 


# 내 답

lan = 50
eng = 60
math = 89 

allscore = lan + eng + math
meanscore = allscore / 3
print(allscore)
print(meanscore)

if meanscore >= 90:
    print("A")
elif meanscore >= 80:
    print("B")
elif meanscore >= 70:
    print("C")
elif meanscore >= 60:
    print("D")
else:
    print("F")



# 강사님 답

kor, eng, math = map(int, input("국,영,수 입력: ").split())
total = kor + eng + math
avg = total/3
print("총점:", total)
print("평균: {:.1f}".format(avg))

print("등급:", end="")
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")









