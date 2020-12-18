# 주어진 datast 에서 제곱의 결과가 10보다 큰 결과만 담은 list 작성

dataset = [1, -2, 3, -4 ,5]
# => [16. 25]

result = [
        x ** 2
        for x in dataset
        if x**2 > 10
        ]

print(result)



# set comprehension
# {표현식 for ~ in [if ~]}
result = [ num % 3  for num in range(10)]
print(result)


result = { num % 3  for num in range(10)}
print(result)


# dict comprehension  -> set comprehension과 {}로 묶이는 것은 같으나 key와 value가 다름
# {key:value for ~ in [if ~]}


result = {
        n : n ** 2
        for n in range(5)
        }
print(result)


print()

result = {
        x : list(range(x))
        for x in [1, 2, 3, 4, 5]
        }

print(result)






