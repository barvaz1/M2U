# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Sign_up_ui(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(999, 561)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 1000, 562))
        self.label.setObjectName("label")
        self.welcome = QtWidgets.QLabel(Dialog)
        self.welcome.setGeometry(QtCore.QRect(80, 10, 501, 81))
        self.welcome.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome.setObjectName("welcome")
        self.user_name = QtWidgets.QLabel(Dialog)
        self.user_name.setGeometry(QtCore.QRect(80, 90, 140, 40))
        self.user_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_name.setObjectName("user_name")
        self.user_name_3 = QtWidgets.QLineEdit(Dialog)
        self.user_name_3.setGeometry(QtCore.QRect(80, 140, 461, 31))
        self.user_name_3.setStyleSheet("border-radius: 15px;")
        self.user_name_3.setObjectName("user_name_3")
        self.user_name_2 = QtWidgets.QLabel(Dialog)
        self.user_name_2.setGeometry(QtCore.QRect(80, 240, 140, 40))
        self.user_name_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_name_2.setObjectName("user_name_2")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(80, 280, 461, 31))
        self.password.setStyleSheet("border-radius: 15px;")
        self.password.setObjectName("password")
        self.pushButton_signup = QtWidgets.QPushButton(Dialog)
        self.pushButton_signup.setGeometry(QtCore.QRect(140, 390, 351, 41))
        self.pushButton_signup.setStyleSheet("background-color: rgb(177, 223, 242);\n"
"\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;")
        self.pushButton_signup.setObjectName("pushButton_login")
        self.pushButton_return = QtWidgets.QPushButton(Dialog)
        self.pushButton_return.setGeometry(QtCore.QRect(10, 500, 211, 41))
        self.pushButton_return.setStyleSheet("background-color: rgb(177, 223, 242);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;")
        self.pushButton_return.setObjectName("pushButton_singup")
        self.user_name_4 = QtWidgets.QLabel(Dialog)
        self.user_name_4.setGeometry(QtCore.QRect(80, 170, 140, 40))
        self.user_name_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_name_4.setObjectName("user_name_4")
        self.password_2 = QtWidgets.QLineEdit(Dialog)
        self.password_2.setGeometry(QtCore.QRect(80, 210, 461, 31))
        self.password_2.setStyleSheet("border-radius: 15px;")
        self.password_2.setObjectName("password_2")
        self.password_3 = QtWidgets.QLineEdit(Dialog)
        self.password_3.setGeometry(QtCore.QRect(80, 340, 461, 31))
        self.password_3.setStyleSheet("border-radius: 15px;")
        self.password_3.setObjectName("password_3")
        self.user_name_5 = QtWidgets.QLabel(Dialog)
        self.user_name_5.setGeometry(QtCore.QRect(80, 310, 211, 40))
        self.user_name_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_name_5.setObjectName("user_name_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/sing_up.png\"/></p></body></html>"))
        self.welcome.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">SIGN UP</span></p></body></html>"))
        self.user_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">USER NAME</span></p></body></html>"))
        self.user_name_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">PASSWORD</span></p></body></html>"))
        self.pushButton_signup.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">I\'m ready to go!</span></p></body></html>"))
        self.pushButton_signup.setText(_translate("Dialog", "I\'m ready to go!"))
        self.pushButton_return.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">I\'m ready to go!</span></p></body></html>"))
        self.pushButton_return.setText(_translate("Dialog", "RETURN"))
        self.user_name_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">E - MAIL</span></p></body></html>"))
        self.user_name_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">CONFIRM PASSWORD</span></p></body></html>"))
import resource_file


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Sign_up_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
