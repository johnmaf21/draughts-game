import sys
from PyQt4 import QtCore, QtGui

class instructionsPageUI(QtGui.QMainWindow):

    def __init__(self):
        super(instructionsPageUI, self).__init__()
        self.setupUi()
        self.setGeometry(0,0,640,480)
        self.setWindowTitle("instructions Page")

    def openGame(self):
        pass

    def setupUi(self):
        pg9TitleLbl = QtGui.QLabel(self)
        pg9TitleLbl.setGeometry(QtCore.QRect(220, 40, 220, 70))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        pg9TitleLbl.setFont(font)
        pg9TitleLbl.setObjectName("pg9TitleLbl")
        pg9TitleLbl.setText("Instructions")

        startButton = QtGui.QPushButton(self)
        startButton.setGeometry(QtCore.QRect(270, 360, 100, 30))
        startButton.setObjectName("startButton")
        startButton.setText("Start")

        startButton.clicked.connect( lambda: self.openGame())


        instructionsLbl = QtGui.QLabel(self)
        instructionsLbl.setGeometry(QtCore.QRect(110, 110, 420, 230))
        font.setPointSize(8)
        font.setWeight(12)
        instructionsLbl.setFont(font)
        instructionsLbl.setObjectName("instructionsLbl")
        instructionsLbl.setText("Draughts is a head to head game where the person with pieces still left on the board\nwill win. Red pieces will go first and the game will alternate\n after each turn. The pieces are only allowed to move diagonally one square unless it's taking\nthe other person's piece. To get a draw no pieces can be taken in 40 moves.")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = instructionsPageUI()
    window.show()
    sys.exit(app.exec_())





