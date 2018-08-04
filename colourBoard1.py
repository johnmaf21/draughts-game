import sys
from PyQt4 import QtCore, QtGui

boardColour1=()

class boardColour1PageUI(QtGui.QMainWindow):
    def __init__(self):
        super(boardColour1PageUI, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("1st Board Colour")
    #these are all the methods for changing the colour display box when the button is pressed
    def chooseBlack(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(0, 0, 0); border:5px solid;")
    def chooseWhite(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(255,255,255); border: 5px solid;")
    def choosePink(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(255,51,204); border: 5px solid;")
    def chooseDarkGreen(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(0,102,0); border: 5px solid;")
    def chooseGreen(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(0,255,0); border: 5px solid;")
    def choosePurple(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(153,51,255); border: 5px solid;")
    def chooseBlue(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(0,102,255); border: 5px solid;")
    def chooseLightBlue(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(51,204,255); border: 5px solid;")
    def chooseYellow(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(255,204,0); border: 5px solid;")
    def chooseBrown(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(153,51,0); border: 5px solid;")
    def chooseGrey(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(179,179,179); border: 5px solid;")
    def chooseGreenBlue(self,chosenColourDisplay):
        chosenColourDisplay.setStyleSheet("background-color: rgb(0,102,102) ; border: 5px solid;")

    def setupUi(self):
        global boardColour1
        #this is the code for the title of this page
        pg8aTitleLbl = QtGui.QLabel(self)
        pg8aTitleLbl.setGeometry(QtCore.QRect(200, 40, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        pg8aTitleLbl.setFont(font)
        pg8aTitleLbl.setObjectName("pg8aTitleLbl")
        pg8aTitleLbl.setText("Board Colour 1")
        #these are all the colour buttons
        blackButton = QtGui.QPushButton(self)
        blackButton.setGeometry(QtCore.QRect(90, 130, 50, 50))
        blackButton.setStyleSheet("background-color: rgb(0, 0, 0);")
        blackButton.setObjectName("blackButton")

        blackButton.clicked.connect(lambda: self.chooseBlack(chosenColourDisplay) )

        whiteButton = QtGui.QPushButton(self)
        whiteButton.setGeometry(QtCore.QRect(160, 130, 50, 50))
        whiteButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        whiteButton.setObjectName("whiteButton")

        whiteButton.clicked.connect(lambda: self.chooseWhite(chosenColourDisplay) )

        pinkButton = QtGui.QPushButton(self)
        pinkButton.setGeometry(QtCore.QRect(230, 130, 50, 50))
        pinkButton.setStyleSheet("background-color: rgb(255,51,204);")
        pinkButton.setObjectName("pinkButton")

        pinkButton.clicked.connect(lambda: self.choosePink(chosenColourDisplay))

        darkGreenButton = QtGui.QPushButton(self)
        darkGreenButton.setGeometry(QtCore.QRect(300, 130, 50, 50))
        darkGreenButton.setStyleSheet("background-color: rgb(0,102,0);")
        darkGreenButton.setObjectName("darkGreenButton")

        darkGreenButton.clicked.connect(lambda: self.chooseDarkGreen(chosenColourDisplay))

        greenButton = QtGui.QPushButton(self)
        greenButton.setGeometry(QtCore.QRect(90, 210, 50, 50))
        greenButton.setStyleSheet("background-color: rgb(0,255,0);")
        greenButton.setObjectName("greenButton")

        greenButton.clicked.connect(lambda: self.chooseGreen(chosenColourDisplay))

        purpleButton = QtGui.QPushButton(self)
        purpleButton.setGeometry(QtCore.QRect(160, 210, 50, 50))
        purpleButton.setStyleSheet("background-color: rgb(153,51,255);")
        purpleButton.setObjectName("purpleButton")

        purpleButton.clicked.connect(lambda: self.choosePurple(chosenColourDisplay))

        blueButton = QtGui.QPushButton(self)
        blueButton.setGeometry(QtCore.QRect(230, 210, 50, 50))
        blueButton.setStyleSheet("background-color: rgb(0,102,255);")
        blueButton.setObjectName("blueButton")

        blueButton.clicked.connect(lambda: self.chooseBlue(chosenColourDisplay))

        lightBlueButton = QtGui.QPushButton(self)
        lightBlueButton.setGeometry(QtCore.QRect(300, 210, 50, 50))
        lightBlueButton.setStyleSheet("background-color: rgb(51,204,255);")
        lightBlueButton.setObjectName("lightBlueButton")

        lightBlueButton.clicked.connect(lambda: self.chooseLightBlue(chosenColourDisplay))

        yellowButton = QtGui.QPushButton(self)
        yellowButton.setGeometry(QtCore.QRect(90, 290, 50, 50))
        yellowButton.setStyleSheet("background-color: rgb(255,204,0);")
        yellowButton.setObjectName("yellowButton")

        yellowButton.clicked.connect(lambda: self.chooseYellow(chosenColourDisplay))

        brownButton = QtGui.QPushButton(self)
        brownButton.setGeometry(QtCore.QRect(160, 290, 51, 51))
        brownButton.setStyleSheet("background-color: rgb(153,51,0);")
        brownButton.setObjectName("brownButton")

        brownButton.clicked.connect(lambda: self.chooseBrown(chosenColourDisplay))

        greyButton = QtGui.QPushButton(self)
        greyButton.setGeometry(QtCore.QRect(230, 290, 50, 50))
        greyButton.setStyleSheet("background-color: rgb(179,179,179);")
        greyButton.setObjectName("greyButton")

        greyButton.clicked.connect(lambda: self.chooseGrey(chosenColourDisplay))

        greenBlueButton = QtGui.QPushButton(self)
        greenBlueButton.setGeometry(QtCore.QRect(300, 290, 50, 50))
        greenBlueButton.setStyleSheet("background-color: rgb(0,102,102);")
        greenBlueButton.setObjectName("greenBlueButton")

        greenBlueButton.clicked.connect(lambda: self.chooseGreenBlue(chosenColourDisplay))

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
    window = boardColour1PageUI()
    window.show()
    sys.exit(app.exec_())





