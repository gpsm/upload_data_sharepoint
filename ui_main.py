# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASEpCCGXr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(434, 149)
        Dialog.setMaximumSize(QSize(434, 150))
        Dialog.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.label_xmlPath = QLabel(Dialog)
        self.label_xmlPath.setObjectName(u"label_xmlPath")
        self.label_xmlPath.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_xmlPath.setFont(font)
        self.label_xmlPath.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 191, 92);\n"
"border: none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_xmlPath.setMargin(0)
        self.xmlFilePath = QTextEdit(Dialog)
        self.xmlFilePath.setObjectName(u"xmlFilePath")
        self.xmlFilePath.setGeometry(QRect(10, 50, 251, 31))
        self.xmlFilePath.setStyleSheet(u"border:2px solid rgb(85, 85, 127);\n"
"color: rgb(241, 241, 241);\n"
"border-radius: 10px;")
        self.xmlFilePath.setReadOnly(True)
        self.browseButton = QPushButton(Dialog)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(300, 50, 75, 31))
        self.browseButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.browseButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(31, 22, 66);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(26, 26, 26);\n"
"background-color: rgb(208, 208, 208);\n"
"border-radius:10px;\n"
"}")
        self.browseButton.setFlat(False)
        self.exportButton = QPushButton(Dialog)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(180, 100, 75, 31))
        self.exportButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.exportButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(31, 22, 66);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(26, 26, 26);\n"
"background-color: rgb(208, 208, 208);\n"
"border-radius:10px;\n"
"}")
        self.exportButton.setFlat(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"eTearSheet Exporter", None))
        self.label_xmlPath.setText(QCoreApplication.translate("Dialog", u"XML File Path:", None))
        self.xmlFilePath.setPlaceholderText(QCoreApplication.translate("Dialog", u"xml file path", None))
        self.browseButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.exportButton.setText(QCoreApplication.translate("Dialog", u"Export", None))
    # retranslateUi

