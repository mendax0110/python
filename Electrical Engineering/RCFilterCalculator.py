import math
import sys

# import the PyQt5 plotting module
import pyqtgraph as pg
from PyQt5.QtGui import QDoubleValidator
# import the Qt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QPushButton


class FilterCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # create the GUI widgets
        self.type_label = QLabel("Filter Type:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Lowpass", "Highpass"])

        self.resistor_label = QLabel("Resistor (Ω):")
        self.resistor_edit = QLineEdit()
        self.resistor_edit.setValidator(QDoubleValidator())

        self.capacitor_label = QLabel("Capacitor (F):")
        self.capacitor_edit = QLineEdit()
        self.capacitor_edit.setValidator(QDoubleValidator())

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_filter)

        # create the PyQt5 plot widget
        self.plot_widget = pg.PlotWidget()

        # create a vertical layout to hold the widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.type_label)
        vbox.addWidget(self.type_combo)
        vbox.addWidget(self.resistor_label)
        vbox.addWidget(self.resistor_edit)
        vbox.addWidget(self.capacitor_label)
        vbox.addWidget(self.capacitor_edit)
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.plot_widget)

        # set the layout and show the window
        self.setLayout(vbox)
        self.show()

    def calculate_filter(self):
        # get the filter type and values from the GUI widgets
        filter_type = self.type_combo.currentText()
        resistor = float(self.resistor_edit.text())
        capacitor = float(self.capacitor_edit.text())

        # calculate the cutoff frequency
        cutoff_frequency = 1 / (2 * math.pi * resistor * capacitor)

        # create the x and y data for the plot
        num_points = 100
        x_data = [i * cutoff_frequency / num_points for i in range(num_points + 1)]
        y_data = []
        for x in x_data:
            if filter_type == "Lowpass":
                y = 1 / (1 + (1j * x * resistor * capacitor))
            else:  # filter_type == "Highpass"
                y = (1j * x * resistor * capacitor) / (1 + (1j * x * resistor * capacitor))
            y_data.append(abs(y))

        # plot the data
        self.plot_widget.clear()
        self.plot_widget.plot(x_data, y_data)


if __name__ == "__main__":
    # create the Qt5 application and the filter calculator window
    app = QApplication(sys.argv)
    window = FilterCalculator()

    # start the Qt5 application
    sys.exit(app.exec_())
