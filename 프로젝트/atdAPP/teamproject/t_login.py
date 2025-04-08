# 시스템 모듈 임포트
import sys
# PyQt5 위젯 및 GUI 관련 모듈 임포트
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets, uic

# Oracle 데이터베이스 연결을 위한 cx_Oracle 모듈 임포트
import cx_Oracle as oci

# Oracle 데이터베이스 연결 정보 설정
sid = 'XE'  # 데이터베이스 SID
host = '210.119.14.71'  # 데이터베이스 호스트 주소 (외부 접속 시 변경 필요)
# host = 'localhost'
port = 1521  # 데이터베이스 포트 번호
username = 'attendance'  # 데이터베이스 사용자 이름
password = '12345'  # 데이터베이스 비밀번호
basic_msg = 'OO고등학교 출결관리앱 v1.0'

# 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()  # UI 초기화 함수 호출

    # UI 초기화 함수
    def initUI(self):
        # UI 파일 로드
        uic.loadUi('./t_login.ui', self)
        self.setWindowTitle('교사용 로그인')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('./image/app01.png'))

        # 로그인 버튼 클릭 시그널 연결
        self.btn_login.clicked.connect(self.btnAddClick)

        # 상태바에 메시지 추가
        self.statusbar.showMessage(basic_msg)


    # 입력 필드 초기화 함수
    def clearInput(self):
        self.input_T_ID.clear()  # 아이디 입력 필드 초기화
        self.input_T_PW.clear()  # 비밀번호 입력 필드 초기화

    # 로그인 버튼 클릭 이벤트 처리 함수
    def btnAddClick(self):
        # 입력 필드에서 아이디와 비밀번호 값 가져오기
        T_ID = self.input_T_ID.text()
        T_PW = self.input_T_PW.text()

        # 입력값 검증 (Validation Check)
        if T_ID == '' or T_PW == '':
            # 입력값이 비어있을 경우 경고 메시지 표시
            QMessageBox.warning(self, '경고', '아이디,비밀번호 입력은 필수 입니다!')
            return  # 함수 종료
        else:
            print('로그인 진행!') 
            values = (T_ID, T_PW)  # 입력값을 튜플로 저장
            # 데이터베이스에서 로그인 정보 확인
            if self.addData(values) == True:  # 로그인 성공
                QMessageBox.about(self, '로그인 성공!', '선생님 어서오세요! ')
                self.openCheckWindow(values[0])  # T_ID 전달
            else:  # 로그인 실패
                QMessageBox.about(self, '로그인 실패!', '로그인 실패, 관리자에게 문의하세요.')
        self.clearInput()  # 입력 필드 초기화

    def openCheckWindow(self, t_id):
        from TAtd_chk import TAtdMainWindow as CheckWindow  # check.py에서 MainWindow 가져오기
        self.check_window = CheckWindow(t_id)  # T_ID 전달
        self.check_window.show()  # 출결 체크 창 열기
        self.close()  # 현재 창 닫기

    # 데이터베이스에서 로그인 정보 확인 함수
    def addData(self, values):
        isSucceed = False  # 로그인 성공 여부 초기화
        # 데이터베이스 연결
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()  # 커서 객체 생성

        try:
            # 로그인 정보 확인 쿼리
            query = '''
                    SELECT COUNT(*)
                      FROM TEACHER
                     WHERE T_ID = :v_T_ID
                       AND T_PW = :v_T_PW
                    '''
            # 쿼리 실행 (바인딩 변수 사용)
            cursor.execute(query, {'v_T_ID': values[0], 'v_T_PW': values[1]})
            result = cursor.fetchone()  # 결과 가져오기

            # 결과가 0보다 크면 로그인 성공
            if result[0] > 0:
                isSucceed = True
        except Exception as e:
            # 예외 발생 시 오류 메시지 출력
            print(f"❌ 오류 발생: {e}")
        finally:
            # 커서와 연결 종료
            cursor.close()
            conn.close()

        return isSucceed  # 로그인 성공 여부 반환

# 프로그램 실행 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    win = MainWindow()  # MainWindow 객체 생성
    win.show()  # 메인 윈도우 표시
    app.exec_()  # 이벤트 루프 실행