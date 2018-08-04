import sys
from PyQt4 import QtCore, QtGui

userID=0
class loginPageUI(QtGui.QMainWindow):
    def __init__(self):
        super(loginPageUI, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Login")

    def openHomePage(self):
        import homepage1

    def login(self,emailInput,passwordInput):
        email=emailInput.text()
        password=passwordInput()
        userLoginQuery= "SELECT email FROM draughtsuser WHERE where email=%s"



    def setupUi(self):
        Pg3titleLbl = QtGui.QLabel(self)
        Pg3titleLbl.setGeometry(QtCore.QRect(270, 60, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        Pg3titleLbl.setFont(font)
        Pg3titleLbl.setObjectName("Pg3titleLbl")
        Pg3titleLbl.setText("Login")

        HomeButton = QtGui.QPushButton(self)
        HomeButton.setGeometry(QtCore.QRect(0, 170, 60, 120))
        HomeButton.setObjectName("HomeButton")
        HomeButton.setText("Home")

        HomeButton.clicked.connect(lambda: self.openHomePage())

        loginButton = QtGui.QPushButton(self)
        loginButton.setGeometry(QtCore.QRect(270, 320, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        loginButton.setFont(font)
        loginButton.setObjectName("loginButton")
        loginButton.setText("login")

        login.clicked.connect(self.login(emailInput,passwordInput))

        emailLbl = QtGui.QLabel(self)
        emailLbl.setGeometry(QtCore.QRect(160, 170, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        emailLbl.setFont(font)
        emailLbl.setObjectName("emailLbl")
        emailLbl.setText("Email:")

        emailInput = QtGui.QLineEdit(self)
        emailInput.setGeometry(QtCore.QRect(220, 180, 260, 30))
        emailInput.setObjectName("emailInput")

        passwordLbl = QtGui.QLabel(self)
        passwordLbl.setGeometry(QtCore.QRect(120, 240, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        passwordLbl.setFont(font)
        passwordLbl.setObjectName("passwordLbl")
        passwordLbl.setText("Password:")

        passwordInput = QtGui.QLineEdit(self)
        passwordInput.setGeometry(QtCore.QRect(220, 250, 260, 30))
        passwordInput.setObjectName("passwordInput")

        registerPageLink = QtGui.QPushButton(self)
        registerPageLink.setGeometry(QtCore.QRect(390, 410, 240, 30))
        registerPageLink.setStyleSheet("QPushButton {border: 0px;} QPushButton:hover {color:rgb(0,0,225);}")
        registerPageLink.setObjectName("registerPageLink")
        registerPageLink.setText("If you don't have an account, register here")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = loginPageUI()
    window.show()
    sys.exit(app.exec_())










