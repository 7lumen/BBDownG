import os

from PySide6.QtWidgets import QDialog, QFileDialog

from UI.setup import Ui_Dialog_SetUp
from tools import save_config, load_config, workdir, get_bbdown_path, system

h = ".exe" if system == "Windows" else ""


class Window(QDialog, Ui_Dialog_SetUp):
    def __init__(self, flag):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("BBDownG - 设置")

        if flag:
            self.lineEdit_ffmpeg.setText(
                os.path.join(workdir, f"ffmpeg{h}")
            )  # 默认ffmpeg位置
            self.lineEdit_aria2c_path.setText(
                os.path.join(workdir, f"aria2c{h}")
            )  # 默认aria2c位置
            self.lineEdit_bbdown.setText(get_bbdown_path())  # 默认BBDown路径
            self.lineEdit_aria2c_args.setText("-x16 -s16 -j16 -k 5M")
            save_config(self)

        load_config(self)  # 加载配置文件
        self.pushButton_save.clicked.connect(self.save)  # 保存修改后的配置
        self.pushButton_ffmpeg.clicked.connect(self.ffmpeg_path)
        self.pushButton_bbdown.clicked.connect(self.bbdown_path)
        self.pushButton_aria2c.clicked.connect(self.aria2c_path)
        self.pushButton_mp4box.clicked.connect(self.mp4box_path)

    # 选择ffmpeg程序路径
    def ffmpeg_path(self):
        ffmpeg_file = QFileDialog.getOpenFileName(
            None, "选择文件", workdir, f"ffmpeg (ffmpeg{h})"
        )[0]
        if ffmpeg_file:
            self.lineEdit_ffmpeg.setText(ffmpeg_file)

    # 选择BBDownT程序路径
    def bbdown_path(self):
        bbdown_file = QFileDialog.getOpenFileName(
            None, "选择文件", workdir, f"BBDown.* (BBDown*{h})"
        )[0]
        if bbdown_file:
            self.lineEdit_bbdown.setText(bbdown_file)

    # 选择aria2c程序
    def aria2c_path(self):
        aria2c_file = QFileDialog.getOpenFileName(
            None, '选择文件', workdir, f"aria2c (aria2c{h})"
        )[0]
        if aria2c_file:
            self.lineEdit_aria2c_path.setText(aria2c_file)

    def mp4box_path(self):
        mp4box_file = QFileDialog.getOpenFileName(
            None, '选择文件', workdir, f"MP4Box.* (MP4Box*{h})"
        )[0]
        if mp4box_file:
            self.lineEdit_mp4box_path.setText(mp4box_file)

    def save(self):
        save_config(self)  # 保存修改后的配置
        self.close()  # 关闭窗口
