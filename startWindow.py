#use pyqt5 to establish a window that can start myGestureControl.py(which is a python file that can control the mouse and keyboard)
#add a notice that the window will be closed when you press esc

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
import os

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('Start Gesture Control', self)
        btn.move(40, 40)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.startGesture)

        btn2 = QPushButton('Exit', self)
        btn2.move(40, 80)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)
        # add a notice that the window will be closed when you press esc
        btn2.setToolTip('Press <b>ESC</b> to quit')

        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Gesture Control')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
        self.resize(300, 150)
        self.center()
        self.setWindowTitle('Gesture Control')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def startGesture(self):
        os.system("python myGestureControl.py")

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# if __name__ == '__main__':

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())