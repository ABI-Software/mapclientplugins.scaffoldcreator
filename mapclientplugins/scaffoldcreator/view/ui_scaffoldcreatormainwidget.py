# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scaffoldcreatormainwidget.ui'
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

class Ui_ScaffoldCreatorMainWidget(object):
    def setupUi(self, ScaffoldCreatorMainWidget):
        if not ScaffoldCreatorMainWidget.objectName():
            ScaffoldCreatorMainWidget.setObjectName(u"ScaffoldCreatorMainWidget")
        ScaffoldCreatorMainWidget.resize(800, 600)
        self.sceneviewer_widget = NodeEditorSceneviewerWidget(ScaffoldCreatorMainWidget)
        self.sceneviewer_widget.setObjectName(u"sceneviewer_widget")
        ScaffoldCreatorMainWidget.setCentralWidget(self.sceneviewer_widget)

        self.retranslateUi(ScaffoldCreatorMainWidget)

        QMetaObject.connectSlotsByName(ScaffoldCreatorMainWidget)
    # setupUi

    def retranslateUi(self, ScaffoldCreatorMainWidget):
        ScaffoldCreatorMainWidget.setWindowTitle(QCoreApplication.translate("ScaffoldCreatorMainWidget", u"Scaffold Creator", None))
    # retranslateUi

