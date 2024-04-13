import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("종료 버튼", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.close)

        # 크기 조절도 가능합니다.
        self.btn.resize(100, 100)

        # 활성화 / 비활성화 여부도 선택 가능합니다.
        self.btn.setEnabled(True)
        self.btn.setDisabled(False)

        # 버튼의 텍스트를 얻어 오는 것도 가능합니다.
        print(self.btn.text())

app = QApplication(sys.argv)

window = MyWindow()
window.setGeometry(300, 300, 500, 500)
window.show()

app.exec_()
