# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1stBoardColour.ui'
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

class Ui_BoardColour1Page(object):
    def setupUi(self, BoardColour1Page):
        BoardColour1Page.setObjectName(_fromUtf8("BoardColour1Page"))
        BoardColour1Page.resize(640, 480)
        self.centralwidget = QtGui.QWidget(BoardColour1Page)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pg8aTitleLbl = QtGui.QLabel(self.centralwidget)
        self.pg8aTitleLbl.setGeometry(QtCore.QRect(200, 40, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pg8aTitleLbl.setFont(font)
        self.pg8aTitleLbl.setObjectName(_fromUtf8("pg8aTitleLbl"))
        self.blackButton = QtGui.QPushButton(self.centralwidget)
        self.blackButton.setGeometry(QtCore.QRect(90, 130, 51, 51))
        self.blackButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.blackButton.setText(_fromUtf8(""))
        self.blackButton.setObjectName(_fromUtf8("blackButton"))
        self.whiteButton = QtGui.QPushButton(self.centralwidget)
        self.whiteButton.setGeometry(QtCore.QRect(160, 130, 51, 51))
        self.whiteButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.whiteButton.setText(_fromUtf8(""))
        self.whiteButton.setObjectName(_fromUtf8("whiteButton"))
        self.pinkButton = QtGui.QPushButton(self.centralwidget)
        self.pinkButton.setGeometry(QtCore.QRect(230, 130, 51, 51))
        self.pinkButton.setStyleSheet(_fromUtf8("background-color: rgb(255,51,204);"))
        self.pinkButton.setText(_fromUtf8(""))
        self.pinkButton.setObjectName(_fromUtf8("pinkButton"))
        self.darkGreenButton = QtGui.QPushButton(self.centralwidget)
        self.darkGreenButton.setGeometry(QtCore.QRect(300, 130, 51, 51))
        self.darkGreenButton.setStyleSheet(_fromUtf8("background-color: rgb(0,102,0);"))
        self.darkGreenButton.setText(_fromUtf8(""))
        self.darkGreenButton.setObjectName(_fromUtf8("darkGreenButton"))
        self.greenButton = QtGui.QPushButton(self.centralwidget)
        self.greenButton.setGeometry(QtCore.QRect(90, 210, 51, 51))
        self.greenButton.setStyleSheet(_fromUtf8("background-color: rgb(0,255,0);"))
        self.greenButton.setText(_fromUtf8(""))
        self.greenButton.setObjectName(_fromUtf8("greenButton"))
        self.purpleButton = QtGui.QPushButton(self.centralwidget)
        self.purpleButton.setGeometry(QtCore.QRect(160, 210, 51, 51))
        self.purpleButton.setStyleSheet(_fromUtf8("background-color: rgb(153,51,255);"))
        self.purpleButton.setText(_fromUtf8(""))
        self.purpleButton.setObjectName(_fromUtf8("purpleButton"))
        self.blueButton = QtGui.QPushButton(self.centralwidget)
        self.blueButton.setGeometry(QtCore.QRect(230, 210, 51, 51))
        self.blueButton.setStyleSheet(_fromUtf8("background-color: rgb(0,102,255);"))
        self.blueButton.setText(_fromUtf8(""))
        self.blueButton.setObjectName(_fromUtf8("blueButton"))
        self.lightBlueButton = QtGui.QPushButton(self.centralwidget)
        self.lightBlueButton.setGeometry(QtCore.QRect(300, 210, 51, 51))
        self.lightBlueButton.setStyleSheet(_fromUtf8("background-color: rgb(51,204,255);"))
        self.lightBlueButton.setText(_fromUtf8(""))
        self.lightBlueButton.setObjectName(_fromUtf8("lightBlueButton"))
        self.yellowButton = QtGui.QPushButton(self.centralwidget)
        self.yellowButton.setGeometry(QtCore.QRect(90, 290, 51, 51))
        self.yellowButton.setStyleSheet(_fromUtf8("background-color: rgb(255,204,0);"))
        self.yellowButton.setText(_fromUtf8(""))
        self.yellowButton.setObjectName(_fromUtf8("yellowButton"))
        self.brownButton = QtGui.QPushButton(self.centralwidget)
        self.brownButton.setGeometry(QtCore.QRect(160, 290, 51, 51))
        self.brownButton.setStyleSheet(_fromUtf8("background-color: rgb(153,51,0);"))
        self.brownButton.setText(_fromUtf8(""))
        self.brownButton.setObjectName(_fromUtf8("brownButton"))
        self.greyButton = QtGui.QPushButton(self.centralwidget)
        self.greyButton.setGeometry(QtCore.QRect(230, 290, 51, 51))
        self.greyButton.setStyleSheet(_fromUtf8("background-color: rgb(179,179,179);"))
        self.greyButton.setText(_fromUtf8(""))
        self.greyButton.setObjectName(_fromUtf8("greyButton"))
        self.greenBlueButton = QtGui.QPushButton(self.centralwidget)
        self.greenBlueButton.setGeometry(QtCore.QRect(300, 290, 51, 51))
        self.greenBlueButton.setStyleSheet(_fromUtf8("background-color: rgb(0,102,102);"))
        self.greenBlueButton.setText(_fromUtf8(""))
        self.greenBlueButton.setObjectName(_fromUtf8("greenBlueButton"))
        self.chosenColourLbl = QtGui.QLabel(self.centralwidget)
        self.chosenColourLbl.setGeometry(QtCore.QRect(440, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chosenColourLbl.setFont(font)
        self.chosenColourLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosenColourLbl.setObjectName(_fromUtf8("chosenColourLbl"))
        self.chosenColourDisplay = QtGui.QLabel(self.centralwidget)
        self.chosenColourDisplay.setGeometry(QtCore.QRect(420, 150, 161, 161))
        self.chosenColourDisplay.setStyleSheet(_fromUtf8("border:5px solid;\n"
"\n"
""))
        self.chosenColourDisplay.setText(_fromUtf8(""))
        self.chosenColourDisplay.setObjectName(_fromUtf8("chosenColourDisplay"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(454, 352, 91, 31))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 180, 61, 121))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        BoardColour1Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BoardColour1Page)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BoardColour1Page.setStatusBar(self.statusbar)

        self.retranslateUi(BoardColour1Page)
        QtCore.QMetaObject.connectSlotsByName(BoardColour1Page)

    def retranslateUi(self, BoardColour1Page):
        BoardColour1Page.setWindowTitle(_translate("BoardColour1Page", "MainWindow", None))
        self.pg8aTitleLbl.setText(_translate("BoardColour1Page", "Board Colour 1", None))
        self.chosenColourLbl.setText(_translate("BoardColour1Page", "Chosen Colour", None))
        self.saveButton.setText(_translate("BoardColour1Page", "Save", None))
        self.backButton.setText(_translate("BoardColour1Page", "Back", None))

