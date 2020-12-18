# 파이썬 설치시 '기본적'으로 설치된 라이브러리로부터 사용 가능한 함수들
# 라이브러리(library) 란 파이썬 프로그래밍에 사용가능한 프로그램을을 모아놓은 것.
# https://docs.python.org/3/library/index.html    <-- Python Standard Library
# 파이썬에서는 위와 같은 라이브러리를 모듈(module)이라고도 한다.


# time 모듈
import time
print(time.time())   # timestamp 값.  1970. 01. 01 00:00:00 기준으로 경과한 시간(초)

# 현재시간 연도, 월, 일, 시, 분, 초, 요일의 형태로 변환
print(time.localtime())                              # 현재 시각

# 특정 타임스탬프의 값을 매개변수로 받을수도 있다.
print(time.localtime(1))

print(time.localtime(time.time()))                   # 현재 시각

t = time.localtime()

print(t.tm_mon)                                      # 월
print(t.tm_year)                                     # 연도


# timestamp -> str로 바꾸기
result = time.strftime("%x", t);
print(result)

result = time.strftime("%c", t);
print(result)

result = time.strftime("%Y-%m-%d %H:%M:%S", t);
print(result)


# -----------------------------------
# 일정시간 delay -> sleep() 함수

# 경과시간 측정 (elapsed time)

start_time = time.time()                              # 시작 시간 

for i in range(5):
    print(i)
    time.sleep(2)                                     # 단위 sec

end_time = time.time()                                # 종료 시간

elapsed_time = end_time - start_time                  # 경과 시간
print("---- %s seconds ---" % (elapsed_time))





