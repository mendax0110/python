import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from scipy.integrate import odeint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create input widgets
        self.equation_label = QLabel('Equation:')
        self.equation_textbox = QLineEdit()
        self.x0_label = QLabel('Initial x:')
        self.x0_textbox = QLineEdit()
        self.y0_label = QLabel('Initial y:')
        self.y0_textbox = QLineEdit()
        self.xf_label = QLabel('Final x:')
        self.xf_textbox = QLineEdit()
        self.steps_label = QLabel('Steps:')
        self.steps_textbox = QLineEdit()

        # Create button to solve and plot equation
        self.plot_button = QPushButton('Plot')
        self.plot_button.clicked.connect(self.plot_equation)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.equation_label)
        layout.addWidget(self.equation_textbox)
        layout.addWidget(self.x0_label)
        layout.addWidget(self.x0_textbox)
        layout.addWidget(self.y0_label)
        layout.addWidget(self.y0_textbox)
        layout.addWidget(self.xf_label)
        layout.addWidget(self.xf_textbox)
        layout.addWidget(self.steps_label)
        layout.addWidget(self.steps_textbox)
        layout.addWidget(self.plot_button)

        # Create Matplotlib canvas
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)
        self.show()

    def plot_equation(self):
        # Extract user input
        equation = self.equation_textbox.text()
        x0 = float(self.x0_textbox.text())
        y0 = float(self.y0_textbox.text())
        xf = float(self.xf_textbox.text())
        steps = int(self.steps_textbox.text())

        # Define the equation as a function of y and x
        def eqn(y, x):
            return eval(equation)

        # Solve the equation using odeint
        xs = np.linspace(x0, xf, steps)
        ys = odeint(eqn, y0, xs)[:, 0]

        # Clear the previous plot
        self.figure.clear()

        # Plot the solution
        ax = self.figure.add_subplot(111)
        ax.plot(xs, ys)
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        # Update the canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
