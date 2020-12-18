SELECT * FROM T_PROFESSOR; --16
SELECT * FROM T_DEPARTMENT; --12
SELECT 16 *12 FROM dual;

--ORACLE
SELECT p.NAME, p.DEPTNOM, d.DNAME FROM T_PROFESSOR p, T_DEPARTMENT d
WHERE p.DEPTNO = d.DEPTNO;

--ANSI
-- �����, �̳�����
SELECT p.NAME, p.DEPTNO, d.DNAME FROM T_PROFESSOR p 
	JOIN T_DEPARTMENT d ON p.DEPTNO = d.DEPTNO;

SELECT * FROM T_CUSTOMER;

SELECT * FROM T_EMP2;
SELECT * FROM T_POST;
SELECT e.NAME ����̸�, e.POST ����, e.PAY �޿�, p.S_PAY ���ѱ޿�, p.E_PAY ���ѱ޿�
FROM T_EMP2 e, T_POST p WHERE e.POST = p.POST;

-- EMP, DEPT ���̺��� �����ȣ, ����̸�, �μ����� �˻�
SELECT * FROM T_EMP;
SELECT * FROM T_DEPT;
--ORACLE
SELECT e.EMPNO, e.ENAME, d.LOC FROM T_EMP e, T_DEPT d 
WHERE e.DEPTNO = d.DEPTNO;

--ANSI
SELECT e.EMPNO �����ȣ, e.ENAME ����̸�, d.LOC �μ����� FROM T_EMP e
	JOIN T_DEPT d ON e.DEPTNO = d.DEPTNO;

--NATURAL JOIN
SELECT * FROM T_EMP e
	JOIN T_DEPT d USING(DEPTNO);
SELECT * FROM T_EMP NATURAL JOIN T_DEPT;


-- PLAYER, TEAM ���̺��� ������ ������ ���� ���� ��ȭ��ȣ �˻�
--									CONCAT(CONCAT(t.DDD, '-'), t.TEL)
SELECT p.PLAYER_NAME �̸�, t.TEAM_NAME ���̸�, t.DDD ||'-'|| t.TEL ��ȭ��ȣ
FROM PLAYER p
	JOIN TEAM t ON p.TEAM_ID = t.TEAM_ID
WHERE p.PLAYER_NAME = '������'


-- JOBS ���̺��� JOB_ID�� EMAIL, Ǯ����, JOB_TITLE �˻�
SELECT * FROM JOBS;
SELECT * FROM EMPLOYEES;

SELECT e.EMAIL, e.FIRST_NAME ||' '|| e.LAST_NAME "FULL NAME", j.JOB_TITLE FROM JOBS j
	JOIN EMPLOYEES e ON j.JOB_ID = e.JOB_ID;


-- T_STUDENT, T_DEPARTMENT ���̺��� �л��̸�, 1���� �а���ȣ, 1���� �а� �̸� �˻�
SELECT * FROM T_STUDENT;
SELECT * FROM T_DEPARTMENT;

SELECT s.NAME �л��̸�, s.DEPTNO1 "1���� �а���ȣ", d.DNAME "1���� �а� �̸�" FROM T_STUDENT s 
	JOIN T_DEPARTMENT d ON d.DEPTNO = s.DEPTNO1;
-- T_STUDENT, T_PROFESSOR ���̺��� �л��̸�, �������� ��ȣ, �������� �̸� �˻�
SELECT * FROM T_STUDENT;
SELECT * FROM T_PROFESSOR;

SELECT s.NAME �л��̸�, s.PROFNO "�������� ��ȣ", p.NAME "�������� �̸�" FROM T_STUDENT s
	JOIN T_PROFESSOR p ON p.PROFNO = s.PROFNO;

-- OUTER JOIN
SELECT s.NAME �л��̸�, s.PROFNO ����������ȣ, p.NAME ���������̸� FROM T_STUDENT s
	LEFT OUTER JOIN T_PROFESSOR p ON s.PROFNO=p.PROFNO;

SELECT s.NAME �л��̸�, s.PROFNO ����������ȣ, p.NAME ���������̸� FROM T_STUDENT s
	RIGHT OUTER JOIN T_PROFESSOR p ON s.PROFNO=p.PROFNO
WHERE p.NAME = '����';

SELECT s.STADIUM_NAME �����, t.TEAM_NAME ���̸� FROM STADIUM s
	LEFT OUTER JOIN TEAM t ON s.HOMETEAM_ID = t.TEAM_ID;

SELECT * FROM STADIUM s
	FULL OUTER JOIN TEAM t ON s.HOMETEAM_ID = t.TEAM_ID;

-- EMP ���̺��� ����� �̸��� �� ����� �Ŵ��� �̸��� �Բ� ���
-- SELF ����
SELECT * FROM T_EMP;
SELECT e1.ENAME ����̸�, e2.ENAME �Ŵ����̸� FROM T_EMP e1
	JOIN T_EMP e2 ON e1.MGR=e2.EMPNO;


-- CROSS ����
-- īƼ�� ���� ������� �����ش�.
-- SELECT p.NAME, p.DEPTNO, d.DNAME FROM T_PROFESSOR p, T_DEPARTMENT d;
SELECT p.NAME, p.DEPTNO, d.DNAME FROM T_PROFESSOR p
	CROSS JOIN T_DEPARTMENT d;
	

-- T_DEPT2 ���̺��� �μ���� �� �μ��� �����μ� ���
SELECT * FROM T_DEPT2;
SELECT d1.DNAME, d2.DNAME FROM T_DEPT2 d1
	JOIN T_DEPT2 d2 ON d1.PDEPT = d2.DCODE;

-- T_PROFESSOR ���̺��� ���� ��ȣ, �����̸�, �Ի���, �ڱ⺸�� �Ի��� ���� ����� �ο��� ���
SELECT * FROM T_PROFESSOR;
SELECT p1.PROFNO ������ȣ, p1.NAME �����̸�, p1.HIREDATE �Ի���, COUNT(P2.HIREDATE) FROM T_PROFESSOR p1, T_PROFESSOR p2
	WHERE p1.HIREDATE > p2.HIREDATE
GROUP BY p1.PROFNO, p1.NAME, p1.HIREDATE;

SELECT p1.PROFNO ������ȣ, p1.NAME �����̸�, p1.HIREDATE �Ի���, COUNT(P2.HIREDATE) "�Ի����� ���� ��� ��" FROM T_PROFESSOR p1 
	LEFT OUTER JOIN T_PROFESSOR p2 ON p1.HIREDATE > p2.HIREDATE
GROUP BY p1.PROFNO, p1.NAME, p1.HIREDATE;


-- T_CUSTOMER ���̺��� �� ���� ����Ʈ���� ���� �� �ִ� ��ǰ�� ��ȸ -> �̸�, ����Ʈ, ��ǰ�� ���
SELECT * FROM T_CUSTOMER;
SELECT * FROM T_GIFT;

SELECT c.C_NAME, c.C_POINT, g.G_NAME FROM T_CUSTOMER c
	LEFT OUTER JOIN T_GIFT g ON g.G_END >= c.C_POINT AND g.G_START <= c.C_POINT;

-- ������ ��
SELECT c.C_NAME, c.C_POINT, g.G_NAME FROM T_CUSTOMER c
	JOIN T_GIFT g ON c.C_POINT >= g.G_START AND c.C_POINT <= g.G_END;

-- �� ��ǰ�� �̸��� �ʿ��� ������ �����
SELECT g.G_NAME, COUNT(g.G_NAME) FROM T_GIFT g
	JOIN T_CUSTOMER c ON g.G_END > c.C_POINT AND g.G_START <= c.C_POINT
GROUP BY g.G_NO, g.G_NAME, g.G_END, g.G_START;

-- ������ ��
SELECT g.G_NAME, COUNT(c.C_NAME) FROM T_GIFT g
	JOIN T_CUSTOMER c ON c.C_POINT BETWEEN g.G_START AND g.G_END
GROUP BY g.G_NAME;


-- T_STUDENT ���̺�� T_EXAM01 �� �л��� �̸�, ����, ����
SELECT * FROM T_STUDENT;
SELECT * FROM T_EXAM01;
SELECT * FROM T_CREDIT;

SELECT s.NAME, e.TOTAL, c.GRADE FROM T_STUDENT s, T_EXAM01 e, T_CREDIT c
	WHERE c.MIN_POINT <= e.TOTAL AND c.MAX_POINT >= e.TOTAL AND e.STUDNO = s.STUDNO;

-- ������ ��
SELECT s.NAME, e.TOTAL, c.GRADE FROM T_STUDENT s
	JOIN T_EXAM01 e ON s.STUDNO = e.STUDNO
	JOIN T_CREDIT c ON e.TOTAL BETWEEN c.MIN_POINT AND c.MAX_POINT;

-- T_CUSTOMER, T_GIFT�� �����ؼ� ��ǿ� �����Ÿ� ������ �� �ִ� ���� �̸�, ����Ʈ ���
SELECT * FROM T_GIFT;
SELECT * FROM T_CUSTOMER;

SELECT c.C_NAME �̸�, c.C_POINT FROM T_CUSTOMER c, T_GIFT g
	WHERE g.G_END >= c.C_POINT AND g.G_START <= c.C_POINT AND G_NAME = '��ǿ�������';
	
-- ������ ��
SELECT c.C_NAME, c.C_POINT FROM T_CUSTOMER c
	JOIN T_GIFT g ON c.C_POINT >= g.G_START AND G_NAME = '��ǿ�������';

-- WHERE �ᵵ ������ ������ ���� �������� �����ɸ��� ������ JOIN ON���� ���°� �� ����.
/* SELECT c.C_NAME, c.C_POINT FROM T_CUSTOMER c
	JOIN T_GIFT g ON c.C_POINT >= g.G_START 
	WHERE G_NAME = '��ǿ�������';
*/
