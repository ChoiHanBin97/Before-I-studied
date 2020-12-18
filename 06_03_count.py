# 주어진 문자열을 알파벳별로 출현빈도 구하려면?

# 대소문자 구분없이 소문자로만

# 입력예
# "Gorilla"
# ↓
# {
#     "g": 1,
#     "o": 1,
#     "i": 1,
#     "l": 2,
#     "a": 1,
#     "r": 1
# }




data = "Alice in Wonderland"
data = data.lower()                  # 소문자로 변경

result = {}
for ch in data:
    if "a" <= ch <= "z":             # 알파벳인 경우만 계수
        if not result.get(ch):       # 첫 등장이면 1
            result[ch] = 1
        else:                        # 이전에 이미 등장했으면 + 1
            result[ch] += 1

print(result)

print("-" * 50)
# dict comprehension
result = {       
        ch : data.lower().count(ch)        
        for ch in 
            [chr(ch_code) for ch_code in range(ord("a"), ord("z") + 1)]
        if ch in data.lower()
        }




print(result)



data = "간장공장공장장"

result = {       
        ch : data.lower().count(ch)        
        for ch in 
            [chr(ch_code) for ch_code in range(ord("가"), ord("힣") + 1)]
        if ch in data.lower()
        }

print(result)

data = "Alice in Wonderland"

result = {
        a : data.lower().count(a)
        for a in
        [ chr(a)  for a in range(ord("a") - ord("z") + 1)]
        if a in data.lower()
        }

print(result)





























