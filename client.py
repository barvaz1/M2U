from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
import ast
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import sys
from login import Lon_in_ui
from signup import Sign_up_ui
from client_communicate import Socket_controller

import checkInput


class Login(Lon_in_ui):
    gotoSignup_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def setup(self):
        self.pushButton_singup.clicked.connect(self.goto_Signup)
        self.gotoSignup_signal.emit()

        self.lineEdit_user_name.editingFinished.connect(self.check_input)
        self.lineEdit_password.editingFinished.connect(self.check_input)

    def goto_Signup(self):
        self.gotoSignup_signal.emit()

    def check_input(self):

        temp = 0
        # chnge the color of the line edit
        print("check_input")
        if checkInput.check_user_name(self.lineEdit_user_name.text()):
            self.lineEdit_user_name.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                                  "outset;border-width: 2px;")
            temp += 1
        else:
            self.lineEdit_user_name.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                                  "outset;border-width: 2px;")

        if checkInput.check_password(self.lineEdit_password.text()):
            self.lineEdit_password.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                                 "outset;border-width: 2px;")
            temp += 1
        else:
            print(12345567890)
            self.lineEdit_password.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                                 "outset;border-width: 2px;")

        return temp == 2


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

        self.user_name_lineEdit.editingFinished.connect(self.check_input)
        self.email_line_edit.editingFinished.connect(self.check_input)
        self.password_line_edit.editingFinished.connect(self.check_input)
        self.password_2_line_edit.editingFinished.connect(self.check_input)

    def goto_login(self):
        self.gotoLogin_signal.emit()

    def sign_up(self):
        if self.check_input():
            self.signup_signal.emit({
                "user name": self.user_name_lineEdit.text(),
                "E-mail": self.email_line_edit.text(),
                "password": self.password_line_edit.text(),
                "password2": self.password_2_line_edit.text()
            })

    def change_text_boxs(self, data):
        print(data)
        if data['user name']:
            self.user_name_lineEdit.setText(data['user name'])
        if data['E-mail']:
            self.email_line_edit.setText(data['E-mail'])



    def check_input(self):

        # chnge the color of the line edit
        print("check_input")

        temp = 0
        # user name
        if checkInput.check_user_name(self.user_name_lineEdit.text()):
            self.user_name_lineEdit.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                                  "outset;border-width: 2px;")
            temp += 1
        else:
            self.user_name_lineEdit.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                                  "outset;border-width: 2px;")

        # user e_mail
        if checkInput.check_email(self.email_line_edit.text()):
            self.email_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                               "outset;border-width: 2px;")

            temp += 1
        else:
            self.email_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                               "outset;border-width: 2px;")

        # user password
        if checkInput.check_password(self.password_line_edit.text()):
            self.password_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                                  "outset;border-width: 2px;")

            temp += 1
        else:
            self.password_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                                  "outset;border-width: 2px;")

        # user password 2
        if self.password_line_edit.text() == self.password_2_line_edit.text():
            self.password_2_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(124,252,0);border-style: "
                                                    "outset;border-width: 2px;")

            temp += 1
        else:
            self.password_2_line_edit.setStyleSheet("border-radius: 15px;border-color: rgb(255,0,0);border-style: "
                                                    "outset;border-width: 2px;")

        print(temp)
        return temp == 4


class Controller:
    def __init__(self):
        self.login = None
        self.signup = None
        self.cur_screen = None
        self.Dialog = QtWidgets.QDialog()

        self.show_login_screen()

        self.socket_controller = Socket_controller(self)

    def show_signup_screen(self):
        #        if self.cur_screen:
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
        #################################################################
        # check staff
        #################################################################
        if self.signup.check_input():
            # after check!
            del data_dict["password2"]
            data = "sign_up" + str(data_dict)
            self.socket_controller.send_data(data)

            try:
                print(ast.literal_eval(data[7:]))

            except Exception as e:
                print(e.__str__())
                raise

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

    def handel_server_input(self, data):

        print("handel_server_input")
        ##################################
        # in case of sign up
        ##################################
        if data[0:7] == "sign_up":
            data = ast.literal_eval(data[7:])
            print(data)

            if data["success"]:
                pass # move to chat window
            else:
                del data["password"]
                del data["success"]
                self.signup.change_text_boxs(data)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    controller = Controller()

import atexit

# atexit.register(controller.socket_controller.send_data, data = "EXIT")

sys.exit(app.exec_())
