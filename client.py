from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from login import Lon_in_ui
from signup import Sign_up_ui

import time


class Login(Lon_in_ui):
    gotoSignup_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def setup(self):
        self.pushButton_singup.clicked.connect(self.goto_Signup)
        self.gotoSignup_signal.emit()

    def goto_Signup(self):
        self.gotoSignup_signal.emit()


class Signup(Sign_up_ui, ):
    gotoLogin_signal = QtCore.pyqtSignal()
    signup_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def setup(self):
        # setup return button
        self.pushButton_return.clicked.connect(self.goto_login)

        # set up Sign up button
        self.pushButton_signup.clicked.connect(self.sign_up)

    def goto_login(self):
        self.gotoLogin_signal.emit()

    def sign_up(self):
        self.signup_signal.emit({
            "user name" : self.user_name_lineEdit.text(),
            "E-main" : self.email_line_edit.text(),
            "password" : self.password_line_edit.text(),
            "password2" : self.password_2_line_edit.text()
        })


class Controller:
    def __init__(self):
        self.login = None
        self.signup = None
        self.cur_screen = None
        self.Dialog = QtWidgets.QDialog()

        self.show_login_screen()

    def show_signup_screen(self):
        if self.cur_screen:
            self.cur_screen.close()

        self.signup = Signup()
        self.cur_screen = self.signup
        self.Dialog.hide()

        self.signup.setupUi(self.Dialog)
        self.signup.setup()

        self.signup.gotoLogin_signal.connect(self.show_login_screen)
        self.signup.signup_signal.connect(self.sign_up)

        self.Dialog.show()

    def sign_up(self, data_dict):
        print(data_dict)

    def show_login_screen(self):
        try:
            self.cur_screen.close()
        except:
            pass

        self.login = Login()
        self.cur_screen = self.login

        self.Dialog.hide()

        self.login.setupUi(self.Dialog)
        self.login.setup()

        self.login.gotoSignup_signal.connect(self.show_signup_screen)

        self.Dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    controller = Controller()

sys.exit(app.exec_())
