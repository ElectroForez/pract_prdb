from PyQt5.QtCore import QObject, pyqtSlot

from models.LoginHistoryModel import LoginHistoryModel
from views.LoginHistoryView import LoginHistoryView


class PersonalAccountController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot()
    def open_history(self):
        model = LoginHistoryModel()
        view = LoginHistoryView(model)
        view.show()
