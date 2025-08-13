# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotationtoolswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from cmlibs.widgets.fieldchooserwidget import FieldChooserWidget

class Ui_AnnotationTools(object):
    def setupUi(self, AnnotationTools):
        if not AnnotationTools.objectName():
            AnnotationTools.setObjectName(u"AnnotationTools")
        AnnotationTools.resize(723, 510)
        self.verticalLayout = QVBoxLayout(AnnotationTools)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.annotationButton_frame = QFrame(AnnotationTools)
        self.annotationButton_frame.setObjectName(u"annotationButton_frame")
        self.annotationButton_frame.setFrameShape(QFrame.StyledPanel)
        self.annotationButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.annotationButton_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.annotationGroupNew_pushButton = QPushButton(self.annotationButton_frame)
        self.annotationGroupNew_pushButton.setObjectName(u"annotationGroupNew_pushButton")

        self.horizontalLayout.addWidget(self.annotationGroupNew_pushButton)

        self.annotationGroupNewMarker_pushButton = QPushButton(self.annotationButton_frame)
        self.annotationGroupNewMarker_pushButton.setObjectName(u"annotationGroupNewMarker_pushButton")

        self.horizontalLayout.addWidget(self.annotationGroupNewMarker_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.annotationGroupRedefine_pushButton = QPushButton(self.annotationButton_frame)
        self.annotationGroupRedefine_pushButton.setObjectName(u"annotationGroupRedefine_pushButton")

        self.horizontalLayout.addWidget(self.annotationGroupRedefine_pushButton)

        self.annotationGroupEdit_pushButton = QPushButton(self.annotationButton_frame)
        self.annotationGroupEdit_pushButton.setObjectName(u"annotationGroupEdit_pushButton")

        self.horizontalLayout.addWidget(self.annotationGroupEdit_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.annotationGroupDelete_pushButton = QPushButton(self.annotationButton_frame)
        self.annotationGroupDelete_pushButton.setObjectName(u"annotationGroupDelete_pushButton")

        self.horizontalLayout.addWidget(self.annotationGroupDelete_pushButton)


        self.verticalLayout.addWidget(self.annotationButton_frame)

        self.annotationGroup_frame = QFrame(AnnotationTools)
        self.annotationGroup_frame.setObjectName(u"annotationGroup_frame")
        self.annotationGroup_frame.setFrameShape(QFrame.NoFrame)
        self.formLayout_2 = QFormLayout(self.annotationGroup_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.annotationGroup_label = QLabel(self.annotationGroup_frame)
        self.annotationGroup_label.setObjectName(u"annotationGroup_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.annotationGroup_label)

        self.annotationGroup_comboBox = QComboBox(self.annotationGroup_frame)
        self.annotationGroup_comboBox.setObjectName(u"annotationGroup_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annotationGroup_comboBox.sizePolicy().hasHeightForWidth())
        self.annotationGroup_comboBox.setSizePolicy(sizePolicy)
        self.annotationGroup_comboBox.setMinimumSize(QSize(180, 0))
        self.annotationGroup_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.annotationGroup_comboBox.setMinimumContentsLength(24)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.annotationGroup_comboBox)

        self.annotationGroupOntId_label = QLabel(self.annotationGroup_frame)
        self.annotationGroupOntId_label.setObjectName(u"annotationGroupOntId_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.annotationGroupOntId_label)

        self.annotationGroupOntId_lineEdit = QLineEdit(self.annotationGroup_frame)
        self.annotationGroupOntId_lineEdit.setObjectName(u"annotationGroupOntId_lineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.annotationGroupOntId_lineEdit)

        self.annotationGroupDimension_label = QLabel(self.annotationGroup_frame)
        self.annotationGroupDimension_label.setObjectName(u"annotationGroupDimension_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.annotationGroupDimension_label)

        self.annotationGroupDimension_spinBox = QSpinBox(self.annotationGroup_frame)
        self.annotationGroupDimension_spinBox.setObjectName(u"annotationGroupDimension_spinBox")
        self.annotationGroupDimension_spinBox.setMinimum(0)
        self.annotationGroupDimension_spinBox.setMaximum(3)
        self.annotationGroupDimension_spinBox.setValue(0)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.annotationGroupDimension_spinBox)

        self.marker_groupBox = QGroupBox(self.annotationGroup_frame)
        self.marker_groupBox.setObjectName(u"marker_groupBox")
        self.marker_groupBox.setEnabled(True)
        self.formLayout_5 = QFormLayout(self.marker_groupBox)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_5.setHorizontalSpacing(7)
        self.formLayout_5.setVerticalSpacing(7)
        self.formLayout_5.setContentsMargins(-1, 3, -1, 11)
        self.marker_frame = QFrame(self.marker_groupBox)
        self.marker_frame.setObjectName(u"marker_frame")
        self.marker_frame.setFrameShape(QFrame.NoFrame)
        self.formLayout_4 = QFormLayout(self.marker_frame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.markerMaterialCoordinates_label = QLabel(self.marker_frame)
        self.markerMaterialCoordinates_label.setObjectName(u"markerMaterialCoordinates_label")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.markerMaterialCoordinates_label)

        self.markerMaterialCoordinates_lineEdit = QLineEdit(self.marker_frame)
        self.markerMaterialCoordinates_lineEdit.setObjectName(u"markerMaterialCoordinates_lineEdit")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.markerMaterialCoordinates_lineEdit)

        self.markerElement_label = QLabel(self.marker_frame)
        self.markerElement_label.setObjectName(u"markerElement_label")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.markerElement_label)

        self.markerElement_lineEdit = QLineEdit(self.marker_frame)
        self.markerElement_lineEdit.setObjectName(u"markerElement_lineEdit")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.markerElement_lineEdit)

        self.markerXiCoordinates_label = QLabel(self.marker_frame)
        self.markerXiCoordinates_label.setObjectName(u"markerXiCoordinates_label")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.markerXiCoordinates_label)

        self.markerXiCoordinates_lineEdit = QLineEdit(self.marker_frame)
        self.markerXiCoordinates_lineEdit.setObjectName(u"markerXiCoordinates_lineEdit")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.markerXiCoordinates_lineEdit)

        self.markerMaterialCoordinatesField_label = QLabel(self.marker_frame)
        self.markerMaterialCoordinatesField_label.setObjectName(u"markerMaterialCoordinatesField_label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.markerMaterialCoordinatesField_label)

        self.markerMaterialCoordinatesField_fieldChooser = FieldChooserWidget(self.marker_frame)
        self.markerMaterialCoordinatesField_fieldChooser.setObjectName(u"markerMaterialCoordinatesField_fieldChooser")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.markerMaterialCoordinatesField_fieldChooser)


        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.marker_frame)


        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.marker_groupBox)


        self.verticalLayout.addWidget(self.annotationGroup_frame)

        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AnnotationTools)

        QMetaObject.connectSlotsByName(AnnotationTools)
    # setupUi

    def retranslateUi(self, AnnotationTools):
        AnnotationTools.setWindowTitle(QCoreApplication.translate("AnnotationTools", u"Annotation Tools", None))
        self.annotationGroupNew_pushButton.setText(QCoreApplication.translate("AnnotationTools", u"New", None))
        self.annotationGroupNewMarker_pushButton.setText(QCoreApplication.translate("AnnotationTools", u"New Marker", None))
        self.annotationGroupRedefine_pushButton.setText(QCoreApplication.translate("AnnotationTools", u"Redefine", None))
        self.annotationGroupEdit_pushButton.setText(QCoreApplication.translate("AnnotationTools", u"Edit", None))
        self.annotationGroupDelete_pushButton.setText(QCoreApplication.translate("AnnotationTools", u"Delete", None))
        self.annotationGroup_label.setText(QCoreApplication.translate("AnnotationTools", u"Group:", None))
        self.annotationGroupOntId_label.setText(QCoreApplication.translate("AnnotationTools", u"ONT:ID:", None))
        self.annotationGroupDimension_label.setText(QCoreApplication.translate("AnnotationTools", u"Dimension:", None))
        self.marker_groupBox.setTitle(QCoreApplication.translate("AnnotationTools", u"Marker", None))
        self.markerMaterialCoordinates_label.setText(QCoreApplication.translate("AnnotationTools", u"Material coordinates:", None))
        self.markerElement_label.setText(QCoreApplication.translate("AnnotationTools", u"Element:", None))
        self.markerXiCoordinates_label.setText(QCoreApplication.translate("AnnotationTools", u"Element xi coordinates:", None))
        self.markerMaterialCoordinatesField_label.setText(QCoreApplication.translate("AnnotationTools", u"Material coordinates field:", None))
    # retranslateUi

