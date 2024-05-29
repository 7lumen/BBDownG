# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(544, 381)
        MainWindow.setMinimumSize(QSize(544, 381))
        MainWindow.setMaximumSize(QSize(544, 381))
        self.action_set_up = QAction(MainWindow)
        self.action_set_up.setObjectName(u"action_set_up")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_login = QPushButton(self.groupBox_4)
        self.pushButton_login.setObjectName(u"pushButton_login")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(10)
        self.pushButton_login.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_login)

        self.pushButton_logintv = QPushButton(self.groupBox_4)
        self.pushButton_logintv.setObjectName(u"pushButton_logintv")
        self.pushButton_logintv.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_logintv)


        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.groupBox_3.setSizeIncrement(QSize(0, 0))
        self.groupBox_3.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_source = QComboBox(self.groupBox_3)
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.setObjectName(u"comboBox_source")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_source.sizePolicy().hasHeightForWidth())
        self.comboBox_source.setSizePolicy(sizePolicy)
        self.comboBox_source.setSizeIncrement(QSize(0, 0))
        self.comboBox_source.setFont(font)

        self.horizontalLayout_3.addWidget(self.comboBox_source)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_encoding = QComboBox(self.groupBox_3)
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.setObjectName(u"comboBox_encoding")
        self.comboBox_encoding.setFont(font)

        self.horizontalLayout_4.addWidget(self.comboBox_encoding)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_p = QCheckBox(self.groupBox)
        self.checkBox_p.setObjectName(u"checkBox_p")
        self.checkBox_p.setFont(font)

        self.gridLayout.addWidget(self.checkBox_p, 1, 1, 1, 1)

        self.radioButton_p_all = QRadioButton(self.groupBox)
        self.radioButton_p_all.setObjectName(u"radioButton_p_all")
        self.radioButton_p_all.setFont(font)

        self.gridLayout.addWidget(self.radioButton_p_all, 0, 1, 1, 1)

        self.lineEdit_p = QLineEdit(self.groupBox)
        self.lineEdit_p.setObjectName(u"lineEdit_p")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_p.sizePolicy().hasHeightForWidth())
        self.lineEdit_p.setSizePolicy(sizePolicy1)
        self.lineEdit_p.setMinimumSize(QSize(0, 0))
        self.lineEdit_p.setMaximumSize(QSize(81, 20))
        self.lineEdit_p.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_p, 2, 1, 1, 1)

        self.radioButton_p_current = QRadioButton(self.groupBox)
        self.radioButton_p_current.setObjectName(u"radioButton_p_current")
        self.radioButton_p_current.setEnabled(True)
        self.radioButton_p_current.setFont(font)
        self.radioButton_p_current.setTabletTracking(False)
        self.radioButton_p_current.setAcceptDrops(False)
        self.radioButton_p_current.setAutoFillBackground(False)
        self.radioButton_p_current.setCheckable(True)
        self.radioButton_p_current.setChecked(True)
        self.radioButton_p_current.setAutoRepeat(False)

        self.gridLayout.addWidget(self.radioButton_p_current, 0, 0, 1, 1)

        self.checkBox_p_delay = QCheckBox(self.groupBox)
        self.checkBox_p_delay.setObjectName(u"checkBox_p_delay")
        self.checkBox_p_delay.setFont(font)

        self.gridLayout.addWidget(self.checkBox_p_delay, 1, 0, 1, 1)

        self.lineEdit_p_delay = QLineEdit(self.groupBox)
        self.lineEdit_p_delay.setObjectName(u"lineEdit_p_delay")
        self.lineEdit_p_delay.setMinimumSize(QSize(0, 0))
        self.lineEdit_p_delay.setMaximumSize(QSize(81, 16777215))

        self.gridLayout.addWidget(self.lineEdit_p_delay, 2, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_dfn_1080P = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_1080P.setObjectName(u"radioButton_dfn_1080P")
        self.radioButton_dfn_1080P.setFont(font)

        self.gridLayout_2.addWidget(self.radioButton_dfn_1080P, 1, 0, 1, 1)

        self.radioButton_dfn_360P = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_360P.setObjectName(u"radioButton_dfn_360P")
        self.radioButton_dfn_360P.setFont(font)

        self.gridLayout_2.addWidget(self.radioButton_dfn_360P, 2, 1, 1, 1)

        self.radioButton_dfn_480P = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_480P.setObjectName(u"radioButton_dfn_480P")
        self.radioButton_dfn_480P.setFont(font)

        self.gridLayout_2.addWidget(self.radioButton_dfn_480P, 2, 0, 1, 1)

        self.radioButton_dfn_priority = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_priority.setObjectName(u"radioButton_dfn_priority")
        self.radioButton_dfn_priority.setFont(font)
        self.radioButton_dfn_priority.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_dfn_priority, 0, 0, 1, 1)

        self.radioButton_dfn_720P = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_720P.setObjectName(u"radioButton_dfn_720P")
        self.radioButton_dfn_720P.setFont(font)

        self.gridLayout_2.addWidget(self.radioButton_dfn_720P, 1, 1, 1, 1)

        self.comboBox_dfn_more = QComboBox(self.groupBox_2)
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.addItem("")
        self.comboBox_dfn_more.setObjectName(u"comboBox_dfn_more")
        self.comboBox_dfn_more.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_dfn_more, 3, 1, 1, 1)

        self.radioButton_dfn_more = QRadioButton(self.groupBox_2)
        self.radioButton_dfn_more.setObjectName(u"radioButton_dfn_more")
        self.radioButton_dfn_more.setFont(font)

        self.gridLayout_2.addWidget(self.radioButton_dfn_more, 3, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_dir = QLineEdit(self.centralwidget)
        self.lineEdit_dir.setObjectName(u"lineEdit_dir")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.lineEdit_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_dir.setSizePolicy(sizePolicy3)
        self.lineEdit_dir.setMinimumSize(QSize(0, 0))
        self.lineEdit_dir.setSizeIncrement(QSize(0, 0))
        self.lineEdit_dir.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit_dir)

        self.pushButton_save_dir = QPushButton(self.centralwidget)
        self.pushButton_save_dir.setObjectName(u"pushButton_save_dir")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.pushButton_save_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_save_dir.setSizePolicy(sizePolicy4)
        self.pushButton_save_dir.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_save_dir)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_url = QLineEdit(self.centralwidget)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        sizePolicy3.setHeightForWidth(self.lineEdit_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_url.setSizePolicy(sizePolicy3)
        self.lineEdit_url.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_url)

        self.pushButton_text = QPushButton(self.centralwidget)
        self.pushButton_text.setObjectName(u"pushButton_text")
        sizePolicy4.setHeightForWidth(self.pushButton_text.sizePolicy().hasHeightForWidth())
        self.pushButton_text.setSizePolicy(sizePolicy4)
        self.pushButton_text.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.pushButton_download = QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName(u"pushButton_download")
        sizePolicy4.setHeightForWidth(self.pushButton_download.sizePolicy().hasHeightForWidth())
        self.pushButton_download.setSizePolicy(sizePolicy4)
        self.pushButton_download.setMinimumSize(QSize(0, 0))
        self.pushButton_download.setSizeIncrement(QSize(0, 10))
        self.pushButton_download.setFont(font)

        self.horizontalLayout_7.addWidget(self.pushButton_download)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 544, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_set_up)
        self.menu.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_set_up.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u8d26\u53f7", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.pushButton_logintv.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\uff08TV\uff09", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f16\u7801&&\u4e0b\u8f7d\u6e90", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6e90\uff1a", None))
        self.comboBox_source.setItemText(0, QCoreApplication.translate("MainWindow", u"TV\u7aef", None))
        self.comboBox_source.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u7aef", None))
        self.comboBox_source.setItemText(2, QCoreApplication.translate("MainWindow", u"APP\u7aef", None))
        self.comboBox_source.setItemText(3, QCoreApplication.translate("MainWindow", u"\u56fd\u9645\u7aef", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f16\u7801\u683c\u5f0f\uff1a", None))
        self.comboBox_encoding.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u53ef\u7528\u7f16\u7801", None))
        self.comboBox_encoding.setItemText(1, QCoreApplication.translate("MainWindow", u"AVC", None))
        self.comboBox_encoding.setItemText(2, QCoreApplication.translate("MainWindow", u"AV1", None))
        self.comboBox_encoding.setItemText(3, QCoreApplication.translate("MainWindow", u"HEVC", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5206p", None))
        self.checkBox_p.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u5206p\u8303\u56f4", None))
        self.radioButton_p_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5206p", None))
        self.lineEdit_p.setText(QCoreApplication.translate("MainWindow", u"1-2", None))
        self.radioButton_p_current.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5206p", None))
        self.checkBox_p_delay.setText(QCoreApplication.translate("MainWindow", u"\u5206p\u4e0b\u8f7d\u95f4\u9694", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u753b\u8d28", None))
        self.radioButton_dfn_1080P.setText(QCoreApplication.translate("MainWindow", u"1080P \u9ad8\u6e05", None))
        self.radioButton_dfn_360P.setText(QCoreApplication.translate("MainWindow", u"360P \u6d41\u7545", None))
        self.radioButton_dfn_480P.setText(QCoreApplication.translate("MainWindow", u"480P \u6e05\u6670", None))
        self.radioButton_dfn_priority.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u4e0b\u8f7d\u6700\u9ad8\u753b\u8d28", None))
        self.radioButton_dfn_720P.setText(QCoreApplication.translate("MainWindow", u"720P \u9ad8\u6e05", None))
        self.comboBox_dfn_more.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u4e0b\u8f7d\u6700\u9ad8\u753b\u8d28", None))
        self.comboBox_dfn_more.setItemText(1, QCoreApplication.translate("MainWindow", u"8K \u8d85\u9ad8\u6e05", None))
        self.comboBox_dfn_more.setItemText(2, QCoreApplication.translate("MainWindow", u"\u675c\u6bd4\u89c6\u754c", None))
        self.comboBox_dfn_more.setItemText(3, QCoreApplication.translate("MainWindow", u"HDR \u771f\u5f69", None))
        self.comboBox_dfn_more.setItemText(4, QCoreApplication.translate("MainWindow", u"4K \u8d85\u6e05", None))
        self.comboBox_dfn_more.setItemText(5, QCoreApplication.translate("MainWindow", u"1080P \u9ad8\u5e27\u7387", None))
        self.comboBox_dfn_more.setItemText(6, QCoreApplication.translate("MainWindow", u"1080P \u9ad8\u7801\u7387", None))
        self.comboBox_dfn_more.setItemText(7, QCoreApplication.translate("MainWindow", u"720P \u9ad8\u5e27\u7387", None))

        self.radioButton_dfn_more.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.lineEdit_dir.setText("")
        self.pushButton_save_dir.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u5730\u5740\uff1a", None))
        self.pushButton_text.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

