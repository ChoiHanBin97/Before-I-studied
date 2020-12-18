"""
연습: 단위 변환
1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
처음에는 야드를 입력받고, 두번째는 인치를 입력받아 
각각 cm로 변환하여 다음 형식에 맞추어 소수 둘째자리까지 출력하시오.​
예)
yard 입력: 23.45
inch 입력: 41.273
23.45 yard 는 2144.27cm
41.27 inch 는 104.83cm

"""

# 내 답
yd, inch = map(float, input("yard와 inch를 입력하세요:").split())
print(yd*91.44,"cm", inch*2.54, "cm")


# 강사님 답
yard = float(input("yard 입력: "))
inch = float(input("inch를 입력: "))
print("%.2f, yard 는 %.2fcm" % (yard, yard*91.44))
print("%.2f, inch 는 %.2fcm" % (inch, inch*2.54))