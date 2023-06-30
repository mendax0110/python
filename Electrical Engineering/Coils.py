import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coils")
        self.setGeometry(100, 100, 800, 600)

        self.current_curve_points = []

        # Create input fields
        self.l_label = QLabel("L(mH):")
        self.l_input = QLineEdit()
        self.r_label = QLabel("R(Ohm):")
        self.r_input = QLineEdit()
        self.u_label = QLabel("U(Volt):")
        self.u_input = QLineEdit()

        # Create buttons
        self.calculate_button = QPushButton("Calculate Current Curve")
        self.calculate_button.clicked.connect(self.calculate_current_curve)

        # Create the plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create the main layout
        layout = QVBoxLayout()
        layout.addWidget(self.l_label)
        layout.addWidget(self.l_input)
        layout.addWidget(self.r_label)
        layout.addWidget(self.r_input)
        layout.addWidget(self.u_label)
        layout.addWidget(self.u_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

    def calculate_tau(self, L, R):
        return L / R

    def calculate_current(self, U, R, t, Tau):
        return U / R * (1 - math.exp(-t / Tau))

    def calculate_current_curve(self):
        try:
            L = float(self.l_input.text())
            R = float(self.r_input.text())
            U = float(self.u_input.text())

            Tau = self.calculate_tau(L, R)

            self.current_curve_points.clear()

            for t in range(0, 101):
                t /= 10
                current = self.calculate_current(U, R, t, Tau)
                self.current_curve_points.append((t, current))

            self.draw_current_curve()

        except ValueError:
            pass

    def draw_current_curve(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_xlabel("t (s)")
        ax.set_ylabel("I (mA)")
        ax.plot([p[0] for p in self.current_curve_points], [p[1] for p in self.current_curve_points], color='red')
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
