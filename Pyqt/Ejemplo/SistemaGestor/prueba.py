# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Form.resize(948, 591)
        Form.setStyleSheet(_fromUtf8("background-image: url(:/image/SGTPS.png);"))
        self.btn_register = QtGui.QToolButton(Form)
        self.btn_register.setGeometry(QtCore.QRect(350, 310, 169, 35))
        self.btn_register.setStyleSheet(_fromUtf8("background-image: url(:/image/THE.png);\n"
"border-style: flat;"))
        self.btn_register.setText(_fromUtf8(""))
        self.btn_register.setObjectName(_fromUtf8("btn_register"))
        self.ledit_email = QtGui.QLineEdit(Form)
        self.ledit_email.setGeometry(QtCore.QRect(290, 230, 301, 41))
        self.ledit_email.setStyleSheet(_fromUtf8("color: rgb(132, 132, 132);\n"
"background-image: url(:/image/Ingreso.png);\n"
"\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"border-style: flat;"))
        self.ledit_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_email.setObjectName(_fromUtf8("ledit_email"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ledit_email.setText(_translate("Form", "    Datos", None))

import resource

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

