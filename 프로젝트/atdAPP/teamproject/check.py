import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5 import uic
from PyQt5.QtGui import QPixmap  # QPixmap 모듈 추가

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()  # UI 초기화 함수 호출
        self.generated_numbers = set()  # 생성된 숫자를 저장할 집합 초기화

    # UI 초기화 함수
    def initUI(self):
        # UI 파일 로드
        uic.loadUi('./atd_chk.ui', self)
        self.setWindowTitle('교사용 출결체크')  # 윈도우 제목 설정

        # QLabel 객체 가져오기
        self.num_chk_label = self.findChild(QLabel, 'num_chk')  # QLabel ID가 'num_chk'인 위젯 가져오기
        self.my_page_label = self.findChild(QLabel, 'my_page')  # QLabel ID가 'image_label'인 위젯 가져오기
        self.my_atd_label = self.findChild(QLabel, 'my_atd')  # QLabel ID가 'image_label'인 위젯 가져오기

        # QLabel에 이미지 설정
        pixmap = QPixmap('./images/mypage.png')  # 이미지 파일 경로
        self.my_page_label.setPixmap(pixmap)  # QLabel에 이미지 설정
        self.my_page_label.setScaledContents(True)  # 이미지가 QLabel 크기에 맞게 조정되도록 설정

        pixmap = QPixmap('./images/atd.png')  # 이미지 파일 경로
        self.my_atd_label.setPixmap(pixmap)  # QLabel에 이미지 설정
        self.my_atd_label.setScaledContents(True)  # 이미지가 QLabel 크기에 맞게 조정되도록 설정

        # 출결번호 생성 버튼 클릭 시그널 연결
        self.btn_chk.clicked.connect(self.btnchkClick)

    # btn_chk 버튼 클릭 이벤트 처리 함수
    def btnchkClick(self):
        # 중복되지 않은 랜덤 숫자 생성
        if len(self.generated_numbers) >= 100:
            QMessageBox.warning(self, '경고', '모든 숫자가 생성되었습니다!')
            return
        while True:
            random_number = random.randint(1, 100)
            if random_number not in self.generated_numbers:
                self.generated_numbers.add(random_number)
                break
        # 생성된 랜덤 숫자를 QLabel에 표시
        self.num_chk_label.setText(str(random_number))
        
# 프로그램 실행 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    win = MainWindow()  # MainWindow 객체 생성
    win.show()  # 메인 윈도우 표시
    app.exec_()  # 이벤트 루프 실행