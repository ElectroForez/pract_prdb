from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QCheckBox
from views.authorizeDesign import Ui_MainWindow


class AuthorizeView(QMainWindow):

    def __init__(self, model, controller):
        super().__init__()

        self._controller = controller
        self._model = model
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.show_pass_box.stateChanged.connect(self.on_show_pass_changed)
        self._ui.auth_button.clicked.connect(self.on_authorize_click)
        self._model.user_authorized.connect(self.on_authorize_result)

    def init_data(self):
        self._ui.login_edit.setText("Ivanov@namecomp.ru")
        self._ui.pass_edit.setText("2L6KZG")

    @pyqtSlot(int)
    def on_show_pass_changed(self, isChecked):
        mode = QLineEdit.Normal if isChecked else QLineEdit.Password
        self._ui.pass_edit.setEchoMode(mode)

    @pyqtSlot()
    def on_authorize_click(self):
        login = self._ui.login_edit.text()
        password = self._ui.pass_edit.text()
        self._controller.authorize(login, password)

    @pyqtSlot(bool)
    def on_authorize_result(self, value):
        print(value)
