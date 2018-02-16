# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerPage.ui'
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

class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        RegisterPage.setObjectName(_fromUtf8("RegisterPage"))
        RegisterPage.resize(640, 480)
        self.centralwidget = QtGui.QWidget(RegisterPage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pg4titleLbl = QtGui.QLabel(self.centralwidget)
        self.pg4titleLbl.setGeometry(QtCore.QRect(250, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pg4titleLbl.setFont(font)
        self.pg4titleLbl.setObjectName(_fromUtf8("pg4titleLbl"))
        self.HomePageLink = QtGui.QPushButton(self.centralwidget)
        self.HomePageLink.setGeometry(QtCore.QRect(0, 170, 61, 121))
        self.HomePageLink.setObjectName(_fromUtf8("HomePageLink"))
        self.enterUsernameLbl = QtGui.QLabel(self.centralwidget)
        self.enterUsernameLbl.setGeometry(QtCore.QRect(90, 130, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.enterUsernameLbl.setFont(font)
        self.enterUsernameLbl.setObjectName(_fromUtf8("enterUsernameLbl"))
        self.createEmaillLbl = QtGui.QLabel(self.centralwidget)
        self.createEmaillLbl.setGeometry(QtCore.QRect(130, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createEmaillLbl.setFont(font)
        self.createEmaillLbl.setObjectName(_fromUtf8("createEmaillLbl"))
        self.createPaswordLbl = QtGui.QLabel(self.centralwidget)
        self.createPaswordLbl.setGeometry(QtCore.QRect(100, 230, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createPaswordLbl.setFont(font)
        self.createPaswordLbl.setObjectName(_fromUtf8("createPaswordLbl"))
        self.confirmPasswordLbl = QtGui.QLabel(self.centralwidget)
        self.confirmPasswordLbl.setGeometry(QtCore.QRect(110, 280, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirmPasswordLbl.setFont(font)
        self.confirmPasswordLbl.setObjectName(_fromUtf8("confirmPasswordLbl"))
        self.UsernameInput = QtGui.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(290, 140, 261, 31))
        self.UsernameInput.setObjectName(_fromUtf8("UsernameInput"))
        self.createEmailInput = QtGui.QLineEdit(self.centralwidget)
        self.createEmailInput.setGeometry(QtCore.QRect(290, 190, 261, 31))
        self.createEmailInput.setObjectName(_fromUtf8("createEmailInput"))
        self.createPasswordInput = QtGui.QLineEdit(self.centralwidget)
        self.createPasswordInput.setGeometry(QtCore.QRect(290, 240, 261, 31))
        self.createPasswordInput.setObjectName(_fromUtf8("createPasswordInput"))
        self.confirmPasswordInput = QtGui.QLineEdit(self.centralwidget)
        self.confirmPasswordInput.setGeometry(QtCore.QRect(290, 290, 261, 31))
        self.confirmPasswordInput.setObjectName(_fromUtf8("confirmPasswordInput"))
        self.registerButton = QtGui.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(260, 350, 111, 31))
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.loginPageLink = QtGui.QPushButton(self.centralwidget)
        self.loginPageLink.setGeometry(QtCore.QRect(390, 420, 241, 31))
        self.loginPageLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" color:rgb(0,0,225);\n"
" }"))
        self.loginPageLink.setObjectName(_fromUtf8("loginPageLink"))
        RegisterPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(RegisterPage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RegisterPage.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterPage)
        QtCore.QMetaObject.connectSlotsByName(RegisterPage)

    def retranslateUi(self, RegisterPage):
        RegisterPage.setWindowTitle(_translate("RegisterPage", "MainWindow", None))
        self.pg4titleLbl.setText(_translate("RegisterPage", "Register", None))
        self.HomePageLink.setText(_translate("RegisterPage", "Home", None))
        self.enterUsernameLbl.setText(_translate("RegisterPage", "Choose a username:", None))
        self.createEmaillLbl.setText(_translate("RegisterPage", "Create an Email:", None))
        self.createPaswordLbl.setText(_translate("RegisterPage", "Choose a Password:", None))
        self.confirmPasswordLbl.setText(_translate("RegisterPage", "Confirm password:", None))
        self.registerButton.setText(_translate("RegisterPage", "Register", None))
        self.loginPageLink.setText(_translate("RegisterPage", "If you already have an account, login here", None))

