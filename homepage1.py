import sys
from PyQt4 import QtCore, QtGui
from loginPage import *
from player1SetupPage import player1SetupPageUI
from player2SetupPage import *
from gameOptionsPage import *




class homePageUI(QtGui.QMainWindow):
    def __init__(self):
        super(homePageUI, self).__init__()
        self.setupUi()

        self.setGeometry(350,165,640,480)
        self.setWindowTitle("Home")

    def openPlayer1Setup(self):
            self.window=QtGui.QMainWindow()
            self.ui=player1SetupPageUI
            self.ui.setupUi(self.window)
            self.window.resize(640,480)
            self.window.move(350,165)
            homeWindow.hide()
            self.window.show()

    def openGameOptions(self):
            self.window=QtGui.QMainWindow()
            self.ui=gameOptionsPageUI
            super(self.ui,self).__init()
            self.ui.setupUi(self.window)
            self.window.resize(640,480)
            self.window.move(350,165)
            homeWindow.hide()
            self.window.show()

    def openPlayer2Setup(self):
            self.window=QtGui.QMainWindow()
            self.ui=player2SetupPageUI
            self.ui.setupUi(self.window)
            self.window.resize(640,480)
            self.window.move(350,165)
            homeWindow.hide()
            self.window.show()

    def openLogin(self):
            app=QtGui.QApplication(sys.argv)
            self.window=QtGui.QMainWindow()
            self.ui=loginPageUI
            super(self.ui,self).__init()
            self.ui.setupUi(self.window)
            self.window.resize(640,480)
            self.window.move(350,165)
            homeWindow.hide()
            self.window.show()
            sys.exit(app.exec_())




    def setupUi(self):
        #this is the code for the title label of the window
        pg1TitleLbl = QtGui.QLabel(self)
        pg1TitleLbl.setGeometry(QtCore.QRect(230, 50, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        pg1TitleLbl.setFont(font)
        pg1TitleLbl.setObjectName("pg1TitleLbl")
        pg1TitleLbl.setText("Draughts")

        #this is creating the visual for the button which when clicked will open the login page
        signInButton = QtGui.QPushButton(self)
        signInButton.setGeometry(QtCore.QRect(530, 20, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        signInButton.setFont(font)
        signInButton.setObjectName("signInButton")
        signInButton.setText("Sign in")

        signInButton.clicked.connect(lambda: self.openLogin())

        #this is creating the button on gui which will open up the player 1 setup page
        player1Link = QtGui.QPushButton(self)
        player1Link.setGeometry(QtCore.QRect(50, 130, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        player1Link.setFont(font)
        player1Link.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153)}")
        player1Link.setObjectName("player1Link")
        player1Link.setText("Player vs. Computer ")

        player1Link.clicked.connect(lambda: self.openPlayer1Setup())

        #this is creating the button on the gui which  will open the two player set page
        twoPlayerLink = QtGui.QPushButton(self)
        twoPlayerLink.setGeometry(QtCore.QRect(50, 200, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        twoPlayerLink.setFont(font)
        twoPlayerLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153);}")
        twoPlayerLink.setObjectName("twoPlayerLink")
        twoPlayerLink.setText("Player 1 vs. Player 2")

        twoPlayerLink.clicked.connect(lambda: self.openPlayer2Setup())

        #this is creating the button on the gui which will open up the game options page
        gameOptionsLink = QtGui.QPushButton(self)
        gameOptionsLink.setGeometry(QtCore.QRect(50, 270, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        gameOptionsLink.setFont(font)
        gameOptionsLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color:rgb(153, 153, 153);}")
        gameOptionsLink.setObjectName("gameOptionsLink")
        gameOptionsLink.setText("Game Options")

        gameOptionsLink.clicked.connect(lambda: self.openGameOptions())

        #this is creating the button on the gui which will also open up the game options page
        miniGameLink = QtGui.QPushButton(self)
        miniGameLink.setGeometry(QtCore.QRect(50, 340, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        miniGameLink.setFont(font)
        miniGameLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153);}")
        miniGameLink.setObjectName("miniGameLink")
        miniGameLink.setText("Mini-Game")

        miniGameLink.clicked.connect(lambda: self.openPlayer1Setup())



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    homeWindow = homePageUI()
    homeWindow.show()
    sys.exit(app.exec_())









