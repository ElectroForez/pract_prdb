from PyQt5.QtCore import QObject, pyqtSlot


class LoginHistoryController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view
