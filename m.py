from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from a import Ui_Form as Ui_Angle_View
from r import Ui_Form as Ui_Ruler

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(213, 57)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 213, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAngle_View = QtWidgets.QAction(MainWindow)
        self.actionAngle_View.setObjectName("actionAngle_View")
        self.actionAngle_View.triggered.connect(self.open_angle_view_window)
        self.actionRuler = QtWidgets.QAction(MainWindow)
        self.actionRuler.setObjectName("actionRuler")
        self.actionRuler.triggered.connect(self.open_ruler_window)
        self.menuFile.addAction(self.actionOpen)
        self.menuTools.addAction(self.actionAngle_View)
        self.menuTools.addAction(self.actionRuler)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.btn_close_ruler = QtWidgets.QPushButton()
        self.btn_close_ruler.setObjectName("btnClose")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.btn_close_ruler)

        self.btn_close_angle = QtWidgets.QPushButton()
        self.btn_close_angle.setObjectName("btnClose")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.btn_close_angle)

        self.btn_close_angle.clicked.connect(self.close_angle_view_window)

        self.open_angle_view_window()
        self.open_ruler_window()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_angle_view_window(self):
        self.angle_view_window = QtWidgets.QWidget()
        self.uia = Ui_Angle_View()
        self.uia.setupUi(self.angle_view_window)
        self.angle_view_window.show()
      
    def close_angle_view_window(self):
        self.angle_view_window.hide()

    def open_ruler_window(self):
        self.ruler_window = QtWidgets.QWidget()
        self.uir = Ui_Ruler()
        self.uir.setupUi(self.ruler_window)
        self.ruler_window.show()

    def close_ruler_window(self):
        self.ruler_window.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionOpen.setText(_translate("MainWindow", "Exit"))
        self.actionAngle_View.setText(_translate("MainWindow", "Angle View"))
        self.actionRuler.setText(_translate("MainWindow", "Ruler"))
        self.btn_close_ruler.setText(_translate("MainWindow", "Close Ruler"))
        self.btn_close_angle.setText(_translate("MainWindow", "Close Angle View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
