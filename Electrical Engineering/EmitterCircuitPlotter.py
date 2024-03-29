import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emitter Circuit Plotter")

        # Set up GUI widgets
        self.amplitude_label = QLabel("Amplitude (V):")
        self.amplitude_textbox = QLineEdit()
        self.frequency_label = QLabel("Frequency (Hz):")
        self.frequency_textbox = QLineEdit()
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.on_plot_button_clicked)

        # Set up plot widget
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_widget = QtWidgets.QWidget()
        self.plot_layout = QtWidgets.QVBoxLayout(self.plot_widget)
        self.plot_layout.addWidget(self.canvas)

        # Set up layout
        self.main_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.amplitude_label)
        self.input_layout.addWidget(self.amplitude_textbox)
        self.input_layout.addWidget(self.frequency_label)
        self.input_layout.addWidget(self.frequency_textbox)
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.plot_button)
        self.main_layout.addWidget(self.plot_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def on_plot_button_clicked(self):
        # Parse input values from text boxes
        try:
            amplitude = float(self.amplitude_textbox.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Invalid amplitude value")
            return

        try:
            frequency = float(self.frequency_textbox.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Invalid frequency value")
            return

        # Set up circuit components
        Rb = 10e3  # Base resistor
        Rc = 1e3  # Collector resistor
        Re = 470  # Emitter resistor
        Vcc = 5  # Supply voltage
        Vbe = 0.7  # Base-emitter voltage drop
        hfe = 100  # Transistor current gain

        # Create data for plot
        x = np.linspace(0, 1, 1000)
        v_in = amplitude * np.sin(2 * np.pi * frequency * x)
        v_out = np.zeros_like(x)

        # Calculate output waveform
        for i in range(len(x)):
            # Calculate transistor bias and DC operating point
            Ic = (Vcc - Vbe) / (Rb + (hfe + 1) * Re)
            Vce = Vcc - Ic * Rc
            Ve = Vce - Vbe

            # Calculate AC voltage gain and output waveform
            gm = Ic / Ve
            v_out[i] = -gm * v_in[i] * Re / (1 + gm * (Rc + Re))

        # Clear old plot and create new one
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, v_out)

        # Update plot widget
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
