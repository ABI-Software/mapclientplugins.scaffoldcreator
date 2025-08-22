from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.context import Context
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphics, Graphicslineattributes
from cmlibs.zinc.material import Material
from mapclientplugins.scaffoldcreator.model.scaffoldcreatormodel import ScaffoldCreatorModel
from mapclientplugins.scaffoldcreator.model.segmentationdatamodel import SegmentationDataModel
from scaffoldmaker.scaffolds import Scaffolds_decodeJSON, Scaffolds_JSONEncoder
import os
import json
from PySide6 import QtCore


class MasterModel:

    def __init__(self, location, identifier):
        self._location = location
        self._identifier = identifier
        self._filenameStem = os.path.join(self._location, self._identifier)
        self._context = Context("ScaffoldCreator")
        self._timekeeper = self._context.getTimekeepermodule().getDefaultTimekeeper()
        self._timer = QtCore.QTimer()
        self._current_time = 0.0
        self._timeValueUpdate = None
        self._frameIndexUpdate = None
        self._initialise()
        self._region = self._context.createRegion()
        self._creator_model = ScaffoldCreatorModel(self._context, self._region, self._materialmodule)
        self._segmentation_data_model = SegmentationDataModel(self._region, self._materialmodule)
        self._settings = {}
        self._displaySettings = {
            'displayTheme': 'Dark'
        }

    def printLog(self):
        logger = self._context.getLogger()
        for index in range(logger.getNumberOfMessages()):
            print(logger.getMessageTextAtIndex(index))

    def _initialise(self):
        self._filenameStem = os.path.join(self._location, self._identifier)
        tess = self._context.getTessellationmodule().getDefaultTessellation()
        tess.setRefinementFactors(12)
        # set up standard materials and glyphs so we can use them elsewhere
        self._materialmodule = self._context.getMaterialmodule()
        self._materialmodule.defineStandardMaterials()
        solid_blue = self._materialmodule.createMaterial()
        solid_blue.setName('solid_blue')
        solid_blue.setManaged(True)
        solid_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
        solid_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
        solid_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
        solid_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
        solid_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
        trans_blue = self._materialmodule.createMaterial()
        trans_blue.setName('trans_blue')
        trans_blue.setManaged(True)
        trans_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
        trans_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
        trans_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
        trans_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
        trans_blue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.3)
        trans_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()

    def getIdentifier(self):
        return self._identifier

    def getZincScaffoldFilename(self):
        return self._filenameStem + '.exf'

    def getJsonSettingsFilename(self):
        return self._filenameStem + '-settings.json'

    def getJsonDisplaySettingsFilename(self):
        return self._filenameStem + '-display-settings.json'

    def getDisplayTheme(self):
        return self._displaySettings['displayTheme']

    def _applyDisplayTheme(self):
        """
        Update sub-model graphics materials for the current theme.
        """
        displayThemeName = self._displaySettings['displayTheme']
        # defaultColourRGB = [0.0, 0.0, 0.0] if (themeName == 'Light') else [1.0, 1.0, 1.0]
        # defaultMaterial = self._materialmodule.getDefaultMaterial()
        # defaultMaterial.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, defaultColourRGB)
        # defaultMaterial.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, defaultColourRGB)
        self._creator_model.setDisplayTheme(displayThemeName)
        self._segmentation_data_model.setDisplayTheme(displayThemeName)

    def setDisplayTheme(self, displayThemeName):
        assert displayThemeName in ('Dark', 'Light')
        self._displaySettings['displayTheme'] = displayThemeName
        self._applyDisplayTheme()

    def getCreatorModel(self):
        return self._creator_model

    def getSegmentationDataModel(self):
        return self._segmentation_data_model

    def getScene(self):
        return self._region.getScene()

    def getContext(self):
        return self._context

    def registerSceneChangeCallback(self, sceneChangeCallback):
        self._creator_model.registerSceneChangeCallback(sceneChangeCallback)

    def done(self):
        # save settings first in case of issues with other outputs
        self._saveSettings()
        self._creator_model.done()
        self._creator_model.writeModel(self.getZincScaffoldFilename())
        self._creator_model.exportToVtk(self._filenameStem)

    SCAFFOLD_CREATOR_SETTINGS_ID = 'scaffold creator settings'

    def _getSettings(self):
        """
        :return: Settings for scaffold, segmentation data and metadata, ready to write.
        """
        self._creator_model.updateSettingsBeforeWrite()
        return {
            'id': self.SCAFFOLD_CREATOR_SETTINGS_ID,
            'version': '1.0.0',
            'general_settings': self._settings,
            'scaffold_settings': self._creator_model.getSettings(),
            'segmentation_data_settings': self._segmentation_data_model.getSettings(),
            'metadata': self._creator_model.getMetadata()
        }

    SCAFFOLD_CREATOR_DISPLAY_SETTINGS_ID = 'scaffold creator display settings'

    def _getDisplaySettings(self):
        """
        :return: Combined display settings for scaffold and segmentation data, ready to write.
        """
        return {
            'id': self.SCAFFOLD_CREATOR_DISPLAY_SETTINGS_ID,
            'version': '1.0.0',
            'general_settings': self._displaySettings,
            'scaffold_settings': self._creator_model.getDisplaySettings(),
            'segmentation_data_settings': self._segmentation_data_model.getDisplaySettings()
        }

    @classmethod
    def migrateLegacyCombinedSettings(cls, settings):
        """
        Migrate from legacy combined creator and display settings to separate dicts.
        A number of legacy options are also migrated by this function.
        :param settings: Combined legacy settings read from file.
        :return: settings dict, displaySettings dict
        """
        if 'generator_settings' in settings:
            # migrate from generator_settings in version 0.3.2
            settings = {
                'scaffold_settings': settings['generator_settings'],
                'segmentation_data_settings': settings.pop('segmentation_data_settings', {})
            }
        if 'scaffold_settings' not in settings:
            # migrate from version 0.2.0 settings
            settings = {
                'scaffold_settings': settings,
                'segmentation_data_settings': settings.pop('segmentation_data_settings', {})
            }
        ScaffoldCreatorModel.migrateLegacyCombinedSettings(settings['scaffold_settings'])
        # separate display settings which were in the same file
        scaffoldDisplaySettings = {}
        removeKeys = []
        creator_settings = settings['scaffold_settings']
        for key, value in creator_settings.items():
            if 'display' in key:
                scaffoldDisplaySettings[key] = value
                removeKeys.append(key)
        for key in removeKeys:
            creator_settings.pop(key)
        # note: at the time, segmentation data only had display settings
        SegmentationDataModel.migrateLegacyCombinedSettings(settings['segmentation_data_settings'])
        displaySettings = {
            'scaffold_settings': scaffoldDisplaySettings,
            'segmentation_data_settings': settings['segmentation_data_settings']
        }
        # add settings for future/new use:
        settings['segmentation_data_settings'] = {}
        settings['general_settings'] = {}
        displaySettings['general_settings'] = {}
        return settings, displaySettings

    def loadSettings(self):
        displaySettings = {}  # may be set from legacy combined settings and display settings
        settingsFilename = self.getJsonSettingsFilename()
        hasSettingsFile = os.path.isfile(settingsFilename)
        if hasSettingsFile:
            with open(self.getJsonSettingsFilename(), 'r') as f:
                settings = json.loads(f.read(), object_hook=Scaffolds_decodeJSON)
            if 'version' in settings:
                assert settings['id'] == self.SCAFFOLD_CREATOR_SETTINGS_ID
            else:
                settings, displaySettings = self.migrateLegacyCombinedSettings(settings)
            self._settings.update(settings.get('general_settings', {}))
            self._creator_model.setSettings(settings['scaffold_settings'])
            self._segmentation_data_model.setSettings(settings['segmentation_data_settings'])

        displaySettingsFileName = self.getJsonDisplaySettingsFilename()
        hasDisplaySettingsFile = os.path.isfile(displaySettingsFileName)
        if hasDisplaySettingsFile or displaySettings:
            if hasDisplaySettingsFile:
                with open(displaySettingsFileName, "r") as f:
                    displaySettings = json.loads(f.read())
                assert displaySettings['id'] == self.SCAFFOLD_CREATOR_DISPLAY_SETTINGS_ID
                assert 'version' in displaySettings
            self._displaySettings.update(displaySettings.get('general_settings', {}))
            self._creator_model.setDisplaySettings(displaySettings['scaffold_settings'])
            self._segmentation_data_model.setDisplaySettings(displaySettings['segmentation_data_settings'])

        self._creator_model.generate()
        self._segmentation_data_model.buildGraphics()
        self._applyDisplayTheme()

    def _saveSettings(self):
        settings = self._getSettings()
        with open(self.getJsonSettingsFilename(), 'w') as f:
            f.write(json.dumps(settings, cls=Scaffolds_JSONEncoder, sort_keys=True, indent=4))
        displaySettings = self._getDisplaySettings()
        with open(self.getJsonDisplaySettingsFilename(), "w") as f:
            f.write(json.dumps(displaySettings, sort_keys=True, indent=4))

    def setSegmentationDataFile(self, data_filename):
        self._segmentation_data_model.setDataFilename(data_filename)
