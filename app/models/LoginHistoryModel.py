from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from models.Db import db


class LoginHistoryModel(QObject):

    def __init__(self):
        super().__init__()

    @property
    def history(self):
        return self.get_history_from_db()

    def get_history_from_db(self):
        db.cursor.execute("SELECT * FROM история_входа")
        result = db.cursor.fetchall()
        return result
