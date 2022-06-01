# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(5120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Inter")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:  #000000;\n"
"}\n"
"QLabel{\n"
"    color: #FFFFFF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lista = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lista.sizePolicy().hasHeightForWidth())
        self.lista.setSizePolicy(sizePolicy)
        self.lista.setMinimumSize(QtCore.QSize(1920, 145))
        self.lista.setMaximumSize(QtCore.QSize(1920, 145))
        self.lista.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lista.setObjectName("lista")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.lista)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clock = QtWidgets.QLabel(self.lista)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clock.sizePolicy().hasHeightForWidth())
        self.clock.setSizePolicy(sizePolicy)
        self.clock.setMinimumSize(QtCore.QSize(290, 125))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(90)
        self.clock.setFont(font)
        self.clock.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.clock.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.clock.setObjectName("clock")
        self.horizontalLayout.addWidget(self.clock, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_3.addWidget(self.lista, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.hello = QtWidgets.QFrame(self.centralwidget)
        self.hello.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hello.sizePolicy().hasHeightForWidth())
        self.hello.setSizePolicy(sizePolicy)
        self.hello.setObjectName("hello")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.hello)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.now = QtWidgets.QFrame(self.hello)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.now.sizePolicy().hasHeightForWidth())
        self.now.setSizePolicy(sizePolicy)
        self.now.setMinimumSize(QtCore.QSize(1000, 460))
        self.now.setMaximumSize(QtCore.QSize(1000, 540))
        self.now.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.now.setAutoFillBackground(False)
        self.now.setStyleSheet("QWidget {\n"
"    color: #FFFFFF;\n"
"    background-color: #2B2B2B;\n"
"    border-radius: 20px;\n"
"}")
        self.now.setObjectName("now")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.now)
        self.verticalLayout_2.setContentsMargins(20, 50, 20, 50)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.now_start_end = QtWidgets.QLabel(self.now)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.now_start_end.sizePolicy().hasHeightForWidth())
        self.now_start_end.setSizePolicy(sizePolicy)
        self.now_start_end.setMinimumSize(QtCore.QSize(0, 130))
        self.now_start_end.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(120)
        self.now_start_end.setFont(font)
        self.now_start_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.now_start_end.setObjectName("now_start_end")
        self.verticalLayout_2.addWidget(self.now_start_end)
        self.now_who = QtWidgets.QLabel(self.now)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.now_who.sizePolicy().hasHeightForWidth())
        self.now_who.setSizePolicy(sizePolicy)
        self.now_who.setMinimumSize(QtCore.QSize(0, 100))
        self.now_who.setMaximumSize(QtCore.QSize(1000000, 100))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(90)
        self.now_who.setFont(font)
        self.now_who.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.now_who.setObjectName("now_who")
        self.verticalLayout_2.addWidget(self.now_who)
        self.now_what = QtWidgets.QLabel(self.now)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.now_what.sizePolicy().hasHeightForWidth())
        self.now_what.setSizePolicy(sizePolicy)
        self.now_what.setMinimumSize(QtCore.QSize(0, 70))
        self.now_what.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(50)
        self.now_what.setFont(font)
        self.now_what.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.now_what.setObjectName("now_what")
        self.verticalLayout_2.addWidget(self.now_what)
        self.progressBar = QtWidgets.QProgressBar(self.now)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(900, 50))
        self.progressBar.setMaximumSize(QtCore.QSize(900, 50))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"text-align: top;\n"
"border-radius: 25px;\n"
"background: #B8B8B8;\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: #007AFF;\n"
"border-radius: 25px;\n"
"}")
        self.progressBar.setProperty("value", 40)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.now, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.next = QtWidgets.QFrame(self.hello)
        self.next.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        self.next.setMinimumSize(QtCore.QSize(560, 250))
        self.next.setMaximumSize(QtCore.QSize(560, 250))
        self.next.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.next.setStyleSheet("QWidget {\n"
"    background-color: #2B2B2B;\n"
"    border-radius: 20px;\n"
"}")
        self.next.setObjectName("next")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.next)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.next_start_end = QtWidgets.QLabel(self.next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_start_end.sizePolicy().hasHeightForWidth())
        self.next_start_end.setSizePolicy(sizePolicy)
        self.next_start_end.setMinimumSize(QtCore.QSize(520, 70))
        self.next_start_end.setMaximumSize(QtCore.QSize(520, 70))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(70)
        self.next_start_end.setFont(font)
        self.next_start_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.next_start_end.setObjectName("next_start_end")
        self.verticalLayout_4.addWidget(self.next_start_end)
        self.next_who = QtWidgets.QLabel(self.next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_who.sizePolicy().hasHeightForWidth())
        self.next_who.setSizePolicy(sizePolicy)
        self.next_who.setMinimumSize(QtCore.QSize(0, 70))
        self.next_who.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(50)
        self.next_who.setFont(font)
        self.next_who.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.next_who.setObjectName("next_who")
        self.verticalLayout_4.addWidget(self.next_who)
        self.verticalLayout.addWidget(self.next, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.next.raise_()
        self.now.raise_()
        self.verticalLayout_3.addWidget(self.hello, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clock.setText(_translate("MainWindow", "12:22"))
        self.now_start_end.setText(_translate("MainWindow", "13:30 - 13:45"))
        self.now_who.setText(_translate("MainWindow", "@namelessnobody"))
        self.now_what.setText(_translate("MainWindow", "agdx-prechadzka(report)"))
        self.next_start_end.setText(_translate("MainWindow", "13:45 - 15:00"))
        self.next_who.setText(_translate("MainWindow", "@danielmstc"))
