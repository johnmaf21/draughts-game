# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructionsPage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_instructionsPage(object):
    def setupUi(self, instructionsPage):
        instructionsPage.setObjectName(_fromUtf8("instructionsPage"))
        instructionsPage.resize(640, 480)
        self.centralwidget = QtGui.QWidget(instructionsPage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pg9TitleLbl = QtGui.QLabel(self.centralwidget)
        self.pg9TitleLbl.setGeometry(QtCore.QRect(210, 40, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pg9TitleLbl.setFont(font)
        self.pg9TitleLbl.setObjectName(_fromUtf8("pg9TitleLbl"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(270, 360, 101, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.instructionsLbl = QtGui.QLabel(self.centralwidget)
        self.instructionsLbl.setGeometry(QtCore.QRect(110, 110, 421, 231))
        self.instructionsLbl.setObjectName(_fromUtf8("instructionsLbl"))
        instructionsPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(instructionsPage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        instructionsPage.setStatusBar(self.statusbar)

        self.retranslateUi(instructionsPage)
        QtCore.QMetaObject.connectSlotsByName(instructionsPage)

    def retranslateUi(self, instructionsPage):
        instructionsPage.setWindowTitle(_translate("instructionsPage", "MainWindow", None))
        self.pg9TitleLbl.setText(_translate("instructionsPage", "Instructions", None))
        self.startButton.setText(_translate("instructionsPage", "Start", None))
        self.instructionsLbl.setText(_translate("instructionsPage", "TextLabel", None))

