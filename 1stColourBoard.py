import sys
from PyQt4 import QtCore, QtGui

class BoardColour1Page(QtGui.QMainWindow):
    def __init__(self):
        super(BoardColour1Page, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("1st Board Colour")

    def setupUi(self):

        pg8aTitleLbl = QtGui.QLabel(self)
        pg8aTitleLbl.setGeometry(QtCore.QRect(200, 40, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        pg8aTitleLbl.setFont(font)
        pg8aTitleLbl.setObjectName("pg8aTitleLbl")
        pg8aTitleLbl.setText("Board Colour 1")

        blackButton = QtGui.QPushButton(self)
        blackButton.setGeometry(QtCore.QRect(90, 130, 50, 50))
        blackButton.setStyleSheet("background-color: rgb(0, 0, 0);")
        blackButton.setObjectName("blackButton")
        def choseBlack():
            chosenColourDisplay.setStyleSheet("background-color: rgb(0, 0, 0);")


        whiteButton = QtGui.QPushButton(self)
        whiteButton.setGeometry(QtCore.QRect(160, 130, 50, 50))
        whiteButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        whiteButton.setObjectName("whiteButton")

        pinkButton = QtGui.QPushButton(self)
        pinkButton.setGeometry(QtCore.QRect(230, 130, 50, 50))
        pinkButton.setStyleSheet("background-color: rgb(255,51,204);")
        pinkButton.setObjectName("pinkButton")

        darkGreenButton = QtGui.QPushButton(self)
        darkGreenButton.setGeometry(QtCore.QRect(300, 130, 50, 50))
        darkGreenButton.setStyleSheet("background-color: rgb(0,102,0);")
        darkGreenButton.setObjectName("darkGreenButton")

        greenButton = QtGui.QPushButton(self)
        greenButton.setGeometry(QtCore.QRect(90, 210, 50, 50))
        greenButton.setStyleSheet("background-color: rgb(0,255,0);")
        greenButton.setObjectName("greenButton")

        purpleButton = QtGui.QPushButton(self)
        purpleButton.setGeometry(QtCore.QRect(160, 210, 50, 50))
        purpleButton.setStyleSheet("background-color: rgb(153,51,255);")
        purpleButton.setObjectName("purpleButton")

        blueButton = QtGui.QPushButton(self)
        blueButton.setGeometry(QtCore.QRect(230, 210, 50, 50))
        blueButton.setStyleSheet("background-color: rgb(0,102,255);")
        blueButton.setObjectName("blueButton")

        lightBlueButton = QtGui.QPushButton(self)
        lightBlueButton.setGeometry(QtCore.QRect(300, 210, 50, 50))
        lightBlueButton.setStyleSheet("background-color: rgb(51,204,255);")
        lightBlueButton.setObjectName("lightBlueButton")

        yellowButton = QtGui.QPushButton(self)
        yellowButton.setGeometry(QtCore.QRect(90, 290, 50, 50))
        yellowButton.setStyleSheet("background-color: rgb(255,204,0);")
        yellowButton.setObjectName("yellowButton")

        brownButton = QtGui.QPushButton(self)
        brownButton.setGeometry(QtCore.QRect(160, 290, 51, 51))
        brownButton.setStyleSheet("background-color: rgb(153,51,0);")
        brownButton.setObjectName("brownButton")

        greyButton = QtGui.QPushButton(self)
        greyButton.setGeometry(QtCore.QRect(230, 290, 50, 50))
        greyButton.setStyleSheet("background-color: rgb(179,179,179);")
        greyButton.setObjectName("greyButton")

        greenBlueButton = QtGui.QPushButton(self)
        greenBlueButton.setGeometry(QtCore.QRect(300, 290, 50, 50))
        greenBlueButton.setStyleSheet("background-color: rgb(0,102,102);")
        greenBlueButton.setObjectName("greenBlueButton")

        chosenColourLbl = QtGui.QLabel(self)
        chosenColourLbl.setGeometry(QtCore.QRect(440, 120, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        chosenColourLbl.setFont(font)
        chosenColourLbl.setAlignment(QtCore.Qt.AlignCenter)
        chosenColourLbl.setObjectName("chosenColourLbl")
        chosenColourLbl.setText( "Chosen Colour")

        chosenColourDisplay = QtGui.QLabel(self)
        chosenColourDisplay.setGeometry(QtCore.QRect(420, 150, 160, 160))
        chosenColourDisplay.setStyleSheet("border:5px solid;")
        chosenColourDisplay.setObjectName("chosenColourDisplay")

        saveButton = QtGui.QPushButton(self)
        saveButton.setGeometry(QtCore.QRect(454, 352, 90, 30))
        saveButton.setObjectName("saveButton")
        saveButton.setText("Save")

        backButton = QtGui.QPushButton(self)
        backButton.setGeometry(QtCore.QRect(0, 180, 60, 120))
        backButton.setObjectName("backButton")
        backButton.setText("Back")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = BoardColour1Page()
    window.show()
    sys.exit(app.exec_())





