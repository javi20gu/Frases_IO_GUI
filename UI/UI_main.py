# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(651, 361)
        Principal.setMinimumSize(QtCore.QSize(651, 361))
        Principal.setMaximumSize(QtCore.QSize(651, 361))
        Principal.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.texto = QtWidgets.QLabel(Principal)
        self.texto.setGeometry(QtCore.QRect(20, 0, 191, 71))
        self.texto.setStyleSheet("#texto {\n"
"    color: rgb(53, 52, 56);\n"
"    font: 87 18pt \"Segoe UI Black\";\n"
"}")
        self.texto.setObjectName("texto")
        self.inputTexto = QtWidgets.QLineEdit(Principal)
        self.inputTexto.setGeometry(QtCore.QRect(20, 80, 611, 41))
        self.inputTexto.setStyleSheet("#inputTexto {\n"
"    border-radius: 5px;\n"
"    border: 0.5px solid rgb(217, 217, 217);\n"
"    color: #989898;\n"
"    padding-left: 8px;\n"
"    font: 87 17pt \"Segoe UI Black\";\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.inputTexto.setText("")
        self.inputTexto.setCursorPosition(0)
        self.inputTexto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputTexto.setClearButtonEnabled(True)
        self.inputTexto.setObjectName("inputTexto")
        self.inputResultado = QtWidgets.QListWidget(Principal)
        self.inputResultado.setGeometry(QtCore.QRect(20, 161, 611, 171))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.inputResultado.setFont(font)
        self.inputResultado.setStyleSheet("#inputResultado {\n"
"    border: 0.5px solid rgb(217, 217, 217);\n"
"    color: rgb(112, 112, 112);\n"
"    border-radius: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 6px;\n"
"    padding-top: 6px;\n"
"}")
        self.inputResultado.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputResultado.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inputResultado.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.inputResultado.setObjectName("inputResultado")
        self.salir = QtWidgets.QPushButton(Principal)
        self.salir.setGeometry(QtCore.QRect(590, 20, 41, 41))
        self.salir.setStyleSheet("background-color: rgba(255, 255, 255, .0);")
        self.salir.setText("")
        self.salir.setIconSize(QtCore.QSize(53, 53))
        self.salir.setObjectName("salir")

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Frases IO"))
        self.texto.setText(_translate("Principal", "FRASES IO"))
        self.inputTexto.setPlaceholderText(_translate("Principal", "INTRODUCE TU FRASE O PALABRA"))

