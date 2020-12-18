# 파이썬의 내장함수 (Built-in Functions)
# 별도의 import 없이 바로 사용가능한 함수들    

# 레퍼런스 :  https://docs.python.org/3/library/functions.html
        
# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()	 
# delattr()	hash()	memoryview()	set()	 



print("hello")
print(type(print))

# print = 10
# print(123123)     # 동작안함


# 실수로 내장함수를 덮어쓰기 한 경우 복원하려면
# print = __builtins__.print 를 콘솔창에서 치자.
print(123)


sum = 10 + 20

sum = __builtins__.sum

sum([1, 2])








