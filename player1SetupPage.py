import sys
from PyQt4 import QtCore, QtGui

class player1SetupPageUI(QtGui.QMainWindow):
    def __init__(self):
        super(player1SetupPageUI,self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("One Player")

    def setupUi(self):
        player1NameInput = QtGui.QLineEdit(self)
        player1NameInput.setGeometry(QtCore.QRect(130, 60, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        player1NameInput.setFont(font)
        player1NameInput.setAlignment(QtCore.Qt.AlignCenter)
        player1NameInput.setObjectName("player1NameInput")
        player1NameInput.setText("Player 1")

        player1Red = QtGui.QPushButton(self)
        player1Red.setGeometry (QtCore.QRect(90, 150, 90, 90))
        player1Red.setStyleSheet ('background-color: red; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player1Red.setObjectName('player1Red')

        player1Black = QtGui.QPushButton(self)
        player1Black.setGeometry(QtCore.QRect(210, 150, 90, 90))
        player1Black.setStyleSheet ('background-color: black; border-width: 2px; border-radius: 45px; border-colour:rgb(0,0,0);')
        player1Black.setObjectName('player1Black')


        difficultyLbl = QtGui.QLabel(self)
        difficultyLbl.setGeometry(QtCore.QRect(390, 60, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        difficultyLbl.setFont(font)
        difficultyLbl.setStyleSheet("border:4px solid;")
        difficultyLbl.setAlignment(QtCore.Qt.AlignCenter)
        difficultyLbl.setObjectName("difficultyLbl")
        difficultyLbl.setText("Difficulty")

        easyDifficultyButton = QtGui.QPushButton(self)
        easyDifficultyButton.setGeometry(QtCore.QRect(390, 120, 140, 60))
        easyDifficultyButton.setStyleSheet("QPushButton {border: 0px; background-color: green;}")
        easyDifficultyButton.setObjectName("easyDifficultyButton")
        easyDifficultyButton.setText("Easy")

        mediumDifficultyButton = QtGui.QPushButton(self)
        mediumDifficultyButton.setGeometry(QtCore.QRect(390, 200, 141, 61))
        mediumDifficultyButton.setStyleSheet("QPushButton {border: 0px; background-color: yellow;}")
        mediumDifficultyButton.setObjectName("mediumDifficultyButton")
        mediumDifficultyButton.setText("Medium")

        hardDifficultyButton = QtGui.QPushButton(self)
        hardDifficultyButton.setGeometry(QtCore.QRect(390, 280, 140, 60))
        hardDifficultyButton.setStyleSheet("QPushButton {border: 0px; background-color: red;}")
        hardDifficultyButton.setObjectName("hardDifficultyButton")
        hardDifficultyButton.setText("Hard")

        HomeButton = QtGui.QPushButton(self)
        HomeButton.setGeometry(QtCore.QRect(0, 190, 60, 120))
        HomeButton.setObjectName("HomeButton")
        HomeButton.setText("Home")

        playNowButton = QtGui.QPushButton(self)
        playNowButton.setGeometry(QtCore.QRect(260, 380, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        playNowButton.setFont(font)
        playNowButton.setObjectName("playNowButton")
        playNowButton.setText("Next")

        playNowButton.clicked.connect( openInstructions())

        player1NameInput.setText("Player 1")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = player1SetupPageUI()
    window.show()
    sys.exit(app.exec_())




