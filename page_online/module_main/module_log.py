from PyQt5.QtCore import QDateTime,QTimer
from PyQt5.QtWidgets import QTextBrowser, QFileDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from page_online.module_main.module_motor import MyMotor


class MyLog(QTextBrowser,MyMotor):
    def __init__(self,parent = None):
        super(MyLog,self).__init__(parent)
        self.initUi()


    def initUi(self):
        # self.timer=QTimer()
        # self.timer.timeout.connect(self.showTime)#这个通过调用槽函数来刷新时间
        self.setGeometry(QtCore.QRect(0, 0, 581, 261))


    def showTime(self):
        time=QDateTime.currentDateTime()#获取当前时间
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss ")#格式化一下时间
        if self.status =='停机':
            str= '['+timedisplay+']'+'已停机'
            # self.timer.stop()
        elif self.status=='故障':
            str = '['+timedisplay+']'+'运行'+self.status+\
                  '\r\n故障状态：' +self.status_fault+\
                  ' \r\n处理状态：待处理'
        else:
            str = '['+timedisplay+']'+'运行'+self.status
        self.append(str)
        self.cursor = self.textCursor()
        self.moveCursor(self.cursor.End)

    #
    # def startTimer(self):
    #     self.timer.start(1000)#每隔一秒刷新一次，这里设置为1000ms
    #
    # def stopTimer(self):
    #     self.status = '停机'

    def exportData(self):
        # 控件作用：打开文件资源管理器，获得你需要保存的文件名。
        # (注意：它不会帮你创建文件，只返回一个元组）
        # 元组第一项为你的文件路径（包括你给的文件名），第二项为该文件的类型。
        save_path, ok = QFileDialog.getSaveFileName(None, "日志导出",'.','*.txt')

        if save_path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.toPlainText())
            print('已保存！')


    def save_text(self):
        global save_path



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyLog()
    ex.show()
    sys.exit(app.exec_())