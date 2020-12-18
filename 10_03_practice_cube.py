# 상속 연습 

# 정사각형(Square)
#   └─ 정육면체 (Cube)

# '정사각형' 객체 정의 
#  클래스 이름 : Square
#  생성자 : '한 면의 길이(side)'를 받아서 초기화
#  면적을 계산하여 리턴하는 메소드 : getArea()

# '정육면체' 객체 정의 <-- Square 상속받아 정의
#  클래스 이름 : Cube
#  getArea() : 정육면체의 총 면적
#  getVolume() : 정육면체의 부피 게산


# 내 답

class Square:
    def __init__(self, side):
        self.side = side
        
    def getArea(self):
        return self.side ** 2
    
s1 = Square(5)

print(s1.getArea())

class Cube(Square):
    
    def getArea(self):
        return self.side ** 2 * 6
    
    def getVolume(self):
        return self.side ** 3
    
c1 = Cube(5)
print(c1.getArea(), c1.getVolume())


# 선생님 답

class Square:
    def __init__(self, side = 0):
        self.side = side
        
    def getArea(self):
        return self.side ** 2
    
# 정육면체
class Cube(Square):
    
    # 오버라이딩!
    def getArea(self):
        return self.side ** 2 * 6
    
    # 추가되는 메소드, 부피
    def getVolume(self):
        return self.side ** 3
    
c1 = Cube(2)
print("면적 :",c1.getArea(), "부피 :", c1.getVolume())


print("한 면의 면적 :", Square.getArea(c1))
print("한 면의 면적 :", super(Cube, c1).getArea())


























































