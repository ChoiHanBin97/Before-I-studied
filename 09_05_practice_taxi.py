# taxi 클래스 설계

# '택시'에는 승객들에게 공통적으로 적용되는 값
# - 택시 요율 (거리당 요금) : 700(거리 1km당 요금)
# - 기본 요금 : 3000
# - 최초 기본 주행 거리 : 2km

# 택시 객체 생성시 승객별로 '돈'과, '거리'를 받아서 생성 
#  ---> 생성자 매개변수로

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

# 내 답

class Taxi:
    
    rate = 700
    fixed = 3000
    first_distance = 2
    
    def __init__(self, money = 0, distance = 0):
        self.money = money
        self.distance = distance
        
    def calc_cost(self):
        if self.distance > 2:
            cost = Taxi.fixed + (self.distance - 2) * Taxi.rate
        else:
            cost = Taxi.fixed
        return cost
        
        
    def get_change(self):
        if self.distance > 2:
            cost = Taxi.fixed + (self.distance - 2) * Taxi.rate
        else:
            cost = Taxi.fixed
        change = self.money - cost
        return change
        

passenger1 = Taxi(20000, 1)
print("비용은",passenger1.calc_cost(), "원 입니다,", "잔돈은", passenger1.get_change(), "원 입니다,")
passenger2 = Taxi(30000, 10)
print("비용은", passenger2.calc_cost(),"원 입니다.", "잔돈은", passenger2.get_change(), "원 입니다,")



# 선생님 답

class Taxi2:
    
    fare_rate = 700
    init_fare = 3000
    free_dist = 2
    
    def __init__(self, money, distance):
        self.money = money
        self.distance = distance
        
        
    def calc_cost(self):
        cost = Taxi2.init_fare
        if self.distance >= Taxi.free_dist:
            cost += (self.distance - Taxi2.free_dist) * Taxi2.fare_rate
        return cost
    
    def get_change(self):
        change = self.money - self.calc_cost()
        return change


passenger1 = Taxi2(20000, 1)
print("비용은",passenger1.calc_cost(), "원 입니다,", "잔돈은", passenger1.get_change(), "원 입니다,")
passenger2 = Taxi2(30000, 10)
print("비용은", passenger2.calc_cost(),"원 입니다.", "잔돈은", passenger2.get_change(), "원 입니다,")




























