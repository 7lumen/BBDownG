import os
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

from UI.main_ui import Ui_MainWindow
from about import DialogAbout
from output import DialogOutput
from set_up import Window
from tools import workdir, save_config, load_config, read_config, config_path
from UI import icon


# 主界面
class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.parent = QMainWindow()
        self.setupUi(self.parent)
        self.parent.setWindowTitle('BBDownG - 1.0')

        flag = 0
        # 判断是否有配置文件
        if not os.path.isfile(config_path):
            self.lineEdit_dir.setText(os.path.join(workdir, 'Download'))  # 设置默认下载路径
            save_config(self)
            flag = 1
        else:
            load_config(self)  # 加载配置文件

        self.setup_window = Window(flag=flag)

        self.pushButton_save_dir.clicked.connect(self.down_path)  # 下载路径
        self.pushButton_text.clicked.connect(self.open_url_text)  # 选择文本文件
        self.action_set_up.triggered.connect(self.open_setup)  # 打开设置界面
        self.action_about.triggered.connect(self.open_about)  # 打开关于界面
        self.pushButton_download.clicked.connect(self.download)  # 开始下载

    # 设置下载保存路径
    def down_path(self):
        down_dir = QFileDialog.getExistingDirectory(None, '选择保存路径')
        if down_dir:
            self.lineEdit_dir.setText(down_dir)

    # 设置选择需要下载的url的文本文件
    def open_url_text(self):
        url_text = QFileDialog.getOpenFileName(None, '选择文件', '', '*.txt *.ini')[0]
        if url_text:
            self.lineEdit_url.setText(url_text)

    # 打开设置界面
    def open_setup(self):
        self.setup_window.exec_()

    # 开始下载
    def download(self):
        save_config(self)  # 保存配置
        args = self.arg()

        # 如果用户填写的下载地址是一个文本就根据文本内容下载
        print(args)
        if os.path.isfile(self.lineEdit_url.text()):
            with open(self.lineEdit_url.text(), 'r') as f:
                lines = f.readlines()
            for line in lines:
                if line.strip() == '':
                    return
                parts = args.split(' ')
                parts[1] = f'"{line.strip()}"'
                new_args = ' '.join(parts)

                # 将参数传递到下载界面
                output_window = DialogOutput(new_args, True)
                output_window.exec_()

        else:
            # 将参数传递到下载界面
            output_window = DialogOutput(args)
            output_window.exec_()

    # 下载参数
    def arg(self):
        args = ''

        # 读取配置文件
        config = read_config()

        # BBDown路径
        args += f'"{config["lineEdit_bbdown"]}"'

        # 视频下载地址
        args += f' "{self.lineEdit_url.text()}" '

        # 画质选择
        if self.radioButton_dfn_priority.isChecked():
            pass
        elif self.radioButton_dfn_1080P.isChecked():
            args += ' --dfn-priority "1080P 高清" '
        elif self.radioButton_dfn_720P.isChecked():
            args += ' --dfn-priority "720P 高清" '
        elif self.radioButton_dfn_480P.isChecked():
            args += ' --dfn-priority "480P 清晰" '
        elif self.radioButton_dfn_360P.isChecked():
            args += ' --dfn-priority "360P 流畅" '
        elif self.radioButton_dfn_more.isChecked():  # 更多选项
            if self.comboBox_dfn_more.currentIndex() != 0:
                dfn = self.comboBox_dfn_more.itemText(self.comboBox_dfn_more.currentIndex())
                args += f' --dfn-priority "{dfn}"'

        # 下载源选择
        choice = ['-tv', '', '-app', '-intl']
        args += ' ' + choice[self.comboBox_source.currentIndex()] + ' '

        # 下载视频编码选择
        if self.comboBox_encoding.currentIndex() != 0:
            choice = ['', 'AVC', 'AV1', 'HEVC']
            args += ' --encoding-priority ' + choice[self.comboBox_encoding.currentIndex()] + ' '

        # 指定FFmpeg路径
        if config['checkBox_ffmpeg']:
            args += f' --ffmpeg-path "{config["lineEdit_ffmpeg"]}" '

        # 下载分P选项
        if self.radioButton_p_current.isChecked():
            pass
        elif self.radioButton_p_all.isChecked():
            args += ' -p ALL '

        # 下载选项
        if config['checkBox_audio_only']:  # 仅下载音频
            args += ' --audio-only '
        if config['checkBox_video_only']:  # 仅下载视频
            args += ' --video-only '
        if config['checkBox_sub_only']:  # 仅下载字幕
            args += ' --sub-only '
        if config['checkBox_danmaku']:  # 下载弹幕
            args += ' -dd '

        # 交互选项
        if config['checkBox_ia']:  # 交互式选择清晰度
            args += ' -ia '
        if config['checkBox_info']:  # 仅解析而不进行下载
            args += ' -info '
        if config['checkBox_info']:  # 不显示所有音视频流
            args += ' -hs '
        if config['checkBox_info']:  # 输出调试日志
            args += ' --debug '

        # Cookies
        if config['checkBox_token']:  # 单独设置access_token
            args += f' -token "{config["lineEdit_token"]}" '
        if config['checkBox_c']:  # 单独设置cookie
            args += f' -c "{config["lineEdit_c"]}" '

        # 跳过选项
        if config['checkBox_skip_subtitle']:  # 跳过字幕下载
            args += ' --skip-subtitle '
        if config['checkBox_skip_cover']:  # 跳过封面下载
            args += ' --skip-cover '
        if config['checkBox_skip_mux']:  # 跳过混流步骤
            args += ' --skip-mux '
        if config['checkBox_skip_ai']:  # 跳过AI字幕下载
            args += ' --skip-ai true '
        else:
            args += ' --skip-ai false '

        # MP4box
        if config['checkBox_mp4box']:  # 使用MP4Box来混流
            args += ' --use-mp4box '
        if config['checkBox_mp4box_path']:  # 设置MP4Box的路径
            args += f' --mp4box-path "{config["lineEdit_mp4box_path"]}" '

        # 其他
        if config['checkBox_mt']:  # 使用多线程下载
            args += ' -mt true '
        else:
            args += ' -mt false '
        if config['checkBox_force_http']:  # 使用HTTP替换HTTPS
            args += ' --force-http  true '
        else:
            args += ' --force-http  false '
        if config['checkBox_language']:  # 设置混流的音频语言代码
            args += f' --language {config["lineEdit_language"]} '

        # 分P
        if config['checkBox_p']:  # 指定分p范围
            args += f' -p {config["lineEdit_p"]} '
        if config['checkBox_p_delay']:  # 分p下载间隔
            args += f' --delay-per-page {config["lineEdit_p_delay"]} '

        # aria2c
        if config['checkBox_use_aria2c']:  # 使用aria2c
            args += ' --use-aria2c '
            if config['checkBox_aria2c_path']:  # 文件路径
                args += f' --aria2c-path "{config["lineEdit_aria2c_path"]}" '
            if config['checkBox_aria2c_proxy']:  # 代理地址
                args += f' --aria2c-proxy {config["lineEdit_aria2c_proxy"]} '
            if config['checkBox_aria2c_args']:  # 附加参数
                args += f' --aria2c-args "{config["lineEdit_aria2c_args"]}" '

        # 文件名选项
        if config['checkBox_F']:  # 单分P
            args += f' -F "{config["lineEdit_F"]}" '
        if config['checkBox_M']:  # 多分P
            args += f' -M "{config["lineEdit_M"]}" '

        # 代理
        if config['checkBox_enable_proxy']:  # 启用代理
            if config['checkBox_host']:  # 代理地址
                args += f' --host {config["lineEdit_host"]} '
            if config['checkBox_ep_host']:  # 番剧代理
                args += f' --ep-host {config["lineEdit_ep_host"]} '
            if config['checkBox_area']:  # 地区指定
                args += f' --area {config["lineEdit_area"]} '

        # 下载路径
        args += f' --work-dir "{self.lineEdit_dir.text()}" '

        return args

    # 启动关于界面
    def open_about(self):
        about_window = DialogAbout()
        about_window.exec_()


# 启动主界面
def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':icon/icon.ico'))  # 设置图标
    window = MainWindow()
    window.parent.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
