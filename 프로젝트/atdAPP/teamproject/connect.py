import sys
from PyQt5.QtWidgets import QApplication
from sel_login import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()