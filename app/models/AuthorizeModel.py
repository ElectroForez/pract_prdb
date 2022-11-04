from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from models.User import UserModel


class AuthorizeModel(QObject):

    user_authorized = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self._user_model = UserModel()
        self._cur_user = None

    @property
    def users(self):
        return self._user_model.get_users()

    def check_authorize(self, login, password):
        candidate = self._user_model.get_user(login, password)

        if candidate:
            self.user_authorized.emit(True)
        else:
            self.user_authorized.emit(False)

