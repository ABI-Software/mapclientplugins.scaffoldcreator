# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scaffoldsettingswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ScaffoldSettings(object):
    def setupUi(self, ScaffoldSettings):
        if not ScaffoldSettings.objectName():
            ScaffoldSettings.setObjectName(u"ScaffoldSettings")
        ScaffoldSettings.resize(554, 773)
        self.verticalLayout_2 = QVBoxLayout(ScaffoldSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.subscaffold_frame = QFrame(ScaffoldSettings)
        self.subscaffold_frame.setObjectName(u"subscaffold_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subscaffold_frame.sizePolicy().hasHeightForWidth())
        self.subscaffold_frame.setSizePolicy(sizePolicy)
        self.subscaffold_frame.setMinimumSize(QSize(0, 0))
        self.subscaffold_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.subscaffold_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.subscaffold_label = QLabel(self.subscaffold_frame)
        self.subscaffold_label.setObjectName(u"subscaffold_label")

        self.verticalLayout_5.addWidget(self.subscaffold_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(89, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.subscaffoldBack_pushButton = QPushButton(self.subscaffold_frame)
        self.subscaffoldBack_pushButton.setObjectName(u"subscaffoldBack_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.subscaffoldBack_pushButton.sizePolicy().hasHeightForWidth())
        self.subscaffoldBack_pushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.subscaffoldBack_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.subscaffold_frame)

        self.meshType_frame = QFrame(ScaffoldSettings)
        self.meshType_frame.setObjectName(u"meshType_frame")
        self.meshType_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout = QFormLayout(self.meshType_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.meshType_label = QLabel(self.meshType_frame)
        self.meshType_label.setObjectName(u"meshType_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.meshType_label)

        self.meshType_comboBox = QComboBox(self.meshType_frame)
        self.meshType_comboBox.setObjectName(u"meshType_comboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.meshType_comboBox)

        self.parameterSet_label = QLabel(self.meshType_frame)
        self.parameterSet_label.setObjectName(u"parameterSet_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.parameterSet_label)

        self.parameterSet_comboBox = QComboBox(self.meshType_frame)
        self.parameterSet_comboBox.setObjectName(u"parameterSet_comboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.parameterSet_comboBox)


        self.verticalLayout_2.addWidget(self.meshType_frame)

        self.meshTypeOptions_frame = QFrame(ScaffoldSettings)
        self.meshTypeOptions_frame.setObjectName(u"meshTypeOptions_frame")
        self.meshTypeOptions_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.meshTypeOptions_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_2.addWidget(self.meshTypeOptions_frame)

        self.modifyOptions_frame = QFrame(ScaffoldSettings)
        self.modifyOptions_frame.setObjectName(u"modifyOptions_frame")
        self.modifyOptions_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.modifyOptions_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deleteElementsRanges_frame = QFrame(self.modifyOptions_frame)
        self.deleteElementsRanges_frame.setObjectName(u"deleteElementsRanges_frame")
        self.deleteElementsRanges_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.deleteElementsRanges_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.deleteElementsRanges_label = QLabel(self.deleteElementsRanges_frame)
        self.deleteElementsRanges_label.setObjectName(u"deleteElementsRanges_label")

        self.verticalLayout_10.addWidget(self.deleteElementsRanges_label)

        self.deleteElementsRanges_lineEdit = QLineEdit(self.deleteElementsRanges_frame)
        self.deleteElementsRanges_lineEdit.setObjectName(u"deleteElementsRanges_lineEdit")

        self.verticalLayout_10.addWidget(self.deleteElementsRanges_lineEdit)


        self.verticalLayout.addWidget(self.deleteElementsRanges_frame)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.deleteElementsSelection_pushButton = QPushButton(self.modifyOptions_frame)
        self.deleteElementsSelection_pushButton.setObjectName(u"deleteElementsSelection_pushButton")

        self.horizontalLayout_13.addWidget(self.deleteElementsSelection_pushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.rotation_label = QLabel(self.modifyOptions_frame)
        self.rotation_label.setObjectName(u"rotation_label")

        self.verticalLayout.addWidget(self.rotation_label)

        self.rotation_lineEdit = QLineEdit(self.modifyOptions_frame)
        self.rotation_lineEdit.setObjectName(u"rotation_lineEdit")

        self.verticalLayout.addWidget(self.rotation_lineEdit)

        self.scale_label = QLabel(self.modifyOptions_frame)
        self.scale_label.setObjectName(u"scale_label")

        self.verticalLayout.addWidget(self.scale_label)

        self.scale_lineEdit = QLineEdit(self.modifyOptions_frame)
        self.scale_lineEdit.setObjectName(u"scale_lineEdit")

        self.verticalLayout.addWidget(self.scale_lineEdit)

        self.translation_label = QLabel(self.modifyOptions_frame)
        self.translation_label.setObjectName(u"translation_label")

        self.verticalLayout.addWidget(self.translation_label)

        self.translation_lineEdit = QLineEdit(self.modifyOptions_frame)
        self.translation_lineEdit.setObjectName(u"translation_lineEdit")

        self.verticalLayout.addWidget(self.translation_lineEdit)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.applyTransformation_pushButton = QPushButton(self.modifyOptions_frame)
        self.applyTransformation_pushButton.setObjectName(u"applyTransformation_pushButton")

        self.horizontalLayout_12.addWidget(self.applyTransformation_pushButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.autoAlignTransformation_pushButton = QPushButton(self.modifyOptions_frame)
        self.autoAlignTransformation_pushButton.setObjectName(u"autoAlignTransformation_pushButton")

        self.horizontalLayout_5.addWidget(self.autoAlignTransformation_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.modifyOptions_frame)

        self.verticalSpacer = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(ScaffoldSettings)

        QMetaObject.connectSlotsByName(ScaffoldSettings)
    # setupUi

    def retranslateUi(self, ScaffoldSettings):
        ScaffoldSettings.setWindowTitle(QCoreApplication.translate("ScaffoldSettings", u"Scaffold Settings", None))
        self.subscaffold_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Subscaffold", None))
        self.subscaffoldBack_pushButton.setText(QCoreApplication.translate("ScaffoldSettings", u"<< Back", None))
        self.meshType_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Scaffold type:", None))
        self.parameterSet_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Parameter set:", None))
        self.deleteElementsRanges_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Delete element ID ranges (e.g. 1,2-5,13):", None))
        self.deleteElementsSelection_pushButton.setText(QCoreApplication.translate("ScaffoldSettings", u"Delete selected elements", None))
        self.rotation_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Rotation in degrees about z, y, x", None))
        self.scale_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Scale x, y, z:", None))
        self.translation_label.setText(QCoreApplication.translate("ScaffoldSettings", u"Translation x, y, z", None))
        self.applyTransformation_pushButton.setText(QCoreApplication.translate("ScaffoldSettings", u"Apply transformation", None))
        self.autoAlignTransformation_pushButton.setText(QCoreApplication.translate("ScaffoldSettings", u"Auto align", None))
    # retranslateUi

