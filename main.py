# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMessageBox, QApplication, QInputDialog, QWidget

from face_detection import *
from recognizer import *
from trainner import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Face Recognition")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-image:url(./image/timg.jpg);")
        MainWindow.setWindowIcon(QtGui.QIcon('./image/tubiao.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 511, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        font_1 = QtGui.QFont()
        font_1.setFamily("Adobe Arabic")
        font_1.setPointSize(20)
        font_1.setBold(True)
        font_1.setWeight(75)
        font_2 = QtGui.QFont()
        font_2.setFamily("Adobe Arabic")
        font_2.setPointSize(16)
        font_2.setBold(True)
        font_2.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(0, 170, 255);\n"
"background:none;")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(100, 230, 300, 200))
        self.label_1.setObjectName("label")
        self.label_1.setFont(font_1)
        self.label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_1.setAcceptDrops(False)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet("color: red;\n"
                                 "background:none;border:2px solid lightblue")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 470, 180, 100))
        self.label_2.setObjectName("label")
        self.label_2.setFont(font_2)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(0, 255, 255);\n"
                                   "background:none;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 230, 161, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 18pt \"Adobe Arabic\";\n"
"color: rgb(0, 255, 255);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 310, 161, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 18pt \"Adobe Arabic\";\n"
"color: rgb(0, 255, 255);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 390, 161, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("font: 18pt \"Adobe Arabic\";\n"
"color: rgb(0, 255, 255);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Face Recognition"))
        self.label.setText(self._translate("MainWindow", "Face Recognition"))
        self.label_2.setText(self._translate("MainWindow", "Author:Jiao Pengbo\nDate:2019.03.11\nEmail:jpbzms@163.com"))
        self.pushButton.setText(self._translate("MainWindow", "采集信息"))
        self.pushButton_2.setText(self._translate("MainWindow", "训练分类器"))
        self.pushButton_3.setText(self._translate("MainWindow", "系统启用"))
        self.pushButton.clicked.connect(self.buttionCliked)
        self.pushButton_2.clicked.connect(self.buttionCliked_1)
        self.pushButton_3.clicked.connect(self.buttionCliked_2)

    # 采集人脸
    def buttionCliked(self):
        self.label_1.setText(self._translate("MainWindow", "正在准备人脸信息采集...\n如需退出请按‘q’键"))
        QApplication.processEvents()
        ex = App()
        print('======')
        self.label_1.setText(self._translate("MainWindow", "人脸信息采集完成！"))
        QApplication.processEvents()

    #训练分类器
    def buttionCliked_1(self):
        self.label_1.setText(self._translate("MainWindow", "正在训练人脸模型..."))
        QApplication.processEvents()
        print('正在训练人脸模型...')
        face, Ids = getImageand_labels('dataSet')
        recognizer.train(face, np.array(Ids))
        # 保存到数据到指定文件
        recognizer.save('./trainner/trainner.yml')
        print('已完成')
        self.label_1.setText(self._translate("MainWindow", "人脸模型训练成功！"))
        QApplication.processEvents()


    #识别系统开启
    def buttionCliked_2(self):
        self.label_1.setText(self._translate("MainWindow", "正在打开人脸识别系统...如\n需退出请按‘q’键"))
        QApplication.processEvents()
        recognizerFn()
        self.label_1.setText(self._translate("MainWindow", "人脸识别系统已关闭！"))
        QApplication.processEvents()


# 输入id弹框
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.getInteger()
        self.show()

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "input your faceID","intput your faceID:", 1, 0, 100, 1)
        if okPressed:
            faceDetection(i)
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())