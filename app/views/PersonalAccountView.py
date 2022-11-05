from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from views.personalAccountDesign import Ui_MainWindow
from models.PersonalAccountModel import PersonalAccountModel

from controllers.PersonalAccountController import PersonalAccountController


class PersonalAccountView(QMainWindow):

    def __init__(self, model: PersonalAccountModel):
        super().__init__()

        self._model = model
        self._controller = PersonalAccountController(self, self._model)
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)
        self.init_slots()
        self.init_data()

    def init_slots(self):
        self._ui.see_history.clicked.connect(self._controller.open_history)

    def init_data(self):
        fio = self._model.user['ФИО ']
        position = self._model.user['должность']

        lastname = fio.split()[0]
        photo = QPixmap(f"./img/{lastname}.jpeg")

        self._ui.photo_label.setPixmap(photo)
        self._ui.fio_label.setText(fio)
        self._ui.position_label.setText(position)

        if position != 'Администратор':
            self._ui.see_history.hide()
