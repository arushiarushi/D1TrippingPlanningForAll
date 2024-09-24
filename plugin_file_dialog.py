import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsMessageLog, QgsProject
from PyQt5.QtCore import QTime

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'plugin_file_dialog_base.ui'))

class MyDialogPluginDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MyDialogPluginDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.saveName)
        self.saveFile.clicked.connect(self.onSaveFileClicked)  # connect saveFile button to the function
        self.saveTimesButton.clicked.connect(self.saveTimes)

        self.saveFileClicked = False  # variable to track whether the saveFile button is clicked

    def onSaveFileClicked(self):
        self.saveFileClicked = True

    def saveName(self):
        name = self.name_input.toPlainText()
        zoneInput = self.zoneInput.text()  # assuming zoneInput is the input for GeoJSON file

        if name:
            self.saveToFile(name, zoneInput, self.saveFileClicked)
            self.close()
        else:
            QgsMessageLog.logMessage("Please enter a name.", "Your Plugin Name")

    def saveToFile(self, name, zoneInput, saveFileClicked):
        # Specify the absolute path for the directory
        directory = '/Users/arushiagarwal/Desktop/plugin_file'
        file_path = os.path.join(directory, 'output.txt')

        try:
            # Create the directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)

            with open(file_path, 'a') as file:
                file.write(f"Name: {name}\n")
                if saveFileClicked:
                    file.write(f"GeoJSON Link: {zoneInput}\n")
            QgsMessageLog.logMessage(f"Data saved to file: {file_path}", "Your Plugin Name")
        except Exception as e:
            QgsMessageLog.logMessage(f"Error saving data to file: {str(e)}", "Your Plugin Name")

    def saveTimes(self):
        time_from = self.weekdayFrom.time()
        time_to = self.weekdayTo.time()
        weekend_from = self.weekendFrom.time()
        weekend_to = self.weekendTo.time()
        holiday_from = self.holidayFrom.time()
        holiday_to = self.holidayTo.time()

        try:
            self.saveTimesToFile(time_from, time_to, weekend_from, weekend_to, holiday_from, holiday_to)
            self.close()
        except Exception as e:
            QgsMessageLog.logMessage(f"Error saving times to file: {str(e)}", "Your Plugin Name")

    def saveTimesToFile(self, time_from, time_to, weekend_from, weekend_to, holiday_from, holiday_to):
        # Specify the absolute path for the directory
        directory = '/Users/arushiagarwal/Desktop/plugin_file'
        file_path = os.path.join(directory, 'output.txt')

        try:
            # Create the directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)

            with open(file_path, 'a') as file:
                file.write(f"Weekday: from {time_from.toString('hh:mm')} to {time_to.toString('hh:mm')}\n")
                file.write(f"Weekend: from {weekend_from.toString('hh:mm')} to {weekend_to.toString('hh:mm')}\n")
                file.write(f"Holiday: from {holiday_from.toString('hh:mm')} to {holiday_to.toString('hh:mm')}\n")
            QgsMessageLog.logMessage(f"Times saved to file: {file_path}", "Your Plugin Name")
        except Exception as e:
            QgsMessageLog.logMessage(f"Error saving times to file: {str(e)}", "Your Plugin Name")

    def saveToFile(self, name, zoneInput, saveFileClicked):
    # Specify the absolute path for the directory
    directory = '/Users/arushiagarwal/Desktop/plugin_file'
    file_path = os.path.join(directory, 'output.txt')
    geojson_path = os.path.join(directory, f'{zoneInput}.geojson')  # New GeoJSON file path

    try:
        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        with open(file_path, 'a') as file:
            file.write(f"Name: {name}\n")
            if saveFileClicked:
                file.write(f"GeoJSON Link: {zoneInput}\n")
        
        # Rename the GeoJSON file
        os.rename(zoneInput, geojson_path)

        QgsMessageLog.logMessage(f"Data saved to file: {file_path}", "Your Plugin Name")
        QgsMessageLog.logMessage(f"GeoJSON renamed to: {geojson_path}", "Your Plugin Name")
    except Exception as e:
        QgsMessageLog.logMessage(f"Error saving data to file: {str(e)}", "Your Plugin Name")

