from PyQt5.QtCore import QObject, pyqtSlot


class AuthorizeController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(str, str)
    def authorize(self, login, password):
        self._model.check_authorize(login, password)
