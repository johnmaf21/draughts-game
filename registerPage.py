import sys
from PyQt4 import QtCore, QtGui
import mysql.connector


class RegisterPage(QtGui.QMainWindow):
    def __init__(self):
        super(RegisterPage, self).__init__()
        self.setupUi()

        self.setGeometry(0,0,640,480)
        self.setWindowTitle("Register")

    def setupUi(self):

        #this part of the code is for the title of the of the register page
        pg4titleLbl = QtGui.QLabel(self)
        pg4titleLbl.setGeometry(QtCore.QRect(250, 50, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        pg4titleLbl.setFont(font)
        pg4titleLbl.setObjectName("pg4titleLbl")
        pg4titleLbl.setText("Register")

        #this part of the code is the button to take the user back to the homepage
        HomePageLink = QtGui.QPushButton(self)
        HomePageLink.setGeometry(QtCore.QRect(0, 170, 60, 120))
        HomePageLink.setObjectName("HomePageLink")
        HomePageLink.setText("Home")

        def goHome(self):
            self.homePage_ui=homePage
            self.homePage_ui.show()

        #this part of the code is to let the users know they need to enter a username
        enterUsernameLbl = QtGui.QLabel(self)
        enterUsernameLbl.setGeometry(QtCore.QRect(90, 130, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        enterUsernameLbl.setFont(font)
        enterUsernameLbl.setObjectName("enterUsernameLbl")
        enterUsernameLbl.setText("Choose a username:")

        #this part of the code is there so the user can input their username they want to create
        usernameInput = QtGui.QLineEdit(self)
        usernameInput.setGeometry(QtCore.QRect(290, 140, 260, 30))
        usernameInput.setObjectName("UsernameInput")

        #this part of the code is to let the user know that they need to enter an email
        createEmailLbl = QtGui.QLabel(self)
        createEmailLbl.setGeometry(QtCore.QRect(130, 180, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        createEmailLbl.setFont(font)
        createEmailLbl.setObjectName("createEmailLbl")
        createEmailLbl.setText("Create an Email:")

        #this part of the code is there so the user can input their email they want to use
        createEmailInput = QtGui.QLineEdit(self)
        createEmailInput.setGeometry(QtCore.QRect(290, 190, 260, 30))
        createEmailInput.setObjectName("createEmailInput")

        #this part of the code is to let the user know that they need to make a password
        createPaswordLbl = QtGui.QLabel(self)
        createPaswordLbl.setGeometry(QtCore.QRect(100, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        createPaswordLbl.setFont(font)
        createPaswordLbl.setObjectName("createPaswordLbl")
        createPaswordLbl.setText("Choose a Password:")

        #this part of the code is there so the user can input the password they want to create
        createPasswordInput = QtGui.QLineEdit(self)
        createPasswordInput.setGeometry(QtCore.QRect(290, 240, 260, 30))
        createPasswordInput.setObjectName("createPasswordInput")

        #this part of the of the code is to let the user know that they need to re-enter the password they just created
        confirmPasswordLbl = QtGui.QLabel(self)
        confirmPasswordLbl.setGeometry(QtCore.QRect(110, 280, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        confirmPasswordLbl.setFont(font)
        confirmPasswordLbl.setObjectName("confirmPasswordLbl")
        confirmPasswordLbl.setText("Confirm password:")

        #this part of the code is there so the user can re-enter the password they just create
        confirmPasswordInput = QtGui.QLineEdit(self)
        confirmPasswordInput.setGeometry(QtCore.QRect(290, 290, 260, 30))
        confirmPasswordInput.setObjectName("confirmPasswordInput")

        #this button is used so the user can input there data into the system
        registerButton = QtGui.QPushButton(self)
        registerButton.setGeometry(QtCore.QRect(260, 350, 110, 30))
        registerButton.setObjectName("registerButton")
        registerButton.setText("Register")


        def register():
            if createPasswordInput.text()==confirmPasswordInput.text():
                password=confirmPasswordInput.text()
            else:
                msg = QtGui.QMessageBox.information(self, 'Message', 'Inputted passwords are not the same', QtGui.QMessageBox.Ok)
            email=createEmailInput.text()
            username=usernameInput.text()
            if password=="" or email=="" or username=="":
                msg = QtGui.QMessageBox.information(self, 'Message', 'please fill in all boxes', QtGui.QMessageBox.Ok)
            else:
                cnx = mysql.connector.connect(user='scott', password='password',host='127.0.0.1',database='employees')
                add_user = ("INSERT INTO draughtsUsers "
               "(username, passsword, email) "
               "VALUES (%s, %s, %s)")
                cursor=cnx.cursor()
                userData=(username,password,email)
                cursor.execute(add_user, userData)
                userId= cursor.lastrowid
                cnx.commit()
                cursor.close()
                cnx.close()


        #this button will take the user back to the login page if they already have an account
        loginPageLink = QtGui.QPushButton(self)
        loginPageLink.setGeometry(QtCore.QRect(390, 420, 240, 30))
        loginPageLink.setStyleSheet("QPushButton { border: 0px;\n} QPushButton:hover {color:rgb(0,0,225);}")
        loginPageLink.setObjectName("loginPageLink")
        loginPageLink.setText("If you already have an account, login here")

        def loginPage(self):
            self.loginPage_ui=loginpage
            self.loginPage_ui.show()




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = RegisterPage()
    window.show()
    sys.exit(app.exec_())










