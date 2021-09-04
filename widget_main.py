# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui.py'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import *
from page_online.module_main.module_graph import MyGraph
from page_online.module_main.module_status import MyStatus
from page_online.module_main.module_log import MyLog
from page_online.widget_online import MyOnlineWidget
from page_video.widget_video import MyVideoWidget

class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置视频监控页面
        self.pic_video =MyVideoWidget(self.widget_video)

        # self.pic_video.setStyleSheet('background-image: url(resource/video.jpg);')
        # self.pic_video.setWindowIconText('111')
        # 将在线监测的所有界面连接到主界面
        self.table_online = MyOnlineWidget(self.widget_online)
        for list in self.table_online.btn:
            for btn in list:
                btn.clicked.connect(self.showMainWindow)
        # 设置当前页面为在线监测
        self.stackedWidget_main.setCurrentIndex(3)

        # 设置主页面的图表区
        self.tabWidget.setCurrentIndex(0)
        self.graph_current =MyGraph('Current',self.widget_current)
        self.graph_voltage = MyGraph('Current',self.widget_voltage)
        self.graph_load = MyGraph('Load',self.widget_load)
        self.graph_temp = MyGraph('Load',self.widget_temp)
        # 设置主页面的运行日志区
        self.log =MyLog(self.textBrowser)
        # 设置主页面的状态显示
        self.status_show =MyStatus('Iforest',self.widget_status)
        # self.status_show =MyStatus('HOG_SVM',self.widget_status)

        # 设置按钮的信号与槽
        self.myBtnSet()
    def runMotor(self):
        self.log.status =  self.status_show.status
        self.log.status_fault=  self.status_show.status_fault
        self.log.status_hold = self.status_show.status_hold
        self.log.showTime()
        self.status_show.predictResult()

    def startMotor(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "page_online/data")
        self.status_show.status = '正常'
        self.status_show.data_path = directory

        self.graph_current.data_path = directory
        self.graph_load.data_path = directory
        self.graph_voltage.data_path = directory
        self.graph_temp.data_path = directory
        self.timer.start(1000)

    def stopMotor(self):
        self.status_show.status = '停机'
        self.log.status = self.status_show.status
        # self.timer.stop()

    def myBtnSet(self):
        # 为启动设定定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.runMotor)
        # 设置界面切换按钮
        self.btn_alarm.clicked.connect(self.showAlarm)
        self.btn_check.clicked.connect(self.showCheck)
        self.btn_video.clicked.connect(self.showVideo)
        self.btn_online.clicked.connect(self.showOnline)

        # 设置数据处理按钮
        self.btn_faultdeal.clicked.connect(self.faultDeal)
        self.btn_importlog.clicked.connect(self.log.exportData)

        # 设置电机启动
        self.btn_start.clicked.connect(self.startMotor)
        self.btn_start.clicked.connect(self.graph_current.startTimer)
        self.btn_start.clicked.connect(self.graph_load.startTimer)

        # 设置电机停止
        self.btn_stop.clicked.connect(self.stopMotor)
        self.btn_stop.clicked.connect(self.graph_current.stopTimer)
        self.btn_stop.clicked.connect(self.graph_load.stopTimer)


    def showAlarm(self):
        self.stackedWidget_main.setCurrentIndex(1)
    def showCheck(self):
        self.stackedWidget_main.setCurrentIndex(4)
    def showVideo(self):
        self.stackedWidget_main.setCurrentIndex(2)
    def showMainWindow(self):
        self.stackedWidget_main.setCurrentIndex(0)
    def showOnline(self):
        self.stackedWidget_main.setCurrentIndex(3)
    def faultDeal(self):
        i=0




if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

