import sys
from PyQt4 import QtCore, QtGui


class homePage(QtGui.QMainWindow):
    def __init__(self):
        super(homePage, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Home")


    def setupUi(self):
        pg1TitleLbl = QtGui.QLabel(self)
        pg1TitleLbl.setGeometry(QtCore.QRect(230, 50, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        pg1TitleLbl.setFont(font)
        pg1TitleLbl.setObjectName("pg1TitleLbl")
        pg1TitleLbl.setText("Draughts")

        signInButton = QtGui.QPushButton(self)
        signInButton.setGeometry(QtCore.QRect(530, 20, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        signInButton.setFont(font)
        signInButton.setObjectName("signInButton")
        signInButton.setText("Sign in")

        player1Link = QtGui.QPushButton(self)
        player1Link.setGeometry(QtCore.QRect(50, 130, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        player1Link.setFont(font)
        player1Link.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153)}")
        player1Link.setObjectName("player1Link")
        player1Link.setText("Player vs. Computer ")

        twoPlayerLink = QtGui.QPushButton(self)
        twoPlayerLink.setGeometry(QtCore.QRect(50, 200, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        twoPlayerLink.setFont(font)
        twoPlayerLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153);}")
        twoPlayerLink.setObjectName("twoPlayerLink")
        twoPlayerLink.setText("Player 1 vs. Player 2")

        gameOptionsLink = QtGui.QPushButton(self)
        gameOptionsLink.setGeometry(QtCore.QRect(50, 270, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        gameOptionsLink.setFont(font)
        gameOptionsLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color:rgb(153, 153, 153);}")
        gameOptionsLink.setObjectName("gameOptionsLink")
        gameOptionsLink.setText("Game Options")

        miniGameLink = QtGui.QPushButton(self)
        miniGameLink.setGeometry(QtCore.QRect(50, 340, 270, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        miniGameLink.setFont(font)
        miniGameLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {background-color: rgb(153, 153, 153);}")
        miniGameLink.setObjectName("miniGameLink")
        miniGameLink.setText("Mini-Game")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = homePage()
    window.show()
    sys.exit(app.exec_())











