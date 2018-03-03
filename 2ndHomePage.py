import sys
from PyQt4 import QtCore, QtGui
import mysql.connector


class UserHomePage(QtGui.QMainWindow):
    def __init__(self):
        super(UserHomePage, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Home")

    def setupUi(self):


        pg1TitleLbl = QtGui.QLabel(self)
        pg1TitleLbl.setGeometry(QtCore.QRect(230, 60, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        pg1TitleLbl.setFont(font)
        pg1TitleLbl.setObjectName("pg1TitleLbl")
        pg1TitleLbl.setText("Draughts")

        player1Link = QtGui.QPushButton(self)
        player1Link.setGeometry(QtCore.QRect(50, 150, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        player1Link.setFont(font)
        player1Link.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(220,0,0);}")
        player1Link.setObjectName("player1Link")
        player1Link.setText("Player vs. Computer ")

        twoPlayerLink = QtGui.QPushButton(self)
        twoPlayerLink.setGeometry(QtCore.QRect(50, 220, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        twoPlayerLink.setFont(font)
        twoPlayerLink.setStyleSheet("QPushButton { border: 0px;} QPushButton:hover {background-color: rgb(0, 0, 0); color:rgb(225,225,225); }")
        twoPlayerLink.setObjectName("twoPlayerLink")
        twoPlayerLink.setText("Player 1 vs. Player 2")

        gameOptionsLink = QtGui.QPushButton(self)
        gameOptionsLink.setGeometry(QtCore.QRect(50, 290, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        gameOptionsLink.setFont(font)
        gameOptionsLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color:rgb(220,0,0);}")
        gameOptionsLink.setObjectName("gameOptionsLink")
        gameOptionsLink.setText("Game Options")

        miniGameLink = QtGui.QPushButton(self)
        miniGameLink.setGeometry(QtCore.QRect(50, 360, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        miniGameLink.setFont(font)
        miniGameLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(0, 0, 0); color:rgb(225,225,225);}")
        miniGameLink.setObjectName("miniGameLink")
        miniGameLink.setText("Mini-Game")

        label = QtGui.QLabel(self)
        label.setGeometry(QtCore.QRect(420, 20, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        label.setFont(font)
        label.setObjectName("label")
        label.setText("Hi, " )

        previousGameFrame = QtGui.QFrame(self)
        previousGameFrame.setGeometry(QtCore.QRect(350, 170, 260, 260))
        previousGameFrame.setStyleSheet("border:5px solid;")
        previousGameFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        previousGameFrame.setFrameShadow(QtGui.QFrame.Raised)
        previousGameFrame.setObjectName("previousGameFrame")

        previousGameLbl = QtGui.QLabel(self)
        previousGameLbl.setGeometry(QtCore.QRect(440, 180, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        previousGameLbl.setFont(font)
        previousGameLbl.setStyleSheet("border:0px;")
        previousGameLbl.setObjectName("previousGameLbl")
        previousGameLbl.setText("Your pervious game")

        gameTypeLbl = QtGui.QLabel(self)
        gameTypeLbl.setGeometry(QtCore.QRect(440, 220, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        gameTypeLbl.setFont(font)
        gameTypeLbl.setStyleSheet("border:0px;")
        gameTypeLbl.setObjectName("gameTypeLbl")
        gameTypeLbl.setText("")

        PreviousTallyLbl = QtGui.QLabel(self)
        PreviousTallyLbl.setGeometry(QtCore.QRect(440, 130, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        PreviousTallyLbl.setFont(font)
        PreviousTallyLbl.setStyleSheet("border:0px;")
        PreviousTallyLbl.setObjectName("PreviousTallyLbl")
        PreviousTallyLbl.setText("TextLabel")

        playNowButton = QtGui.QPushButton(self)
        playNowButton.setGeometry(QtCore.QRect(440, 380, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        playNowButton.setFont(font)
        playNowButton.setStyleSheet("QPushButton:hover {background-color: rgb(220,0,0);}")
        playNowButton.setObjectName("playNowButton")
        playNowButton.setText("Play Now")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = UserHomePage()
    window.show()
    sys.exit(app.exec_())










