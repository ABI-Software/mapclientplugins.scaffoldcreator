# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'displaysettingswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from cmlibs.widgets.fieldchooserwidget import FieldChooserWidget

class Ui_DisplaySettings(object):
    def setupUi(self, DisplaySettings):
        if not DisplaySettings.objectName():
            DisplaySettings.setObjectName(u"DisplaySettings")
        DisplaySettings.resize(689, 551)
        self.verticalLayout = QVBoxLayout(DisplaySettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.displayData_frame = QFrame(DisplaySettings)
        self.displayData_frame.setObjectName(u"displayData_frame")
        self.displayData_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.displayData_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.displayDataPoints_frame = QFrame(self.displayData_frame)
        self.displayDataPoints_frame.setObjectName(u"displayDataPoints_frame")
        self.displayDataPoints_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.displayDataPoints_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.displayDataPoints_checkBox = QCheckBox(self.displayDataPoints_frame)
        self.displayDataPoints_checkBox.setObjectName(u"displayDataPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataPoints_checkBox)

        self.displayDataContours_checkBox = QCheckBox(self.displayDataPoints_frame)
        self.displayDataContours_checkBox.setObjectName(u"displayDataContours_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataContours_checkBox)

        self.displayDataRadius_checkBox = QCheckBox(self.displayDataPoints_frame)
        self.displayDataRadius_checkBox.setObjectName(u"displayDataRadius_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataRadius_checkBox)

        self.displayDataPoints_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.displayDataPoints_horizontalSpacer)


        self.verticalLayout_11.addWidget(self.displayDataPoints_frame)

        self.displayDataMarkers_frame = QFrame(self.displayData_frame)
        self.displayDataMarkers_frame.setObjectName(u"displayDataMarkers_frame")
        self.displayDataMarkers_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.displayDataMarkers_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.displayDataMarkerPoints_checkBox = QCheckBox(self.displayDataMarkers_frame)
        self.displayDataMarkerPoints_checkBox.setObjectName(u"displayDataMarkerPoints_checkBox")

        self.horizontalLayout_10.addWidget(self.displayDataMarkerPoints_checkBox)

        self.displayDataMarkerNames_checkBox = QCheckBox(self.displayDataMarkers_frame)
        self.displayDataMarkerNames_checkBox.setObjectName(u"displayDataMarkerNames_checkBox")

        self.horizontalLayout_10.addWidget(self.displayDataMarkerNames_checkBox)

        self.displayDataMarkers_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.displayDataMarkers_horizontalSpacer)


        self.verticalLayout_11.addWidget(self.displayDataMarkers_frame)


        self.verticalLayout.addWidget(self.displayData_frame)

        self.displayModelCoordinates_frame = QFrame(DisplaySettings)
        self.displayModelCoordinates_frame.setObjectName(u"displayModelCoordinates_frame")
        self.displayModelCoordinates_frame.setFrameShape(QFrame.NoFrame)
        self.formLayout_3 = QFormLayout(self.displayModelCoordinates_frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displayModelCoordinates_label = QLabel(self.displayModelCoordinates_frame)
        self.displayModelCoordinates_label.setObjectName(u"displayModelCoordinates_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.displayModelCoordinates_label)

        self.displayModelCoordinates_fieldChooser = FieldChooserWidget(self.displayModelCoordinates_frame)
        self.displayModelCoordinates_fieldChooser.setObjectName(u"displayModelCoordinates_fieldChooser")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.displayModelCoordinates_fieldChooser)


        self.verticalLayout.addWidget(self.displayModelCoordinates_frame)

        self.displayNodes_frame = QFrame(DisplaySettings)
        self.displayNodes_frame.setObjectName(u"displayNodes_frame")
        self.displayNodes_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNodes_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNodePoints_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodePoints_checkBox.setObjectName(u"displayNodePoints_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeNumbers_checkBox.setObjectName(u"displayNodeNumbers_checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayNodeNumbers_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeNumbers_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodeDerivatives_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeDerivatives_checkBox.setObjectName(u"displayNodeDerivatives_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivatives_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivatives_checkBox.setSizePolicy(sizePolicy)
        self.displayNodeDerivatives_checkBox.setTristate(True)

        self.horizontalLayout_6.addWidget(self.displayNodeDerivatives_checkBox)

        self.displayNodeDerivativesVersion_spinBox = QSpinBox(self.displayNodes_frame)
        self.displayNodeDerivativesVersion_spinBox.setObjectName(u"displayNodeDerivativesVersion_spinBox")

        self.horizontalLayout_6.addWidget(self.displayNodeDerivativesVersion_spinBox)


        self.verticalLayout.addWidget(self.displayNodes_frame)

        self.displayNodeDerivativeLabels_frame = QFrame(DisplaySettings)
        self.displayNodeDerivativeLabels_frame.setObjectName(u"displayNodeDerivativeLabels_frame")
        self.displayNodeDerivativeLabels_frame.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.displayNodeDerivativeLabels_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.displayNodeDerivativeLabels_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.displayNodeDerivativeLabels_horizontalSpacer, 0, 0, 1, 1)

        self.displayNodeDerivativeLabelsD1_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD1_checkBox.setObjectName(u"displayNodeDerivativeLabelsD1_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD1_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD1_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD1_checkBox, 0, 1, 1, 1)

        self.displayNodeDerivativeLabelsD2_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD2_checkBox.setObjectName(u"displayNodeDerivativeLabelsD2_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD2_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD2_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD2_checkBox, 0, 2, 1, 1)

        self.displayNodeDerivativeLabelsD3_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD3_checkBox.setObjectName(u"displayNodeDerivativeLabelsD3_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD3_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD3_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD3_checkBox, 0, 3, 1, 1)

        self.displayNodeDerivativeLabelsD12_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD12_checkBox.setObjectName(u"displayNodeDerivativeLabelsD12_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD12_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD12_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD12_checkBox, 0, 4, 1, 1)

        self.displayNodeDerivativeLabelsD13_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD13_checkBox.setObjectName(u"displayNodeDerivativeLabelsD13_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD13_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD13_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD13_checkBox, 0, 5, 1, 1)

        self.displayNodeDerivativeLabelsD23_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD23_checkBox.setObjectName(u"displayNodeDerivativeLabelsD23_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD23_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD23_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD23_checkBox, 0, 6, 1, 1)

        self.displayNodeDerivativeLabelsD123_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD123_checkBox.setObjectName(u"displayNodeDerivativeLabelsD123_checkBox")
        sizePolicy.setHeightForWidth(self.displayNodeDerivativeLabelsD123_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD123_checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.displayNodeDerivativeLabelsD123_checkBox, 0, 7, 1, 1)


        self.verticalLayout.addWidget(self.displayNodeDerivativeLabels_frame)

        self.displayLines_frame = QFrame(DisplaySettings)
        self.displayLines_frame.setObjectName(u"displayLines_frame")
        self.displayLines_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.displayLines_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.displayLines_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLines_checkBox.setObjectName(u"displayLines_checkBox")

        self.horizontalLayout_5.addWidget(self.displayLines_checkBox)

        self.displayLinesExterior_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLinesExterior_checkBox.setObjectName(u"displayLinesExterior_checkBox")
        sizePolicy.setHeightForWidth(self.displayLinesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLinesExterior_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.displayLinesExterior_checkBox)

        self.displayModelRadius_checkBox = QCheckBox(self.displayLines_frame)
        self.displayModelRadius_checkBox.setObjectName(u"displayModelRadius_checkBox")

        self.horizontalLayout_5.addWidget(self.displayModelRadius_checkBox)

        self.displayLines_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.displayLines_horizontalSpacer)


        self.verticalLayout.addWidget(self.displayLines_frame)

        self.displaySurfaces_frame = QFrame(DisplaySettings)
        self.displaySurfaces_frame.setObjectName(u"displaySurfaces_frame")
        self.displaySurfaces_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displaySurfaces_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName(u"displaySurfaces_checkBox")

        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)

        self.displaySurfacesExterior_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName(u"displaySurfacesExterior_checkBox")
        sizePolicy.setHeightForWidth(self.displaySurfacesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesExterior_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)

        self.displaySurfacesTranslucent_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName(u"displaySurfacesTranslucent_checkBox")
        sizePolicy.setHeightForWidth(self.displaySurfacesTranslucent_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesTranslucent_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)

        self.displaySurfacesWireframe_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName(u"displaySurfacesWireframe_checkBox")
        sizePolicy.setHeightForWidth(self.displaySurfacesWireframe_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesWireframe_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)

        self.displaySurfaces_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.displaySurfaces_horizontalSpacer)


        self.verticalLayout.addWidget(self.displaySurfaces_frame)

        self.displayMisc_frame = QFrame(DisplaySettings)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displayMarkerPoints_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayMarkerPoints_checkBox.setObjectName(u"displayMarkerPoints_checkBox")

        self.horizontalLayout_8.addWidget(self.displayMarkerPoints_checkBox)

        self.displayZeroJacobianContours_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayZeroJacobianContours_checkBox.setObjectName(u"displayZeroJacobianContours_checkBox")

        self.horizontalLayout_8.addWidget(self.displayZeroJacobianContours_checkBox)

        self.displaytMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.displaytMisc_horizontalSpacer)


        self.verticalLayout.addWidget(self.displayMisc_frame)

        self.displayElements_frame = QFrame(DisplaySettings)
        self.displayElements_frame.setObjectName(u"displayElements_frame")
        self.displayElements_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.displayElements_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayElementNumbers_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementNumbers_checkBox.setObjectName(u"displayElementNumbers_checkBox")

        self.horizontalLayout_4.addWidget(self.displayElementNumbers_checkBox)

        self.displayElementAxes_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementAxes_checkBox.setObjectName(u"displayElementAxes_checkBox")
        sizePolicy.setHeightForWidth(self.displayElementAxes_checkBox.sizePolicy().hasHeightForWidth())
        self.displayElementAxes_checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.displayElementAxes_checkBox)

        self.displayElements_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.displayElements_horizontalSpacer)


        self.verticalLayout.addWidget(self.displayElements_frame)

        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DisplaySettings)

        QMetaObject.connectSlotsByName(DisplaySettings)
    # setupUi

    def retranslateUi(self, DisplaySettings):
        DisplaySettings.setWindowTitle(QCoreApplication.translate("DisplaySettings", u"Display Settings", None))
        self.displayDataPoints_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Data points", None))
        self.displayDataContours_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Data contours", None))
        self.displayDataRadius_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Data radius", None))
        self.displayDataMarkerPoints_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Data marker points", None))
        self.displayDataMarkerNames_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Data marker names", None))
        self.displayModelCoordinates_label.setText(QCoreApplication.translate("DisplaySettings", u"Model coordinates:", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Node numbers", None))
#if QT_CONFIG(tooltip)
        self.displayNodeDerivatives_checkBox.setToolTip(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p>Show node derivatives on:<br/>[ ] None<br/>[-] Selected nodes<br/>[/] All nodes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayNodeDerivatives_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Node derivatives", None))
#if QT_CONFIG(tooltip)
        self.displayNodeDerivativesVersion_spinBox.setToolTip(QCoreApplication.translate("DisplaySettings", u"<html><head/><body><p>Show specified node derivative version, or 0 to show all versions.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayNodeDerivativeLabelsD1_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D1", None))
        self.displayNodeDerivativeLabelsD2_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D2", None))
        self.displayNodeDerivativeLabelsD3_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D3", None))
        self.displayNodeDerivativeLabelsD12_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D12", None))
        self.displayNodeDerivativeLabelsD13_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D13", None))
        self.displayNodeDerivativeLabelsD23_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D23", None))
        self.displayNodeDerivativeLabelsD123_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"D123", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Exterior", None))
        self.displayModelRadius_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Model radius", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Wireframe", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Axes", None))
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Marker points", None))
        self.displayZeroJacobianContours_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Zero Jacobian contours", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("DisplaySettings", u"Element axes", None))
    # retranslateUi

