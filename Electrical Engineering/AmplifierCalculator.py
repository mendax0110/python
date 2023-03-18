import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class AmplifierCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Amplifier Calculator")
        self.setGeometry(100, 100, 800, 450)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QHBoxLayout()
        central_widget.setLayout(central_layout)

        # Create input section
        input_widget = QWidget()
        input_layout = QVBoxLayout()
        input_widget.setLayout(input_layout)

        vin_label = QLabel("Vin:")
        self.vin_edit = QLineEdit()
        self.vin_edit.setFixedWidth(100)
        self.vin_edit.setAlignment(Qt.AlignRight)

        r1_label = QLabel("R1:")
        self.r1_edit = QLineEdit()
        self.r1_edit.setFixedWidth(100)
        self.r1_edit.setAlignment(Qt.AlignRight)

        r2_label = QLabel("R2:")
        self.r2_edit = QLineEdit()
        self.r2_edit.setFixedWidth(100)
        self.r2_edit.setAlignment(Qt.AlignRight)

        input_layout.addWidget(vin_label)
        input_layout.addWidget(self.vin_edit)
        input_layout.addWidget(r1_label)
        input_layout.addWidget(self.r1_edit)
        input_layout.addWidget(r2_label)
        input_layout.addWidget(self.r2_edit)
        input_layout.addStretch()

        # Create calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFixedWidth(100)
        self.calculate_button.clicked.connect(self.calculate_values)

        # Create amplifier values section
        values_widget = QWidget()
        values_layout = QVBoxLayout()
        values_widget.setLayout(values_layout)

        self.a_label = QLabel()
        self.b_label = QLabel()
        self.c_label = QLabel()

        values_layout.addWidget(self.a_label)
        values_layout.addWidget(self.b_label)
        values_layout.addWidget(self.c_label)
        values_layout.addStretch()

        # Add input and amplifier value sections to central layout
        central_layout.addWidget(input_widget)
        central_layout.addWidget(self.calculate_button)
        central_layout.addWidget(values_widget)

        # Create graph section
        self.graph = plt.figure(figsize=(6, 4), dpi=100)
        self.graph_canvas = FigureCanvas(self.graph)
        graph_widget = QWidget()
        graph_layout = QVBoxLayout()
        graph_widget.setLayout(graph_layout)
        graph_layout.addWidget(self.graph_canvas)

        # Add graph section to central layout
        central_layout.addWidget(graph_widget)

    def calculate_values(self):
        # Get input values
        try:
            vin = float(self.vin_edit.text())
            r1 = float(self.r1_edit.text())
            r2 = float(self.r2_edit.text())
        except ValueError:
            return

        # Calculate amplifier values
        a = r2 / (r1 + r2)
        b = 1 / (1 - a)
        c = a / (1 - a)

        # Update labels
        self.a_label.setText("A: {:.2f}".format(a))
        self.b_label.setText("B: {:.2f}".format(b))
        self.c_label.setText("C: {:.2f}".format(c))

        # Create and plot sine wave on graph
        x = np.linspace(0, 2 * np.pi, 100)
        y = vin * np.sin(x)
        ax = self.graph.add_subplot(111)
        ax.clear()
        ax.plot(x, y)

        # Update graph
        self.graph_canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AmplifierCalculator()
    window.show()
    sys.exit(app.exec_())