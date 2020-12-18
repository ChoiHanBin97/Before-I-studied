# 파이썬 기본 입력 :  input()
# 키보드로부터 입력받아(우측 콘솔에서 입력함) 문자열(str) 결과 리턴

      # a = input()
      # print("입력하신 값은", a)

# 프롬프트(prompt) 출력
      #a = input("a 값을 입력하세요:")
      #print("입력하신 값은", a)

      # b = input("정수를입력하세요:")
      # print("b + 100 = ", b + 100)      # typeerror -> 문자열과 스트링
      
      # b = input("정수를입력하세요:")
      # print("b + 100 = ", "b + 100")  -> 입력해도 b로만 출력됨
      
      
#형 변환 함수 사용하면 된다.
      # b = int(input("정수를 입력하세요:")) 
      # print("b + 100", b + 100)     


# 키를 입력(cm) 받아서 (m)로 계산한 결과 출력해보세요 
#내 답
      # c = int(input("키를 입력하세요:"))
      # print("키는 : ", c/100, "M입니다.")

#강사님 답
      # height_cm = float(input("키를 입력하세요(cm)"))
      # print("키는", height_cm / 100, "M 입니다.")


# 여러개의 값을 한번에 입력받기
a, b, c = 10, 20, 30
      # a, b, c = input('3개의 정수를 입력하세요.')  # 문자열은 3가지로 입력 x
      # 방법 1: input().split()  : 공백으로 구분하여 여러문자열로 결과 리턴
      # a, b, c = input("정수 3개를 입력하세요.").split()
      # print('입력값은', a, b, c)
      # a = int(a)
      # b = int(b)
      # c = int(c)    -> a,b,c int값 나옴 
      
# 조금 더 쉽게 입력받은 값'들'을 int 값으로 변환하기
# 변수 1, 변수2, ... = map(int, input(). split())   ->  map(int, input...) input으로 받은 값에 모두 int를 적용해라
      # a, b, c = map(int, input('3개 정수 입력: ').split())
      # print("합계는", a + b + c)

# 20:37:32 <-- 이와 같이 입력받아서, 시, 분, 초로 쪼개기

      # hour, minute, second = input("시:분:초 입력").split(':')
      # print(hour,"시", minute, "분", second, "초")

































