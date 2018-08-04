import sys
from PyQt4 import QtCore, QtGui
forceMove=True
showMoves=True
hints=True
pink=(255,51,204)
green=(0,102,0)
lightGreen=(0,255,0)
purple=(153,51,255)
blue=(0,102,255)
lightBlue=(51,204,255)
yellow=(255,204,0)
brown=(153,51,0)
grey=(179,179,179)
greenBlue=(0,102,102)

boardColour1=yellow
boardColour2=brown

class gameOptionsPageUI(QtGui.QMainWindow):
    def __init__(self):
        super(gameOptionsPageUI, self).__init__()
        self.setupUi()
        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Game Options")


    def setupUi(self):

        Pg7titleLbl = QtGui.QLabel(self)
        Pg7titleLbl.setGeometry(QtCore.QRect(240, 40, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        Pg7titleLbl.setFont(font)
        Pg7titleLbl.setObjectName("Pg7titleLbl")
        Pg7titleLbl.setText("Options")

        chooseBoardColour1Button = QtGui.QPushButton(self)
        chooseBoardColour1Button.setGeometry(QtCore.QRect(150, 100, 150, 40))
        chooseBoardColour1Button.setStyleSheet("background-color: rgb("+str(boardColour1)+");")
        chooseBoardColour1Button.setObjectName("chooseBoardColour1Button")
        chooseBoardColour1Button.setText("Board Colour 1")

        HomeButton = QtGui.QPushButton(self)
        HomeButton.setGeometry(QtCore.QRect(0, 190, 60, 120))
        HomeButton.setObjectName("HomeButton")
        HomeButton.setText("Home")

        chooseBoardColour2Button = QtGui.QPushButton(self)
        chooseBoardColour2Button.setGeometry(QtCore.QRect(320, 100, 150, 40))
        chooseBoardColour2Button.setStyleSheet("background-color: rgb("+str(boardColour2)+");")
        chooseBoardColour2Button.setObjectName("chooseBoardColour2Button")
        chooseBoardColour2Button.setText("Board Colour 2")

        SaveButton = QtGui.QPushButton(self)
        SaveButton.setGeometry(QtCore.QRect(260, 390, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        SaveButton.setFont(font)
        SaveButton.setObjectName("SaveButton")
        SaveButton.setText("Save")

        forceJumpLbl = QtGui.QLabel(self)
        forceJumpLbl.setGeometry(QtCore.QRect(160, 180, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        forceJumpLbl.setFont(font)
        forceJumpLbl.setObjectName("forceJumpLbl")
        forceJumpLbl.setText("Force jump:")

        forceJumpOnRbutton = QtGui.QRadioButton(self)
        forceJumpOnRbutton.setGeometry(QtCore.QRect(280, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        forceJumpOnRbutton.setFont(font)
        forceJumpOnRbutton.setObjectName("forceJumpOnRbutton")
        forceJumpOnRbutton.setText("On")

        forceJumpOffRbutton = QtGui.QRadioButton(self)
        forceJumpOffRbutton.setGeometry(QtCore.QRect(370, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        forceJumpOffRbutton.setFont(font)
        forceJumpOffRbutton.setObjectName("forceJumpOffRbutton")
        forceJumpOffRbutton.setText("Off")


        showsMovesLbl = QtGui.QLabel(self)
        showsMovesLbl.setGeometry(QtCore.QRect(150, 240, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        showsMovesLbl.setFont(font)
        showsMovesLbl.setObjectName("showsMovesLbl")
        showsMovesLbl.setText("Show moves:")

        showsMovesOnRbutton = QtGui.QRadioButton(self)
        showsMovesOnRbutton.setGeometry(QtCore.QRect(280, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        showsMovesOnRbutton.setFont(font)
        showsMovesOnRbutton.setObjectName("showsMovesOnRbutton")
        showsMovesOnRbutton.setText("On")

        showsMovesOffRbutton = QtGui.QRadioButton(self)
        showsMovesOffRbutton.setGeometry(QtCore.QRect(370, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        showsMovesOffRbutton.setFont(font)
        showsMovesOffRbutton.setObjectName("showsMovesOffRbutton")
        showsMovesOffRbutton.setText("Off")

        HintsLbl = QtGui.QLabel(self)
        HintsLbl.setGeometry(QtCore.QRect(200, 300, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        HintsLbl.setFont(font)
        HintsLbl.setObjectName("HintsLbl")
        HintsLbl.setText("Hints:")

        HintsOnRbutton = QtGui.QRadioButton(self)
        HintsOnRbutton.setGeometry(QtCore.QRect(280, 300, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        HintsOnRbutton.setFont(font)
        HintsOnRbutton.setObjectName("HintsOnRbutton")
        HintsOnRbutton.setText("On")

        HintsOffRbutton = QtGui.QRadioButton(self)
        HintsOffRbutton.setGeometry(QtCore.QRect(370, 300, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        HintsOffRbutton.setFont(font)
        HintsOffRbutton.setObjectName("HintsOffRbutton")
        HintsOffRbutton.setText("Off")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = gameOptionsPageUI()
    window.show()
    sys.exit(app.exec_())