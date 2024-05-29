# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog_SetUp(object):
    def setupUi(self, Dialog_SetUp):
        if not Dialog_SetUp.objectName():
            Dialog_SetUp.setObjectName(u"Dialog_SetUp")
        Dialog_SetUp.resize(806, 528)
        Dialog_SetUp.setMinimumSize(QSize(806, 528))
        Dialog_SetUp.setMaximumSize(QSize(999, 999))
        self.verticalLayout_12 = QVBoxLayout(Dialog_SetUp)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Dialog_SetUp)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_audio_only = QCheckBox(self.groupBox)
        self.checkBox_audio_only.setObjectName(u"checkBox_audio_only")
        self.checkBox_audio_only.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_audio_only)

        self.checkBox_video_only = QCheckBox(self.groupBox)
        self.checkBox_video_only.setObjectName(u"checkBox_video_only")
        self.checkBox_video_only.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_video_only)

        self.checkBox_sub_only = QCheckBox(self.groupBox)
        self.checkBox_sub_only.setObjectName(u"checkBox_sub_only")
        self.checkBox_sub_only.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_sub_only)

        self.checkBox_danmaku = QCheckBox(self.groupBox)
        self.checkBox_danmaku.setObjectName(u"checkBox_danmaku")
        self.checkBox_danmaku.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_danmaku)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_9 = QGroupBox(Dialog_SetUp)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_ia = QCheckBox(self.groupBox_9)
        self.checkBox_ia.setObjectName(u"checkBox_ia")
        self.checkBox_ia.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_ia)

        self.checkBox_info = QCheckBox(self.groupBox_9)
        self.checkBox_info.setObjectName(u"checkBox_info")
        self.checkBox_info.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_info)

        self.checkBox_hs = QCheckBox(self.groupBox_9)
        self.checkBox_hs.setObjectName(u"checkBox_hs")
        self.checkBox_hs.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_hs)

        self.checkBox_debug = QCheckBox(self.groupBox_9)
        self.checkBox_debug.setObjectName(u"checkBox_debug")
        self.checkBox_debug.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_debug)


        self.horizontalLayout.addWidget(self.groupBox_9)

        self.groupBox_5 = QGroupBox(Dialog_SetUp)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_token = QCheckBox(self.groupBox_5)
        self.checkBox_token.setObjectName(u"checkBox_token")
        self.checkBox_token.setFont(font)

        self.verticalLayout_8.addWidget(self.checkBox_token)

        self.lineEdit_token = QLineEdit(self.groupBox_5)
        self.lineEdit_token.setObjectName(u"lineEdit_token")
        self.lineEdit_token.setFont(font)

        self.verticalLayout_8.addWidget(self.lineEdit_token)

        self.checkBox_c = QCheckBox(self.groupBox_5)
        self.checkBox_c.setObjectName(u"checkBox_c")
        self.checkBox_c.setFont(font)

        self.verticalLayout_8.addWidget(self.checkBox_c)

        self.lineEdit_c = QLineEdit(self.groupBox_5)
        self.lineEdit_c.setObjectName(u"lineEdit_c")
        self.lineEdit_c.setFont(font)

        self.verticalLayout_8.addWidget(self.lineEdit_c)


        self.horizontalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_10 = QGroupBox(Dialog_SetUp)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_skip_subtitle = QCheckBox(self.groupBox_10)
        self.checkBox_skip_subtitle.setObjectName(u"checkBox_skip_subtitle")
        self.checkBox_skip_subtitle.setFont(font)

        self.verticalLayout_4.addWidget(self.checkBox_skip_subtitle)

        self.checkBox_skip_cover = QCheckBox(self.groupBox_10)
        self.checkBox_skip_cover.setObjectName(u"checkBox_skip_cover")
        self.checkBox_skip_cover.setFont(font)

        self.verticalLayout_4.addWidget(self.checkBox_skip_cover)

        self.checkBox_skip_mux = QCheckBox(self.groupBox_10)
        self.checkBox_skip_mux.setObjectName(u"checkBox_skip_mux")
        self.checkBox_skip_mux.setFont(font)

        self.verticalLayout_4.addWidget(self.checkBox_skip_mux)

        self.checkBox_skip_ai = QCheckBox(self.groupBox_10)
        self.checkBox_skip_ai.setObjectName(u"checkBox_skip_ai")
        self.checkBox_skip_ai.setFont(font)
        self.checkBox_skip_ai.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_skip_ai)


        self.horizontalLayout_2.addWidget(self.groupBox_10)

        self.groupBox_4 = QGroupBox(Dialog_SetUp)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(168, 155))
        self.groupBox_4.setMaximumSize(QSize(178, 162))
        self.groupBox_4.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_mp4box = QCheckBox(self.groupBox_4)
        self.checkBox_mp4box.setObjectName(u"checkBox_mp4box")
        self.checkBox_mp4box.setFont(font)

        self.verticalLayout_6.addWidget(self.checkBox_mp4box)

        self.checkBox_mp4box_path = QCheckBox(self.groupBox_4)
        self.checkBox_mp4box_path.setObjectName(u"checkBox_mp4box_path")
        self.checkBox_mp4box_path.setFont(font)

        self.verticalLayout_6.addWidget(self.checkBox_mp4box_path)

        self.lineEdit_mp4box_path = QLineEdit(self.groupBox_4)
        self.lineEdit_mp4box_path.setObjectName(u"lineEdit_mp4box_path")
        self.lineEdit_mp4box_path.setFont(font)

        self.verticalLayout_6.addWidget(self.lineEdit_mp4box_path)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_11 = QGroupBox(Dialog_SetUp)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 0))
        self.groupBox_11.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_mt = QCheckBox(self.groupBox_11)
        self.checkBox_mt.setObjectName(u"checkBox_mt")
        self.checkBox_mt.setFont(font)
        self.checkBox_mt.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_mt)

        self.checkBox_force_http = QCheckBox(self.groupBox_11)
        self.checkBox_force_http.setObjectName(u"checkBox_force_http")
        self.checkBox_force_http.setFont(font)
        self.checkBox_force_http.setChecked(False)

        self.verticalLayout_10.addWidget(self.checkBox_force_http)

        self.checkBox_archives = QCheckBox(self.groupBox_11)
        self.checkBox_archives.setObjectName(u"checkBox_archives")

        self.verticalLayout_10.addWidget(self.checkBox_archives)

        self.checkBox_ua = QCheckBox(self.groupBox_11)
        self.checkBox_ua.setObjectName(u"checkBox_ua")

        self.verticalLayout_10.addWidget(self.checkBox_ua)

        self.lineEdit_ua = QLineEdit(self.groupBox_11)
        self.lineEdit_ua.setObjectName(u"lineEdit_ua")
        self.lineEdit_ua.setMinimumSize(QSize(0, 0))

        self.verticalLayout_10.addWidget(self.lineEdit_ua)

        self.checkBox_language = QCheckBox(self.groupBox_11)
        self.checkBox_language.setObjectName(u"checkBox_language")
        self.checkBox_language.setFont(font)

        self.verticalLayout_10.addWidget(self.checkBox_language)

        self.lineEdit_language = QLineEdit(self.groupBox_11)
        self.lineEdit_language.setObjectName(u"lineEdit_language")
        self.lineEdit_language.setFont(font)

        self.verticalLayout_10.addWidget(self.lineEdit_language)


        self.horizontalLayout_2.addWidget(self.groupBox_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.groupBox_7 = QGroupBox(Dialog_SetUp)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_F = QCheckBox(self.groupBox_7)
        self.checkBox_F.setObjectName(u"checkBox_F")
        self.checkBox_F.setFont(font)

        self.verticalLayout_2.addWidget(self.checkBox_F)

        self.lineEdit_F = QLineEdit(self.groupBox_7)
        self.lineEdit_F.setObjectName(u"lineEdit_F")
        self.lineEdit_F.setFont(font)

        self.verticalLayout_2.addWidget(self.lineEdit_F)

        self.checkBox_M = QCheckBox(self.groupBox_7)
        self.checkBox_M.setObjectName(u"checkBox_M")
        self.checkBox_M.setFont(font)

        self.verticalLayout_2.addWidget(self.checkBox_M)

        self.lineEdit_M = QLineEdit(self.groupBox_7)
        self.lineEdit_M.setObjectName(u"lineEdit_M")
        self.lineEdit_M.setFont(font)

        self.verticalLayout_2.addWidget(self.lineEdit_M)

        self.label_val = QLabel(self.groupBox_7)
        self.label_val.setObjectName(u"label_val")
        self.label_val.setFont(font)

        self.verticalLayout_2.addWidget(self.label_val)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.horizontalLayout_3.addWidget(self.groupBox_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_12 = QGroupBox(Dialog_SetUp)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_use_aria2c = QCheckBox(self.groupBox_12)
        self.checkBox_use_aria2c.setObjectName(u"checkBox_use_aria2c")
        self.checkBox_use_aria2c.setFont(font)

        self.verticalLayout_7.addWidget(self.checkBox_use_aria2c)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_aria2c_path = QCheckBox(self.groupBox_12)
        self.checkBox_aria2c_path.setObjectName(u"checkBox_aria2c_path")
        self.checkBox_aria2c_path.setFont(font)
        self.checkBox_aria2c_path.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox_aria2c_path)

        self.lineEdit_aria2c_path = QLineEdit(self.groupBox_12)
        self.lineEdit_aria2c_path.setObjectName(u"lineEdit_aria2c_path")
        self.lineEdit_aria2c_path.setFont(font)
        self.lineEdit_aria2c_path.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEdit_aria2c_path)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_aria2c_proxy = QCheckBox(self.groupBox_12)
        self.checkBox_aria2c_proxy.setObjectName(u"checkBox_aria2c_proxy")
        self.checkBox_aria2c_proxy.setFont(font)

        self.horizontalLayout_7.addWidget(self.checkBox_aria2c_proxy)

        self.lineEdit_aria2c_proxy = QLineEdit(self.groupBox_12)
        self.lineEdit_aria2c_proxy.setObjectName(u"lineEdit_aria2c_proxy")
        self.lineEdit_aria2c_proxy.setFont(font)

        self.horizontalLayout_7.addWidget(self.lineEdit_aria2c_proxy)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_aria2c_args = QCheckBox(self.groupBox_12)
        self.checkBox_aria2c_args.setObjectName(u"checkBox_aria2c_args")
        self.checkBox_aria2c_args.setFont(font)
        self.checkBox_aria2c_args.setChecked(True)

        self.horizontalLayout_8.addWidget(self.checkBox_aria2c_args)

        self.lineEdit_aria2c_args = QLineEdit(self.groupBox_12)
        self.lineEdit_aria2c_args.setObjectName(u"lineEdit_aria2c_args")
        self.lineEdit_aria2c_args.setFont(font)

        self.horizontalLayout_8.addWidget(self.lineEdit_aria2c_args)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addWidget(self.groupBox_12)

        self.horizontalSpacer = QSpacerItem(24, 0, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.groupBox_13 = QGroupBox(Dialog_SetUp)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFont(font)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_enable_proxy = QCheckBox(self.groupBox_13)
        self.checkBox_enable_proxy.setObjectName(u"checkBox_enable_proxy")
        self.checkBox_enable_proxy.setFont(font)
        self.checkBox_enable_proxy.setChecked(False)

        self.verticalLayout_9.addWidget(self.checkBox_enable_proxy)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_host = QCheckBox(self.groupBox_13)
        self.checkBox_host.setObjectName(u"checkBox_host")
        self.checkBox_host.setFont(font)

        self.horizontalLayout_9.addWidget(self.checkBox_host)

        self.lineEdit_host = QLineEdit(self.groupBox_13)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        self.lineEdit_host.setFont(font)

        self.horizontalLayout_9.addWidget(self.lineEdit_host)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_ep_host = QCheckBox(self.groupBox_13)
        self.checkBox_ep_host.setObjectName(u"checkBox_ep_host")
        self.checkBox_ep_host.setFont(font)

        self.horizontalLayout_11.addWidget(self.checkBox_ep_host)

        self.lineEdit_ep_host = QLineEdit(self.groupBox_13)
        self.lineEdit_ep_host.setObjectName(u"lineEdit_ep_host")
        self.lineEdit_ep_host.setFont(font)

        self.horizontalLayout_11.addWidget(self.lineEdit_ep_host)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_area = QCheckBox(self.groupBox_13)
        self.checkBox_area.setObjectName(u"checkBox_area")
        self.checkBox_area.setFont(font)

        self.horizontalLayout_10.addWidget(self.checkBox_area)

        self.lineEdit_area = QLineEdit(self.groupBox_13)
        self.lineEdit_area.setObjectName(u"lineEdit_area")
        self.lineEdit_area.setFont(font)

        self.horizontalLayout_10.addWidget(self.lineEdit_area)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)


        self.horizontalLayout_4.addWidget(self.groupBox_13)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(13, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_bbdown = QLabel(Dialog_SetUp)
        self.label_bbdown.setObjectName(u"label_bbdown")
        self.label_bbdown.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_bbdown)

        self.lineEdit_bbdown = QLineEdit(Dialog_SetUp)
        self.lineEdit_bbdown.setObjectName(u"lineEdit_bbdown")

        self.horizontalLayout_13.addWidget(self.lineEdit_bbdown)

        self.pushButton_bbdown = QPushButton(Dialog_SetUp)
        self.pushButton_bbdown.setObjectName(u"pushButton_bbdown")
        self.pushButton_bbdown.setFont(font)

        self.horizontalLayout_13.addWidget(self.pushButton_bbdown)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_3 = QSpacerItem(24, 18, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_ffmpeg = QCheckBox(Dialog_SetUp)
        self.checkBox_ffmpeg.setObjectName(u"checkBox_ffmpeg")
        self.checkBox_ffmpeg.setFont(font)
        self.checkBox_ffmpeg.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox_ffmpeg)

        self.lineEdit_ffmpeg = QLineEdit(Dialog_SetUp)
        self.lineEdit_ffmpeg.setObjectName(u"lineEdit_ffmpeg")
        self.lineEdit_ffmpeg.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_ffmpeg)

        self.pushButton_ffmpeg = QPushButton(Dialog_SetUp)
        self.pushButton_ffmpeg.setObjectName(u"pushButton_ffmpeg")
        self.pushButton_ffmpeg.setEnabled(True)
        self.pushButton_ffmpeg.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_ffmpeg)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(728, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.pushButton_save = QPushButton(Dialog_SetUp)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(19, 31))
        self.pushButton_save.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_save)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.retranslateUi(Dialog_SetUp)

        QMetaObject.connectSlotsByName(Dialog_SetUp)
    # setupUi

    def retranslateUi(self, Dialog_SetUp):
        Dialog_SetUp.setWindowTitle(QCoreApplication.translate("Dialog_SetUp", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u4e0b\u8f7d\u9009\u9879", None))
        self.checkBox_audio_only.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ec5\u4e0b\u8f7d\u97f3\u9891", None))
        self.checkBox_video_only.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ec5\u4e0b\u8f7d\u89c6\u9891", None))
        self.checkBox_sub_only.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ec5\u4e0b\u8f7d\u5b57\u5e55", None))
        self.checkBox_danmaku.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4e0b\u8f7d\u5f39\u5e55", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u4ea4\u4e92\u9009\u9879", None))
        self.checkBox_ia.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ea4\u4e92\u5f0f\u9009\u62e9\u6e05\u6670\u5ea6", None))
        self.checkBox_info.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ec5\u89e3\u6790\u800c\u4e0d\u8fdb\u884c\u4e0b\u8f7d", None))
        self.checkBox_hs.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4e0d\u663e\u793a\u6240\u6709\u97f3\u89c6\u9891\u6d41", None))
        self.checkBox_debug.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8f93\u51fa\u8c03\u8bd5\u65e5\u5fd7", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_SetUp", u"cookies", None))
#if QT_CONFIG(tooltip)
        self.checkBox_token.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8bbe\u7f6eaccess_token\u7528\u4ee5\u4e0b\u8f7dTV/APP\u63a5\u53e3\u7684\u4f1a\u5458\u5185\u5bb9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_token.setText(QCoreApplication.translate("Dialog_SetUp", u"\u5355\u72ec\u8bbe\u7f6eaccess_token", None))
        self.lineEdit_token.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.checkBox_c.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8bbe\u7f6e\u5b57\u7b26\u4e32cookie\u7528\u4ee5\u4e0b\u8f7d\u7f51\u9875\u63a5\u53e3\u7684\u4f1a\u5458\u5185\u5bb9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_c.setText(QCoreApplication.translate("Dialog_SetUp", u"\u5355\u72ec\u8bbe\u7f6ecookie", None))
        self.lineEdit_c.setPlaceholderText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u8df3\u8fc7\u9009\u9879", None))
        self.checkBox_skip_subtitle.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8df3\u8fc7\u5b57\u5e55\u4e0b\u8f7d", None))
        self.checkBox_skip_cover.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8df3\u8fc7\u5c01\u9762\u4e0b\u8f7d", None))
        self.checkBox_skip_mux.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8df3\u8fc7\u6df7\u6d41\u6b65\u9aa4", None))
        self.checkBox_skip_ai.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8df3\u8fc7AI\u5b57\u5e55\u4e0b\u8f7d", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_SetUp", u"MP4Box", None))
        self.checkBox_mp4box.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4f7f\u7528MP4Box\u6765\u6df7\u6d41", None))
        self.checkBox_mp4box_path.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8bbe\u7f6eMP4Box\u7684\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_mp4box_path.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>mp4box\u7684\u8def\u5f84</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_mp4box_path.setWhatsThis(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8def\u5f84\u4e0d\u8981\u5305\u542b\u7a7a\u683c</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox_11.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u5176\u4ed6", None))
        self.checkBox_mt.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4f7f\u7528\u591a\u7ebf\u7a0b\u4e0b\u8f7d", None))
        self.checkBox_force_http.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4f7f\u7528HTTP\u66ff\u6362HTTPS", None))
        self.checkBox_archives.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8bb0\u5f55\u5df2\u4e0b\u8f7d\u89c6\u9891\uff0c\u540e\u7eed\u8df3\u8fc7", None))
        self.checkBox_ua.setText(QCoreApplication.translate("Dialog_SetUp", u"\u6307\u5b9auser-agent", None))
#if QT_CONFIG(tooltip)
        self.checkBox_language.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8bbe\u7f6e\u6df7\u6d41\u7684\u97f3\u9891\u8bed\u8a00(\u4ee3\u7801)\uff0c\u5982chi, jpn\u7b49</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_language.setText(QCoreApplication.translate("Dialog_SetUp", u"\u8bbe\u7f6e\u6df7\u6d41\u7684\u97f3\u9891\u8bed\u8a00\u4ee3\u7801", None))
        self.lineEdit_language.setPlaceholderText(QCoreApplication.translate("Dialog_SetUp", u"\u5982chi,jpn", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u4f7f\u7528\u5185\u7f6e\u53d8\u91cf\u5b58\u50a8\u6587\u4ef6\u6587\u4ef6\u540d\u9009\u9879", None))
        self.checkBox_F.setText(QCoreApplication.translate("Dialog_SetUp", u"\u5355\u5206P", None))
        self.lineEdit_F.setPlaceholderText(QCoreApplication.translate("Dialog_SetUp", u"<videoTitle>", None))
        self.checkBox_M.setText(QCoreApplication.translate("Dialog_SetUp", u"\u591a\u5206P", None))
        self.lineEdit_M.setPlaceholderText(QCoreApplication.translate("Dialog_SetUp", u"<videoTitle>/[P<pageNumberWithZero>]<pageTitle>", None))
        self.label_val.setText(QCoreApplication.translate("Dialog_SetUp", u"\u5185\u7f6e\u53d8\u91cf", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Dialog_SetUp", u"<videoTitle>: \u89c6\u9891\u4e3b\u6807\u9898\n"
"<pageNumber>: \u89c6\u9891\u5206P\u5e8f\u53f7\n"
"<pageNumberWithZero>: \u89c6\u9891\u5206P\u5e8f\u53f7(\u524d\u7f00\u8865\u96f6)\n"
"<pageTitle>: \u89c6\u9891\u5206P\u6807\u9898\n"
"<bvid>: \u89c6\u9891BV\u53f7\n"
"<aid>: \u89c6\u9891aid\n"
"<cid>: \u89c6\u9891cid\n"
"<dfn>: \u89c6\u9891\u6e05\u6670\u5ea6\n"
"<res>: \u89c6\u9891\u5206\u8fa8\u7387\n"
"<fps>: \u89c6\u9891\u5e27\u7387\n"
"<videoCodecs>: \u89c6\u9891\u7f16\u7801\n"
"<videoBandwidth>: \u89c6\u9891\u7801\u7387\n"
"<audioCodecs>: \u97f3\u9891\u7f16\u7801\n"
"<audioBandwidth>: \u97f3\u9891\u7801\u7387\n"
"<ownerName>: \u4e0a\u4f20\u8005\u540d\u79f0\n"
"<ownerMid>: \u4e0a\u4f20\u8005mid\n"
"<publishDate>: \u6536\u85cf\u5939/\u756a\u5267/\u5408\u96c6\u53d1\u5e03\u65f6\u95f4\n"
"<videoDate>: \u89c6\u9891\u53d1\u5e03\u65f6\u95f4(\u5206p\u89c6\u9891\u53d1\u5e03\u65f6\u95f4\u4e0e<publishDate>\u76f8\u540c)\n"
"<apiType>: API\u7c7b\u578b(TV/APP/INTL/WEB)\n"
"\u9ed8\u8ba4\u4e3a: <videoTitle>", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Dialog_SetUp", u"aria2c", None))
        self.checkBox_use_aria2c.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4f7f\u7528aria2c", None))
        self.checkBox_aria2c_path.setText(QCoreApplication.translate("Dialog_SetUp", u"\u6587\u4ef6\u8def\u5f84", None))
        self.lineEdit_aria2c_path.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox_aria2c_proxy.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8c03\u7528aria2c\u8fdb\u884c\u4e0b\u8f7d\u65f6\u7684\u4ee3\u7406\u5730\u5740\u914d\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_aria2c_proxy.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ee3\u7406\u5730\u5740", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_aria2c_proxy.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>\u8c03\u7528aria2c\u8fdb\u884c\u4e0b\u8f7d\u65f6\u7684\u4ee3\u7406\u5730\u5740\u914d\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_aria2c_args.setText(QCoreApplication.translate("Dialog_SetUp", u"\u9644\u52a0\u53c2\u6570", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Dialog_SetUp", u"\u4ee3\u7406", None))
        self.checkBox_enable_proxy.setText(QCoreApplication.translate("Dialog_SetUp", u"\u542f\u7528\u4ee3\u7406", None))
        self.checkBox_host.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4ee3\u7406\u5730\u5740", None))
        self.checkBox_ep_host.setText(QCoreApplication.translate("Dialog_SetUp", u"\u756a\u5267\u4ee3\u7406", None))
        self.checkBox_area.setText(QCoreApplication.translate("Dialog_SetUp", u"\u5730\u533a\u6307\u5b9a", None))
        self.lineEdit_area.setText("")
        self.lineEdit_area.setPlaceholderText(QCoreApplication.translate("Dialog_SetUp", u"\u5982hk", None))
        self.label_bbdown.setText(QCoreApplication.translate("Dialog_SetUp", u"BBDown\u4f4d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_bbdown.setToolTip(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p>BBDown \u7a0b\u5e8f\u4f4d\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_bbdown.setWhatsThis(QCoreApplication.translate("Dialog_SetUp", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_bbdown.setText(QCoreApplication.translate("Dialog_SetUp", u"\u6d4f\u89c8", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_ffmpeg.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.checkBox_ffmpeg.setText(QCoreApplication.translate("Dialog_SetUp", u"ffmpeg", None))
        self.lineEdit_ffmpeg.setText("")
        self.pushButton_ffmpeg.setText(QCoreApplication.translate("Dialog_SetUp", u"\u6d4f\u89c8", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog_SetUp", u"\u4fdd\u5b58", None))
    # retranslateUi

