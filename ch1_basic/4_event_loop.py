import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

print("111111111111111")
app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()
print("222222222222222")
