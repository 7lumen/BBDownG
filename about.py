from PySide2.QtWidgets import QDialog

from UI.about_ui import Ui_Dialog_about


class DialogAbout(QDialog, Ui_Dialog_about):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('BBDownG - 关于')
