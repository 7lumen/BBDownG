import subprocess
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QDialog

from UI.output_ui import Ui_Dialog_output
from tools import log


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
        self.p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def run(self):
        while True:
            out = self.p.stdout.readline().decode('gbk')  # 获取输出内容
            if out == '':
                self.info_signal.emit(True)
                break
            # 传递内容
            self.output_signal.emit(out)


# 窗体
class DialogOutput(QDialog, Ui_Dialog_output):
    def __init__(self, args, flag=False):
        super().__init__()
        self.setupUi(self)
        self.flag = flag
        self.args = args
        self.setWindowTitle('BBDownG - 下载')

        # 显示下载参数
        self.lineEdit_cmd.setText(self.args)
        self.lineEdit_cmd.setCursorPosition(0)
        self.pushButton_stop.clicked.connect(self.stop)  # 暂停下载
        self.flage_stop = False
        self.stat_down()  # 开始下载

    # 创建线程，开始下载
    def stat_down(self):
        self.thread = NewThreads(self.args)
        self.thread.start()
        self.thread.output_signal.connect(self.display)
        self.thread.info_signal.connect(self.close_down_window)

    # 将信息显示出来
    def display(self, m):
        self.textEdit_output.setText(self.textEdit_output.toPlainText() + m.strip() + '\n')
        self.textEdit_output.verticalScrollBar().setValue(self.textEdit_output.verticalScrollBar().maximum())

    # 暂停下载
    def stop(self):
        if self.flage_stop:
            return
        # 调用命令，暂停下载
        subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(self.thread.p.pid)], shell=True)
        self.display('')
        self.display('')
        self.display(log() + ' 下载已停止')
        self.flage_stop = True

    # 关闭下载窗口
    def close_down_window(self):
        if self.flag:
            sleep(3)  # 休眠3秒
            self.close()  # 关闭窗口
