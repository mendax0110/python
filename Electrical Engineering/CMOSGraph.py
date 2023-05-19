import sys

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('QT5Agg')

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox

#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget for the main window
        self.widget = QWidget(self)

        # Create a grid layout for the widget
        self.grid_layout = QGridLayout(self.widget)

        # Add labels and text boxes for input values
        self.vdd_label = QLabel("VDD (V):")
        self.grid_layout.addWidget(self.vdd_label, 0, 0)
        self.vdd_text = QLineEdit(self)
        self.grid_layout.addWidget(self.vdd_text, 0, 1)

        self.vgs_label = QLabel("VGS (V):")
        self.grid_layout.addWidget(self.vgs_label, 1, 0)
        self.vgs_text = QLineEdit(self)
        self.grid_layout.addWidget(self.vgs_text, 1, 1)

        # Add a button to plot the graph
        self.plot_button = QPushButton("Plot Graph", self)
        self.plot_button.clicked.connect(self.plot_graph)
        self.grid_layout.addWidget(self.plot_button, 2, 1)

        # Set the layout of the widget
        self.setCentralWidget(self.widget)

    # create a function to plot the graph
    def plot_graph(self):
        try:
            # Get input values from text boxes
            vdd = float(self.vdd_text.text())
            vgs = np.linspace(0, float(self.vgs_text.text()), 1000)

            # Calculate output current
            ids = np.where(vgs < 0, 0, np.where(vgs < (vdd - 0.5), 0.5 * vgs ** 2, (vdd - 0.25) * (vdd - vgs)))

            # Create a plot of the output characteristics
            fig, ax = plt.subplots()
            ax.plot(vgs, ids)
            ax.set_xlabel("VGS (V)")
            ax.set_ylabel("ID (A)")
            ax.set_title("Output Characteristics of CMOS Transistor")
            plt.show()
        except ValueError as e:
            error_message = f"Invalid input: {str(e)}"
            QMessageBox.critical(self, "Error", error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
