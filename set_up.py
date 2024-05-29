import os

from PySide6.QtWidgets import QDialog, QFileDialog

from UI.setup_ui import Ui_Dialog_SetUp
from tools import save_config, load_config, workdir, bbdown_path, system

h = '.exe' if system == 'Windows' else ''


class Window(QDialog, Ui_Dialog_SetUp):
    def __init__(self, flag):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('BBDownG - 设置')

        if flag:
            self.lineEdit_ffmpeg.setText(os.path.join(workdir, f'ffmpeg{h}'))  # 默认ffmpeg位置
            self.lineEdit_aria2c_path.setText(os.path.join(workdir, f'aria2c{h}'))  # 默认aria2c位置
            self.lineEdit_bbdown.setText(bbdown_path)  # 默认BBDown路径
            self.lineEdit_aria2c_args.setText('-x16 -s16 -j16 -k 5M')
            save_config(self)

        load_config(self)  # 加载配置文件
        self.pushButton_save.clicked.connect(self.save)  # 保存修改后的配置
        self.pushButton_ffmpeg.clicked.connect(self.ffmpeg_path)
        self.pushButton_bbdown.clicked.connect(self.bbdown_path)

    # 选择ffmpeg程序路径
    def ffmpeg_path(self):
        ffmpeg_file = QFileDialog.getOpenFileName(None, '选择文件', workdir, f'ffmpeg (ffmpeg{h})')[0]
        if ffmpeg_file:
            self.lineEdit_ffmpeg.setText(ffmpeg_file)

    # 选择BBDown程序路径
    def bbdown_path(self):
        bbdown_file = QFileDialog.getOpenFileName(None, '选择文件', workdir, f'BBDown (BBDown{h})')[0]
        if bbdown_file:
            self.lineEdit_bbdown.setText(bbdown_file)

    def save(self):
        save_config(self)  # 保存修改后的配置
        self.close()  # 关闭窗口
