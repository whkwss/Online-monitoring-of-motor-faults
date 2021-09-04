from PyQt5.QtCore import QDateTime,QTimer
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MyOnlineWidget(QTableWidget):
    def __init__(self,parent = None):
        super(MyOnlineWidget,self).__init__(parent)
        self.btn = [[]]
        self.initUi()

    def initUi(self):
        self.setGeometry(QtCore.QRect(0, 0, 860, 540))
        self.setRowCount(4)
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        i =0

        while i < 4:
            j = 0
            self.btn.append([])
            while j<4:
                self.btn[i].append(QPushButton())
                status = '正常'
                text =  '编号:00'+str(j+4*i)+'\r\n'+'运行区域:'+str(i)+'区\r\n'+'运行状态:'+status+'\r\n'+'运行时间:'+str(j+2*i)+'h'
                self.btn[i][j].setText(text)
                self.setCellWidget(i,j,self.btn[i][j])
                j =j+1
            i = i+1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyOnlineWidget()
    ex.show()
    sys.exit(app.exec_())