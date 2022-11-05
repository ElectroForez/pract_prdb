from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from views.authorizeDesign import Ui_MainWindow

from controllers.AuthorizeController import AuthorizeController


class AuthorizeView(QMainWindow):

    def __init__(self, model):
        super().__init__()

        self._model = model
        self._controller = AuthorizeController(self, self._model)
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.show_pass_box.stateChanged.connect(self.on_show_pass_changed)
        self._ui.auth_button.clicked.connect(self.on_authorize_click)
        self._model.user_authorized.connect(self.on_authorize_result)
        self._model.block_auth.connect(self.on_block_auth)

    def init_data(self):
        self._ui.login_edit.setText("fedorov@namecomp.ru")
        self._ui.pass_edit.setText("8ntwUp")

    def show_error(self, text):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка авторизации")
        msg_box.exec()

    @pyqtSlot(int)
    def on_show_pass_changed(self, is_checked):
        mode = QLineEdit.Normal if is_checked else QLineEdit.Password
        self._ui.pass_edit.setEchoMode(mode)

    @pyqtSlot()
    def on_authorize_click(self):
        login = self._ui.login_edit.text()
        password = self._ui.pass_edit.text()
        self._controller.authorize(login, password)

    @pyqtSlot(bool)
    def on_authorize_result(self, value):
        print(value)

    @pyqtSlot()
    def on_block_auth(self):
        timer = QTimer
        self._ui.auth_button.setDisabled(True)
        timer.singleShot(10000, self.block_auth)

    def block_auth(self):
        self._ui.auth_button.setDisabled(False)
