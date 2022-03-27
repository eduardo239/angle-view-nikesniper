# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from a2 import Ui_Form as Ui_Angle_View
from r import Ui_Form as Ui_Ruler

class Ui_AngleViewNikesniper(object):
    def setupUi(self, AngleViewNikesniper):
        AngleViewNikesniper.setObjectName("AngleViewNikesniper")
        AngleViewNikesniper.resize(272, 84)
        self.screenwidth = QtWidgets.QDesktopWidget().screenGeometry().width()
        self.screenheight = QtWidgets.QDesktopWidget().screenGeometry().height()
        # position screen at the bottom of the screen
        AngleViewNikesniper.move(int(self.screenwidth / 2) - AngleViewNikesniper.width(), self.screenheight - AngleViewNikesniper.height() - 64)
        self.centralwidget = QtWidgets.QWidget(AngleViewNikesniper)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        AngleViewNikesniper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AngleViewNikesniper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        AngleViewNikesniper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AngleViewNikesniper)
        self.statusbar.setObjectName("statusbar")
        AngleViewNikesniper.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(AngleViewNikesniper)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.pushButton.clicked.connect(self.toogle_ruler_window)
        self.pushButton_2.clicked.connect(self.toogle_angle_window)
        
        self.angle_view_window = QtWidgets.QWidget()
        self.uia = Ui_Angle_View()
        self.uia.setupUi(self.angle_view_window)

        self.ruler_window = QtWidgets.QWidget()
        self.uia = Ui_Ruler()
        self.uia.setupUi(self.ruler_window)

        self.retranslateUi(AngleViewNikesniper)
        QtCore.QMetaObject.connectSlotsByName(AngleViewNikesniper)

    # TODO: add a ruler window
    def closeEvent(self, event):
        print("closing")	
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
      
    def toogle_angle_window(self):
        if self.angle_view_window.isHidden():
            self.pushButton_2.setText("close angle")
            self.angle_view_window.show()
        else:
            self.pushButton_2.setText("open angle")
            self.angle_view_window.hide()

    def toogle_ruler_window(self):
        if self.ruler_window.isHidden():
            self.pushButton.setText("close ruler")
            self.ruler_window.show()
        else:
            self.pushButton.setText("open ruler")
            self.ruler_window.hide()

    def open_ruler_window(self):
        self.ruler_window = QtWidgets.QWidget()
        self.uir = Ui_Ruler()
        self.uir.setupUi(self.ruler_window)
        self.ruler_window.show()

    def close_ruler_window(self):
        self.ruler_window.hide()

    def retranslateUi(self, AngleViewNikesniper):
        _translate = QtCore.QCoreApplication.translate
        AngleViewNikesniper.setWindowTitle(_translate("AngleViewNikesniper", "MainWindow"))
        self.pushButton.setText(_translate("AngleViewNikesniper", "open ruler"))
        self.pushButton_2.setText(_translate("AngleViewNikesniper", "open angle"))
        self.menuFile.setTitle(_translate("AngleViewNikesniper", "File"))
        self.actionExit.setText(_translate("AngleViewNikesniper", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AngleViewNikesniper = QtWidgets.QMainWindow()
    ui = Ui_AngleViewNikesniper()
    ui.setupUi(AngleViewNikesniper)
    AngleViewNikesniper.show()
    sys.exit(app.exec_())