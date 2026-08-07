"""
Dialog/UI for interacting with scaffoldcreatormodel.
"""
import webbrowser

from PySide6 import QtCore, QtWidgets
from functools import partial

from mapclientplugins.scaffoldcreator.view.functionoptionsdialog import FunctionOptionsDialog
from mapclientplugins.scaffoldcreator.view.ui_scaffoldcreatorwidget import Ui_ScaffoldCreatorWidget
from mapclientplugins.scaffoldcreator.view.ui_scaffoldsettingswidget import Ui_ScaffoldSettings
from mapclientplugins.scaffoldcreator.view.ui_annotationtoolswidget import Ui_AnnotationTools

from cmlibs.maths.vectorops import dot, magnitude, mult, normalize, sub
from cmlibs.widgets.collapsibleboxwidget import CollapsibleBox
from cmlibs.widgets.groupeditorwidget import GroupEditorWidget
from cmlibs.widgets.helpers.widgetvisibility import setting_visibility
from cmlibs.widgets.ui.ui_displaysettingswidget import Ui_DisplaySettings
from cmlibs.widgets.ui.ui_buttonswidget import Ui_Buttons
from cmlibs.widgets.utils import parse_vector, parse_int
from cmlibs.utils.zinc.field import field_is_managed_coordinates, field_is_managed_group
from scaffoldmaker.scaffoldpackage import ScaffoldPackage


def get_zinc_groups(annotation_groups):
    """
    Convert a list of AnnotationGroups into a list of Zinc FieldGroups.
    """
    zinc_groups = []
    for annotation_group in annotation_groups:
        zinc_group = annotation_group.getGroup()
        zinc_groups.append(zinc_group)
    return zinc_groups


class ScaffoldCreatorWidget(QtWidgets.QMainWindow):

    def __init__(self, model, parent=None):
        super(ScaffoldCreatorWidget, self).__init__(parent)
        self._ui = Ui_ScaffoldCreatorWidget()
        self._ui.setupUi(self)
        self._model = model
        self._setup_dock_widget()
        self._scaffold_model = model.getCreatorModel()
        self._segmentation_data_model = model.getSegmentationDataModel()
        self._ui.sceneviewer_widget.setContext(model.getContext())
        self._ui.sceneviewer_widget.setGeneratorModel(model.getCreatorModel())
        self._model.getCreatorModel().registerCustomParametersCallback(self._customParametersChange)
        self._model.registerSceneChangeCallback(self._sceneChanged)
        self._scaffold_model.registerTransformationChangeCallback(self._transformationChanged)
        self._doneCallback = None
        self._refreshScaffoldTypeNames()
        self._refreshParameterSetNames()
        self._refreshAnnotationGroups()
        self._makeConnections()

    def _setup_dock_widget(self):
        parent_widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(parent_widget)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        self._identifier_label = QtWidgets.QLabel("Identifier: " + self._model.getIdentifier())
        layout.addWidget(self._identifier_label)

        self._annotation_tools_ui = Ui_AnnotationTools()
        self._display_settings_ui = Ui_DisplaySettings()
        self._scaffold_settings_ui = Ui_ScaffoldSettings()
        self._buttons_ui = Ui_Buttons()

        for ui in [self._scaffold_settings_ui, self._annotation_tools_ui, self._display_settings_ui]:
            form_container = QtWidgets.QWidget()
            ui.setupUi(form_container)
            tools_box = CollapsibleBox(form_container.windowTitle(), checked=True if ui is self._scaffold_settings_ui else False)
            tools_box.add_widget(form_container)
            layout.addWidget(tools_box, stretch=1)

        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        layout.addSpacerItem(spacer)

        form_container = QtWidgets.QWidget()
        self._buttons_ui.setupUi(form_container)
        layout.addWidget(form_container)

        setting_visibility(self._display_settings_ui, 'scaffoldcreator')

        self._dock_widget = QtWidgets.QDockWidget("Controls", self)
        self._dock_widget.setObjectName("ControlsDock")
        self._dock_widget.setWidget(parent_widget)

        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self._dock_widget)

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        Set custom scene from model
        """
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            self._model.loadSettings()
            self._setDisplayThemeBackground()
            self._refreshOptions()
            scene = self._model.getScene()
            self._ui.sceneviewer_widget.setScene(scene)
            # self._ui.sceneviewer_widget.setSelectModeAll()
            sceneviewer.setLookatParametersNonSkew([2.0, -2.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0])
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            self._autoPerturbLines()
            self._viewAllButtonClicked()

    def _setDisplayThemeBackground(self):
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            themeName = self._model.getDisplayTheme()
            backgroundColourRGB = [1.0, 1.0, 1.0] if (themeName == 'Light') else [0.0, 0.0, 0.0]
            sceneviewer.setBackgroundColourRGB(backgroundColourRGB)

    def _customParametersChange(self):
        """
        Callback when scaffold options or mesh edits are made, so custom parameter set now in use.
        """
        self._refreshParameterSetNames()

    def _sceneChanged(self):
        # new model region for choosing fields from
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setRegion(self._scaffold_model.getRegion())
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setField(
            self._scaffold_model.getDisplayModelCoordinatesField())
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setRegion(
            self._scaffold_model.getRegion())
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.getScene()
            self._ui.sceneviewer_widget.setScene(scene)
            self._autoPerturbLines()

    def _transformationChanged(self):
        self._scaffold_settings_ui.rotation_lineEdit.setText(self._scaffold_model.getRotationText())
        self._scaffold_settings_ui.scale_lineEdit.setText(self._scaffold_model.getScaleText())
        self._scaffold_settings_ui.translation_lineEdit.setText(self._scaffold_model.getTranslationText())

    def _autoPerturbLines(self):
        """
        Enable scene viewer perturb lines iff solid surfaces are drawn with lines.
        Call whenever lines, surfaces or translucency changes
        """
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setPerturbLinesFlag(self._scaffold_model.needPerturbLines())

    def _makeConnections(self):
        self._ui.sceneviewer_widget.graphicsInitialized.connect(self._graphicsInitialized)
        self._buttons_ui.pushButtonDocumentation.clicked.connect(self._documentationButtonClicked)
        self._buttons_ui.done_pushButton.clicked.connect(self._doneButtonClicked)
        self._buttons_ui.stdViews_pushButton.clicked.connect(self._stdViewsButtonClicked)
        self._buttons_ui.viewAll_pushButton.clicked.connect(self._viewAllButtonClicked)
        self._scaffold_settings_ui.subscaffoldBack_pushButton.clicked.connect(self._subscaffoldBackButtonPressed)
        self._scaffold_settings_ui.meshType_comboBox.currentIndexChanged.connect(self._scaffoldTypeChanged)
        self._scaffold_settings_ui.parameterSet_comboBox.currentIndexChanged.connect(self._parameterSetChanged)
        self._scaffold_settings_ui.deleteElementsRanges_lineEdit.editingFinished.connect(self._deleteElementRangesLineEditChanged)
        self._scaffold_settings_ui.deleteElementsSelection_pushButton.clicked.connect(self._deleteElementsSelectionButtonPressed)
        self._scaffold_settings_ui.rotation_lineEdit.editingFinished.connect(self._rotationLineEditChanged)
        self._scaffold_settings_ui.scale_lineEdit.editingFinished.connect(self._scaleLineEditChanged)
        self._scaffold_settings_ui.translation_lineEdit.editingFinished.connect(self._translationLineEditChanged)
        self._scaffold_settings_ui.applyTransformation_pushButton.clicked.connect(self._applyTransformationButtonPressed)
        self._scaffold_settings_ui.autoAlignTransformation_pushButton.clicked.connect(self._autoAlignTransformationButtonPressed)
        self._display_settings_ui.displayDataGroup_fieldChooser.setNullObjectName('-')
        self._display_settings_ui.displayDataGroup_fieldChooser.setRegion(self._segmentation_data_model.getRegion())
        self._display_settings_ui.displayDataGroup_fieldChooser.setConditional(field_is_managed_group)
        self._display_settings_ui.displayDataGroup_fieldChooser.currentIndexChanged.connect(
            self._displayDataGroupChanged)
        self._display_settings_ui.displayDataPoints_checkBox.clicked.connect(self._displayDataPointsClicked)
        self._display_settings_ui.displayDataLines_checkBox.clicked.connect(self._displayDataLinesClicked)
        self._display_settings_ui.displayDataRadius_checkBox.clicked.connect(self._displayDataRadiusClicked)
        self._display_settings_ui.displayDataMarkerPoints_checkBox.clicked.connect(self._displayDataMarkerPointsClicked)
        self._display_settings_ui.displayDataMarkerNames_checkBox.clicked.connect(self._displayDataMarkerNamesClicked)
        self._display_settings_ui.displayMarkerPoints_checkBox.clicked.connect(self._displayMarkerPointsClicked)
        self._display_settings_ui.displayMarkerNames_checkBox.clicked.connect(self._displayMarkerNamesClicked)
        self._display_settings_ui.displayZeroJacobianContours_checkBox.clicked.connect(self._displayZeroJacobianContoursClicked)
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setRegion(self._scaffold_model.getRegion())
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._display_settings_ui.displayModelCoordinates_fieldChooser.currentIndexChanged.connect(
            self._displayModelCoordinatesFieldChanged)
        self._display_settings_ui.displayAxes_checkBox.clicked.connect(self._displayAxesClicked)
        self._display_settings_ui.displayElementAxes_checkBox.clicked.connect(self._displayElementAxesClicked)
        self._display_settings_ui.displayElementNumbers_checkBox.clicked.connect(self._displayElementNumbersClicked)
        self._display_settings_ui.displayLines_checkBox.clicked.connect(self._displayLinesClicked)
        self._display_settings_ui.displayLinesExterior_checkBox.clicked.connect(self._displayLinesExteriorClicked)
        self._display_settings_ui.displayModelRadius_checkBox.clicked.connect(self._displayModelRadiusClicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD1_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD1Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD2_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD2Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD3_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD3Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD12_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD12Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD13_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD13Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD23_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD23Clicked)
        self._display_settings_ui.displayNodeDerivativeLabelsD123_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD123Clicked)
        self._display_settings_ui.displayNodeDerivatives_checkBox.clicked.connect(self._displayNodeDerivativesClicked)
        self._display_settings_ui.displayNodeDerivativesVersion_spinBox.valueChanged.connect(
            self._displayNodeDerivativeVersionValueChanged)
        self._display_settings_ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbersClicked)
        self._display_settings_ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePointsClicked)
        self._display_settings_ui.displaySurfaces_checkBox.clicked.connect(self._displaySurfacesClicked)
        self._display_settings_ui.displaySurfacesExterior_checkBox.clicked.connect(self._displaySurfacesExteriorClicked)
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.clicked.connect(self._displaySurfacesTranslucentClicked)
        self._display_settings_ui.displaySurfacesWireframe_checkBox.clicked.connect(self._displaySurfacesWireframeClicked)
        self._display_settings_ui.displayTheme_comboBox.currentIndexChanged.connect(self._displayThemeChanged)
        self._annotation_tools_ui.annotationGroup_comboBox.currentIndexChanged.connect(self._annotationGroupChanged)
        self._annotation_tools_ui.annotationGroupNew_pushButton.clicked.connect(self._annotationGroupNewButtonClicked)
        self._annotation_tools_ui.annotationGroupNewMarker_pushButton.clicked.connect(self._annotationGroupNewMarkerButtonClicked)
        self._annotation_tools_ui.annotationGroupRedefine_pushButton.clicked.connect(self._annotationGroupRedefineButtonClicked)
        self._annotation_tools_ui.annotationGroupEdit_pushButton.clicked.connect(self._annotationGroupEditButtonClicked)
        self._annotation_tools_ui.annotationGroupDelete_pushButton.clicked.connect(self._annotationGroupDeleteButtonClicked)
        self._annotation_tools_ui.annotationGroupOntId_lineEdit.editingFinished.connect(self._annotationGroupOntIdLineEditChanged)
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setRegion(self._scaffold_model.getRegion())
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setNullObjectName("-")
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setConditional(field_is_managed_coordinates)
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.currentIndexChanged.connect(
            self._markerMaterialCoordinatesFieldChanged)
        self._annotation_tools_ui.markerMaterialCoordinates_lineEdit.editingFinished.connect(
            self._markerMaterialCoordinatesLineEditChanged)
        self._annotation_tools_ui.markerElement_lineEdit.editingFinished.connect(self._markerElementLineEditChanged)
        self._annotation_tools_ui.markerXiCoordinates_lineEdit.editingFinished.connect(self._markerXiCoordinatesLineEditChanged)

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key.Key_S) and (not event.isAutoRepeat()):
            self._ui.sceneviewer_widget._selectionKeyPressed = True
            event.setAccepted(True)
        else:
            event.ignore()

    def keyReleaseEvent(self, event):
        if (event.key() == QtCore.Qt.Key.Key_S) and (not event.isAutoRepeat()):
            self._ui.sceneviewer_widget._selectionKeyPressed = False
            event.setAccepted(True)
        else:
            event.ignore()

    @staticmethod
    def _refreshComboBoxNames(comboBox, names, currentName):
        comboBox.blockSignals(True)
        comboBox.clear()
        currentIndex = 0
        index = 0
        for name in names:
            comboBox.addItem(name)
            if name == currentName:
                currentIndex = index
            index += 1
        comboBox.setCurrentIndex(currentIndex)
        comboBox.blockSignals(False)

    def _refreshScaffoldTypeNames(self):
        self._refreshComboBoxNames(
            self._scaffold_settings_ui.meshType_comboBox,
            self._scaffold_model.getAvailableScaffoldTypeNames(),
            self._scaffold_model.getEditScaffoldTypeName())

    def _refreshParameterSetNames(self):
        self._refreshComboBoxNames(
            self._scaffold_settings_ui.parameterSet_comboBox,
            self._scaffold_model.getAvailableParameterSetNames(),
            self._scaffold_model.getParameterSetName())

    def _refreshAnnotationGroups(self):
        annotationGroups = self._scaffold_model.getAnnotationGroups()
        currentAnnotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        self._refreshComboBoxNames(
            self._annotation_tools_ui.annotationGroup_comboBox,
            ['-'] + [annotationGroup.getName() for annotationGroup in annotationGroups],
            currentAnnotationGroup.getName() if currentAnnotationGroup else '-')

        view_width = self._annotation_tools_ui.annotationGroup_comboBox.minimumSizeHint().width()
        self._annotation_tools_ui.annotationGroup_comboBox.view().setMinimumWidth(view_width)

    def getModel(self):
        return self._model

    def _documentationButtonClicked(self):
        webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.argonviewerstep/docs/index.html")

    def registerDoneExecution(self, doneCallback):
        self._doneCallback = doneCallback

    def _doneButtonClicked(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        try:
            self._dock_widget.setFloating(False)
            self._model.done()
            self._model = None
            self._doneCallback()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _stdViewsButtonClicked(self):
        sceneviewer = self._ui.sceneviewer_widget.getSceneviewer()
        if sceneviewer is not None:
            result, eyePosition, lookatPosition, upVector = sceneviewer.getLookatParameters()
            upVector = normalize(upVector)
            viewVector = sub(lookatPosition, eyePosition)
            viewDistance = magnitude(viewVector)
            viewVector = normalize(viewVector)
            # viewX = dot(viewVector, [1.0, 0.0, 0.0])
            viewY = dot(viewVector, [0.0, 1.0, 0.0])
            viewZ = dot(viewVector, [0.0, 0.0, 1.0])
            # upX = dot(upVector, [1.0, 0.0, 0.0])
            upY = dot(upVector, [0.0, 1.0, 0.0])
            upZ = dot(upVector, [0.0, 0.0, 1.0])
            if (viewZ < -0.999) and (upY > 0.999):
                # XY -> XZ
                viewVector = [0.0, 1.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            elif (viewY > 0.999) and (upZ > 0.999):
                # XZ -> YZ
                viewVector = [-1.0, 0.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            else:
                # XY
                viewVector = [0.0, 0.0, -1.0]
                upVector = [0.0, 1.0, 0.0]
            eyePosition = sub(lookatPosition, mult(viewVector, viewDistance))
            sceneviewer.setLookatParametersNonSkew(eyePosition, lookatPosition, upVector)

    def _viewAllButtonClicked(self):
        if self._ui.sceneviewer_widget.getSceneviewer() is not None:
            self._ui.sceneviewer_widget.viewAll()

    def _annotationGroupChanged(self, index):
        annotationGroupName = self._annotation_tools_ui.annotationGroup_comboBox.itemText(index)
        self._scaffold_model.setCurrentAnnotationGroupByName(annotationGroupName)
        self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupNewButtonClicked(self):
        self._scaffold_model.createUserAnnotationGroup()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupNewMarkerButtonClicked(self):
        self._scaffold_model.createUserMarkerAnnotationGroup()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupRedefineButtonClicked(self):
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        if annotationGroup:
            reply = QtWidgets.QMessageBox.question(
                self, 'Confirm action',
                'Redefine annotation group \'' + annotationGroup.getName() + '\' from selection?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                if self._scaffold_model.redefineCurrentAnnotationGroupFromSelection():
                    self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupEditButtonClicked(self):
        annotationGroups = self._scaffold_model.getAnnotationGroups()
        zinc_groups = get_zinc_groups(annotationGroups)
        currentAnnotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        current_zinc_group = currentAnnotationGroup.getGroup()

        # Call a refresh to make the current selection view consistent with the current group.
        self._refresh()
        group_editor = GroupEditorWidget(self, current_zinc_group, zinc_groups)
        group_editor.group_updated.connect(self._refresh)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(group_editor)
        dlg = QtWidgets.QDialog(self)
        group_editor.close_requested.connect(dlg.close)
        dlg.setWindowFlags(dlg.windowFlags() | QtCore.Qt.WindowType.WindowContextHelpButtonHint)
        dlg.setLayout(layout)
        dlg.resize(600, 400)
        dlg.show()

    def _refresh(self):
        self._annotationGroupChanged(self._annotation_tools_ui.annotationGroup_comboBox.currentIndex())

    def _annotationGroupDeleteButtonClicked(self):
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        if annotationGroup:
            reply = QtWidgets.QMessageBox.question(
                self, 'Confirm action',
                'Delete annotation group \'' + annotationGroup.getName() + '\'?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                if self._scaffold_model.deleteAnnotationGroup(annotationGroup):
                    self._refreshAnnotationGroups()
                    self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupNameLineEditChanged(self):
        newName = self._annotation_tools_ui.annotationGroup_comboBox.currentText()
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        if annotationGroup and (annotationGroup.getName() != newName):
            if self._scaffold_model.setCurrentAnnotationGroupName(newName):
                self._refreshAnnotationGroups()
            else:
                self._refreshCurrentAnnotationGroupSettings()

    def _annotationGroupOntIdLineEditChanged(self):
        newOntId = self._annotation_tools_ui.annotationGroupOntId_lineEdit.text()
        if not self._scaffold_model.setCurrentAnnotationGroupOntId(newOntId):
            self._refreshCurrentAnnotationGroupSettings()

    def _markerMaterialCoordinatesFieldChanged(self, index):
        """
        Callback for change in marker material coordinates field.
        """
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        isUser = self._scaffold_model.isUserAnnotationGroup(annotationGroup)
        if isUser:
            markerMaterialCoordinatesField = self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.getField()
            annotationGroup.setMarkerMaterialCoordinates(markerMaterialCoordinatesField)
            self._annotation_tools_ui.markerMaterialCoordinates_lineEdit.setEnabled(markerMaterialCoordinatesField is not None)
        self._refreshCurrentAnnotationGroupSettings()

    def _markerMaterialCoordinatesLineEditChanged(self):
        """
        Callback for change in marker material coordinates.
        """
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        isUser = self._scaffold_model.isUserAnnotationGroup(annotationGroup)
        if isUser and annotationGroup.isMarker():
            markerMaterialCoordinatesField = self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.getField()
            values = parse_vector(self._annotation_tools_ui.markerMaterialCoordinates_lineEdit)
            if isinstance(values, list) and markerMaterialCoordinatesField:
                componentsCount = markerMaterialCoordinatesField.getNumberOfComponents()
                if len(values) < componentsCount:
                    values = values + [0.0]*(componentsCount - len(values))
                annotationGroup.setMarkerMaterialCoordinates(markerMaterialCoordinatesField, values)
        self._refreshCurrentAnnotationGroupSettings()

    def _markerElementLineEditChanged(self):
        """
        Callback for change in marker location element.
        """
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        isUser = self._scaffold_model.isUserAnnotationGroup(annotationGroup)
        if isUser and annotationGroup.isMarker():
            xi = annotationGroup.getMarkerLocation()[1]
            identifier = parse_int(self._annotation_tools_ui.markerElement_lineEdit)
            mesh = self._scaffold_model.getMesh()
            if isinstance(identifier, int) and isinstance(xi, list):
                element = mesh.findElementByIdentifier(identifier)
                if element.isValid():
                    annotationGroup.setMarkerLocation(element, xi)
        self._refreshCurrentAnnotationGroupSettings()

    def _markerXiCoordinatesLineEditChanged(self):
        """
        Callback for change in marker location xi coordinates.
        """
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        isUser = self._scaffold_model.isUserAnnotationGroup(annotationGroup)
        if isUser and annotationGroup.isMarker():
            element, oldXi = annotationGroup.getMarkerLocation()
            xi = parse_vector(self._annotation_tools_ui.markerXiCoordinates_lineEdit)
            if element.isValid() and isinstance(xi, list):
                dimension = element.getDimension()
                if len(xi) < dimension:
                    xi = xi + [0.0]*(dimension - len(xi))
                annotationGroup.setMarkerLocation(element, xi)
        self._refreshCurrentAnnotationGroupSettings()

    def _refreshCurrentAnnotationGroupSettings(self):
        """
        Display current annotation group settings.
        """
        annotationGroup = self._scaffold_model.getCurrentAnnotationGroup()
        isUser = (annotationGroup is not None) and self._scaffold_model.isUserAnnotationGroup(annotationGroup)
        self._annotation_tools_ui.annotationGroup_comboBox.setEditable(isUser)
        if isUser:
            self._annotation_tools_ui.annotationGroup_comboBox.lineEdit().editingFinished.connect(
                self._annotationGroupNameLineEditChanged)
            self._annotation_tools_ui.annotationGroup_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self._annotation_tools_ui.annotationGroupOntId_lineEdit.setText(annotationGroup.getId() if annotationGroup else '-')
        self._annotation_tools_ui.annotationGroupOntId_lineEdit.setEnabled(isUser)
        self._annotation_tools_ui.annotationGroupDimension_spinBox.setValue(annotationGroup.getDimension() if annotationGroup else 0)
        self._annotation_tools_ui.annotationGroupDimension_spinBox.setEnabled(False)
        self._annotation_tools_ui.annotationGroupRedefine_pushButton.setEnabled(isUser and not annotationGroup.isMarker())
        self._annotation_tools_ui.annotationGroupEdit_pushButton.setEnabled(isUser and not annotationGroup.isMarker())
        self._annotation_tools_ui.annotationGroupDelete_pushButton.setEnabled(isUser)
        markerMaterialCoordinatesField = None
        markerMaterialCoordinatesText = ""
        markerElementText = ""
        markerXiText = ""
        if (annotationGroup is not None) and annotationGroup.isMarker():
            markerMaterialCoordinatesField, markerMaterialCoordinates = annotationGroup.getMarkerMaterialCoordinates()
            self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setField(markerMaterialCoordinatesField)
            realFormat = "{:.6g}"
            if markerMaterialCoordinates:
                markerMaterialCoordinatesText = ", ".join(realFormat.format(e) for e in markerMaterialCoordinates)
            element, xi = annotationGroup.getMarkerLocation()
            if element.isValid():
                markerElementText = str(element.getIdentifier())
                markerXiText = ", ".join(realFormat.format(e) for e in xi)
            self._annotation_tools_ui.markerMaterialCoordinates_lineEdit.setEnabled(markerMaterialCoordinatesField is not None)
        self._annotation_tools_ui.markerMaterialCoordinatesField_fieldChooser.setField(markerMaterialCoordinatesField)
        self._annotation_tools_ui.markerMaterialCoordinates_lineEdit.setText(markerMaterialCoordinatesText)
        self._annotation_tools_ui.markerElement_lineEdit.setText(markerElementText)
        self._annotation_tools_ui.markerXiCoordinates_lineEdit.setText(markerXiText)
        self._annotation_tools_ui.marker_groupBox.setEnabled(isUser and (annotationGroup is not None) and annotationGroup.isMarker())

    def _scaffoldTypeChanged(self, index):
        scaffoldTypeName = self._scaffold_settings_ui.meshType_comboBox.itemText(index)
        self._scaffold_model.setScaffoldTypeByName(scaffoldTypeName)
        self._refreshParameterSetNames()
        self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _parameterSetChanged(self, index):
        parameterSetName = self._scaffold_settings_ui.parameterSet_comboBox.itemText(index)
        self._scaffold_model.setParameterSetName(parameterSetName)
        self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _meshTypeOptionCheckBoxClicked(self, checkBox):
        dependentChanges = self._scaffold_model.setScaffoldOption(checkBox.objectName(), checkBox.isChecked())
        if dependentChanges:
            self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _subscaffoldBackButtonPressed(self):
        self._scaffold_model.endEditScaffoldPackageOption()
        self._refreshScaffoldTypeNames()
        self._refreshParameterSetNames()
        self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _meshTypeOptionScaffoldPackageButtonPressed(self, pushButton):
        optionName = pushButton.objectName()
        self._scaffold_model.editScaffoldPackageOption(optionName)
        self._refreshScaffoldTypeNames()
        self._refreshParameterSetNames()
        self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _meshTypeInteractiveFunctionButtonPressed(self, pushButton):
        functionName = pushButton.objectName()
        functionOptions = self._scaffold_model.getInteractiveFunctionOptions(functionName)
        functionOptionsDialog = FunctionOptionsDialog(functionName, functionOptions, self)
        if functionOptionsDialog.exec():
            optionsChanged = self._scaffold_model.performInteractiveFunction(functionName, functionOptions)
            if optionsChanged:
                self._refreshScaffoldOptions()

    def _meshTypeOptionLineEditChanged(self, lineEdit):
        dependentChanges = self._scaffold_model.setScaffoldOption(lineEdit.objectName(), lineEdit.text())
        if dependentChanges:
            self._refreshScaffoldOptions()
        else:
            lineEdit.setText(self._scaffold_model.getEditScaffoldOptionStr(lineEdit.objectName()))
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()

    def _refreshScaffoldOptions(self):
        layout = self._scaffold_settings_ui.meshTypeOptions_frame.layout()
        # remove all current mesh type widgets
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        optionNames = self._scaffold_model.getEditScaffoldOrderedOptionNames()
        for key in optionNames:
            value = self._scaffold_model.getEditScaffoldOption(key)
            # print('key ', key, ' value ', value)
            if type(value) is bool:
                checkBox = QtWidgets.QCheckBox(self._scaffold_settings_ui.meshTypeOptions_frame)
                checkBox.setObjectName(key)
                checkBox.setText(key)
                checkBox.setChecked(value)
                callback = partial(self._meshTypeOptionCheckBoxClicked, checkBox)
                checkBox.clicked.connect(callback)
                layout.addWidget(checkBox)
            else:
                label = QtWidgets.QLabel(self._scaffold_settings_ui.meshTypeOptions_frame)
                label.setObjectName(key)
                label.setText(key)
                layout.addWidget(label)
                if isinstance(value, ScaffoldPackage):
                    pushButton = QtWidgets.QPushButton()
                    pushButton.setObjectName(key)
                    pushButton.setText('Edit >>')
                    callback = partial(self._meshTypeOptionScaffoldPackageButtonPressed, pushButton)
                    pushButton.clicked.connect(callback)
                    layout.addWidget(pushButton)
                else:
                    lineEdit = QtWidgets.QLineEdit(self._scaffold_settings_ui.meshTypeOptions_frame)
                    lineEdit.setObjectName(key)
                    lineEdit.setText(self._scaffold_model.getEditScaffoldOptionStr(key))
                    callback = partial(self._meshTypeOptionLineEditChanged, lineEdit)
                    lineEdit.editingFinished.connect(callback)
                    layout.addWidget(lineEdit)
        interativeFunctions = self._scaffold_model.getInteractiveFunctions()
        for interactiveFunction in interativeFunctions:
            pushButton = QtWidgets.QPushButton()
            pushButton.setObjectName(interactiveFunction[0])
            pushButton.setText(interactiveFunction[0])
            callback = partial(self._meshTypeInteractiveFunctionButtonPressed, pushButton)
            pushButton.clicked.connect(callback)
            layout.addWidget(pushButton)
        # refresh or show/hide standard scaffold options for transformation and deleting element ranges
        editingRootScaffold = self._scaffold_model.editingRootScaffoldPackage()
        self._buttons_ui.done_pushButton.setEnabled(editingRootScaffold)
        self._scaffold_settings_ui.subscaffold_frame.setVisible(not editingRootScaffold)
        if editingRootScaffold:
            self._scaffold_settings_ui.deleteElementsRanges_lineEdit.setText(self._scaffold_model.getDeleteElementsRangesText())
        else:
            self._scaffold_settings_ui.subscaffold_label.setText(self._scaffold_model.getEditScaffoldOptionDisplayName())
        self._scaffold_settings_ui.deleteElementsRanges_frame.setVisible(editingRootScaffold)
        self._scaffold_settings_ui.rotation_lineEdit.setText(self._scaffold_model.getRotationText())
        self._scaffold_settings_ui.scale_lineEdit.setText(self._scaffold_model.getScaleText())
        self._scaffold_settings_ui.translation_lineEdit.setText(self._scaffold_model.getTranslationText())

    def _refreshOptions(self):
        self._identifier_label.setText('Identifier:  ' + self._model.getIdentifier())
        self._display_settings_ui.displayDataGroup_fieldChooser.setField(
            self._segmentation_data_model.getDisplayDataGroup())
        self._display_settings_ui.displayDataPoints_checkBox.setChecked(self._segmentation_data_model.isDisplayDataPoints())
        self._display_settings_ui.displayDataLines_checkBox.setChecked(self._segmentation_data_model.isDisplayDataLines())
        self._display_settings_ui.displayDataRadius_checkBox.setChecked(self._segmentation_data_model.isDisplayDataRadius())
        self._display_settings_ui.displayDataMarkerPoints_checkBox.setChecked(self._segmentation_data_model.isDisplayDataMarkerPoints())
        self._display_settings_ui.displayDataMarkerNames_checkBox.setChecked(self._segmentation_data_model.isDisplayDataMarkerNames())
        self._display_settings_ui.displayData_frame.setVisible(self._segmentation_data_model.hasData())
        self._display_settings_ui.displayMarkerPoints_checkBox.setChecked(self._scaffold_model.isDisplayMarkerPoints())
        self._display_settings_ui.displayMarkerNames_checkBox.setChecked(self._scaffold_model.isDisplayMarkerNames())

        self._display_settings_ui.displayZeroJacobianContours_checkBox.setChecked(self._scaffold_model.isDisplayZeroJacobianContours())
        self._display_settings_ui.displayAxes_checkBox.setChecked(self._scaffold_model.isDisplayAxes())
        self._display_settings_ui.displayElementNumbers_checkBox.setChecked(self._scaffold_model.isDisplayElementNumbers())
        self._display_settings_ui.displayElementAxes_checkBox.setChecked(self._scaffold_model.isDisplayElementAxes())
        self._display_settings_ui.displayLines_checkBox.setChecked(self._scaffold_model.isDisplayLines())
        self._display_settings_ui.displayLinesExterior_checkBox.setChecked(self._scaffold_model.isDisplayLinesExterior())
        self._display_settings_ui.displayModelRadius_checkBox.setChecked(self._scaffold_model.isDisplayModelRadius())
        self._display_settings_ui.displayNodeDerivativeLabelsD1_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D1'))
        self._display_settings_ui.displayNodeDerivativeLabelsD2_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D2'))
        self._display_settings_ui.displayNodeDerivativeLabelsD3_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D3'))
        self._display_settings_ui.displayNodeDerivativeLabelsD12_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D12'))
        self._display_settings_ui.displayNodeDerivativeLabelsD13_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D13'))
        self._display_settings_ui.displayNodeDerivativeLabelsD23_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D23'))
        self._display_settings_ui.displayNodeDerivativeLabelsD123_checkBox.setChecked(
            self._scaffold_model.isDisplayNodeDerivativeLabels('D123'))
        displayNodeDerivatives = self._scaffold_model.getDisplayNodeDerivatives()
        self._display_settings_ui.displayNodeDerivatives_checkBox.setCheckState(
            QtCore.Qt.CheckState.Unchecked if not displayNodeDerivatives else
            QtCore.Qt.CheckState.PartiallyChecked if (displayNodeDerivatives == 1) else
            QtCore.Qt.CheckState.Checked)
        self._display_settings_ui.displayNodeDerivativesVersion_spinBox.setValue(self._scaffold_model.getDisplayNodeDerivativeVersion())
        self._display_settings_ui.displayNodeNumbers_checkBox.setChecked(self._scaffold_model.isDisplayNodeNumbers())
        self._display_settings_ui.displayNodePoints_checkBox.setChecked(self._scaffold_model.isDisplayNodePoints())
        self._display_settings_ui.displaySurfaces_checkBox.setChecked(self._scaffold_model.isDisplaySurfaces())
        self._display_settings_ui.displaySurfacesExterior_checkBox.setChecked(self._scaffold_model.isDisplaySurfacesExterior())
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.setChecked(self._scaffold_model.isDisplaySurfacesTranslucent())
        self._display_settings_ui.displaySurfacesWireframe_checkBox.setChecked(self._scaffold_model.isDisplaySurfacesWireframe())
        index = self._display_settings_ui.displayTheme_comboBox.findText(self._model.getDisplayTheme())
        self._display_settings_ui.displayTheme_comboBox.blockSignals(True)
        self._display_settings_ui.displayTheme_comboBox.setCurrentIndex(index)
        self._display_settings_ui.displayTheme_comboBox.blockSignals(False)
        index = self._scaffold_settings_ui.meshType_comboBox.findText(self._scaffold_model.getEditScaffoldTypeName())
        self._scaffold_settings_ui.meshType_comboBox.blockSignals(True)
        self._scaffold_settings_ui.meshType_comboBox.setCurrentIndex(index)
        self._scaffold_settings_ui.meshType_comboBox.blockSignals(False)
        self._refreshParameterSetNames()
        self._refreshScaffoldOptions()
        self._refreshAnnotationGroups()
        self._refreshCurrentAnnotationGroupSettings()
        self._buttons_ui.done_pushButton.setEnabled(True)
        self._scaffold_settings_ui.subscaffold_frame.setVisible(False)

    def _deleteElementRangesLineEditChanged(self):
        self._scaffold_model.setDeleteElementsRangesText(self._scaffold_settings_ui.deleteElementsRanges_lineEdit.text())
        self._scaffold_settings_ui.deleteElementsRanges_lineEdit.setText(self._scaffold_model.getDeleteElementsRangesText())

    def _deleteElementsSelectionButtonPressed(self):
        self._scaffold_model.deleteElementsSelection()
        self._scaffold_settings_ui.deleteElementsRanges_lineEdit.setText(self._scaffold_model.getDeleteElementsRangesText())

    def _rotationLineEditChanged(self):
        self._scaffold_model.setRotationText(self._scaffold_settings_ui.rotation_lineEdit.text())
        self._scaffold_settings_ui.rotation_lineEdit.setText(self._scaffold_model.getRotationText())

    def _scaleLineEditChanged(self):
        self._scaffold_model.setScaleText(self._scaffold_settings_ui.scale_lineEdit.text())
        self._scaffold_settings_ui.scale_lineEdit.setText(self._scaffold_model.getScaleText())

    def _translationLineEditChanged(self):
        self._scaffold_model.setTranslationText(self._scaffold_settings_ui.translation_lineEdit.text())
        self._scaffold_settings_ui.translation_lineEdit.setText(self._scaffold_model.getTranslationText())

    def _applyTransformationButtonPressed(self):
        self._scaffold_model.applyTransformation(self._display_settings_ui.displayModelCoordinates_fieldChooser.getField())
        self._transformationChanged()

    def _autoAlignTransformationButtonPressed(self):
        # Create dialog
        reply = QtWidgets.QDialog(self)
        reply.setWindowTitle('Confirm action')
        layout = QtWidgets.QVBoxLayout(reply)
        hasData = self._segmentation_data_model.hasData()
        if not hasData:
            # Add text
            textLabel = QtWidgets.QLabel('No data file supplied')
            textLabel.setWordWrap(True)
            layout.addWidget(textLabel)
            layout.addSpacing(10)
            # add Ok Button
            buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok)
            buttons.accepted.connect(reply.reject)    
            layout.addWidget(buttons)
        else:
            # Initilize fitter 
            canAutoAlign = self._scaffold_model.initializeAutoAlignTransformation()
            if canAutoAlign:
                # Add text
                textLabel = QtWidgets.QLabel('Automatically align scaffold to data?')
                textLabel.setWordWrap(True)
                layout.addWidget(textLabel)
                layout.addSpacing(10)
                # Add buttons
                buttons = QtWidgets.QDialogButtonBox(
                    QtWidgets.QDialogButtonBox.StandardButton.Yes |
                      QtWidgets.QDialogButtonBox.StandardButton.No
                )
                layout.addWidget(buttons)   
                buttons.accepted.connect(reply.accept)
                buttons.rejected.connect(reply.reject)
            else:
                # Add text
                textLabel = QtWidgets.QLabel('Not enough markers and/or groups' \
                ' to perform automatic alignment to data')
                textLabel.setWordWrap(True)
                layout.addWidget(textLabel)
                layout.addSpacing(10)
                # add Ok Button
                buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok)
                layout.addWidget(buttons)
                buttons.accepted.connect(reply.reject)    
        # Execute dialog
        if reply.exec() == QtWidgets.QDialog.Accepted:
            self._scaffold_model.runAutoAlignTransformation()
            self._transformationChanged()

    def _displayDataGroupChanged(self, index):
        """
        Callback for change in model coordinates field chooser widget.
        """
        field = self._display_settings_ui.displayDataGroup_fieldChooser.getField()
        group = None
        if field:
            group = field.castGroup()
            if not group.isValid():
                group = None
        self._segmentation_data_model.setDisplayDataGroup(group)

    def _displayDataPointsClicked(self):
        self._segmentation_data_model.setDisplayDataPoints(self._display_settings_ui.displayDataPoints_checkBox.isChecked())

    def _displayDataLinesClicked(self):
        self._segmentation_data_model.setDisplayDataLines(self._display_settings_ui.displayDataLines_checkBox.isChecked())

    def _displayDataRadiusClicked(self):
        self._segmentation_data_model.setDisplayDataRadius(self._display_settings_ui.displayDataRadius_checkBox.isChecked())

    def _displayDataMarkerPointsClicked(self):
        self._segmentation_data_model.setDisplayDataMarkerPoints(self._display_settings_ui.displayDataMarkerPoints_checkBox.isChecked())

    def _displayDataMarkerNamesClicked(self):
        self._segmentation_data_model.setDisplayDataMarkerNames(self._display_settings_ui.displayDataMarkerNames_checkBox.isChecked())

    def _displayMarkerPointsClicked(self):
        self._scaffold_model.setDisplayMarkerPoints(self._display_settings_ui.displayMarkerPoints_checkBox.isChecked())

    def _displayMarkerNamesClicked(self):
        self._scaffold_model.setDisplayMarkerNames(self._display_settings_ui.displayMarkerNames_checkBox.isChecked())

    def _displayZeroJacobianContoursClicked(self):
        self._scaffold_model.setDisplayZeroJacobianContours(self._display_settings_ui.displayZeroJacobianContours_checkBox.isChecked())

    def _displayModelCoordinatesFieldChanged(self, index):
        """
        Callback for change in model coordinates field chooser widget.
        """
        field = self._display_settings_ui.displayModelCoordinates_fieldChooser.getField()
        if field:
            self._scaffold_model.setDisplayModelCoordinatesField(field)  # will re-create graphics

    def _displayAxesClicked(self):
        self._scaffold_model.setDisplayAxes(self._display_settings_ui.displayAxes_checkBox.isChecked())

    def _displayElementAxesClicked(self):
        self._scaffold_model.setDisplayElementAxes(self._display_settings_ui.displayElementAxes_checkBox.isChecked())

    def _displayElementNumbersClicked(self):
        self._scaffold_model.setDisplayElementNumbers(self._display_settings_ui.displayElementNumbers_checkBox.isChecked())

    def _displayLinesClicked(self):
        self._scaffold_model.setDisplayLines(self._display_settings_ui.displayLines_checkBox.isChecked())
        self._autoPerturbLines()

    def _displayLinesExteriorClicked(self):
        self._scaffold_model.setDisplayLinesExterior(self._display_settings_ui.displayLinesExterior_checkBox.isChecked())

    def _displayModelRadiusClicked(self):
        self._scaffold_model.setDisplayModelRadius(self._display_settings_ui.displayModelRadius_checkBox.isChecked())

    def _displayNodeDerivativesClicked(self):
        checkState = self._display_settings_ui.displayNodeDerivatives_checkBox.checkState()
        triState = (0 if (checkState == QtCore.Qt.CheckState.Unchecked) else
                    1 if (checkState == QtCore.Qt.CheckState.PartiallyChecked) else 2)
        self._scaffold_model.setDisplayNodeDerivatives(triState)

    def _displayNodeDerivativeLabelsD1Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D1', self._display_settings_ui.displayNodeDerivativeLabelsD1_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD2Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D2', self._display_settings_ui.displayNodeDerivativeLabelsD2_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD3Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D3', self._display_settings_ui.displayNodeDerivativeLabelsD3_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD12Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D12', self._display_settings_ui.displayNodeDerivativeLabelsD12_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD13Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D13', self._display_settings_ui.displayNodeDerivativeLabelsD13_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD23Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D23', self._display_settings_ui.displayNodeDerivativeLabelsD23_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD123Clicked(self):
        self._scaffold_model.setDisplayNodeDerivativeLabels(
            'D123', self._display_settings_ui.displayNodeDerivativeLabelsD123_checkBox.isChecked())

    def _displayNodeDerivativeVersionValueChanged(self, version):
        self._scaffold_model.setDisplayNodeDerivativeVersion(version)

    def _displayNodeNumbersClicked(self):
        self._scaffold_model.setDisplayNodeNumbers(self._display_settings_ui.displayNodeNumbers_checkBox.isChecked())

    def _displayNodePointsClicked(self):
        self._scaffold_model.setDisplayNodePoints(self._display_settings_ui.displayNodePoints_checkBox.isChecked())

    def _displaySurfacesClicked(self):
        self._scaffold_model.setDisplaySurfaces(self._display_settings_ui.displaySurfaces_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesExteriorClicked(self):
        self._scaffold_model.setDisplaySurfacesExterior(self._display_settings_ui.displaySurfacesExterior_checkBox.isChecked())

    def _displaySurfacesTranslucentClicked(self):
        self._scaffold_model.setDisplaySurfacesTranslucent(self._display_settings_ui.displaySurfacesTranslucent_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesWireframeClicked(self):
        self._scaffold_model.setDisplaySurfacesWireframe(self._display_settings_ui.displaySurfacesWireframe_checkBox.isChecked())

    def _displayThemeChanged(self, index):
        themeName = self._display_settings_ui.displayTheme_comboBox.itemText(index)
        self._model.setDisplayTheme(themeName)
        self._setDisplayThemeBackground()
