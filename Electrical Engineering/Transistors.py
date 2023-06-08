import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, \
    QPlainTextEdit


# main window class for the Transistor Curve program
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.TransistorNames = []
        self.TransistorTypes = []
        self.TransistorVoltages = []

        self.setWindowTitle("FETS")
        self.setGeometry(100, 100, 600, 400)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.label = QLabel("Transistor Name:")
        self.layout.addWidget(self.label)

        self.TransistorName = QLineEdit()
        self.layout.addWidget(self.TransistorName)

        self.label = QLabel("Transistor Voltage:")
        self.layout.addWidget(self.label)

        self.TransistorVoltage = QLineEdit()
        self.layout.addWidget(self.TransistorVoltage)

        self.buttonAdd = QPushButton("Add Transistor")
        self.buttonAdd.clicked.connect(self.AddTransistor)
        self.layout.addWidget(self.buttonAdd)

        self.buttonReplace = QPushButton("Replace Transistor")
        self.buttonReplace.clicked.connect(self.ReplaceTransistor)
        self.layout.addWidget(self.buttonReplace)

        self.listBoxOutput = QPlainTextEdit()
        self.layout.addWidget(self.listBoxOutput)

        self.buttonPlot = QPushButton("Plot Transistor")
        self.buttonPlot.clicked.connect(self.PlotTransistor)
        self.layout.addWidget(self.buttonPlot)

    # Check if the transistor is a FET or BJT
    def FETorBJT(self, transistorName):
        secondChar = transistorName[1].upper() if len(transistorName) > 1 else ' '

        if secondChar == 'S':
            return "FET"
        elif secondChar == 'C':
            return "BJT"
        else:
            return "Unknown Transistor Type"

    # Update the list box with the transistor names
    def AddTransistor(self):
        transistorName = self.TransistorName.text()
        transistorVoltage = self.TransistorVoltage.text()

        transistorType = self.FETorBJT(transistorName)

        # Überprüfen, ob der Name bereits vorhanden ist
        if transistorName in self.TransistorNames:
            self.listBoxOutput.appendPlainText("Transistor mit diesem Namen existiert bereits.")
            return

        # Überprüfen, ob die Arrays voll sind
        if len(self.TransistorNames) >= 4:
            self.listBoxOutput.appendPlainText("Alle Speicherplätze sind belegt.")
            return

        # Speichern des Transistornamens, -typs und der Spannung in den Arrays
        self.TransistorNames.append(transistorName)
        self.TransistorTypes.append(transistorType)
        self.TransistorVoltages.append(transistorVoltage)

        self.UpdateListBox()

    # Replace the selected transistor with the new one
    def ReplaceTransistor(self):
        selectedIndexes = self.listBoxOutput.selectedIndexes()
        if selectedIndexes:
            selectedIndex = selectedIndexes[0].row()

            oldTransistorName = self.TransistorNames[selectedIndex]
            transistorName = self.TransistorName.text()
            transistorVoltage = self.TransistorVoltage.text()

            transistorType = self.FETorBJT(transistorName)
            transistorVoltageOld = self.TransistorVoltages[selectedIndex]

            # Überprüfen, ob der Name bereits vorhanden ist
            if transistorName != oldTransistorName and transistorName in self.TransistorNames:
                self.listBoxOutput.appendPlainText("Transistor mit diesem Namen existiert bereits.")
                return

            # Aktualisieren der Daten des ausgewählten Transistors
            self.TransistorNames[selectedIndex] = transistorName
            self.TransistorTypes[selectedIndex] = transistorType
            self.TransistorVoltages[selectedIndex] = transistorVoltage

            self.listBoxOutput.appendPlainText(
                f"Name: {oldTransistorName} - Type: {transistorType} - Spannung: {transistorVoltageOld} Volt wurde durch "
                f"Name: {transistorName} - Type: {transistorType} - Spannung: {transistorVoltage} Volt ersetzt.")

            self.UpdateListBox()

    # Update the list box with the transistor names
    def UpdateListBox(self):
        self.listBoxOutput.clear()
        for i in range(len(self.TransistorNames)):
            name = self.TransistorNames[i]
            typ = self.TransistorTypes[i]
            voltage = self.TransistorVoltages[i]
            self.listBoxOutput.appendPlainText(f"Name: {name} - Type: {typ} - Spannung: {voltage} Volt")

    # Plot the selected transistor
    def PlotTransistor(self):
        selectedText = self.listBoxOutput.toPlainText()
        if selectedText:
            selectedTransistor = selectedText.split('-')[0].strip()
            self.plotTransistor(selectedTransistor)

    # Plot the transistor curve
    def plotTransistor(self, transistorName):
        x = np.linspace(0, 5, 100)
        y = np.sin(x)

        plt.plot(x, y)
        plt.xlabel('Eingangsspannung (V)')
        plt.ylabel('Ausgangsstrom (A)')
        plt.title(f"Ausgangskurve von Transistor: {transistorName}")
        plt.show()

    # Close the window
    def closeEvent(self, event):
        event.accept()


# main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
