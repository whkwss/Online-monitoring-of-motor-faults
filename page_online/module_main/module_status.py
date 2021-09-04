import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, \
    QGraphicsView
from PyQt5.QtCore import QTimer,QRect
import pandas as pd
from page_online.module_main.module_motor import MyMotor
from scipy.fftpack import fft
import pandas as pd
from matplotlib.pylab import mpl
import numpy as np    #进行具体的sum,count等计算时候要用到的
from os import walk
import matplotlib.pyplot as plt
import math
import os

import  matplotlib.pyplot as plt
import joblib
import numpy as np
import pandas as pd
from PIL import Image
from skimage.feature import hog

class MyFFT:
    def __init__(self,Fs,data_path):
        # 时间
        self.t = []
        self.ia = []
        self.ib = []
        self.ic = []
        self.fft_result = []
        self.data_path= data_path
        # 采样频率，默认1000Hz
        self.Fs=Fs

        self.analyseData()


    def analyseData(self):

        df = pd.read_csv(self.data_path+'/current.csv')
        df=df.drop(df.index[0])
        t = df['t'].values
        ia = df['ia'].values
        ib = df['ib'].values
        ic = df['ic'].values
        signals_list = [ia, ib, ic]
        for signal in signals_list:
            fft_result = self.FFT_half(signal,t)
            self.fft_result.append(fft_result)

        plt.plot(np.arange(len(self.fft_result[0])), self.fft_result[0], 'blue')

        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
        mpl.rcParams['axes.unicode_minus'] = False  # 显示负号
        plt.title('单边振幅谱(归一化)', fontsize=8, color='blue')
        fig = plt.gcf()
        fig.set_size_inches(10, 10)
        fig.savefig('page_online/datalog/current_FFT.png', dpi=100)
        plt.close()


    def FFT_half(self,signal,t):
        N=len(t)
        # 进行fft分解
        fft_y=fft(signal)
        # 取复数的绝对值，即复数的模(双边频谱)
        abs_y=np.abs(fft_y)
        # 归一化处理（双边频谱）
        gui_y=abs_y/N
        # 由于对称性，只取一半区间（单边频谱）
        gui_half_y = gui_y[range(int(N/2))]
        return gui_half_y

class MyStatus(QWidget,MyMotor):
    def __init__(self, mode =None,parent = None):
        super(MyStatus,self).__init__(parent)
        self.mode_list=['HOG_SVM','Iforest']

        self.mode = mode
        self.setupUi()
        # self.predictResult()


    def setupUi(self):
        self.setGeometry(QRect(0, 0, 281, 311))
        self.text_status = QtWidgets.QTextBrowser(self)
        self.text_status.setGeometry(QtCore.QRect(30, 240, 231, 61))
        self.text_status.setStyleSheet("border:none;")
        self.text_status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_status.setObjectName("text_status")
        self.lab_pic = QtWidgets.QLabel(self)
        self.lab_pic.setGeometry(QtCore.QRect(0, 20, 281, 211))
        self.lab_pic.setStyleSheet("border:none")
        self.lab_pic.setText("")
        pic = QtGui.QPixmap("page_online/datalog/current_HOG.png").scaled(200,200)
        self.lab_pic.setPixmap(pic)
        self.lab_pic.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.lab_pic.setObjectName("lab_pic")
        self.lab_pic_title = QtWidgets.QLabel(self)
        self.lab_pic_title.setGeometry(QtCore.QRect(0, 0, 281, 20))
        self.lab_pic_title.setStyleSheet("border:none;\n"
                                         "font: 9pt \"微软雅黑\";")
        self.lab_pic_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_pic_title.setObjectName("lab_pic_title")
        text = '编号：'+self.id+\
               '\r\n运行状态：'+self.status+\
               '\r\n故障类型：'+self.status_fault+\
                '\r\n故障情况：'+self.status_hold
        self.text_status.setText(text)
        self.lab_pic_title.setText("Park矢量图")
        self.timer = QTimer(self)

    def predictResult(self):
        if self.mode=='Iforest':
            clf = joblib.load('page_online/model/IFroest_train.model')
            myfft = MyFFT(1000, self.data_path)
            feat = [np.r_[myfft.fft_result[0], myfft.fft_result[1], myfft.fft_result[2]]]
            result = clf.predict(feat)
            if self.status != '停机':
                if result ==[-1]:
                    self.status = '故障'
                    self.status_fault='未知'
                    self.status_hold = '待处理'
                else:
                    self.status ='正常'
                    self.status_fault='正常'
                    self.status_hold = '无'
            pic = QtGui.QPixmap("page_online/datalog/current_FFT.png").scaled(200, 200)
            self.lab_pic.setPixmap(pic)
            self.lab_pic_title.setText("FFT单边频谱图")
            print(result)
        if self.mode == 'HOG_SVM':
            clf = joblib.load('page_online/model/HOG_SVM_train.model')
            self.plotPark()
            feat=self.getHOGFeat()
            result = clf.predict(feat)

            if  self.status !='停机':
                if result =='1':
                    self.status = '正常'
                    self.status_fault = '正常'
                    self.status_hold = '无'
                if result =='2':
                    self.status = '故障'
                    self.status_fault = '开路'
                    self.status_hold ='待处理'
                if result =='3':
                    self.status = '故障'
                    self.status_fault = '短路'
                    self.status_hold = '待处理'
            pic = QtGui.QPixmap("page_online/datalog/current_HOG.png").scaled(220, 220)
            self.lab_pic.setPixmap(pic)
            self.lab_pic_title.setText("Park矢量图")
        text = '编号：'+self.id+\
               '\r\n运行状态：'+self.status+\
               '\r\n故障类型：'+self.status_fault+\
                '\r\n故障情况：'+self.status_hold
        self.text_status.setText(text)



    def plotPark(self):
        data_path = self.data_path + '/current.csv'
        df = pd.read_csv(data_path)
        df = df.drop(df.index[0])
        t = df['t'].values
        ia = df['ia'].values
        ib = df['ib'].values
        ic = df['ic'].values

        id = ia * (math.sqrt(2) / math.sqrt(3)) - ib * (1 / math.sqrt(6)) \
             - ic * (1 / math.sqrt(6));
        iq = (ib - ic) * (1 / math.sqrt(2));
        plt.axis('equal')
        plt.plot(id, iq)
        my_x_ticks = np.arange(-75, 75, 25)
        my_y_ticks = np.arange(-75, 75, 25)
        plt.xticks(my_x_ticks)
        plt.yticks(my_y_ticks)
        fig = plt.gcf()
        fig.set_size_inches(10, 10)
        fig.savefig('page_online/datalog/current_HOG.png', dpi=100)
        plt.close()
    def getHOGFeat(self):
        im = Image.open("page_online/datalog/current_HOG.png")
        im = im.resize((256, 256), Image.ANTIALIAS)
        image = np.reshape(im, (256, 256, 4))
        gray = image[:, :, 0] * 0.2989 + image[:, :, 1] * 0.5870 + image[:, :, 2] * 0.1140
        gray = gray / 255.0
        fd = hog(gray, orientations=9, block_norm='L1', pixels_per_cell=[16, 16],
                 cells_per_block=[2, 2], visualize=False,
                 transform_sqrt=True)
        fd = np.concatenate((fd, [3]))
        data_test_feat = fd[:-1].reshape((1, -1)).astype(np.float64)
        return data_test_feat
    #
    # def plotFFT(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyStatus('Iforest')
    myWin.show()
    sys.exit(app.exec_())
