# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 642)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget_title = QtWidgets.QWidget(self.centralWidget)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 1011, 100))
        self.widget_title.setStyleSheet("background-color:rgb(68,114,196)")
        self.widget_title.setObjectName("widget_title")
        self.lab_logo = QtWidgets.QLabel(self.widget_title)
        self.lab_logo.setGeometry(QtCore.QRect(0, 0, 300, 75))
        self.lab_logo.setText("")
        self.lab_logo.setPixmap(QtGui.QPixmap(":/newPrefix/resource/logo2.png"))
        self.lab_logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lab_logo.setObjectName("lab_logo")
        self.lab_divide = QtWidgets.QLabel(self.widget_title)
        self.lab_divide.setGeometry(QtCore.QRect(0, 75, 1024, 25))
        self.lab_divide.setStyleSheet("background-color:rgb(47, 85, 151)")
        self.lab_divide.setText("")
        self.lab_divide.setObjectName("lab_divide")
        self.lab_title = QtWidgets.QLabel(self.widget_title)
        self.lab_title.setGeometry(QtCore.QRect(300, 0, 351, 75))
        self.lab_title.setStyleSheet("font: 18pt \"微软雅黑\" ;color:white;")
        self.lab_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_title.setObjectName("lab_title")
        self.widget_2 = QtWidgets.QWidget(self.widget_title)
        self.widget_2.setGeometry(QtCore.QRect(570, 0, 374, 75))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.btn_online = QtWidgets.QPushButton(self.widget_2)
        self.btn_online.setGeometry(QtCore.QRect(90, 10, 60, 60))
        self.btn_online.setStyleSheet("")
        self.btn_online.setObjectName("btn_online")
        self.btn_video = QtWidgets.QPushButton(self.widget_2)
        self.btn_video.setGeometry(QtCore.QRect(160, 10, 60, 60))
        self.btn_video.setObjectName("btn_video")
        self.btn_alarm = QtWidgets.QPushButton(self.widget_2)
        self.btn_alarm.setGeometry(QtCore.QRect(230, 10, 60, 60))
        self.btn_alarm.setIconSize(QtCore.QSize(50, 50))
        self.btn_alarm.setObjectName("btn_alarm")
        self.btn_check = QtWidgets.QPushButton(self.widget_2)
        self.btn_check.setGeometry(QtCore.QRect(300, 10, 60, 60))
        self.btn_check.setObjectName("btn_check")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget_main.setGeometry(QtCore.QRect(150, 100, 861, 540))
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.widget_main = QtWidgets.QWidget()
        self.widget_main.setObjectName("widget_main")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_main)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 581, 231))
        self.textBrowser.setStyleSheet("     QPushButton{\n"
"     background-color:rgba(112,173,71,200);\n"
"     border-style:outset;\n"
"     border-width:4px;\n"
"     border-radius:10px;\n"
"     border-color:rgba(255,255,255,30);\n"
"     font:bold 20px;\n"
"     color:rgba(0,0,0,200);\n"
"     padding:6px;\n"
"     }\n"
"\n"
"     QPushButton:pressed{\n"
"     background-color:rgba(112,173,71,200);\n"
"     border-color:rgba(255,255,255,30);\n"
"     border-style:inset;\n"
"     color:rgba(0,0,0,200);\n"
"     }\n"
"\n"
"     QPushButton:hover{\n"
"     background-color:rgba(112,173,71,200);\n"
"     border-color:rgba(255,255,255,200);\n"
"     color:rgba(0,0,0,100);\n"
"     }")
        self.textBrowser.setObjectName("textBrowser")
        self.widget_status = QtWidgets.QWidget(self.widget_main)
        self.widget_status.setGeometry(QtCore.QRect(580, 0, 281, 311))
        self.widget_status.setStyleSheet("border:1px solid rgb(0,0,0) ")
        self.widget_status.setObjectName("widget_status")
        self.text_status = QtWidgets.QTextBrowser(self.widget_status)
        self.text_status.setGeometry(QtCore.QRect(30, 240, 231, 61))
        self.text_status.setStyleSheet("border:none;")
        self.text_status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_status.setObjectName("text_status")
        self.lab_pic = QtWidgets.QLabel(self.widget_status)
        self.lab_pic.setGeometry(QtCore.QRect(0, 20, 281, 211))
        self.lab_pic.setStyleSheet("border:none")
        self.lab_pic.setText("")
        self.lab_pic.setPixmap(QtGui.QPixmap(":/newPrefix/resource/open_Y22.png"))
        self.lab_pic.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lab_pic.setObjectName("lab_pic")
        self.lab_pic_title = QtWidgets.QLabel(self.widget_status)
        self.lab_pic_title.setGeometry(QtCore.QRect(0, 0, 281, 20))
        self.lab_pic_title.setStyleSheet("border:none;\n"
"font: 9pt \"微软雅黑\";")
        self.lab_pic_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_pic_title.setObjectName("lab_pic_title")
        self.widget_button = QtWidgets.QWidget(self.widget_main)
        self.widget_button.setGeometry(QtCore.QRect(580, 310, 281, 231))
        self.widget_button.setStyleSheet("border:1px solid rgb(0,0,0) ")
        self.widget_button.setObjectName("widget_button")
        self.btn_importlog = QtWidgets.QPushButton(self.widget_button)
        self.btn_importlog.setGeometry(QtCore.QRect(60, 171, 158, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_importlog.sizePolicy().hasHeightForWidth())
        self.btn_importlog.setSizePolicy(sizePolicy)
        self.btn_importlog.setStyleSheet("     QPushButton{\n"
"     background-color:rgba(68,114,196);\n"
"     border-style:outset;\n"
"     border-width:4px;\n"
"     border-radius:10px;\n"
"     border-color:rgba(255,255,255,30);\n"
"     font:bold 20px;\n"
"     color:rgba(0,0,0,200);\n"
"     padding:6px;\n"
"     }\n"
"\n"
"     QPushButton:pressed{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,30);\n"
"     border-style:inset;\n"
"     color:rgba(0,0,0,200);\n"
"     }\n"
"\n"
"     QPushButton:hover{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,200);\n"
"     color:rgba(0,0,0,100);\n"
"     }")
        self.btn_importlog.setObjectName("btn_importlog")
        self.btn_start = QtWidgets.QPushButton(self.widget_button)
        self.btn_start.setGeometry(QtCore.QRect(60, 10, 158, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setStyleSheet("     QPushButton{\n"
"     background-color:rgba(68,114,196);\n"
"     border-style:outset;\n"
"     border-width:4px;\n"
"     border-radius:10px;\n"
"     border-color:rgba(255,255,255,30);\n"
"     font:bold 20px;\n"
"     color:rgba(0,0,0,200);\n"
"     padding:6px;\n"
"     }\n"
"\n"
"     QPushButton:pressed{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,30);\n"
"     border-style:inset;\n"
"     color:rgba(0,0,0,200);\n"
"     }\n"
"\n"
"     QPushButton:hover{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,200);\n"
"     color:rgba(0,0,0,100);\n"
"     }")
        self.btn_start.setObjectName("btn_start")
        self.btn_faultdeal = QtWidgets.QPushButton(self.widget_button)
        self.btn_faultdeal.setGeometry(QtCore.QRect(60, 118, 158, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_faultdeal.sizePolicy().hasHeightForWidth())
        self.btn_faultdeal.setSizePolicy(sizePolicy)
        self.btn_faultdeal.setStyleSheet("     QPushButton{\n"
"     background-color:rgba(68,114,196);\n"
"     border-style:outset;\n"
"     border-width:4px;\n"
"     border-radius:10px;\n"
"     border-color:rgba(255,255,255,30);\n"
"     font:bold 20px;\n"
"     color:rgba(0,0,0,200);\n"
"     padding:6px;\n"
"     }\n"
"\n"
"     QPushButton:pressed{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,30);\n"
"     border-style:inset;\n"
"     color:rgba(0,0,0,200);\n"
"     }\n"
"\n"
"     QPushButton:hover{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,200);\n"
"     color:rgba(0,0,0,100);\n"
"     }")
        self.btn_faultdeal.setObjectName("btn_faultdeal")
        self.btn_stop = QtWidgets.QPushButton(self.widget_button)
        self.btn_stop.setGeometry(QtCore.QRect(60, 64, 158, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setStyleSheet("     QPushButton{\n"
"     background-color:rgba(68,114,196);\n"
"     border-style:outset;\n"
"     border-width:4px;\n"
"     border-radius:10px;\n"
"     border-color:rgba(255,255,255,30);\n"
"     font:bold 20px;\n"
"     color:rgba(0,0,0,200);\n"
"     padding:6px;\n"
"     }\n"
"\n"
"     QPushButton:pressed{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,30);\n"
"     border-style:inset;\n"
"     color:rgba(0,0,0,200);\n"
"     }\n"
"\n"
"     QPushButton:hover{\n"
"     background-color:rgba(68,114,196);\n"
"     border-color:rgba(255,255,255,200);\n"
"     color:rgba(0,0,0,100);\n"
"     }")
        self.btn_stop.setObjectName("btn_stop")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_main)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.widget_current = QtWidgets.QWidget()
        self.widget_current.setObjectName("widget_current")
        self.tabWidget.addTab(self.widget_current, "")
        self.widget_voltage = QtWidgets.QWidget()
        self.widget_voltage.setObjectName("widget_voltage")
        self.tabWidget.addTab(self.widget_voltage, "")
        self.widget_load = QtWidgets.QWidget()
        self.widget_load.setObjectName("widget_load")
        self.tabWidget.addTab(self.widget_load, "")
        self.widget_temp = QtWidgets.QWidget()
        self.widget_temp.setObjectName("widget_temp")
        self.tabWidget.addTab(self.widget_temp, "")
        self.stackedWidget_main.addWidget(self.widget_main)
        self.widget_alarm = QtWidgets.QWidget()
        self.widget_alarm.setObjectName("widget_alarm")
        self.table_alarm = QtWidgets.QTableWidget(self.widget_alarm)
        self.table_alarm.setGeometry(QtCore.QRect(0, 0, 861, 541))
        self.table_alarm.setAlternatingRowColors(True)
        self.table_alarm.setRowCount(20)
        self.table_alarm.setColumnCount(4)
        self.table_alarm.setObjectName("table_alarm")
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alarm.setItem(3, 3, item)
        self.table_alarm.horizontalHeader().setVisible(False)
        self.table_alarm.horizontalHeader().setCascadingSectionResizes(True)
        self.table_alarm.horizontalHeader().setDefaultSectionSize(200)
        self.table_alarm.horizontalHeader().setHighlightSections(True)
        self.table_alarm.horizontalHeader().setSortIndicatorShown(False)
        self.table_alarm.horizontalHeader().setStretchLastSection(False)
        self.table_alarm.verticalHeader().setVisible(False)
        self.table_alarm.verticalHeader().setCascadingSectionResizes(True)
        self.table_alarm.verticalHeader().setStretchLastSection(False)
        self.stackedWidget_main.addWidget(self.widget_alarm)
        self.widget_video = QtWidgets.QWidget()
        self.widget_video.setObjectName("widget_video")
        self.stackedWidget_main.addWidget(self.widget_video)
        self.widget_online = QtWidgets.QWidget()
        self.widget_online.setObjectName("widget_online")
        self.stackedWidget_main.addWidget(self.widget_online)
        self.widget_check = QtWidgets.QWidget()
        self.widget_check.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.widget_check.setObjectName("widget_check")
        self.label = QtWidgets.QLabel(self.widget_check)
        self.label.setGeometry(QtCore.QRect(0, 0, 921, 51))
        self.label.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"background-color:rgb(212, 212, 212);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_check)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 531, 51))
        self.label_2.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"background-color:none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widget_check)
        self.label_6.setGeometry(QtCore.QRect(0, 70, 851, 51))
        self.label_6.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"text-decoration:underline;\n"
"background-color:none;\n"
"\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_check)
        self.label_7.setGeometry(QtCore.QRect(0, 130, 851, 51))
        self.label_7.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"text-decoration:underline;\n"
"background-color:none;\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.widget_check)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 531, 51))
        self.label_3.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"background-color:none;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_check)
        self.label_4.setGeometry(QtCore.QRect(0, 170, 531, 51))
        self.label_4.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"background-color:none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.widget_check)
        self.label_8.setGeometry(QtCore.QRect(-20, 190, 851, 51))
        self.label_8.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"text-decoration:underline;\n"
"background-color:none;\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_check)
        self.label_9.setGeometry(QtCore.QRect(-20, 250, 851, 51))
        self.label_9.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"text-decoration:underline;\n"
"background-color:none;\n"
"\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.widget_check)
        self.label_5.setGeometry(QtCore.QRect(0, 230, 531, 51))
        self.label_5.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"color: rgb(47, 85, 151);\n"
"background-color:none;\n"
"")
        self.label_5.setObjectName("label_5")
        self.stackedWidget_main.addWidget(self.widget_check)
        self.widget_tree = QtWidgets.QTreeWidget(self.centralWidget)
        self.widget_tree.setGeometry(QtCore.QRect(0, 100, 151, 541))
        self.widget_tree.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_tree.setFrameShadow(QtWidgets.QFrame.Plain)
        self.widget_tree.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.widget_tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.widget_tree.setTextElideMode(QtCore.Qt.ElideRight)
        self.widget_tree.setAutoExpandDelay(0)
        self.widget_tree.setItemsExpandable(True)
        self.widget_tree.setAllColumnsShowFocus(True)
        self.widget_tree.setObjectName("widget_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.widget_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.widget_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.widget_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.widget_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.widget_tree.header().setCascadingSectionResizes(False)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_title.setText(_translate("MainWindow", "电机在线监测系统"))
        self.btn_online.setText(_translate("MainWindow", "在线监控"))
        self.btn_video.setText(_translate("MainWindow", "视频监控"))
        self.btn_alarm.setText(_translate("MainWindow", "报警监控"))
        self.btn_check.setText(_translate("MainWindow", "检修管理"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">运行日志：</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:00:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">运行正常</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:01:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">运行正常</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:02:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">运行正常</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:03:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">运行正常</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:05:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">检测到故障，待处理</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:06:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">已停机</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:07:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">已停机</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:08:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">已停机</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:09:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">已停机</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#000000;\">[20:10:00]</span><span style=\" font-family:\'等线\'; font-size:12pt; color:#000000;\">已停机</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p></body></html>"))
        self.text_status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; color:#000000;\">编号：</span><span style=\" font-family:\'Calibri\'; color:#000000;\">001</span><span style=\" font-family:\'SimSun\';\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; color:#000000;\">运行状态：运行故障</span><span style=\" font-family:\'SimSun\';\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; color:#000000;\">故障类型：断路</span><span style=\" font-family:\'SimSun\';\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; color:#000000;\">处理情况：待处理</span><span style=\" font-family:\'SimSun\';\"> </span></p></body></html>"))
        self.lab_pic_title.setText(_translate("MainWindow", "  "))
        self.btn_importlog.setText(_translate("MainWindow", "日志导出"))
        self.btn_start.setText(_translate("MainWindow", "启动"))
        self.btn_faultdeal.setText(_translate("MainWindow", "故障处理"))
        self.btn_stop.setText(_translate("MainWindow", "停机"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_current), _translate("MainWindow", "电流"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_voltage), _translate("MainWindow", "电压"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_load), _translate("MainWindow", "负载"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_temp), _translate("MainWindow", "温度"))
        self.table_alarm.setSortingEnabled(False)
        item = self.table_alarm.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "报警ID"))
        item = self.table_alarm.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "报警地点"))
        item = self.table_alarm.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "报警原因"))
        item = self.table_alarm.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "处理状态"))
        __sortingEnabled = self.table_alarm.isSortingEnabled()
        self.table_alarm.setSortingEnabled(False)
        item = self.table_alarm.item(0, 0)
        item.setText(_translate("MainWindow", "005"))
        item = self.table_alarm.item(0, 1)
        item.setText(_translate("MainWindow", "2区"))
        item = self.table_alarm.item(0, 2)
        item.setText(_translate("MainWindow", "短路"))
        item = self.table_alarm.item(0, 3)
        item.setText(_translate("MainWindow", "已处理"))
        item = self.table_alarm.item(1, 0)
        item.setText(_translate("MainWindow", "004"))
        item = self.table_alarm.item(1, 1)
        item.setText(_translate("MainWindow", "1区"))
        item = self.table_alarm.item(1, 2)
        item.setText(_translate("MainWindow", "停机"))
        item = self.table_alarm.item(1, 3)
        item.setText(_translate("MainWindow", "未处理"))
        item = self.table_alarm.item(2, 0)
        item.setText(_translate("MainWindow", "007"))
        item = self.table_alarm.item(2, 1)
        item.setText(_translate("MainWindow", "4区"))
        item = self.table_alarm.item(2, 2)
        item.setText(_translate("MainWindow", "未知"))
        item = self.table_alarm.item(2, 3)
        item.setText(_translate("MainWindow", "未处理"))
        item = self.table_alarm.item(3, 0)
        item.setText(_translate("MainWindow", "018"))
        item = self.table_alarm.item(3, 1)
        item.setText(_translate("MainWindow", "8区"))
        item = self.table_alarm.item(3, 2)
        item.setText(_translate("MainWindow", "未知"))
        item = self.table_alarm.item(3, 3)
        item.setText(_translate("MainWindow", "未处理"))
        self.table_alarm.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "当前待处理事项"))
        self.label_2.setText(_translate("MainWindow", "当前需操作设备维修处理的记录数为2条"))
        self.label_3.setText(_translate("MainWindow", "当前需操作设备维修处理的记录数为2条"))
        self.label_4.setText(_translate("MainWindow", "当前需操作设备二级维护的记录数为1条"))
        self.label_5.setText(_translate("MainWindow", "当前需操作设备润滑补油的记录数为1条"))
        self.widget_tree.headerItem().setText(0, _translate("MainWindow", "电机在线检测"))
        __sortingEnabled = self.widget_tree.isSortingEnabled()
        self.widget_tree.setSortingEnabled(False)
        self.widget_tree.topLevelItem(0).setText(0, _translate("MainWindow", "1区"))
        self.widget_tree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "001"))
        self.widget_tree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "002"))
        self.widget_tree.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "003"))
        self.widget_tree.topLevelItem(1).setText(0, _translate("MainWindow", "2区"))
        self.widget_tree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "004"))
        self.widget_tree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "005"))
        self.widget_tree.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "006"))
        self.widget_tree.topLevelItem(2).setText(0, _translate("MainWindow", "3区"))
        self.widget_tree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "007"))
        self.widget_tree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "008"))
        self.widget_tree.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "009"))
        self.widget_tree.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "010"))
        self.widget_tree.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "011"))
        self.widget_tree.topLevelItem(3).setText(0, _translate("MainWindow", "4区"))
        self.widget_tree.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "012"))
        self.widget_tree.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "013"))
        self.widget_tree.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "014"))
        self.widget_tree.topLevelItem(3).child(3).setText(0, _translate("MainWindow", "015"))
        self.widget_tree.topLevelItem(3).child(4).setText(0, _translate("MainWindow", "016"))
        self.widget_tree.setSortingEnabled(__sortingEnabled)
import myResource_rc
