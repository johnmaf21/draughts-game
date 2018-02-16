# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2ndHomePage.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pg1TitleLbl = QtGui.QLabel(self.centralwidget)
        self.pg1TitleLbl.setGeometry(QtCore.QRect(230, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pg1TitleLbl.setFont(font)
        self.pg1TitleLbl.setObjectName(_fromUtf8("pg1TitleLbl"))
        self.player1Link = QtGui.QPushButton(self.centralwidget)
        self.player1Link.setGeometry(QtCore.QRect(50, 150, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player1Link.setFont(font)
        self.player1Link.setAutoFillBackground(False)
        self.player1Link.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(220,0,0);\n"
" }"))
        self.player1Link.setFlat(False)
        self.player1Link.setObjectName(_fromUtf8("player1Link"))
        self.twoPlayerLink = QtGui.QPushButton(self.centralwidget)
        self.twoPlayerLink.setGeometry(QtCore.QRect(50, 220, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.twoPlayerLink.setFont(font)
        self.twoPlayerLink.setAutoFillBackground(False)
        self.twoPlayerLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(0, 0, 0);\n"
" color:rgb(225,225,225);\n"
" }"))
        self.twoPlayerLink.setFlat(False)
        self.twoPlayerLink.setObjectName(_fromUtf8("twoPlayerLink"))
        self.gameOptionsLink = QtGui.QPushButton(self.centralwidget)
        self.gameOptionsLink.setGeometry(QtCore.QRect(50, 290, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gameOptionsLink.setFont(font)
        self.gameOptionsLink.setAutoFillBackground(False)
        self.gameOptionsLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color:rgb(220,0,0) ;\n"
" }"))
        self.gameOptionsLink.setFlat(False)
        self.gameOptionsLink.setObjectName(_fromUtf8("gameOptionsLink"))
        self.miniGameLink = QtGui.QPushButton(self.centralwidget)
        self.miniGameLink.setGeometry(QtCore.QRect(50, 360, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.miniGameLink.setFont(font)
        self.miniGameLink.setAutoFillBackground(False)
        self.miniGameLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(0, 0, 0);\n"
" color:rgb(225,225,225);\n"
" }"))
        self.miniGameLink.setFlat(False)
        self.miniGameLink.setObjectName(_fromUtf8("miniGameLink"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.previousGameFrame = QtGui.QFrame(self.centralwidget)
        self.previousGameFrame.setGeometry(QtCore.QRect(350, 170, 261, 261))
        self.previousGameFrame.setStyleSheet(_fromUtf8("border:5px solid;"))
        self.previousGameFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.previousGameFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.previousGameFrame.setObjectName(_fromUtf8("previousGameFrame"))
        self.previousGameLbl = QtGui.QLabel(self.previousGameFrame)
        self.previousGameLbl.setGeometry(QtCore.QRect(70, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.previousGameLbl.setFont(font)
        self.previousGameLbl.setStyleSheet(_fromUtf8("border:0px;"))
        self.previousGameLbl.setObjectName(_fromUtf8("previousGameLbl"))
        self.gameTypeLbl = QtGui.QLabel(self.previousGameFrame)
        self.gameTypeLbl.setGeometry(QtCore.QRect(60, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gameTypeLbl.setFont(font)
        self.gameTypeLbl.setStyleSheet(_fromUtf8("border:0px;"))
        self.gameTypeLbl.setObjectName(_fromUtf8("gameTypeLbl"))
        self.PreviousTallyLbl = QtGui.QLabel(self.previousGameFrame)
        self.PreviousTallyLbl.setGeometry(QtCore.QRect(60, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PreviousTallyLbl.setFont(font)
        self.PreviousTallyLbl.setStyleSheet(_fromUtf8("border:0px;"))
        self.PreviousTallyLbl.setObjectName(_fromUtf8("PreviousTallyLbl"))
        self.playNowButton = QtGui.QPushButton(self.previousGameFrame)
        self.playNowButton.setGeometry(QtCore.QRect(90, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.playNowButton.setFont(font)
        self.playNowButton.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"     background-color: rgb(220,0,0);\n"
" }"))
        self.playNowButton.setObjectName(_fromUtf8("playNowButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pg1TitleLbl.setText(_translate("MainWindow", "Draughts", None))
        self.player1Link.setText(_translate("MainWindow", "Player vs. Computer ", None))
        self.twoPlayerLink.setText(_translate("MainWindow", "Player 1 vs. Player 2", None))
        self.gameOptionsLink.setText(_translate("MainWindow", "Game Options", None))
        self.miniGameLink.setText(_translate("MainWindow", "Mini-Game", None))
        self.label.setText(_translate("MainWindow", "Hi,", None))
        self.previousGameLbl.setText(_translate("MainWindow", "Your pervious game", None))
        self.gameTypeLbl.setText(_translate("MainWindow", "TextLabel", None))
        self.PreviousTallyLbl.setText(_translate("MainWindow", "TextLabel", None))
        self.playNowButton.setText(_translate("MainWindow", "Play Now", None))

