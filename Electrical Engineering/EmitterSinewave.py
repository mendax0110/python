import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.qt_compat import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.transistor_type = QtWidgets.QComboBox()
        self.transistor_type.addItems(["NPN", "PNP"])
        self.transistor_type.currentIndexChanged.connect(self.update_graph)
        self.transistor_label = QtWidgets.QLabel("Transistor Type:")
        self.calculate_button = QtWidgets.QPushButton("Calculate Sinewave")
        self.calculate_button.clicked.connect(self.calculate_sinewave)
        self.plot_widget = PlotWidget(self)

        # Set layout
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.transistor_label)
        layout.addWidget(self.transistor_type)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.plot_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize graph
        self.initialize_graph()

    def initialize_graph(self):
        self.plot_widget.ax.set_title("Emitter Sine Wave")
        self.plot_widget.ax.set_xlabel("Time (s)")
        self.plot_widget.ax.set_ylabel("Voltage (V)")
        self.plot_widget.ax.set_ylim([-5, 5])
        self.plot_widget.ax.set_xlim([0, 0.01])
        self.plot_widget.canvas.draw()

    def update_graph(self):
        self.plot_widget.ax.clear()
        self.plot_widget.ax.set_title(f"Emitter Sine Wave ({self.transistor_type.currentText()})")
        self.plot_widget.ax.set_xlabel("Time (s)")
        self.plot_widget.ax.set_ylabel("Voltage (V)")
        self.plot_widget.ax.set_ylim([-5, 5])
        self.plot_widget.ax.set_xlim([0, 0.01])
        self.plot_widget.canvas.draw()

    def calculate_sinewave(self):
        amplitude = 1.0
        frequency = 100.0
        bias = 0.7 if self.transistor_type.currentIndex() == 0 else -0.7

        period = 1.0 / frequency
        dt = period / 100.0  # 100 samples per period
        num_samples = int(np.round(period * 10.0 / dt))  # 10 periods
        t = np.linspace(0.0, period * 10.0, num_samples)

        v = amplitude * np.sin(2.0 * np.pi * frequency * t) + bias

        self.plot_widget.ax.clear()
        self.plot_widget.ax.plot(t, v)
        self.plot_widget.ax.set_title(f"Emitter Sine Wave ({self.transistor_type.currentText()})")
        self.plot_widget.ax.set_xlabel("Time (s)")
        self.plot_widget.ax.set_ylabel("Voltage (V)")
        self.plot_widget.ax.set_ylim([-5, 5])
        self.plot_widget.ax.set_xlim([0, t[-1]])
        self.plot_widget.canvas.draw()


class PlotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create Figure and Axes objects
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

        # Create canvas and set parent
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)

        # Create toolbar
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        # Set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
