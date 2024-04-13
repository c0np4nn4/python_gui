import sys
from PyQt5.QtWidgets import *

# QMainWindow 를 상속받아 Window 를 만듭니다.
class MyWindow(QMainWindow):
    def __init__(self):
        # super == QMainWindow
        super().__init__()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
