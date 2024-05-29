# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrcode_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QSize(400, 400))
        Dialog.setMaximumSize(QSize(400, 400))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_qr = QLabel(Dialog)
        self.label_qr.setObjectName(u"label_qr")
        self.label_qr.setMinimumSize(QSize(214, 214))

        self.verticalLayout.addWidget(self.label_qr)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(9)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_qr.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u83b7\u53d6\u4e8c\u7ef4\u7801\u4e2d", None))
    # retranslateUi

