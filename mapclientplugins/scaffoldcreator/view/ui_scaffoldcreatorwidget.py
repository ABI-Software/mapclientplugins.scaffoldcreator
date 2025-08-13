# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scaffoldcreatorwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

from mapclientplugins.scaffoldcreator.view.nodeeditorsceneviewerwidget import NodeEditorSceneviewerWidget

class Ui_ScaffoldCreatorWidget(object):
    def setupUi(self, ScaffoldCreatorWidget):
        if not ScaffoldCreatorWidget.objectName():
            ScaffoldCreatorWidget.setObjectName(u"ScaffoldCreatorWidget")
        ScaffoldCreatorWidget.resize(800, 600)
        self.sceneviewer_widget = NodeEditorSceneviewerWidget(ScaffoldCreatorWidget)
        self.sceneviewer_widget.setObjectName(u"sceneviewer_widget")
        ScaffoldCreatorWidget.setCentralWidget(self.sceneviewer_widget)

        self.retranslateUi(ScaffoldCreatorWidget)

        QMetaObject.connectSlotsByName(ScaffoldCreatorWidget)
    # setupUi

    def retranslateUi(self, ScaffoldCreatorWidget):
        ScaffoldCreatorWidget.setWindowTitle(QCoreApplication.translate("ScaffoldCreatorWidget", u"Scaffold Creator", None))
    # retranslateUi

