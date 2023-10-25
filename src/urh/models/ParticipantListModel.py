from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, pyqtSignal
from urh.signalprocessing.Participant import Participant


class ParticipantListModel(QAbstractListModel):
    show_state_changed = pyqtSignal()

    def __init__(self, participants, parent=None):
        """

        :type participants: list of Participant
        """
        super().__init__(parent)
        self.participants = participants
        self.show_unassigned = True

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.participants) + 1

    def data(self, index: QModelIndex, role=None):
        row = index.row()
        if role == Qt.ItemDataRole.DisplayRole:
            if row == 0:
                return "not assigned"
            else:
                try:
                    return str(self.participants[row-1])
                except IndexError:
                    return None

        elif role == Qt.ItemDataRole.CheckStateRole:
            if row == 0:
                return Qt.CheckState.Checked if self.show_unassigned else Qt.CheckState.Unchecked
            else:
                try:
                    return Qt.CheckState.Checked if self.participants[row-1].show else Qt.CheckState.Unchecked
                except IndexError:
                    return None

    def setData(self, index: QModelIndex, value, role=None):
        if index.row() == 0 and role == Qt.ItemDataRole.CheckStateRole:
            if bool(value) != self.show_unassigned:
                self.show_unassigned = bool(value)
                self.show_state_changed.emit()

        elif role == Qt.ItemDataRole.CheckStateRole:
            try:
                if self.participants[index.row()-1].show != value:
                    self.participants[index.row()-1].show = value
                    self.show_state_changed.emit()
            except IndexError:
                return False

        return True

    def flags(self, index):
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsUserCheckable

    def update(self):
        self.beginResetModel()
        self.endResetModel()