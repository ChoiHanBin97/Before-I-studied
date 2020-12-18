# 파일 다루기

# 파일을 다루기 위해선 open(), close() 함수 감싸여진다

# 파일객체 = open(파일 이름, 파일 열기 모드)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
# 파일객체.close()

# 파일 열기 모드
# r  읽기모드 - 파일을 읽기만 할 때 사용
# w  쓰기모드 - 파일에 내용을 쓸 때 사용.  해당 파일이 없으면 새로 생성.  ★ 해당 파일이 있었으면 삭제하고 새로 생성 ★
# a  추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용.  해당 파일이 없으면 새로 생성

f = open("새파일.txt", "w")
# 파일 작업....
f.close()



# 쓰기
# write()
f = open("새파일.txt", "w")          # 쓰기 모드

for i in range(1, 11):
    data = "line %d\n" %i
    f.write(data)                   # 파일에 쓰기

f.close()


# 읽기
# 한줄 읽기 readline()
f = open("새파일.txt", "r")         # 읽기 모드
line = f.readline()                # 1번째 줄 
print(line)
line = f.readline()                # 2번째 줄
print(line)

# f 는 파일의 어느 위치까지 읽기 / 쓰기 했는지를 기억하고 있다.

f.close()

# 모든 라인을 읽어오려면?

# 방법 1 : readline() 만으로도 가능
print()

f = open("새파일.txt", "r")
while True:
    line = f.readline()           # 더 이상 읽을 라인이 없는 경우 none 리턴
    if not line: break            # 다 읽었으면 while 종료  
    print(line, end = "")
f.close()

# 방법 2 : readlines()
print()

f = open("새파일.txt", "r")
lines = f.readlines()             # 각각의 line들을 담은 list를 리턴
for line in lines:
    print(line, end="")

f.close()

# 방법 3 : for 사용
print()
f = open("새파일.txt", "r")
for line in f:                    # 파일 객체 f 에서 한 라인씩 읽어들임
    print(line, end="")
f.close()

# 방법 4 : read() 사용
print()

f= open("새파일.txt", "r")
data = f.read()                   # 파일 전체를 읽어들임
print(data)
f.close()



# --------------------------------------------------------------
# 추가 (append)
f = open("새파일.txt", "a")       # 추가 모드
for i in range(11, 20):
    data = "%d Line appended\n" %i
    f.write(data)                # 기존 파일 내용의 끝에서부터 쓰기 시작

f.close()

print("append한 후 결과")
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()


# with 구문
# 자동으로 close 해준다.
with open("새파일.txt", "r") as f:    # 블럭이 끝나면 f를 자동으로 close 해준다.
    data = f.read()
    print(data)














