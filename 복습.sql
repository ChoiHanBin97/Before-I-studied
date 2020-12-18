-- 게임회사 롤 게임 만들기 모델링 실습
-- 1. 요구 분석
-- 캐릭터, 게임전적, 유저, 아이템

-- 2. 개념적 설계(개념 모델링)
-- 캐릭터 테이블 : 캐릭터명, 공격력, 방어력, 체력
-- 유저 테이블 : 아이디, 닉네임, 이름
-- 아이템 테이블 : 아이템명, 가격, 공격력
-- 게임 테이블 : 유저 정보, 캐릭터, kda, 평점

-- 3. 논리적 설계(논리 모델링)
-- 캐릭터 : 캐릭터명(PK), 공격력, 방어력, 체력
-- 유저 : 아이디(PK), 닉네임, 이름       #닉네임도 겹치지 않지만 아이디가 선행적으로 만들어지고 닉네임이 만들어짐 -> 닉네임이 없을 수 있음 -> 개체무결성떄문에 닉네임은 PK불가능
-- 게임 : 게임번호(PK), 아이디(FK), 캐틱터명(FK), kda, 평점
  
-- 4. 물리적 설계(물리 모델링)
-- 캐릭터						게임
-- 캐릭터명 VARCHAR2(20)
-- 공격력 NUMBER(4)
-- 방어력 NUMBER(4)
-- 체력 NUMBER(4)


-- DUAL 테이블
-- 하나의 결과를 얻기 위해 사용하는 테이블(추가로 테이블을 불러오는 것...?)
SELECT SYSDATE, 1+1 FROM DUAL;    
-- 상대 공격력 : 100
-- 내 방어력 : 50
-- 내 체력 : 2000

CREATE TABLE LOL_CHARACTER(
	캐릭터명 VARCHAR2(20) PRIMARY KEY,
	공격력 NUMBER(4),
	방어력 NUMBER(4),
	체력 NUMBER(4)
);
INSERT INTO LOL_CHARACTER VALUES('야스오', 300, 75, 2000);
INSERT INTO LOL_CHARACTER VALUES('티모', 100, 50, 1500);

-- 이런 식으로 구현할 수 있음
SELECT (SELECT 체력 FROM LOL_CHARACTER WHERE 캐릭터명='티모') - ((SELECT 공격력 FROM LOL_CHARACTER WHERE 캐릭터명 = '야스오')-
(SELECT 방어력 FROM LOL_CHARACTER WHERE 캐릭터명 = '티모')) FROM DUAL;
