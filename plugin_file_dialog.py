import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsMessageLog  # Add this import

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'plugin_file_dialog_base.ui'))


class MyDialogPluginDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MyDialogPluginDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.save_button.clicked.connect(self.saveName)

    def saveName(self):
        name = self.name_input.text()

        if name:
            self.saveToFile(name)
            self.close()
        else:
            QgsMessageLog.logMessage("Please enter a name.", "Your Plugin Name", QgsMessageLog.WARNING)

    def saveToFile(self, name):
        file_path = 'Desktop/plugin_file/output.txt'

        try:
            with open(file_path, 'w') as file:
                file.write(name)
            QgsMessageLog.logMessage(f"Name '{name}' saved to file: {file_path}", "Your Plugin Name", QgsMessageLog.INFO)
        except Exception as e:
            QgsMessageLog.logMessage(f"Error saving name to file: {str(e)}", "Your Plugin Name", QgsMessageLog.CRITICAL)
