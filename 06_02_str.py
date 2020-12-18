# 문자열 함수들

# 대표적으로 문자열(str)은 많은 함수(메소드)들을 갖고 있습니다.
# str 의 대표적인 함수들  ==>  split, join, replace, format

# https://docs.python.org/3/library/stdtypes.html#textseq
# str에 대해서 뭐가 있는지 확인해보자~

# upper(), lower() : 대소문자 변환
str1 = "Apple"
print(str1, str1.upper(), str1.lower())


# str.join(), str.split()      -> 03_02 참조
# join - 리스트에서 스트링 / split - 스트링을 리스트로 쪼갬


#----------------------------
# CSV -> TSV 변환하기 
# CSV : Comma Separated Value
# TSV : TAB Separated Value


data = '사과, 바나나, 파인애플, 포도, 복숭아'
print(data.split(','))
print('\t'.join(data.split(',')))



# replace() : 문자열 치환
data = "데이터 분석을 위한 파이썬 프로그래밍"
# "파이썬" => "Python"으로 바꾸기(치환)
print(data)
print(data.replace("파이썬", "Python"))
# 문자열 원본은 변화되지 않는다!
print("replace() 후 data=", data)
a = data.replace("파이썬", "안녕")
print(a)


print("*" * 50)

# index(), find()
# 문자열 안에서 문자열 찾기
print("th" in "python")    # 있느냐 없느냐를 찾는 것 <-> 어디서 찾은 건지도 나옴


data = "hello python"
# index(): 문자열을 발견한 위치(index)를 리턴
print(data.index("lo"))     # 3 -> 문자열 첫번째는 0 
# print(data.index("x"))    # ValueError -> 없는 문자열의 경우 에러


# find()
print(data.find("lo"))      # 3   -> index와 같음
print(data.find("x"))       # -1  -> 없는 문자열의 경우 -1 


# count()
# 문자열 내에서 특정 문자열 패턴의 반복 횟수
data = "aabbabaababaababbaaaaaababbaabababaabaa"
print(data.count("a"))
print(data.count("ba"))


# startswith(); endswith()
# 문자열이 특정 문자열로 시작/종료 하는지 여부
url = "www.naver.com"
print(url.startswith("http://"))

if not url.startswith("http://"):
    url = "http://" + url
    
print(url)
print(url.endswith("com"))

print()


# ord() : 문자의 코드값(정수)
# chr() : 코드의 문자값
# 문자의 코드 값은 사전순 배치

print("a", ord("a"))
print("b", ord("b"))
print(chr(97), chr(98))
print(ord("각"), ord("간"))
print(chr(44034), chr(44035))
print(ord("ㄱ"))


# 문자열에 대해 비교연산자 작동함
# 사전순(코드순) 비교

print("a" < "b")              # True
print("cable" < "bible")      # False
print("가마우지" < "까마귀")   # True
print("까마우지" < "까마귀")   # False


print("aAaA" < "AaAa")        # False
# 대문자가 소문자보다 코드 값이 먼저 등장 ( 더 작다.)
print(ord("a"), ord("A" ))    # 97, 65

data = [
        "aAaA", #1
        "aaAA", #2
        "AAaa", #3
        "AaAa"  #4
        ]

print(sorted(data))           # t사전순 정렬


# 알파벳 개수
print("알파벳 개수", ord("z") - ord("a") + 1)
print("한글 개수", ord("힣") -  ord("가") + 1)


# 연습
# 알파벳 소문자로 이루어진 리스트 작성
# List Comprehension 사용
# ['a', 'b', ... 'z']

result = [
        chr(ch_code)
        for ch_code in range(ord("가"), ord("힣") + 1)
        ]

print(result)


result = [
        chr(x)
        for x in range(ord("a"), ord("z") + 1)
        ]


print(result)

