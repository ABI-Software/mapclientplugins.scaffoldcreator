"""
MAP Client Plugin Step
"""
import json
import os.path

from PySide6 import QtGui, QtWidgets, QtCore

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.scaffoldcreator.configuredialog import ConfigureDialog
from mapclientplugins.scaffoldcreator.model.mastermodel import MasterModel
from mapclientplugins.scaffoldcreator.view.scaffoldcreatorwidget import ScaffoldCreatorWidget


class ScaffoldCreator(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(ScaffoldCreator, self).__init__('Scaffold Creator', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/scaffoldcreator/images/model-viewer.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#json_file_location')
                      ])
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port1_inputZincDataFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port2_jsonMetadataFilename = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#json_file_location
        # Config:
        self._config = {'identifier': '', 'AutoDone': False, 'enable-auto-done': False}
        self._model = None
        self._view = None

    def _create_model(self):
        """
        Ensure self._model is constructed if not already existing.
        """
        if not self._model:
            self._model = MasterModel(self._location, self._config['identifier'])

    def execute(self):
        """
        Kick off the execution of the step, in this case an interactive dialog.
        User invokes the _doneExecution() method when finished, via pushbutton.
        """
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        try:
            self._create_model()
            if self._port1_inputZincDataFile:
                self._model.setSegmentationDataFile(self._port1_inputZincDataFile)
            self._view = ScaffoldCreatorWidget(self._model)
            # self._view.setWindowFlags(QtCore.Qt.Widget)
            if self._config['AutoDone']:
                self._my_done_execution()
            else:
                self._view.registerDoneExecution(self._my_done_execution)
                self._setCurrentWidget(self._view)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _my_done_execution(self):
        self._portData0 = self._model.getOutputModelFilename()
        self._port2_jsonMetadataFilename = self._model.getOutputJsonMetadataFilename()
        self._view = None
        self._model = None
        self._config['enable-auto-done'] = os.path.isfile(self._portData0)
        self._doneExecution()

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        if index == 0:
            return self._portData0  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

        return self._port2_jsonMetadataFilename

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if index == 1:
            self._port1_inputZincDataFile = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def _update_config(self):
        model = MasterModel(self._location, self._config['identifier'])
        output_filename = model.getOutputModelFilename()
        if os.path.isfile(output_filename):
            self._config['enable-auto-done'] = True
        else:
            self._config['enable-auto-done'] = False
            self._config['AutoDone'] = False

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        self._update_config()
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        self._update_config()
        d.setConfig(self._config)
        self._configured = d.validate()

    def getAdditionalConfigFiles(self):
        self._create_model()
        return [self._model.getSettingsFilename()]
