import sys
from PyQt5.QtWidgets import *

def say_hello():
    print("Hello World!")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        # ----------- [1] slot function --------------
        # button 위젯을 생성합니다.
        btn_hello = QPushButton("Hello 버튼", parent=self)
        # 버튼의 위치를 재조정합니다.
        btn_hello.move(10, 30)
        # 버튼에 연결된 `슬롯` 함수를 실행합니다.
        # 버튼을 클릭하는 행위는 `시그널`이라 부릅니다.
        btn_hello.clicked.connect(say_hello)

        # ----------- [2] method as a slot function --------------
        btn_hi = QPushButton("Hi 버튼", parent=self)
        btn_hi.move(10, 50)
        # MyWindow 클래스 내에 정의된 함수도 `슬롯`로 으로 활용할 수 있습니다.
        btn_hi.clicked.connect(self.say_hi)

        # ----------- [3] quit button --------------
        btn_quit = QPushButton("종료",  parent=self)
        btn_quit.move(30, 80)
        btn_quit.clicked.connect(self.close)
        # 아래 방법도 가능합니다.
        # btn_quit.clicked.connect(QApplication.instance().quit)

        



    # 메서드이기 때문에 `self`가 첫 인자가 되어야 합니다.
    def say_hi(self):
        print("Hi World!")

app = QApplication(sys.argv)

window = MyWindow()
window.setGeometry(300, 300, 500, 500)
window.show()

app.exec_()

