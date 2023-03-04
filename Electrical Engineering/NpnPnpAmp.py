import sys
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.plot_widget = PlotWidget(self)
        self.setCentralWidget(self.plot_widget)

        self.setWindowTitle('NPN/PNP Amplifier Plot')


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.plot_figure = Figure()
        self.plot_canvas = FigureCanvas(self.plot_figure)

        self.plot_axes = self.plot_figure.add_subplot()
        self.plot_axes.set_xlabel('Input Voltage (V)')
        self.plot_axes.set_ylabel('Output Voltage (V)')
        self.plot_axes.set_xlim([0, 5])
        self.plot_axes.set_ylim([0, 5])

        self.plot_canvas.draw()

        self.transistor_type_label = QLabel('Transistor Type')
        self.transistor_type_edit = QLineEdit('NPN')

        self.input_voltage_label = QLabel('Input Voltage (V)')
        self.input_voltage_edit = QLineEdit('1.0')

        self.generate_button = QPushButton('Generate Plot')
        self.generate_button.clicked.connect(self.on_generate_button_clicked)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_canvas)

        form_layout = QHBoxLayout()
        form_layout.addWidget(self.transistor_type_label)
        form_layout.addWidget(self.transistor_type_edit)
        form_layout.addWidget(self.input_voltage_label)
        form_layout.addWidget(self.input_voltage_edit)
        form_layout.addWidget(self.generate_button)

        self.layout.addLayout(form_layout)

        self.setLayout(self.layout)

    @pyqtSlot()
    def on_generate_button_clicked(self):
        voltage_max = 5.0  # maximum output voltage
        gain = 100.0  # amplifier gain
        cutoff = 0.7  # cutoff voltage of the transistor

        try:
            input_voltage = float(self.input_voltage_edit.text())
        except ValueError:
            return

        if self.transistor_type_edit.text() == 'NPN':
            x = [i / 100 for i in range(int(input_voltage * 100) + 1)]
            y = [max(min((i - cutoff) * gain, voltage_max), 0.0) for i in x]
            self.plot_axes.plot(x, y, color='blue')
        elif self.transistor_type_edit.text() == 'PNP':
            x = [i / 100 for i in range(int(input_voltage * 100) + 1)]
            y = [max(min((cutoff - i) * gain, voltage_max), 0.0) for i in x]
            self.plot_axes.plot(x, y, color='red')

        self.plot_canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotWindow()
    window.show()
    sys.exit(app.exec())
