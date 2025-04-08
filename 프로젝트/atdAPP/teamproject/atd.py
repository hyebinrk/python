import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtGui
import cx_Oracle as oci

# Oracle 데이터베이스 연결 정보 설정
sid = 'XE'  # 데이터베이스 SID
host = '210.119.14.71'  # 데이터베이스 호스트 주소
port = 1521  # 데이터베이스 포트 번호
username = 'attendance'  # 데이터베이스 사용자 이름
password = '12345'  # 데이터베이스 비밀번호

class SAtdMainWindow(QMainWindow):
    def __init__(self, s_id=None):
        super(SAtdMainWindow, self).__init__()
        self.s_id = s_id  # 학생의 ID
        self.initUI()

    def initUI(self):
        try:
            uic.loadUi('./SAtd_chk.ui', self)  # UI 파일 로드
            self.setWindowTitle('학생용 출결 체크')
            self.setWindowIcon(QIcon('./image/app01.png'))  # 아이콘 설정

            # 버튼 클릭 시 해당 함수 호출
            self.btn_submit.clicked.connect(self.atdCheckClick)  # 출석 버튼 클릭 시
            self.btn_my.clicked.connect(self.MypageWindow)
            self.btn_atd.clicked.connect(self.MgmtAtdWindow)
            self.btn_eal.clicked.connect(self.btnEalClick)
            self.btn_cob.clicked.connect(self.btnCobClick)
            self.btn_out.clicked.connect(self.btnOutClick)

            self.show()  # 창 띄우기

        except Exception as e:
            print(f"Error loading UI: {e}")
            QMessageBox.critical(self, "Error", f"UI 로드 중 오류가 발생했습니다: {e}")

    def atdCheckClick(self):
        """학생이 출석 번호를 입력하고, 해당 번호로 출석 체크 처리"""
        atd_check_number = self.input_number.text()  # 입력된 출석 번호 가져오기
        
        if not atd_check_number:
            QMessageBox.warning(self, "경고", "출석 번호를 입력해 주세요.")
            return
        
        try:
            # 데이터베이스 연결
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            # 학생의 학번을 가져옴
            cursor.execute("SELECT s_no FROM student WHERE s_id = :s_id", {"s_id": self.s_id})
            result = cursor.fetchone()

            if result:
                s_no = result[0]  # 학생 번호 가져오기
                
                # 해당 학생의 출석 번호와 일치하는지 확인
                query = """SELECT checkno FROM atd WHERE checkno = :checkno AND s_no = :s_no AND trunc(atd_date) = trunc(sysdate)"""
                cursor.execute(query, {"checkno": atd_check_number, "s_no": s_no})
                check_result = cursor.fetchone()

                if check_result:
                    # 출석 번호가 일치하면 출석 처리
                    update_query = """UPDATE atd
                                      SET atd_time = CAST(SYSTIMESTAMP AT TIME ZONE 'UTC' AS TIMESTAMP WITH TIME ZONE) AT TIME ZONE 'Asia/Seoul'
                                      WHERE checkno = :checkno AND s_no = :s_no AND trunc(atd_date) = trunc(sysdate)"""
                    cursor.execute(update_query, {"checkno": atd_check_number, "s_no": s_no})
                    connection.commit()

                    QMessageBox.information(self, "출석 처리 완료", "출석이 정상적으로 등록되었습니다.")
                else:
                    QMessageBox.warning(self, "출석 번호 불일치", "입력한 출석 번호가 맞지 않거나, 오늘의 출석 기록이 없습니다.")

            else:
                QMessageBox.warning(self, "오류", "학생 정보를 찾을 수 없습니다.")

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")
        finally:
            cursor.close()
            connection.close()

    def MypageWindow(self):
        """마이페이지 화면 열기"""
        from mypage import MypageWindow  # 마이페이지.py에서 MypageWindow 가져오기
        self.my_page = MypageWindow()  # T_ID 전달
        self.my_page.show()  # 마이페이지 창 열기

    def MgmtAtdWindow(self):
        """출결 관리 화면 열기"""
        from AttendanceApp import AttendanceApp
        self.atd_mgmt = AttendanceApp()  # T_ID 전달
        self.atd_mgmt.show()

    def btnEalClick(self):
        """조퇴 버튼 클릭 시 DB 저장"""
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            cursor.execute("SELECT s_no FROM student WHERE s_id = :s_id", {"s_id": self.s_id})
            result = cursor.fetchone()

            if result:
                s_no = result[0]  # 학생 번호 가져오기

                query = """UPDATE atd
                        SET leave_time = CAST(SYSTIMESTAMP AT TIME ZONE 'UTC' AS TIMESTAMP WITH TIME ZONE) AT TIME ZONE 'Asia/Seoul'
                        WHERE s_no = :s_no
                        AND trunc(atd_date) = trunc(sysdate)"""

                cursor.execute(query, {"s_no": s_no})
                connection.commit()
                QMessageBox.information(self, "조퇴 처리 완료", "조퇴가 정상적으로 등록되었습니다.")
                
            else:
                QMessageBox.warning(self, "오류", "학생 정보를 찾을 수 없습니다.")

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def btnOutClick(self):
        """외출 버튼 클릭 시 DB 저장"""
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            cursor.execute("SELECT s_no FROM student WHERE s_id = :s_id", {"s_id": self.s_id})
            result = cursor.fetchone()

            if result:
                s_no = result[0]  # 학생 번호 가져오기

                query = """UPDATE atd
                        SET out_time = CAST(SYSTIMESTAMP AT TIME ZONE 'UTC' AS TIMESTAMP WITH TIME ZONE) AT TIME ZONE 'Asia/Seoul'
                        WHERE s_no = :s_no
                        AND trunc(atd_date) = trunc(sysdate)"""

                cursor.execute(query, {"s_no": s_no})
                connection.commit()
                QMessageBox.information(self, "외출 처리 완료", "외출이 정상적으로 등록되었습니다.")
            else:
                QMessageBox.warning(self, "오류", "학생 정보를 찾을 수 없습니다.")

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()

    def btnCobClick(self):
        """복귀 버튼 클릭 시 DB 저장"""
        try:
            connection = oci.connect(username, password, f"{host}:{port}/{sid}")
            cursor = connection.cursor()

            cursor.execute("SELECT s_no FROM student WHERE s_id = :s_id", {"s_id": self.s_id})
            result = cursor.fetchone()

            if result:
                s_no = result[0]  # 학생 번호 가져오기

                query = """UPDATE atd
                        SET in_time = CAST(SYSTIMESTAMP AT TIME ZONE 'UTC' AS TIMESTAMP WITH TIME ZONE) AT TIME ZONE 'Asia/Seoul'
                        WHERE s_no = :s_no
                        AND trunc(out_time) = trunc(sysdate)"""

                cursor.execute(query, {"s_no": s_no})
                connection.commit()
                QMessageBox.information(self, "복귀 처리 완료", "복귀가 정상적으로 등록되었습니다.")
            else:
                QMessageBox.warning(self, "오류", "학생 정보를 찾을 수 없습니다.")

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"오류 내용: {str(e)}")

        finally:
            cursor.close()
            connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SAtdMainWindow(s_id="student_id_here")  # 여기에 학생 ID를 전달
    sys.exit(app.exec_())  # QApplication 이벤트 루프 실행
