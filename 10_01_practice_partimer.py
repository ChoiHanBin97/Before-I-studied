# '매 직원(PartTimer)'에 공통적으로 적용되는 자료    (클래스 변수)
# - 시급 8500
# - 전체 직원수

# 각 직원별 객체 생성시 직원별로 '별칭'과 '근무지' '급여총액' 초기화 (속성, 인스턴스 변수)
#   '근무지' 생략시 '113동' 으로 지정
#   직원별로 '급여총액'  0으로 초기화

# 직원의 급여 계산하기(동작)
#    '몇시간 근무',  '+상여금'  에 따른 직원급여 계산
#   '상여금' 은 지정안하면 0 으로 처리


# 예]
# park = PartTimer('라이언')   // park 은 ‘라이언’ 이라는 닉네임의 직원으로 등록

# park 이 4시간 일한 급여 총액은?  → 34000
# park 이 2시간 일한 급여 총액은? → 17000
# park 이 2시간 일한 급여 + 상여급 2000 총액은? → 19000



class Partimer:
    
    wage_per_hour = 8500
    num_emplyee = 0
    
    
    def __init__(self, nickname, workplace = "113동"):
        self.nickname = nickname
        self.workplace = workplace
        self.entile_wage = 0
        Partimer.num_emplyee += 1
        
    def calculate_wage(self, hour, bonus = 0):
        # 근무 시간과 상여금을 급여 계산
        self.bonus = bonus
        self.hour = hour
        self.entile_wage = Partimer.wage_per_hour * self.hour + self.bonus
        return self.entile_wage


a = Partimer("park")
print(a.calculate_wage(10, 2000))



# 강사님 답

class Partimer:
    
    total_rate = 8500
    total_part_timers = 0
    total_wage = 0
    
    def __init__(self, nickname, workplace = "113동"):
        self.nickname = nickname
        self.workplace = workplace
        self.entile_wage = 0
        Partimer.total_part_timers += 1
        
    def calculate_wage(self, hour, bonus = 0):
        # 근무 시간과 상여금을 급여 계산
        self.total_wage = Partimer.total_rate * hour + bonus
        return self.total_wage

Park = Partimer("라이언")
Lee = Partimer("네오", "127-1동")
print(Lee.__dict__)



print(Park.calculate_wage(4))
print(Lee.calculate_wage(2))
print(Partimer.total_part_timers, "명 근무중")
print(Park.calculate_wage(2, 2000))





























