import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0
import matplotlib.animation as animation
from schemdraw import Drawing
from schemdraw.elements import Inductor, Wire


class AirCoilCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Air Coil Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.radius_label = QLabel("Radius (m):", self)
        self.radius_label.setGeometry(50, 50, 100, 20)
        self.radius_textbox = QLineEdit(self)
        self.radius_textbox.setGeometry(150, 50, 100, 20)

        self.height_label = QLabel("Height (m):", self)
        self.height_label.setGeometry(50, 80, 100, 20)
        self.height_textbox = QLineEdit(self)
        self.height_textbox.setGeometry(150, 80, 100, 20)

        self.turns_label = QLabel("Turns:", self)
        self.turns_label.setGeometry(50, 110, 100, 20)
        self.turns_textbox = QLineEdit(self)
        self.turns_textbox.setGeometry(150, 110, 100, 20)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setGeometry(150, 150, 100, 30)
        self.calculate_button.clicked.connect(self.calculate_clicked)

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(50, 200, 300, 30)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Arial", 12))

        self.animation_label = QLabel(self)
        self.animation_label.setGeometry(50, 240, 300, 300)

    def calculate_clicked(self):
        try:
            radius = float(self.radius_textbox.text())
            height = float(self.height_textbox.text())
            turns = int(self.turns_textbox.text())

            inductance = self.calculate_inductance(radius, height, turns)
            self.result_label.setText(f"Inductance: {inductance} H")

            self.plot_circuit(radius, height, turns)
            self.animate_field_lines(radius, height, turns)
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Please enter numeric values.")

    def calculate_inductance(self, radius, height, turns):
        inner_radius = radius
        outer_radius = radius + height
        average_radius = (inner_radius + outer_radius) / 2.0

        inductance = mu_0 * turns ** 2 * average_radius ** 2 / (
                    (2 * average_radius) + (height * (np.log(outer_radius / inner_radius) - 1)))
        return inductance

    def plot_circuit(self, radius, height, turns):
        d = Drawing(unit=2, fontsize=12)
        with d:
            outer_circuit = d.add(Wire().left().label('Outer\nCircuit', loc='lft'))
            inductor = d.add(Inductor().right().label('L', loc='top'))
            inner_circuit = d.add(Wire().right().label('Inner\nCircuit', loc='rgt'))
            d.add(outer_circuit)
            d.add(inductor)
            d.add(inner_circuit)

        d.draw()
        d.save("circuit.png")

    def animate_field_lines(self, radius, height, turns):
        fig, ax = plt.subplots()
        ax.set_xlim(-radius - height, radius + height)
        ax.set_ylim(-radius - height, radius + height)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Field Lines')

        lines = self.calculate_field_lines(radius, height, turns)

        def animate(i):
            ax.clear()
            ax.set_xlim(-radius - height, radius + height)
            ax.set_ylim(-radius - height, radius + height)
            ax.set_aspect('equal', adjustable='box')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('Field Lines')

            for line in lines:
                ax.plot(line[:, 0], line[:, 1], 'b')

        anim = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=False)
        anim.save("field_lines.gif", writer='imagemagick')

        self.animation_label.setPixmap("field_lines.gif")

    def calculate_field_lines(self, radius, height, turns):
        grid_size = 100
        x = np.linspace(-radius - height, radius + height, grid_size)
        y = np.linspace(-radius - height, radius + height, grid_size)
        X, Y = np.meshgrid(x, y)

        field_lines = []

        for t in range(turns):
            line_x = []
            line_y = []
            for i in range(grid_size):
                for j in range(grid_size):
                    point_x = X[i, j]
                    point_y = Y[i, j]
                    r = np.sqrt(point_x ** 2 + point_y ** 2)
                    if r >= radius and r <= radius + height:
                        line_x.append(point_x)
                        line_y.append(point_y)

            field_lines.append(np.column_stack((line_x, line_y)))

        return field_lines


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AirCoilCalculator()
    window.show()
    sys.exit(app.exec_())
