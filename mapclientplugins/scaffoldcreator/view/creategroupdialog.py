from PySide2 import QtCore, QtWidgets
from mapclientplugins.scaffoldcreator.view.ui_creategroupdialog import Ui_CreateGroupDialog

class CreateGroupDialog(QtWidgets.QDialog):
    """
    CreateGroup dialog to present the user with the options to create group.
    """

    def __init__(self, grouplist, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_CreateGroupDialog()
        self._ui.setupUi(self)

        self._groupList = grouplist
        self._selectedGroupList = []
        self._parent = parent

        self._makeConnections()

    def _makeConnections(self):
        # self._parent._refreshComboBoxNames(
        #     self._ui.annotationGroup_comboBox,
        #     ['-'] + [annotationGroup.getName() for annotationGroup in self._groupList],
        #     '-')
        self._buildSelectedGroupList()


    def _buildSelectedGroupList(self):
        """
        Fill the group list widget with the list of groups
        """
        if self._ui.selectedGroup_listWidget is not None:
            self._ui.selectedGroup_listWidget.clear()  # Must clear or holds on to steps references
        for group in self._groupList:
            item = QtWidgets.QListWidgetItem(group.getName())
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self._ui.selectedGroup_listWidget.addItem(item)

    def getSelectedGroupList(self):
        for index in range(self._ui.selectedGroup_listWidget.count()):
            if self._ui.selectedGroup_listWidget.item(index).checkState() == QtCore.Qt.Checked:
                self._selectedGroupList.append(self._ui.selectedGroup_listWidget.item(index).text())
        return self._selectedGroupList

    def accept(self):
        """
        Override the accept method
        """
        QtWidgets.QDialog.accept(self)
