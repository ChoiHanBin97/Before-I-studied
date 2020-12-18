# 파일의 단어 빈도수 구하기

# 오로지 알파벳만. 검증하기
# 대소문자 구문없이 비교
# 단어수 2개 이상인 단어만 카운트 하기
# 빈도수 2회 이상인 단어만 카운트
"""
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""




with open("data/alice30.txt", "r") as f:
    data = f.read()
    data = data.lower()                      # 전부 다 소문자로 변환

print(data)



alpha = [chr(ch_code)
        for ch_code in range(ord("a"), ord("z") + 1)]

print(alpha)

# 알파벳이 아니면 공백으로 치환
for ch in data:
    if  ch not in alpha:
        data = data.replace(ch, " ")

print(data)

# 두 글자 이상인 단어만!
words = [
        word
        for word in data.split()
        if len(word) > 1 
        ]


# print(words)


# 등장빈도 개수
result = {}

for word in words:
    if result.get(word):
        result[word] += 1
    else:
        result[word] = 1
        
# print(result)

# 한번 등장한 건 제외, 2번 이상 등장한 단어만 추려내기
result2 = {
        word : result[word]
        for word in result
            if result[word] >= 100
        }

print(result)


# 빈도수 정렬, 내림차순 정렬까지 한다면

result2_sorted_key = sorted(result2, key=result.get, reverse=True)


for r in result2_sorted_key:
    print(r, result2[r])


print("*" * 50)

# 정규표현식 + split 사용하면 단어 쉽게 분리 가능

import re

print(re.findall("[a-z]+", data))




