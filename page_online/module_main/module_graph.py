import numpy as np
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, \
    QGraphicsView
from PyQt5.QtCore import QTimer,QRect
import pandas as pd
from page_online.module_main.module_motor import MyMotor
class MyGraph(QGraphicsView,MyMotor):
    def __init__(self, mode =None,parent = None):
        super(MyGraph,self).__init__(parent)
        self.ia =[]
        self.ib=[]
        self.ic = []
        self.load =[]
        self.setupUi(mode)

    def setupUi(self,mode):
        self.setGeometry(QRect(0, 0, 581, 280))
        self.timer = QTimer(self)
        self.setPoltOption()
        if mode =='Load':
            self.importLoadData()
            self.setLoadPlot()
            self.timer.timeout.connect(self.plotLoadData)
            # self.startTimer()
        if mode=='Current':
            self.importCurrentData()
            self.setCurrentPlot()
            self.timer.timeout.connect(self.plotCurrentData)
            # self.startTimer()

    def setPoltOption(self):
        self.p = pg.PlotWidget(self)
        self.p.setBackground(None)
        self.p.setGeometry(QRect(0, 0, 581, 280))
        self.p.setXRange(0, 100)
        self.p.showGrid(x=False, y=False)


    def setCurrentPlot(self):
        self.p.setLabel(axis="left", text="电流/A")
        self.p.setLabel(axis="bottom", text="时间/s")
        self.p.addLegend()
        self.curve1 = self.p.plot(pen="r", name="ia")
        self.curve2 = self.p.plot(pen='g', name="ib")
        self.curve3 = self.p.plot(pen='b', name="ic")

    def setLoadPlot(self):
        self.p.setLabel(axis="left", text="转矩/N。M")
        self.p.setLabel(axis="bottom", text="时间/s")
        self.p.addLegend()
        self.curve1 = self.p.plot(pen="r", name="Torque")

    def importCurrentData(self):
        df = pd.read_csv(self.data_path+'/current.csv')
        df=df.drop(df.index[0])
        self.count = 0
        self.t = df['t'].values
        self.ia = df['ia'].values
        self.ib = df['ib'].values
        self.ic = df['ic'].values

    def importLoadData(self):
        df = pd.read_csv(self.data_path+'/torque.csv')
        df=df.drop(df.index[0])
        self.count = 0
        self.t = df['t'].values
        self.load = df['load'].values

    def plotCurrentData(self):
        self.count += 1
        if self.count == 1000:
            self.count = 0
        temp_t = self.t[0:self.count]
        temp_ia = self.ia[0:self.count]
        temp_ib = self.ib[0:self.count]
        temp_ic = self.ic[0:self.count]
        if self.count>100:
            self.p.setXRange(self.t[self.count-100],self.t[self.count])
        else:
            self.p.setXRange(self.t[0], self.t[self.count])
        self.curve1.setData(temp_t,temp_ia)
        self.curve2.setData(temp_t,temp_ib)
        self.curve3.setData(temp_t,temp_ic)

    def plotLoadData(self):
        self.count += 1
        if self.count == 1000:
            self.count = 0
        temp_t = self.t[0:self.count]
        temp_Load = self.load[0:self.count]
        if self.count>100:
            self.p.setXRange(self.t[self.count-100],self.t[self.count])
        else:
            self.p.setXRange(self.t[0], self.t[self.count])
        self.curve1.setData(temp_t,temp_Load)


    def startTimer(self):
        self.timer.start(100)#每隔一秒刷新一次，这里设置为1000ms

    def stopTimer(self):
        self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyGraph('Current')
    ex.show()
    sys.exit(app.exec_())
