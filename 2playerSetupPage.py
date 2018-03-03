import sys
from PyQt4 import QtCore, QtGui

class player2SetupPage(QtGui.QMainWindow):
    def __init__(self):
        super(player2SetupPage, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Two Players")


    def setupUi(self):
        player1NameInput = QtGui.QLineEdit(self)
        player1NameInput.setGeometry(QtCore.QRect(120, 80, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        player1NameInput.setFont(font)
        player1NameInput.setAlignment(QtCore.Qt.AlignCenter)
        player1NameInput.setObjectName("player1NameInput")
        player1NameInput.setText("Player 1")

        player2NameInput = QtGui.QLineEdit(self)
        player2NameInput.setGeometry(QtCore.QRect(400, 80, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        player2NameInput.setFont(font)
        player2NameInput.setAlignment(QtCore.Qt.AlignCenter)
        player2NameInput.setObjectName("player1NameInput_2")
        player2NameInput.setText("Player 2")

        playNowButton = QtGui.QPushButton(self)
        playNowButton.setGeometry(QtCore.QRect(270, 340, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        playNowButton.setFont(font)
        playNowButton.setObjectName("playNowButton")
        playNowButton.setText("Next")

        HomeButton = QtGui.QPushButton(self)
        HomeButton.setGeometry(QtCore.QRect(0, 180, 60, 120))
        HomeButton.setObjectName("HomeButton")
        HomeButton.setText("Home")

        player1Red = QtGui.QPushButton(self)
        player1Red.setGeometry (QtCore.QRect(90, 150, 90, 90))
        player1Red.setStyleSheet ('background-color: red; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player1Red.setObjectName('player1Red')

        player1Black = QtGui.QPushButton(self)
        player1Black.setGeometry(QtCore.QRect(210, 150, 90, 90))
        player1Black.setStyleSheet ('background-color: black; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player1Black.setObjectName('player1Black')

        player2Red = QtGui.QPushButton(self)
        player2Red.setGeometry (QtCore.QRect(380, 150, 90, 90))
        player2Red.setStyleSheet ('background-color: red; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player2Red.setObjectName('pushButton_2')

        player2Black = QtGui.QPushButton(self)
        player2Black.setGeometry(QtCore.QRect(500, 150, 90, 90))
        player2Black.setStyleSheet ('background-color: black; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player2Black.setObjectName('pushButton_2')



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = player2SetupPage()
    window.show()
    sys.exit(app.exec_())




