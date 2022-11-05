from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QWidget, QTableWidget, QTableWidgetItem
from psycopg2.extras import RealDictRow

from views.loginHistoryDesign import Ui_Form
from controllers.LoginHistoryController import LoginHistoryController


class LoginHistoryView(QWidget):

    def __init__(self, model):
        super().__init__()

        self._model = model
        self._controller = LoginHistoryController(self, self._model)
        self._ui = Ui_Form()

        self._ui.setupUi(self)
        self.init_slots()

        self.draw_history()

    def init_slots(self):
        self._model.history_changed.connect(self.on_change_history)
        self._ui.filter_edit.textChanged\
            .connect(lambda: self._controller.filter_by_login(self._ui.filter_edit.text()))

    def draw_history(self):
        history = self._model.history
        print(history)
        table = self._ui.history_table
        table.clear()
        table.clearContents()
        table.setColumnCount(len(history[0]))
        table.setRowCount(len(history))
        table.setHorizontalHeaderLabels(history[0].keys())
        for i in range(len(history)):
            row = history[i]
            for j in range(len(row)):
                value = list(row.values())[j]
                table.setItem(i, j, QTableWidgetItem(str(value)))
        table.resizeColumnsToContents()
        table.setSortingEnabled(True)

    @pyqtSlot()
    def on_change_history(self):
        self.draw_history()
