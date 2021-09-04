from PyQt5.QtCore import QDateTime,QTimer
from PyQt5.QtWidgets import QWidget, QHeaderView, QPushButton, QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MyVideoWidget(QLabel):
    def __init__(self,parent = None):
        super(MyVideoWidget,self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setGeometry(QtCore.QRect(0, 0, 860, 540))
        pic = QtGui.QPixmap("resource/video.jpg").scaled(860,540)
        self.setPixmap(pic)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyVideoWidget()
    ex.show()
    sys.exit(app.exec_())