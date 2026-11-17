import os.path
import subprocess
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from UI.qrcode import Ui_Dialog
from tools import workdir, system, read_config

LOGIN_FILES = {
    "login": "BBDownT.data",
    "logintv": "BBDownTTV.data",
}


# 创建新线程
class WorkThread(QThread):
    status = Signal(str)
    qr_ready = Signal(str)

    def __init__(self, data_file, qr_path, process, parent=None):
        super().__init__(parent)
        self.data_file = data_file
        self.qr_path = qr_path
        self.process = process
        self._last_qr_mtime = None

    def run(self):
        # 超时时间
        deadline = time.monotonic() + 181

        # 等待扫码登录
        while not self.isInterruptionRequested() and time.monotonic() < deadline:
            if os.path.isfile(self.data_file):
                self.status.emit("登录成功")
                return

            if os.path.isfile(self.qr_path):
                try:
                    mtime = os.path.getmtime(self.qr_path)
                except OSError:
                    mtime = None

                if mtime is not None and mtime != self._last_qr_mtime:
                    self._last_qr_mtime = mtime
                    self.qr_ready.emit(self.qr_path)
                    self.status.emit("请扫描二维码")

            if self.process.poll() is not None:
                self.status.emit("登录进程已退出")
                return

            self.status.emit("等待二维码")
            self.msleep(1000)

        if not self.isInterruptionRequested():
            self.status.emit("登录超时")


# 显示登录二维码窗口
class Login(QDialog, Ui_Dialog):
    def __init__(self, arg):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BBdownG - 登录")
        self.label_qr.setScaledContents(True)  # 设置图片自适应大小

        config = read_config()
        bbdown_exe = config.get("lineEdit_bbdown", "")
        if not bbdown_exe or not os.path.isfile(bbdown_exe):  # 获取BBdown程序路径
            raise FileNotFoundError("配置中的 BBDown 程序路径无效")

        bbdown_dir = os.path.dirname(os.path.abspath(bbdown_exe))  # 获取BBdown程序路径位置
        self.data_file = os.path.join(bbdown_dir, LOGIN_FILES[arg])
        self.qr_path = os.path.join(workdir, "qrcode.png")
        self.process = None
        self.work_thread = None
        self._closing = False

        try:
            os.remove(self.data_file)
        except FileNotFoundError:
            pass

        # 清除上次登录留下的二维码，避免显示过期图片。
        try:
            os.remove(self.qr_path)
        except FileNotFoundError:
            pass

        self.process = subprocess.Popen([bbdown_exe, arg])

        self.work_thread = WorkThread(
            self.data_file,
            self.qr_path,
            self.process,
            self,
        )
        self.work_thread.status.connect(self.label.setText)
        self.work_thread.qr_ready.connect(self.show_qrcode)
        self.work_thread.status.connect(self.handle_status)
        self.work_thread.start()

    # 显示图片和信息
    def show_qrcode(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            self.label_qr.setPixmap(pixmap)

    def handle_status(self, message):
        if message in ("登录成功", "登录超时", "登录进程已退出"):
            self.accept()

    def stop_process(self):
        if self.process is None or self.process.poll() is not None:
            return

        self.process.terminate()
        try:
            self.process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()

    def closeEvent(self, event):
        """窗口关闭时确保线程和进程结束"""
        self._closing = True

        if self.work_thread is not None and self.work_thread.isRunning():
            self.work_thread.requestInterruption()
            self.work_thread.wait(3000)

        self.stop_process()
        event.accept()
