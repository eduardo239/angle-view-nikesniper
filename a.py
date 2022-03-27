from PyQt5 import QtCore, QtGui, QtWidgets
import os
import math

class Ui_Form(object):
    def setupUi(self, Form):


        self.sty_button = "QPushButton {\n" \
        "    background-color: #1b1b1b;\n" \
        "    color: #ffffff;\n" \
        "    padding: 8px;\n" \
        "    font: normal 14px;\n" \
        "    border: 0px;\n" \
        "    outline: 0px;\n" \
        "    font-size: 14px;\n" \
        "}\n"

        self.sty_label = "QLabel {\n" \
        "    background-color: rgb(1, 0, 9);\n" \
        "    color: rgb(255, 255, 255);\n" \
        "    padding: 8px;\n" \
        "    font-size: 18px;\n" \
        "    border: 1px solid red;\n" \
        "    }\n"

        self.sty_angle_label = "QLabel {\n" \
        "    background-color: rgb(1, 0, 9);\n" \
        "    color: rgb(255, 0, 0);\n" \
        "    padding: 8px;\n" \
        "    font-size: 18px;\n" \
        "    border: 1px solid red;\n" \
        "    font-weight: bold;\n" \
        "    }\n"

        self.sty_dots = "QLabel#lblDots {\n" \
        "    background-color: #5500ff;\n" \
        "    border-style: none;\n" \
        "    padding: 8px;\n" \
        "    font: bold 20px;\n" \
        "    border-width: 2px;\n" \
        "    border-radius: 0px;\n" \
        "    border-color: #2752B8;\n" \
        "    font-size: 14px;\n" \
        "}\n"


        Form.setObjectName("Form")
        Form.resize(710, 418)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        Form.setFixedSize(Form.size())
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 9, 400, 400))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setText("")
        self.pixmap = QtGui.QPixmap("angle.jpg")
        self.pixmapzoom = self.pixmap.scaled(self.pixmap.size() * 2, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmapzoom)
        self.label.setObjectName("label")
        self.label.mousePressEvent = self.getAngle

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(415, 9, 286, 400))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet(self.sty_angle_label)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setStyleSheet(self.sty_label)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet(self.sty_label)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setStyleSheet(self.sty_label)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet(self.sty_button)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet(self.sty_button)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.change_auto_update)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.clicked.connect(self.pick_folder)
        self.pushButton_3.setStyleSheet(self.sty_button)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblDots = QtWidgets.QLabel(Form)
        self.lblDots.setGeometry(QtCore.QRect(210, 210, 2, 2))
        self.lblDots.setStyleSheet(self.sty_dots)
        self.lblDots.setObjectName("lblDots")
        
        self.lblDots2 = QtWidgets.QLabel(Form)
        self.lblDots2.setGeometry(QtCore.QRect(208, 36, 2, 22))
        self.lblDots2.setStyleSheet(self.sty_dots)
        self.lblDots2.setObjectName("lblDots")

        self.lblDots3 = QtWidgets.QLabel(Form)
        self.lblDots3.setGeometry(QtCore.QRect(364, 208, 22, 2))
        self.lblDots3.setStyleSheet(self.sty_dots)
        self.lblDots3.setObjectName("lblDots")

        self.lblDots4 = QtWidgets.QLabel(Form)
        self.lblDots4.setGeometry(QtCore.QRect(208, 364, 2, 22))
        self.lblDots4.setStyleSheet(self.sty_dots)
        self.lblDots4.setObjectName("lblDots")

        self.lblDots5 = QtWidgets.QLabel(Form)
        self.lblDots5.setGeometry(QtCore.QRect(36, 209, 22, 2))
        self.lblDots5.setStyleSheet(self.sty_dots)
        self.lblDots5.setObjectName("lblDots")

        self.folder = ''
        self.fullPath = ''

        self.isAutoUpdate = False
        self.auto_update()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def change_auto_update(self):
        self.isAutoUpdate = False if self.isAutoUpdate else True
        print(self.isAutoUpdate)
        self.label_5.setText("AUTO UPDATE: ON" if self.isAutoUpdate else "AUTO UPDATE: OFF")

    def auto_update(self):
        if self.isAutoUpdate:
            print(1)
            self.files = os.listdir(self.path)
            self.file = self.files[-1]
            self.fullPath = self.folder + '/' + self.file
            self.pixmap = QtGui.QPixmap(self.folder + '/' + self.file)
            self.pixmapzoom = self.pixmap.scaled(self.pixmap.size() * 2, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmapzoom)
            self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        else:
            print(2)
        # self.pick_folder()

    def pick_folder(self):
        # get the last file from directory
        self.path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\Users\\eucri\\Downloads\\PANGUA\\PangyaUS_851\\capture')
        if self.path != '':
            self.folder = self.path
            # get all files from the directory
            self.files = os.listdir(self.path)
            # get the last file from the directory
            self.file = self.files[-1]
            # get the last file from the directory
            self.fullPath = self.folder + '/' + self.file
            self.pixmap = QtGui.QPixmap(self.folder + '/' + self.file)
            self.pixmapzoom = self.pixmap.scaled(self.pixmap.size() * 2, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmapzoom)
            self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
     
    def getAngle(self, event):
        # get the mouse position
        x = event.x()
        y = event.y()
        # get the image width and height
        width = self.label.width()
        height = self.label.height()
        # get distance from the x axis
        xDistance = abs(int(x - width/2))
        # get distance from the y axis
        yDistance = abs(int(y - height/2))
        # get distance from the center
        distance = math.sqrt(xDistance**2 + yDistance**2)
        print("x =", str(xDistance), ", y =", str(yDistance), ", distance =", str(distance))
        print("distance = ", str(int(distance)))
        # get cos, sin, tan
        cos = xDistance/distance
        sin = yDistance/distance
        tan =  0 if xDistance == 0 else yDistance/xDistance
        print("width = ", str(width), ", height = ", str(height))
        print("cos = ", str(cos), ", sin = ", str(sin), ", tan = ", str(tan))
        # get angle in degrees
        angle = abs(math.degrees(math.atan(tan)) - 90)
        print("angle = ", str(angle))
        self.label_2.setText(str(int(angle)))
        # update label_4 text
        self.label_3.setText("COS " + str(cos))
        self.label_4.setText("SIN " + str(sin))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "34"))
        self.label_3.setText(_translate("Form", "COS"))
        self.label_4.setText(_translate("Form", "SIN"))
        self.label_5.setText(_translate("Form", "AUTO UPDATE: "))
        self.pushButton.setText(_translate("Form", "UPDATE"))
        self.pushButton_2.setText(_translate("Form", "AUTO UPDATE"))
        self.pushButton_3.setText(_translate("Form", "FOLDER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
