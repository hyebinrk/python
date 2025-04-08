import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, Qt
from PyQt5 import uic
import cx_Oracle as oci

# DB 접속 정보
sid = 'XE'
host = '210.119.14.71'
# host = 'localhost'
port = 1521
username = 'attendance'
password = '12345'


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.symbols = {}  
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.load_attendance_data()  

    def load_attendance_data(self):
        try:
            conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
            cursor = conn.cursor()

            query = '''
                SELECT ATD_DATE, STATUS, TO_CHAR(ATD_TIME, 'HH24:MI') 
                FROM ATTENDANCE.ATD 
                WHERE S_NO = 3 
                AND EXTRACT(MONTH FROM ATD_DATE) = 3
            '''
            cursor.execute(query)
            rows = cursor.fetchall()

            status_map = {'P': 'O', 'L': '△', 'A': 'X'}
            for date, status, time in rows:
                qdate = QDate(date.year, date.month, date.day)
                self.symbols[qdate] = (status_map.get(status, ""), time)

        except Exception as e:
            print("데이터베이스 오류:", e)
        finally:
            cursor.close()
            conn.close()

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        if date in self.symbols:
            symbol, time = self.symbols[date]
            color_map = {'O': "blue", '△': "green", 'X': "red"}

            painter.setPen(QColor(color_map.get(symbol, "black")))

            font = QFont("Arial", 12, QFont.Bold)
            painter.setFont(font)
            painter.drawText(rect.adjusted(rect.width() // 3, 0, 0, 0), Qt.AlignLeft, symbol)

            # X 상태일 경우에는 시간을 그리지 않음
            if symbol != 'X':  
                painter.setFont(QFont("Arial", 6)) 
                painter.drawText(rect.adjusted(0, rect.height() // 2, 0, 0), Qt.AlignCenter, time)

        


class AttendanceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('./miniproject01/출석관리,통계.ui', self)
        uic.loadUi('./AttendanceApp.ui', self)


        old_calendar = self.findChild(QCalendarWidget, "calendarWidget")
        if old_calendar:

            self.custom_calendar = CustomCalendar(self)
            self.custom_calendar.setGeometry(old_calendar.geometry())
            self.custom_calendar.setObjectName("calendarWidget")

            layout = old_calendar.parentWidget().layout()
            if layout:
                layout.replaceWidget(old_calendar, self.custom_calendar)
            old_calendar.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AttendanceApp()
    window.show()
    sys.exit(app.exec_())