import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# win = QWidget()
# win.show()

# button = QPushButton("Click")
# button.show()

label = QLabel("Label")
label.show()

app.exec_() # 이벤트 루프 시작
