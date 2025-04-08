-- attendance 로그인

-- 조회
SELECT * FROM "Student";

-- 더미데이터 삽입
INSERT INTO "Student"("s_no", "s_id", "s_pw", "s_name", "s_birth", "s_tel", "s_addr", "a_class")
VALUES (SEQ_STUDENT.nextval, '0122', '0000', '홍길동', '091111', '010-9999-8888', '부산시 해운대구', '03');

COMMIT;

--SELECT s_id, s_name
--		, s_mobile, s_regyear
--	FROM Student;
--
--INSERT INTO STUDENT (std_id, std_name, std_mobile, std_regyear)
--VALUES(SEQ_STUDEN.NEXTVAL, :v_std_name, :v_std_mobile, :v_std_regyear);
