# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/config.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(0, 290, 1024, 8))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(0, 350, 1024, 8))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1024, 8))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_isolate_limit = QtWidgets.QLabel(self.widget)
        self.label_isolate_limit.setGeometry(QtCore.QRect(520, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_isolate_limit.setFont(font)
        self.label_isolate_limit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_isolate_limit.setObjectName("label_isolate_limit")
        self.label_model = QtWidgets.QLabel(self.widget)
        self.label_model.setGeometry(QtCore.QRect(650, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_model.setFont(font)
        self.label_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_model.setObjectName("label_model")
        self.label_check_connect_level = QtWidgets.QLabel(self.widget)
        self.label_check_connect_level.setGeometry(QtCore.QRect(520, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_check_connect_level.setFont(font)
        self.label_check_connect_level.setAlignment(QtCore.Qt.AlignCenter)
        self.label_check_connect_level.setObjectName("label_check_connect_level")
        self.label_unit_mOhm = QtWidgets.QLabel(self.widget)
        self.label_unit_mOhm.setGeometry(QtCore.QRect(790, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_unit_mOhm.setFont(font)
        self.label_unit_mOhm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit_mOhm.setObjectName("label_unit_mOhm")
        self.label_resistance_limit = QtWidgets.QLabel(self.widget)
        self.label_resistance_limit.setGeometry(QtCore.QRect(520, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_resistance_limit.setFont(font)
        self.label_resistance_limit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resistance_limit.setObjectName("label_resistance_limit")
        self.label_unit_volt = QtWidgets.QLabel(self.widget)
        self.label_unit_volt.setGeometry(QtCore.QRect(790, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_unit_volt.setFont(font)
        self.label_unit_volt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit_volt.setObjectName("label_unit_volt")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(0, 230, 1024, 8))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(150, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_unit_Mohm = QtWidgets.QLabel(self.widget)
        self.label_unit_Mohm.setGeometry(QtCore.QRect(790, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_unit_Mohm.setFont(font)
        self.label_unit_Mohm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit_Mohm.setObjectName("label_unit_Mohm")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(150, 250, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(380, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_revision = QtWidgets.QLabel(self.widget)
        self.label_revision.setGeometry(QtCore.QRect(650, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_revision.setFont(font)
        self.label_revision.setAlignment(QtCore.Qt.AlignCenter)
        self.label_revision.setObjectName("label_revision")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(0, 170, 1024, 8))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.button_set_2 = QtWidgets.QPushButton(self.widget)
        self.button_set_2.setGeometry(QtCore.QRect(510, 420, 511, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_set_2.setFont(font)
        self.button_set_2.setObjectName("button_set_2")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 1024, 8))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(150, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setGeometry(QtCore.QRect(650, 190, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(150, 190, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(0, 410, 1024, 8))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.button_set = QtWidgets.QPushButton(self.widget)
        self.button_set.setGeometry(QtCore.QRect(0, 420, 511, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_set.setFont(font)
        self.button_set.setObjectName("button_set")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Model"))
        self.label_isolate_limit.setText(_translate("Form", "10.0"))
        self.label_model.setText(_translate("Form", "800A"))
        self.label_check_connect_level.setText(_translate("Form", "10.0"))
        self.label_unit_mOhm.setText(_translate("Form", "mOhm"))
        self.label_resistance_limit.setText(_translate("Form", "500.1"))
        self.label_unit_volt.setText(_translate("Form", "V"))
        self.label_10.setText(_translate("Form", "Resistance limit"))
        self.label_unit_Mohm.setText(_translate("Form", "Mohm"))
        self.label_8.setText(_translate("Form", "Check connect level"))
        self.label.setText(_translate("Form", "Model configuration detail"))
        self.label_revision.setText(_translate("Form", "001"))
        self.button_set_2.setText(_translate("Form", "Cancel"))
        self.label_12.setText(_translate("Form", "Isolate limit"))
        self.label_name.setText(_translate("Form", "P32A"))
        self.label_6.setText(_translate("Form", "Name"))
        self.label_4.setText(_translate("Form", "Revision"))
        self.button_set.setText(_translate("Form", "OK"))


