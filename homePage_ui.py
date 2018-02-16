
from PyQt4 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pg1TitleLbl = QtGui.QLabel(self.centralwidget)
        self.pg1TitleLbl.setGeometry(QtCore.QRect(230, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pg1TitleLbl.setFont(font)
        self.pg1TitleLbl.setObjectName("pg1TitleLbl")
        self.signInButton = QtGui.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(530, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.signInButton.setFont(font)
        self.signInButton.setAutoFillBackground(False)
        self.signInButton.setObjectName("signInButton")
        self.player1Link = QtGui.QPushButton(self.centralwidget)
        self.player1Link.setGeometry(QtCore.QRect(50, 130, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player1Link.setFont(font)
        self.player1Link.setAutoFillBackground(False)
        self.player1Link.setStyleSheet("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(153, 153, 153);\n"
" }")
        self.player1Link.setFlat(False)
        self.player1Link.setObjectName(_fromUtf8("player1Link"))
        self.twoPlayerLink = QtGui.QPushButton(self.centralwidget)
        self.twoPlayerLink.setGeometry(QtCore.QRect(50, 200, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.twoPlayerLink.setFont(font)
        self.twoPlayerLink.setAutoFillBackground(False)
        self.twoPlayerLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(153, 153, 153);\n"
" }"))

        self.twoPlayerLink.setObjectName("twoPlayerLink")
        self.gameOptionsLink = QtGui.QPushButton(self.centralwidget)
        self.gameOptionsLink.setGeometry(QtCore.QRect(50, 270, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gameOptionsLink.setFont(font)
        self.gameOptionsLink.setAutoFillBackground(False)
        self.gameOptionsLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color:rgb(153, 153, 153) ;\n"
" }"))

        self.gameOptionsLink.setObjectName(_fromUtf8("gameOptionsLink"))
        self.miniGameLink = QtGui.QPushButton(self.centralwidget)
        self.miniGameLink.setGeometry(QtCore.QRect(50, 340, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.miniGameLink.setFont(font)
        self.miniGameLink.setAutoFillBackground(False)
        self.miniGameLink.setStyleSheet(_fromUtf8("QPushButton { \n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(153, 153, 153);\n"
" }"))

        self.miniGameLink.setObjectName(_fromUtf8("miniGameLink"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)


        MainWindow.setWindowTitle("MainWindow", None)
        self.pg1TitleLbl.setText("Draughts", None)
        self.signInButton.setText("Sign in", None)
        self.player1Link.setText("Player vs. Computer ", None)
        self.twoPlayerLink.setText("Player 1 vs. Player 2", None)
        self.gameOptionsLink.setText("Game Options", None)
        self.miniGameLink.setText("Mini-Game", None)

