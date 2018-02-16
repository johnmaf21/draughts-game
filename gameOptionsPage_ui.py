# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameOptionsPage.ui'
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

class Ui_GameOptionsPage(object):
    def setupUi(self, GameOptionsPage):
        GameOptionsPage.setObjectName(_fromUtf8("GameOptionsPage"))
        GameOptionsPage.resize(640, 480)
        self.centralwidget = QtGui.QWidget(GameOptionsPage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Pg7titleLbl = QtGui.QLabel(self.centralwidget)
        self.Pg7titleLbl.setGeometry(QtCore.QRect(240, 40, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Pg7titleLbl.setFont(font)
        self.Pg7titleLbl.setObjectName(_fromUtf8("Pg7titleLbl"))
        self.chooseBoardColour1Button = QtGui.QPushButton(self.centralwidget)
        self.chooseBoardColour1Button.setGeometry(QtCore.QRect(150, 100, 151, 41))
        self.chooseBoardColour1Button.setStyleSheet(_fromUtf8("background-color: rgb(255,204,0);"))
        self.chooseBoardColour1Button.setObjectName(_fromUtf8("chooseBoardColour1Button"))
        self.HomeButton = QtGui.QPushButton(self.centralwidget)
        self.HomeButton.setGeometry(QtCore.QRect(0, 190, 61, 121))
        self.HomeButton.setObjectName(_fromUtf8("HomeButton"))
        self.chooseBoardColour2Button = QtGui.QPushButton(self.centralwidget)
        self.chooseBoardColour2Button.setGeometry(QtCore.QRect(320, 100, 151, 41))
        self.chooseBoardColour2Button.setStyleSheet(_fromUtf8("background-color: rgb(153,51,0);"))
        self.chooseBoardColour2Button.setObjectName(_fromUtf8("chooseBoardColour2Button"))
        self.SaveButton = QtGui.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(260, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.forceJumpLbl = QtGui.QLabel(self.centralwidget)
        self.forceJumpLbl.setGeometry(QtCore.QRect(160, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.forceJumpLbl.setFont(font)
        self.forceJumpLbl.setObjectName(_fromUtf8("forceJumpLbl"))
        self.showsMovesLbl = QtGui.QLabel(self.centralwidget)
        self.showsMovesLbl.setGeometry(QtCore.QRect(150, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.showsMovesLbl.setFont(font)
        self.showsMovesLbl.setObjectName(_fromUtf8("showsMovesLbl"))
        self.HintsLbl = QtGui.QLabel(self.centralwidget)
        self.HintsLbl.setGeometry(QtCore.QRect(200, 300, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HintsLbl.setFont(font)
        self.HintsLbl.setObjectName(_fromUtf8("HintsLbl"))
        self.forceJumpOnRbutton = QtGui.QRadioButton(self.centralwidget)
        self.forceJumpOnRbutton.setGeometry(QtCore.QRect(280, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.forceJumpOnRbutton.setFont(font)
        self.forceJumpOnRbutton.setObjectName(_fromUtf8("forceJumpOnRbutton"))
        self.showsMovesOnRbutton = QtGui.QRadioButton(self.centralwidget)
        self.showsMovesOnRbutton.setGeometry(QtCore.QRect(280, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.showsMovesOnRbutton.setFont(font)
        self.showsMovesOnRbutton.setObjectName(_fromUtf8("showsMovesOnRbutton"))
        self.HintsOnRbutton = QtGui.QRadioButton(self.centralwidget)
        self.HintsOnRbutton.setGeometry(QtCore.QRect(280, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HintsOnRbutton.setFont(font)
        self.HintsOnRbutton.setObjectName(_fromUtf8("HintsOnRbutton"))
        self.forceJumpOffRbutton = QtGui.QRadioButton(self.centralwidget)
        self.forceJumpOffRbutton.setGeometry(QtCore.QRect(370, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.forceJumpOffRbutton.setFont(font)
        self.forceJumpOffRbutton.setObjectName(_fromUtf8("forceJumpOffRbutton"))
        self.showsMovesOffRbutton = QtGui.QRadioButton(self.centralwidget)
        self.showsMovesOffRbutton.setGeometry(QtCore.QRect(370, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.showsMovesOffRbutton.setFont(font)
        self.showsMovesOffRbutton.setObjectName(_fromUtf8("showsMovesOffRbutton"))
        self.HintsOffRbutton = QtGui.QRadioButton(self.centralwidget)
        self.HintsOffRbutton.setGeometry(QtCore.QRect(370, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HintsOffRbutton.setFont(font)
        self.HintsOffRbutton.setObjectName(_fromUtf8("HintsOffRbutton"))
        GameOptionsPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GameOptionsPage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GameOptionsPage.setStatusBar(self.statusbar)

        self.retranslateUi(GameOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(GameOptionsPage)

    def retranslateUi(self, GameOptionsPage):
        GameOptionsPage.setWindowTitle(_translate("GameOptionsPage", "MainWindow", None))
        self.Pg7titleLbl.setText(_translate("GameOptionsPage", "Options", None))
        self.chooseBoardColour1Button.setText(_translate("GameOptionsPage", "Board Colour 1", None))
        self.HomeButton.setText(_translate("GameOptionsPage", "Home", None))
        self.chooseBoardColour2Button.setText(_translate("GameOptionsPage", "Board Colour 2", None))
        self.SaveButton.setText(_translate("GameOptionsPage", "Save", None))
        self.forceJumpLbl.setText(_translate("GameOptionsPage", "Force jump:", None))
        self.showsMovesLbl.setText(_translate("GameOptionsPage", "Show moves:", None))
        self.HintsLbl.setText(_translate("GameOptionsPage", "Hints:", None))
        self.forceJumpOnRbutton.setText(_translate("GameOptionsPage", "On", None))
        self.showsMovesOnRbutton.setText(_translate("GameOptionsPage", "On", None))
        self.HintsOnRbutton.setText(_translate("GameOptionsPage", "On", None))
        self.forceJumpOffRbutton.setText(_translate("GameOptionsPage", "Off", None))
        self.showsMovesOffRbutton.setText(_translate("GameOptionsPage", "Off", None))
        self.HintsOffRbutton.setText(_translate("GameOptionsPage", "Off", None))

