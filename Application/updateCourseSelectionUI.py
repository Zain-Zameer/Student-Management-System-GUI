# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Designs/updateCourseSelectionUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class updateCourseOptions(object):
    def updateName(self):
        os.system("python updateCourseNameUI.py")
    def updateCredit(self):
        os.system("python updateCourseCreditHrsPageUI.py")
    def home(self):
        os.system("python landingPageUI.py")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
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
        self.updateCourseSelectionUpdateNameButton = QtWidgets.QPushButton(self.frame)
        self.updateCourseSelectionUpdateNameButton.setGeometry(QtCore.QRect(240, 230, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.updateCourseSelectionUpdateNameButton.setFont(font)
        self.updateCourseSelectionUpdateNameButton.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid brown;")
        self.updateCourseSelectionUpdateNameButton.setObjectName("updateCourseSelectionUpdateNameButton")
        self.updateCourseSelectionUpdateNameButton.clicked.connect(self.updateName)
        self.updateCoyrseSelectionUpdateCreditHoursButton = QtWidgets.QPushButton(self.frame)
        self.updateCoyrseSelectionUpdateCreditHoursButton.clicked.connect(self.updateCredit)
        self.updateCoyrseSelectionUpdateCreditHoursButton.setGeometry(QtCore.QRect(240, 320, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.updateCoyrseSelectionUpdateCreditHoursButton.setFont(font)
        self.updateCoyrseSelectionUpdateCreditHoursButton.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid brown;")
        self.updateCoyrseSelectionUpdateCreditHoursButton.setObjectName("updateCoyrseSelectionUpdateCreditHoursButton")
        self.updateCourseSelectionUIHomeButton = QtWidgets.QPushButton(self.frame)
        self.updateCourseSelectionUIHomeButton.setGeometry(QtCore.QRect(10, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.updateCourseSelectionUIHomeButton.setFont(font)
        self.updateCourseSelectionUIHomeButton.clicked.connect(self.home)
        self.updateCourseSelectionUIHomeButton.setStyleSheet("background-color: white;\n"
"display: inline-block;\n"
"      padding: 10px 20px;\n"
"      font-size: 30px;\n"
"      text-align: center;\n"
"      text-decoration: none;\n"
"      cursor: pointer;\n"
"      border-radius: 5px;\n"
"      transition: background-color 0.3s ease;\n"
" border: 4px solid brown;")
        self.updateCourseSelectionUIHomeButton.setObjectName("updateCourseSelectionUIHomeButton")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size: 30px;\n"
"color: white;")
        self.label_5.setObjectName("label_5")
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
        self.updateCourseSelectionUpdateNameButton.setText(_translate("MainWindow", "Update Name"))
        self.updateCoyrseSelectionUpdateCreditHoursButton.setText(_translate("MainWindow", "Update Credit Hours"))
        self.updateCourseSelectionUIHomeButton.setText(_translate("MainWindow", "Home"))
        self.label_5.setText(_translate("MainWindow", "Update Course"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = updateCourseOptions()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())