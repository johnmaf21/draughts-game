import sys
import PyQt4
from PyQt4 import QtWidgets
from PyQt4.QtWidgets import QApplication, QWidget,  QPushButton
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import pyqtSlot, QUrl

class MenuPage(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Draughts game'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    #this method is for creating the actual GUI itself for the main page
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #wehn this button is clicked it will go to the sign in page
        signInbutton = QPushButton('Sign in', self)
        button.setToolTip('')
        button.move(100,70)
        button.clicked.connect(self.on_click)#this is what willl open the method to go to that page

        #this is creating the labels for this page
        pg1TitleLbl = Qlabel()
        player1Link = Qlabel()
        twoPlayerLink = Qlabel()
        gameOptionsLink = Qlabel()
        miniGameLink = Qlabel()
        #this is creating the text which will go in the text
        pg1TitleLbl.setText("Draughts Game")
        player1Link.setText("Player vs. Computer")
        twoPlayerLink.setText("Player 1 vs. Player 2")
        gameOptionsLink.setText("Game Options")
        miniGameLink=setText("minigame")
        #this will place the labels into the correct place on the page
        pg1TitleLbl.move()
        player1Link.move()
        twoPlayerLink.move()
        gameOptionsLink.move()
        #this is need so that the labels are clickable and go to teir corresponding pages
        player1Link.mouseReleaseEvent = self.showPlayer1
        twoPlayerLink.mouseReleaseEvent = self.showTwoPlayer
        gameOptionsLink.mouseReleaseEvent = self.showGameOptions
        miniGameLink.mouseReleaseEvent = self.showMiniGame
        #this is the function that will open up the pages the user wants to go to
        def showPlayer1():
            player1GameSetupPage

        self.show()

#this is creating a page for the game options
class GameOptionPage(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(GameOptionPage, self).__init__(parent)
        self.title = 'Game options Page'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
