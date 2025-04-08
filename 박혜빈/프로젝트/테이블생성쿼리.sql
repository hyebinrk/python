-- sys(sysdba)로 작업
-- madang 스키마, 사용자 생성
DROP USER attendance;
CREATE USER attendance IDENTIFIED BY 12345;

-- 권한 설정
GRANT CONNECT, resource TO attendance;

-- attendance로 사용 스키마변경

-- 테이블 Student 생성
CREATE TABLE "Student" (
	"s_no"		number			NOT NULL,
	"s_id"		varchar2(20)	NOT NULL,
	"s_pw"		varchar2(20)	NOT NULL,
	"s_name"	varchar2(15)	NOT NULL,
	"s_birth"	date			NOT NULL,
	"s_tel"		varchar(13)		NOT NULL,
	"s_addr"	varchar2(100)	NOT NULL,
	"a_class"	number(2)		NOT NULL
);

CREATE TABLE "Teacher" (
	"t_no"		number			NOT NULL,
	"t_id"		varchar2(20)	NOT NULL,
	"t_pw"		varchar2(20)	NOT NULL,
	"t_name"	varchar2(20)	NOT NULL,
	"t_tel"		varchar2(13)	NOT NULL,
	"a_class"	number(2)		NOT NULL,
	"s_no"		number			NOT NULL
);

CREATE TABLE "AttendanceInfo" (
	"att_no"	number		NOT NULL,
	"t_no"		number		NOT NULL,
	"s_no"	number			NOT NULL,
	"att_time"	timestamp	NOT NULL,
	"Field2"	date		NOT NULL,
	"Field3"	varchar2(20)NOT NULL
);

ALTER TABLE "Student" ADD CONSTRAINT "PK_STUDENT" PRIMARY KEY (
	"s_no"
);

ALTER TABLE "Teacher" ADD CONSTRAINT "PK_TEACHER" PRIMARY KEY (
	"t_no"
);

ALTER TABLE "AttendanceInfo" ADD CONSTRAINT "PK_ATTENDANCEINFO" PRIMARY KEY (
	"att_no"
);

COMMIT;



-- Student용 시퀀스 생성
CREATE SEQUENCE SEQ_STUDENT
	INCREMENT BY 1		-- 숫자를 1씩 증가
	START WITH 1;		-- 1부터 숫자가 증가됨
	
COMMIT;

-- 사용자 attendance으로 변경
