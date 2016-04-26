# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout_OCR_app.ui'
#
# Created: Fri Feb 19 20:04:37 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1105, 719)
        self.Teach = QtGui.QPushButton(Form)
        self.Teach.setGeometry(QtCore.QRect(460, 120, 112, 41))
        self.Teach.setObjectName(_fromUtf8("Teach"))
        self.Quit = QtGui.QPushButton(Form)
        self.Quit.setGeometry(QtCore.QRect(380, 460, 131, 71))
        self.Quit.setObjectName(_fromUtf8("Quit"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 630, 681, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.Generations_display = QtGui.QTextBrowser(Form)
        self.Generations_display.setGeometry(QtCore.QRect(660, 60, 421, 531))
        self.Generations_display.setObjectName(_fromUtf8("Generations_display"))
        self.Title = QtGui.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(10, 20, 641, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.Name = QtGui.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(670, 680, 431, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.test_warn = QtGui.QLabel(Form)
        self.test_warn.setGeometry(QtCore.QRect(50, 180, 341, 31))
        self.test_warn.setObjectName(_fromUtf8("test_warn"))
        self.epochs_min = QtGui.QLabel(Form)
        self.epochs_min.setGeometry(QtCore.QRect(110, 220, 211, 21))
        self.epochs_min.setObjectName(_fromUtf8("epochs_min"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 300, 411, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Open_file = QtGui.QPushButton(Form)
        self.Open_file.setGeometry(QtCore.QRect(450, 300, 131, 41))
        self.Open_file.setObjectName(_fromUtf8("Open_file"))
        self.Number_gen = QtGui.QLineEdit(Form)
        self.Number_gen.setGeometry(QtCore.QRect(80, 120, 291, 41))
        self.Number_gen.setObjectName(_fromUtf8("Number_gen"))
        self.construct = QtGui.QPushButton(Form)
        self.construct.setGeometry(QtCore.QRect(70, 460, 181, 71))
        self.construct.setObjectName(_fromUtf8("construct"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Teach.setText(_translate("Form", "Teach", None))
        self.Quit.setText(_translate("Form", "Quit", None))
        self.Title.setText(_translate("Form", "OCR application with Neural Networks", None))
        self.Name.setText(_translate("Form", "Bryan Moore & Collin Olander", None))
        self.test_warn.setText(_translate("Form", "You have to teach the network before testing ", None))
        self.epochs_min.setText(_translate("Form", "1000 epochs is a good start", None))
        self.Open_file.setText(_translate("Form", "Open and Test", None))
        self.construct.setText(_translate("Form", "Construct Network", None))

