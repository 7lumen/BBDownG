import subprocess
from time import sleep

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QDialog

from UI.output import Ui_Dialog_output
from tools import log, system

coding = "gbk" if system == "Windows" else "utf-8"


# 创建新线程
class NewThreads(QThread):
    output_signal = Signal(str)
    info_signal = Signal(bool)

    def __init__(self, args):
        """
        :param args: 命令行参数
        """
        super().__init__()
        # 运行命令
        if system == "Windows":
            self._process = subprocess.Popen(
                args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
        else:
            self._process = subprocess.Popen(
                args.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )

    def run(self):
        while True:
            out = self._process.stdout.readline().decode(coding)  # 获取输出内容
            # 传递内容
            self.output_signal.emit(out)
            if out == "":
                self.info_signal.emit(True)
                break

    def terminate_process(self):
        if system == "Windows":
            subprocess.Popen(
                ["taskkill", "/F", "/T", "/PID", str(self._process.pid)], shell=True
            )
        else:
            subprocess.Popen(["kill", "-9", str(self._process.pid)])


# 窗体
class DialogOutput(QDialog, Ui_Dialog_output):
    def __init__(self, args, flag=False):
        super().__init__()
        self.setupUi(self)
        self.flag = flag
        self.setWindowTitle("BBDownG - 下载")

        # 显示下载参数
        self.lineEdit_cmd.setText(args)
        self.lineEdit_cmd.setCursorPosition(0)

        # 暂停下载
        self.pushButton_stop.clicked.connect(self.stop)
        self.flage_stop = False

        # 创建线程，开始下载
        self.thread = NewThreads(args)
        self.thread.output_signal.connect(self.display)
        self.thread.info_signal.connect(self.close_down_window)
        self.thread.start()

    # 将信息显示出来
    def display(self, text):
        """追加输出并自动滚到底部"""
        self.textEdit_output.append(text)
        scrollbar = self.textEdit_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    # 暂停下载
    def stop(self):
        if self.flage_stop:
            return
        self.flage_stop = True
        # 调用命令，暂停下载
        self.thread.terminate_process()

        self.display("")
        self.display("")
        self.display(log() + " 下载已停止")

    # 关闭下载窗口
    def close_down_window(self):
        if self.flag:
            sleep(3)  # 休眠3秒
            self.close()  # 关闭窗口
