# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creategroupdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateGroupDialog(object):
    def setupUi(self, CreateGroupDialog):
        if not CreateGroupDialog.objectName():
            CreateGroupDialog.setObjectName(u"CreateGroupDialog")
        CreateGroupDialog.resize(461, 325)
        self.gridLayout = QGridLayout(CreateGroupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(CreateGroupDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(CreateGroupDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.selectedGroup_listWidget = QListWidget(self.configGroupBox)
        self.selectedGroup_listWidget.setObjectName(u"selectedGroup_listWidget")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.selectedGroup_listWidget)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(CreateGroupDialog)
        self.buttonBox.accepted.connect(CreateGroupDialog.accept)
        self.buttonBox.rejected.connect(CreateGroupDialog.reject)

        QMetaObject.connectSlotsByName(CreateGroupDialog)
    # setupUi

    def retranslateUi(self, CreateGroupDialog):
        CreateGroupDialog.setWindowTitle(QCoreApplication.translate("CreateGroupDialog", u"Create Group Dialog", None))
        self.configGroupBox.setTitle("")
    # retranslateUi

