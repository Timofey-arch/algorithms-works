# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        ErrorWindow.setObjectName("ErrorWindow")
        ErrorWindow.resize(400, 300)
        ErrorWindow.setMinimumSize(QtCore.QSize(400, 300))
        ErrorWindow.setMaximumSize(QtCore.QSize(400, 300))
        ErrorWindow.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"")
        self.ErrorPicture = QtWidgets.QLabel(ErrorWindow)
        self.ErrorPicture.setGeometry(QtCore.QRect(110, 10, 170, 170))
        self.ErrorPicture.setMinimumSize(QtCore.QSize(170, 170))
        self.ErrorPicture.setText("")
        self.ErrorPicture.setPixmap(QtGui.QPixmap("SpotiFuckButtonsImages/cross.png"))
        self.ErrorPicture.setScaledContents(True)
        self.ErrorPicture.setObjectName("ErrorPicture")
        self.OopsError = QtWidgets.QLabel(ErrorWindow)
        self.OopsError.setGeometry(QtCore.QRect(110, 180, 171, 20))
        self.OopsError.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";")
        self.OopsError.setObjectName("OopsError")
        self.ErrorCode = QtWidgets.QLabel(ErrorWindow)
        self.ErrorCode.setGeometry(QtCore.QRect(10, 200, 381, 31))
        self.ErrorCode.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";")
        self.ErrorCode.setText("")
        self.ErrorCode.setObjectName("ErrorCode")
        self.Ok = QtWidgets.QPushButton(ErrorWindow)
        self.Ok.setGeometry(QtCore.QRect(290, 250, 93, 28))
        self.Ok.setObjectName("Ok")

        self.retranslateUi(ErrorWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindow)

    def retranslateUi(self, ErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindow.setWindowTitle(_translate("ErrorWindow", "Dialog"))
        self.OopsError.setText(_translate("ErrorWindow", "OOPS...ERROR"))
        self.Ok.setText(_translate("ErrorWindow", "Ok"))
