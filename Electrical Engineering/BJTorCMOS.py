import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class TransistorCharacteristics(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window dimensions and title
        self.setWindowTitle('Transistor Characteristics')
        self.setGeometry(200, 200, 800, 600)

        # Create the layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        vlayout = QVBoxLayout(main_widget)

        # Create the plot area
        self.figure = Figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.figure)
        vlayout.addWidget(self.canvas)

        # Create the input fields
        input_layout = QHBoxLayout()
        vlayout.addLayout(input_layout)

        ic_label = QLabel('Ic saturation (A):')
        self.ic_input = QLineEdit()
        self.ic_input.setFixedWidth(100)
        input_layout.addWidget(ic_label)
        input_layout.addWidget(self.ic_input)

        voltage_label = QLabel('Vce or Vds (V):')
        self.voltage_input = QLineEdit()
        self.voltage_input.setFixedWidth(100)
        input_layout.addWidget(voltage_label)
        input_layout.addWidget(self.voltage_input)

        current_label = QLabel('Ic or Id (A):')
        self.current_input = QLineEdit()
        self.current_input.setFixedWidth(100)
        input_layout.addWidget(current_label)
        input_layout.addWidget(self.current_input)

        # Create the transistor type buttons
        bjt_button = QPushButton('BJT')
        bjt_button.clicked.connect(self.plot_bjt)
        mosfet_button = QPushButton('MOSFET')
        mosfet_button.clicked.connect(self.plot_mosfet)

        input_layout.addWidget(bjt_button)
        input_layout.addWidget(mosfet_button)

    def plot_bjt(self):
        ic = float(self.ic_input.text())
        v = float(self.voltage_input.text())
        i = float(self.current_input.text())

        # Define transistor model parameters
        beta = 100
        vt = 0.026
        re = vt / ic
        rc = (v - i * re) / i

        # Define x and y values for the plot
        x = [0, v, v]
        y = [0, i, ic]

        # Create the plot
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, label='BJT Characteristics')

        # Add axis labels and legend
        ax.set_xlabel('Vce (V)')
        ax.set_ylabel('Ic (A)')
        ax.legend()

        # Draw the plot
        self.canvas.draw()

    def plot_mosfet(self):
        ic = float(self.ic_input.text())
        v = float(self.voltage_input.text())
        i = float(self.current_input.text())

        # Define transistor model parameters
        kn = 0.3
        vp = -2
        lamb = 0.1
        rd = 1 / (lamb * i)
        rs = vp / (2 * i * kn)
        vgs = v - i * rs
        gm = 2 * i / abs(vgs - vp)

        # Define x and y values for the plot
        x = [0, v, v]
        y = [0, i, ic]

        # Create
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, label='MOSFET Characteristics')

        # Add axis labels and legend
        ax.set_xlabel('Vds (V)')
        ax.set_ylabel('Id (A)')
        ax.legend()

        # Draw the plot
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransistorCharacteristics()
    window.show()
    sys.exit(app.exec_())
