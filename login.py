import os.path
import subprocess
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from UI.qrcode import Ui_Dialog
from tools import workdir, system, read_config


# 创建新线程
class WorkThread(QThread):
    status = Signal(str)

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):

        # 获取BBdown程序路径位置
        bbdown_path = os.path.dirname(read_config()["lineEdit_bbdown"])

        if self.arg == "login":
            data_file = os.path.join(bbdown_path, "BBDownT.data")
        elif self.arg == "logintv":
            data_file = os.path.join(bbdown_path, "BBDownTTV.data")

        qr_path = os.path.join(workdir, "qrcode.png")

        for i in range(181):
            time.sleep(1)
            # 登录成功判定
            if os.path.exists(data_file):
                self.status.emit("登录成功")
                time.sleep(1)
                self.status.emit("关闭窗口")
                return

            # 二维码存在
            if os.path.exists(qr_path):
                self.status.emit("请扫描二维码")
            else:
                self.status.emit("未获取到信息")

        # 超时兜底（避免窗口一直不关）
        self.status.emit("关闭窗口")


# 显示登录二维码窗口
class Login(QDialog, Ui_Dialog):
    def __init__(self, arg):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("BBdownG - 登录")

        self.label_qr.setScaledContents(True)  # 设置图片自适应大小

        # 获取BBdown程序路径
        bbdown_exe = read_config()["lineEdit_bbdown"]

        # 获取BBdown程序路径位置
        bbdown_path = os.path.dirname(read_config()["lineEdit_bbdown"])

        # 判断登录类型和是否有登录后的data文件
        if arg == "login":
            old = os.path.join(bbdown_path, "BBDownT.data")
        elif arg == "logintv":
            old = os.path.join(bbdown_path, "BBDownTTV.data")


        if os.path.exists(old):
            os.remove(old)

        # 调用BBdown获取二维码
        if system == "Windows":
            self.cmd = subprocess.Popen([f"{bbdown_exe}", f"{arg}"], shell=True)
        else:
            self.cmd = subprocess.Popen([f"{bbdown_exe}", f"{arg}"])

        # 调用新线程
        self.work_thread = WorkThread(arg)
        self.work_thread.status.connect(self.display)
        self.work_thread.start()

    # 显示图片和信息
    def display(self, mes):
        self.label_qr.setPixmap(QPixmap(os.path.join(workdir, "qrcode.png")))
        self.label.setText(mes)

        if mes == '关闭窗口':
            self.close_window()

    def close_window(self):
        """关闭后台运行的BBdownT"""

        if system == "Linux":
            subprocess.run(["kill", "-9", str(self.cmd.pid)])
        else:
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(self.cmd.pid)], shell=True
            )
        self.close()

    def closeEvent(self, event) -> None:
        """窗口关闭时确保线程和进程结束"""
        if hasattr(self, "work_thread") and self.work_thread.isRunning():
            self.work_thread.terminate()  # 强制终止线程（可接受）
        self.close_window()
        super().closeEvent(event)
