# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Designs/courseLandingPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def add(self):
        os.system("python addCoursePageUI.py")
    def view(self):
        os.system("python courseViewAllCoursesUI.py")
    def update(self):
        os.system("python updateCourseLandingPage.py")
    def home(self):
        os.system("python landingPageUI.py")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
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
        self.courseLandingPageAddCourse = QtWidgets.QPushButton(self.frame)
        self.courseLandingPageAddCourse.setGeometry(QtCore.QRect(240, 150, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.courseLandingPageAddCourse.setFont(font)
        self.courseLandingPageAddCourse.clicked.connect(self.add)
        self.courseLandingPageAddCourse.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid green;")
        self.courseLandingPageAddCourse.setObjectName("courseLandingPageAddCourse")
        self.courseLandingPageUpdateCourse = QtWidgets.QPushButton(self.frame)
        self.courseLandingPageUpdateCourse.clicked.connect(self.update)
        self.courseLandingPageUpdateCourse.setGeometry(QtCore.QRect(240, 290, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.courseLandingPageUpdateCourse.setFont(font)
        self.courseLandingPageUpdateCourse.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid green;")
        self.courseLandingPageUpdateCourse.setObjectName("courseLandingPageUpdateCourse")
        self.courseLandingPageViewCourse = QtWidgets.QPushButton(self.frame)
        self.courseLandingPageViewCourse.clicked.connect(self.view)
        self.courseLandingPageViewCourse.setGeometry(QtCore.QRect(240, 430, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.courseLandingPageViewCourse.setFont(font)
        self.courseLandingPageViewCourse.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid green;")
        self.courseLandingPageViewCourse.setObjectName("courseLandingPageViewCourse")
        self.courseLandingPageHome = QtWidgets.QPushButton(self.frame)
        self.courseLandingPageHome.setGeometry(QtCore.QRect(10, 10, 141, 61))
        self.courseLandingPageHome.clicked.connect(self.home)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.courseLandingPageHome.setFont(font)
        self.courseLandingPageHome.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid green;")
        self.courseLandingPageHome.setObjectName("courseLandingPageHome")
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
        self.courseLandingPageAddCourse.setText(_translate("MainWindow", "Add Course"))
        self.courseLandingPageUpdateCourse.setText(_translate("MainWindow", "Update Course"))
        self.courseLandingPageViewCourse.setText(_translate("MainWindow", "View Course"))
        self.courseLandingPageHome.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
