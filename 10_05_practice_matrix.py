# 2차원 행렬 정의

"""
mt1 = Matrix2x2([10, 20], [30, 40])
mt2 = Matrix2x2([1, 2], [3, 4])

print(mt1) 실행 결과
    [10, 20]
    [30, 40] 

print(mt2) 실행 결과
    [1, 2]
    [3, 4]
    
print(mt1 + mt2) 실행결과
    [11, 22]
    [33, 44]
    
print(mt1 + mt2 + mt2 + mt2) 실행결과
    [13, 26]
    [39, 52]
"""


class Matrix2x2:
    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2
    
    def __str__(self):
        return str(self.row1) + "\n" + str(self.row2)
    
    def __add__(self, other):
        m = Matrix2x2([self.row1[0] + other.row1[0], self.row1[1] + other.row1[1]],
                      [self.row2[0] + other.row2[0], self.row2[1] + other.row2[1]])
        return m


mt1 = Matrix2x2([10, 20], [30, 40])
print(mt1)

mt2 = Matrix2x2([1, 2], [3, 4])
print(mt2)

print(mt1 + mt2)

print(mt1 + mt2 + mt2 + mt2)





























