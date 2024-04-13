import sys
from PyQt5.QtCore import QFile
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우의 타이틀을 수정합니다.
        self.setWindowTitle("AWESOME Title")

        # 윈도우의 크기를 재조정합니다.
        self.setGeometry(300, 300, 400, 400)

        # 아이콘을 수정합니다.
        # 현재 안되고 있음..
        self.setWindowIcon(QIcon('coffee.ico'))

        # 버튼을 추가합니다.
        button = QPushButton("클릭", parent=self)
        button.move(10, 10)


app = QApplication(sys.argv)

window = MyWindow()
window.show()


app.exec_()
