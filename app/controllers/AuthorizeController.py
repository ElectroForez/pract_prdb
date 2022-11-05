from PyQt5.QtCore import QObject, pyqtSlot

from models.PersonalAccountModel import PersonalAccountModel
from views.PersonalAccountView import PersonalAccountView

class AuthorizeController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot(str, str)
    def authorize(self, login, password):
        candidate = self._model.verify_credentials(login, password)
        if candidate:
            model = PersonalAccountModel(candidate)
            view = PersonalAccountView(model)
            view.show()
            self._view.close()
        else:
            self._view.show_error("Неверный логин или пароль")
