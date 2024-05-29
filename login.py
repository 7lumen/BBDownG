import os.path
import time

from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
import subprocess
from UI.qrcode_ui import Ui_Dialog
from tools import workdir, system, read_config


# 创建新线程
class WorkThread(QThread):
    s = Signal(str)

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        for i in range(181):
            time.sleep(1)
            if ((self.arg == 'login') and (os.path.exists(os.path.join(workdir, 'BBDown.data')))) or (
                    (self.arg == "logintv") and (os.path.exists(os.path.join(workdir, "BBDownTV.data")))):
                self.s.emit('登录成功')
                time.sleep(1)
                self.s.emit("关闭窗口")
                break
            elif os.path.exists(os.path.join(os.getcwd(), 'qrcode.png')):
                self.s.emit('请扫描二维码')
            else:
                self.s.emit('未获取到信息')


# 显示登录二维码窗口
class Login(QDialog, Ui_Dialog):
    def __init__(self, arg):
        super(Login, self).__init__()
        self.setupUi(self)
        self.arg = arg
        self.setWindowTitle('BBdown - 登录')

        self.label_qr.setScaledContents(True)  # 设置图片自适应大小

        # 判断登录类型和是否有登录后的data文件
        if (arg == 'login') and (os.path.exists(os.path.join(workdir, 'BBDown.data'))):
            os.remove(os.path.join(workdir, 'BBDown.data'))
        if (arg == 'logintv') and (os.path.exists(os.path.join(workdir, 'BBDownTV.data'))):
            os.remove(os.path.join(workdir, 'BBDownTV.data'))

        # 获取BBDown程序路径
        config = read_config()['lineEdit_bbdown']

        # 调用BBdown获取二维码
        if system == 'Windows':
            self.cmd = subprocess.Popen([f'{config}', f'{self.arg}'], shell=True)
        else:
            self.cmd = subprocess.Popen([f'{config}', f'{self.arg}'])
        self.execute()

    # 调用新线程
    def execute(self):
        self.work = WorkThread(self.arg)
        self.work.start()
        self.work.s.connect(self.display)

    # 显示图片和信息
    def display(self, s):
        self.label_qr.setPixmap(QPixmap(os.path.join(os.getcwd(), 'qrcode.png')))
        self.label.setText(s)
        if s == '关闭窗口':
            if system == 'Linux':
                subprocess.run(['kill', '-9', str(self.cmd.pid)])
            else:
                subprocess.run(['taskkill', '/F', '/T', '/PID', str(self.cmd.pid)], shell=True)
            self.close()
