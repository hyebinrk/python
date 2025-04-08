import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5 import uic
from PyQt5.QtGui import QPixmap  # QPixmap 모듈 추가

# Oracle 데이터베이스 연결을 위한 cx_Oracle 모듈 임포트
import cx_Oracle as oci

# Oracle 데이터베이스 연결 정보 설정
sid = 'XE'  # 데이터베이스 SID
# host = '210.119.14.71'  # 데이터베이스 호스트 주소 (외부 접속 시 변경 필요)
host = '210.119.14.71'
port = 1521  # 데이터베이스 포트 번호
username = 'attendance'  # 데이터베이스 사용자 이름
password = '12345'  # 데이터베이스 비밀번호

# 메인 윈도우 클래스 정의
class TAtdMainWindow(QMainWindow): 
    def __init__(self, t_id=None):  # t_id 매개변수 추가
        super(TAtdMainWindow, self).__init__() 
        self.t_id = t_id  # 로그인한 T_ID 저장
        self.initUI()  # UI 초기화 함수 호출
        self.generated_numbers = set()  # 생성된 숫자를 저장할 집합 초기화

    # UI 초기화 함수
    def initUI(self):
        # UI 파일 로드
        uic.loadUi('./TAtd_chk.ui', self)
        self.setWindowTitle('교사용 출결 체크')  # 윈도우 제목 설정
        

         # QLabel 객체 가져오기
        self.num_chk_label = self.findChild(QLabel, 'num_chk')
        self.my_page_label = self.findChild(QLabel, 'my_page') 
        self.my_atd_label = self.findChild(QLabel, 'my_atd') 

        # QLabel에 이미지 설정
        pixmap = QPixmap('./image/4543148.png')  # 이미지 파일 경로
        self.my_page_label.setPixmap(pixmap)  # QLabel에 이미지 설정
        scaled_pixmap = pixmap.scaled(200, 150)  
        self.my_page_label.setPixmap(scaled_pixmap)


        pixmap = QPixmap('./image/attendance (2).png')  # 이미지 파일 경로
        self.my_atd_label.setPixmap(pixmap)  # QLabel에 이미지 설정       
        scaled_pixmap = pixmap.scaled(140, 100)  # 비율을 유지하며 크기 조정
        self.my_atd_label.setPixmap(scaled_pixmap)

        # 출결번호 생성 버튼 클릭 시그널 연결
        self.btn_chk.clicked.connect(self.numchkClick)
        self.btn_page.clicked.connect(self.MypageWindow)
        self.btn_atd.clicked.connect(self.AtdMgmtWindow)



    # btn_chk 버튼 클릭 이벤트 처리 함수
    def numchkClick(self):
        print(f"로그인한 사용자: {self.t_id}")  # T_ID 확인용 출력
        # 중복되지 않은 랜덤 숫자 생성
        if len(self.generated_numbers) >= 100:
            QMessageBox.warning(self, '경고', '모든 숫자가 생성되었습니다!')
            return
        while True:
            random_number = random.randint(1, 100)
            if random_number not in self.generated_numbers:
                self.generated_numbers.add(random_number)
                break

        # 데이터베이스에 랜덤 숫자 저장
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()
        try:
            # TEACHER와 ATD 테이블에서 T_NO가 같은 S_NO에게 CHECKNO 부여
            query = '''
                UPDATE ATD
                   SET CHECKNO = :random_number
                 WHERE S_NO IN (
                       SELECT S_NO
                         FROM TEACHER
                        WHERE T_NO = ATD.T_NO
                   )
            '''
            cursor.execute(query, {'random_number': random_number})
            conn.commit()
            QMessageBox.information(self, '성공', f'출석번호 {random_number}이(가) 저장되었습니다.')
        except Exception as e:
            QMessageBox.critical(self, '오류', f'데이터베이스 오류: {e} ')
        finally:
            cursor.close()
            conn.close()

        # QLabel에 텍스트 표시
        self.atd_num_label.setText("번호를 생성하였습니다!")  # 텍스트 변경

    def MypageWindow(self):
        from mypage import MypageWindow as MypageWindow  # 마이페이지.py에서 MypageWindow 가져오기
        self.my_page = MypageWindow()  # T_ID 전달
        self.my_page.show()  # 출결 체크 창 열기

    def AtdMgmtWindow(self):
        from AttendanceApp import AttendanceApp
        self.atd_mgmt = AttendanceApp()  # T_ID 전달
        self.atd_mgmt.show()
    


        # 프로그램 실행 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    win = TAtdMainWindow()  # MainWindow 객체 생성
    win.show()  # 메인 윈도우 표시
    app.exec_()  # 이벤트 루프 실행