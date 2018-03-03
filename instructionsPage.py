import sys
from PyQt4 import QtCore, QtGui

class instructionsPage(QtGui.QMainWindow):

    def __init__(self):
        super(instructionsPage, self).__init__()
        self.setupUi()
        self.setGeometry(0,0,640,480)
        self.setWindowTitle("instructions Page")

    def setupUi(self):
        pg9TitleLbl = QtGui.QLabel(self)
        pg9TitleLbl.setGeometry(QtCore.QRect(210, 40, 220, 70))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        pg9TitleLbl.setFont(font)
        pg9TitleLbl.setObjectName("pg9TitleLbl")
        pg9TitleLbl.setText("Instructions")

        startButton = QtGui.QPushButton(self)
        startButton.setGeometry(QtCore.QRect(270, 360, 100, 30))
        startButton.setObjectName("startButton")
        startButton.setText("Start")

        instructionsLbl = QtGui.QLabel(self)
        instructionsLbl.setGeometry(QtCore.QRect(110, 110, 420, 230))
        instructionsLbl.setObjectName("instructionsLbl")
        instructionsLbl.setText("TextLabel")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = instructionsPage()
    window.show()
    sys.exit(app.exec_())





