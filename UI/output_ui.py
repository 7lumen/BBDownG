# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog_output(object):
    def setupUi(self, Dialog_output):
        if not Dialog_output.objectName():
            Dialog_output.setObjectName(u"Dialog_output")
        Dialog_output.resize(617, 300)
        Dialog_output.setMinimumSize(QSize(617, 300))
        Dialog_output.setMaximumSize(QSize(617, 300))
        self.horizontalLayout_2 = QHBoxLayout(Dialog_output)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_cmd = QLineEdit(Dialog_output)
        self.lineEdit_cmd.setObjectName(u"lineEdit_cmd")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(10)
        self.lineEdit_cmd.setFont(font)
        self.lineEdit_cmd.setDragEnabled(True)
        self.lineEdit_cmd.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_cmd)

        self.pushButton_stop = QPushButton(Dialog_output)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_output = QTextEdit(Dialog_output)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setFont(font)
        self.textEdit_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_output)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_output)

        QMetaObject.connectSlotsByName(Dialog_output)
    # setupUi

    def retranslateUi(self, Dialog_output):
        Dialog_output.setWindowTitle(QCoreApplication.translate("Dialog_output", u"Dialog", None))
        self.lineEdit_cmd.setText("")
        self.pushButton_stop.setText(QCoreApplication.translate("Dialog_output", u"\u505c\u6b62", None))
        self.textEdit_output.setHtml(QCoreApplication.translate("Dialog_output", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5b8b\u4f53'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[\u8f93\u51fa\u5185\u5bb9]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

