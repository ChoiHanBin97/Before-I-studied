"""
연습: 
# 키(cm) 와 몸무게(kg) 를 입력받아 bmi 를 계산하여 출력
# bmi = 몸무게(kg) /  (키(m) x 키(m))   -> 환산해야함
# bmi는 소숫점 한자리까지 출력

예]
키(cm) 와 몸무게(kg) 를 입력하세요183 93
BMI 는 27.8 입니다

"""
# 내 답
height_cm, weight = map(float, input("키와 몸무게를 입력하세요.").split())
height_m = height_cm / 100
bmi = weight / (height_m * height_m )
print(type(bmi))
print("BMI는 %.1f 입니다." %(bmi))


# 강사님 답

height, weight = map(float, input("키(cm)와 몸무게(kg)을 입력하세요").split())
height /= 100
bmi = weight / (height ** 2)
print("BMI는 {:.1f} 입니다.".format(bmi))  # {:.1f} -> format안에 있는 값을
                                          # 소숫점 한자리수까지 나오도록 함