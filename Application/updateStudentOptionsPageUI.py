# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Designs/updateStudentOptionsPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os 

from updateStudentNameUI import updateStudentName

class UpdateStudentOptionsPage(object):
        def updateNameButton(self):
                os.system("python updateStudentNameUI.py")
        def updategeButton(self):
               os.system("python updateStudentAgeUI.py")
        def updateGenderButton(self):
               os.system("python updateStudentGenderUI.py")
        def updateDeptButton(self):
               os.system("python updateStudentDepartmentUI.py")
        def homeBut(self):
               os.system("python landingPageUI.py")
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 591))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.gridLayout.setObjectName("gridLayout")
                self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
                self.frame.setStyleSheet("\n"
        "background-color: #345687;\n"
        "")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(300, 10, 211, 51))
                font = QtGui.QFont()
                font.setFamily("Papyrus")
                font.setPointSize(-1)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("font-size: 40px;\n"
        "color: white;")
                self.label_4.setObjectName("label_4")
                self.updateStudentOptionsPageUpdateNameButton = QtWidgets.QPushButton(self.frame)
                self.updateStudentOptionsPageUpdateNameButton.clicked.connect(self.updateNameButton)
                self.updateStudentOptionsPageUpdateNameButton.setGeometry(QtCore.QRect(240, 150, 341, 61))
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(-1)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.updateStudentOptionsPageUpdateNameButton.setFont(font)
                self.updateStudentOptionsPageUpdateNameButton.setStyleSheet("background-color: white;\n"
        "display: inline-block;\n"
        "      padding: 10px 20px;\n"
        "      font-size: 30px;\n"
        "      text-align: center;\n"
        "      text-decoration: none;\n"
        "      cursor: pointer;\n"
        "      border-radius: 5px;\n"
        "      transition: background-color 0.3s ease;\n"
        " border: 4px solid brown;")
                self.updateStudentOptionsPageUpdateNameButton.setObjectName("updateStudentOptionsPageUpdateNameButton")
                self.updateStudentOptionsPageUpdateAgeButton = QtWidgets.QPushButton(self.frame)
                self.updateStudentOptionsPageUpdateAgeButton.setGeometry(QtCore.QRect(240, 240, 341, 71))
                self.updateStudentOptionsPageUpdateAgeButton.clicked.connect(self.updategeButton)
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(-1)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.updateStudentOptionsPageUpdateAgeButton.setFont(font)
                self.updateStudentOptionsPageUpdateAgeButton.setStyleSheet("background-color: white;\n"
        "display: inline-block;\n"
        "      padding: 10px 20px;\n"
        "      font-size: 30px;\n"
        "      text-align: center;\n"
        "      text-decoration: none;\n"
        "      cursor: pointer;\n"
        "      border-radius: 5px;\n"
        "      transition: background-color 0.3s ease;\n"
        " border: 4px solid brown;")
                self.updateStudentOptionsPageUpdateAgeButton.setObjectName("updateStudentOptionsPageUpdateAgeButton")
                self.updateStudentOptionsPageUpdateGenderButton = QtWidgets.QPushButton(self.frame)
                self.updateStudentOptionsPageUpdateGenderButton.clicked.connect(self.updateGenderButton)
                self.updateStudentOptionsPageUpdateGenderButton.setGeometry(QtCore.QRect(240, 330, 341, 71))
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(-1)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.updateStudentOptionsPageUpdateGenderButton.setFont(font)
                self.updateStudentOptionsPageUpdateGenderButton.setStyleSheet("background-color: white;\n"
        "display: inline-block;\n"
        "      padding: 10px 20px;\n"
        "      font-size: 30px;\n"
        "      text-align: center;\n"
        "      text-decoration: none;\n"
        "      cursor: pointer;\n"
        "      border-radius: 5px;\n"
        "      transition: background-color 0.3s ease;\n"
        " border: 4px solid brown;")
                self.updateStudentOptionsPageUpdateGenderButton.setObjectName("updateStudentOptionsPageUpdateGenderButton")
                self.updateStudentOptionsPageHomeButton = QtWidgets.QPushButton(self.frame)
                self.updateStudentOptionsPageHomeButton.setGeometry(QtCore.QRect(10, 10, 141, 61))
                self.updateStudentOptionsPageHomeButton.clicked.connect(self.homeBut)
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(-1)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.updateStudentOptionsPageHomeButton.setFont(font)
                self.updateStudentOptionsPageHomeButton.setStyleSheet("background-color: white;\n"
        "display: inline-block;\n"
        "      padding: 10px 20px;\n"
        "      font-size: 30px;\n"
        "      text-align: center;\n"
        "      text-decoration: none;\n"
        "      cursor: pointer;\n"
        "      border-radius: 5px;\n"
        "      transition: background-color 0.3s ease;\n"
        " border: 4px solid brown;")
                self.updateStudentOptionsPageHomeButton.setObjectName("updateStudentOptionsPageHomeButton")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(290, 80, 231, 51))
                font = QtGui.QFont()
                font.setFamily("Papyrus")
                font.setPointSize(-1)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("font-size: 30px;\n"
        "color: white;")
                self.label_5.setObjectName("label_5")
                self.updateStudentOptionsPageUpdateDepartmentButton = QtWidgets.QPushButton(self.frame)
                self.updateStudentOptionsPageUpdateDepartmentButton.setGeometry(QtCore.QRect(240, 430, 341, 71))
                self.updateStudentOptionsPageUpdateDepartmentButton.clicked.connect(self.updateDeptButton)
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(-1)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.updateStudentOptionsPageUpdateDepartmentButton.setFont(font)
                self.updateStudentOptionsPageUpdateDepartmentButton.setStyleSheet("background-color: white;\n"
        "display: inline-block;\n"
        "      padding: 10px 20px;\n"
        "      font-size: 30px;\n"
        "      text-align: center;\n"
        "      text-decoration: none;\n"
        "      cursor: pointer;\n"
        "      border-radius: 5px;\n"
        "      transition: background-color 0.3s ease;\n"
        " border: 4px solid brown;")
                self.updateStudentOptionsPageUpdateDepartmentButton.setObjectName("updateStudentOptionsPageUpdateDepartmentButton")
                self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_4.setText(_translate("MainWindow", "My College"))
                self.updateStudentOptionsPageUpdateNameButton.setText(_translate("MainWindow", "Update Name"))
                self.updateStudentOptionsPageUpdateAgeButton.setText(_translate("MainWindow", "Update Age"))
                self.updateStudentOptionsPageUpdateGenderButton.setText(_translate("MainWindow", "Update Gender"))
                self.updateStudentOptionsPageHomeButton.setText(_translate("MainWindow", "Home"))
                self.label_5.setText(_translate("MainWindow", "Update Student"))
                self.updateStudentOptionsPageUpdateDepartmentButton.setText(_translate("MainWindow", "Update Department"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UpdateStudentOptionsPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
