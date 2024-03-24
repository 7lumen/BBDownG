# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_about(object):
    def setupUi(self, Dialog_about):
        if not Dialog_about.objectName():
            Dialog_about.setObjectName(u"Dialog_about")
        Dialog_about.resize(586, 312)
        Dialog_about.setMinimumSize(QSize(586, 312))
        Dialog_about.setMaximumSize(QSize(586, 312))
        self.verticalLayout = QVBoxLayout(Dialog_about)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Dialog_about)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textBrowser = QTextBrowser(Dialog_about)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(0, 89))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(10)
        self.textBrowser.setFont(font1)
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Dialog_about)

        QMetaObject.connectSlotsByName(Dialog_about)
    # setupUi

    def retranslateUi(self, Dialog_about):
        Dialog_about.setWindowTitle(QCoreApplication.translate("Dialog_about", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_about", u"\u5173\u4e8e BBDown - GUI", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog_about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5b8b\u4f53'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">BBDownG</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u672c\u8f6f\u4ef6\u662f\u4e2a\u4eba\u7ec3\u4e60\u6240\u5199\uff0c\u4ee3\u7801\u90e8\u5206\u548cui\u90e8\u5206\u5927\u591a\u6570\u662f\u53c2"
                        "\u8003(</span><a name=\"_GoBack\"></a><span style=\" font-size:12pt; text-decoration: line-through;\">\u6284</span><span style=\" font-size:12pt; text-decoration: line-through;\">\u88ad</span><span style=\" font-family:'SimSun'; font-size:12pt;\">)\u201c</span><span style=\" font-family:'SimSun'; font-size:12pt; font-weight:600;\">BBDOwn - GUI</span><span style=\" font-family:'SimSun'; font-size:12pt;\">\u201d\u8fd9\u4e2a\u8f6f\u4ef6\u3002\u8f6f\u4ef6\u56fe\u6807\u6765\u6e90\u4e8e\u7f51\u7edc\u3002\u672c\u8f6f\u4ef6\u5982\u679c\u6709\u4fb5\u6743\u95ee\u9898\uff0c\u8bf7\u8054\u7cfb\u4f5c\u8005\u5220\u9664\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:12pt;\"><br /></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u5f53\u524d\u7248\u672c\uff1av1.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:16pt; font-weight:600;\">\u81f4\u8c22 Credit</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:16pt; fon"
                        "t-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:14pt; font-weight:600;\">BBDown - GUI</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">\u8f6f\u4ef6\u4f5c\u8005\uff1aZhiyuShang</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">\u534f\u8bae\u8bb8\u53ef\uff1aMIT License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">\u4ed3\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/1299172402/BBDown_GUI\"><span style=\" font-family:'SimSun'; font-size:9pt; text-decoration: underline; color:#0000ff;\">https://github.com/1299172402/BBDown_GUI</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">\u8f6f\u4ef6\u4e0b\u8f7d\uff1a</span><a href=\"https://github.com/1299172402/BBDown_GUI/releases\"><span style=\" font-family:'SimSun'; font-size:9pt; text-decoration: underline; color:#0000ff;\">https://github.com/1299172402/BBDown_GUI/releases</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:14pt; font-weight:600;\">BBDown</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u4ed3\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/nilaoda/BBDown\"><span style=\" font-family:'SimSun'; text-decoration: underline; color:#0000ff;\">https://github.com/nilaoda/BBDown</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u8bb8\u53ef\u534f\u8bae\uff1a</span><a href=\"https://github.com/nilaoda/BBDown/blob/master/LICENSE\"><span style=\" font-family:'SimSun'; text-decoration: underline; color:#0000ff;\">https://github.com/nilaoda/BBDown/blob/master/LICENSE</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:14pt; font-weight:600;\">aria2c</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u4ed3\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/aria2/aria2\"><span style=\" font-family:'SimSun'; text-decoration: underline; color:#0000ff;\">https://github.com/aria2/aria2</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u8bb8\u53ef\u534f\u8bae\uff1a</span><a href=\"https://github.com/aria2/aria2/blob/master/COPYING\"><span style=\" font-family:'SimSun'; text-decoration: underline; color:#0000ff;\">https://github.com/aria2/aria2/blob/master/COPYING</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></"
                        "p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:14pt; font-weight:600;\">FFmpeg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u4ed3\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/FFmpeg/FFmpeg\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/FFmpeg/FFmpeg</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u8bb8\u53ef\u534f\u8bae\uff1a</span><a href=\"https://github.com/FFmpeg/FFmpeg/blob/master"
                        "/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md</span></a></p></body></html>", None))
    # retranslateUi

