# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caculation.ui'
#
# Created: Wed Nov 20 16:34:16 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 408)
        Dialog.setMinimumSize(QtCore.QSize(312, 408))
        Dialog.setMaximumSize(QtCore.QSize(312, 408))
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(50, 140, 40, 40))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 140, 40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 140, 40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus = QtGui.QPushButton(Dialog)
        self.pushButton_plus.setGeometry(QtCore.QRect(230, 140, 40, 40))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 200, 40, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_minus = QtGui.QPushButton(Dialog)
        self.pushButton_minus.setGeometry(QtCore.QRect(230, 200, 40, 40))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 200, 40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 200, 40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 260, 40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 260, 40, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_multi = QtGui.QPushButton(Dialog)
        self.pushButton_multi.setGeometry(QtCore.QRect(230, 260, 40, 40))
        self.pushButton_multi.setObjectName("pushButton_multi")
        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 260, 40, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_point = QtGui.QPushButton(Dialog)
        self.pushButton_point.setGeometry(QtCore.QRect(110, 320, 40, 40))
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_divi = QtGui.QPushButton(Dialog)
        self.pushButton_divi.setGeometry(QtCore.QRect(170, 320, 40, 40))
        self.pushButton_divi.setObjectName("pushButton_divi")
        self.pushButton_0 = QtGui.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(50, 320, 41, 41))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtGui.QPushButton(Dialog)
        self.pushButton_equal.setGeometry(QtCore.QRect(230, 320, 40, 40))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 221, 81))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton1.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_minus.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_multi.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_point.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_divi.setText(QtGui.QApplication.translate("Dialog", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_0.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_equal.setText(QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))

