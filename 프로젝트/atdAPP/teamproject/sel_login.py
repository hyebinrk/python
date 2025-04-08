import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets,uic

# # Oracle 모듈
# import cx_Oracle as oci

## DB연결 설정
sid = 'XE'
host = '210.119.14.71'
port = 1521
username = 'attendance'
password = '12345'


# 교사/학생 로그인 선택    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./sel_login.ui', self)
        self.setWindowTitle('학생용 출결 체크')
        self.setWindowIcon(QIcon('./image/app01.png'))  # 아이콘 설정
      

        # 버튼 아이콘 추가
        self.btnTeacherSelect.setIcon(QIcon('./image/teacher.png'))
        self.btnStudentSelect.setIcon(QIcon('./image/student.png'))
        
        # 버튼 이벤트 추가
        self.btnTeacherSelect.clicked.connect(self.TLoginWindow)
        self.btnStudentSelect.clicked.connect(self.SLoginWindow)

    
    def TLoginWindow(self):
        from t_login import MainWindow as TLoginWindow
        self.my_page = TLoginWindow()  
        self.my_page.show() 
        self.close()

    def SLoginWindow(self):
        from s_login import MainWindow  # SAtdMainWindow.py에서 SAtd_chk 가져오기
        self.check_window = MainWindow()  
        self.check_window.show()  # 출결 체크 창 열기
        self.close()  # 현재 창 닫기

# class TeacherloginWindow(QMainWindow):
#     def __init__(self):
#         super(TeacherloginWindow, self).__init__()
#         self.initUI()
#         # self.loadData()
    
#     def initUI(self):
#         uic.loadUi('./t_login.ui', self)
#         self.setWindowTitle('교사 로그인')

# class StudentloginWindow(QMainWindow):
#     def __init__(self):
#         super(StudentloginWindow, self).__init__()
#         self.initUI()
#         # self.loadData()
    
#     def initUI(self):
#         uic.loadUi('./학생 로그인 화면.ui', self)
#         self.setWindowTitle('학생 로그인')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()