import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("MOSFET Curves")
        self.setGeometry(100, 100, 600, 400)

        # Create sliders
        self.vgs_slider = QSlider(Qt.Horizontal, self)
        self.vgs_slider.setMinimum(0)
        self.vgs_slider.setMaximum(10)
        self.vgs_slider.setValue(5)
        self.vgs_slider.setTickInterval(1)
        self.vgs_slider.setTickPosition(QSlider.TicksBelow)
        self.vgs_slider.valueChanged.connect(self.update_graph)

        self.vds_slider = QSlider(Qt.Horizontal, self)
        self.vds_slider.setMinimum(0)
        self.vds_slider.setMaximum(10)
        self.vds_slider.setValue(5)
        self.vds_slider.setTickInterval(1)
        self.vds_slider.setTickPosition(QSlider.TicksBelow)
        self.vds_slider.valueChanged.connect(self.update_graph)

        # Create labels for sliders
        self.vgs_label = QLabel("Vgs: 5.00 V", self)
        self.vds_label = QLabel("Vds: 5.00 V", self)

        # Create plot
        self.fig, self.ax = plt.subplots()
        self.line1, = self.ax.plot([], [], 'b', label='Id')
        self.line2, = self.ax.plot([], [], 'r', label='Vds')
        self.ax.legend(loc='upper left')
        self.ax.set_xlabel('Vds (V)')
        self.ax.set_ylabel('Id (mA)')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 5)
        self.ax.grid(True)

        # Create canvas to display plot
        self.canvas = FigureCanvas(self.fig)

        # Add widgets to layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.vgs_slider)
        vbox.addWidget(self.vgs_label)
        vbox.addWidget(self.vds_slider)
        vbox.addWidget(self.vds_label)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

        # Update plot with initial values
        self.update_graph()

    def update_graph(self):
        vgs = self.vgs_slider.value() / 10
        vds_max = self.vds_slider.value() / 10

        # Calculate Vds and Id values for given Vgs and Vds
        vds, id = calculate_id(vgs, vds_max)

        # Update plot with new data
        self.line1.set_data(vds, id)
        self.line2.set_data(vds, vds)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

        # Update labels with slider values
        self.vgs_label.setText(f"Vgs: {vgs:.2f} V")
        self.vds_label.setText(f"Vds: {vds_max:.2f} V")


def calculate(vgs, vds):
    vth = 2
    k = 0.5
    lam = 0.1
    id = 0

    if vgs < vth:
        id = 0
    elif vds < vgs - vth:
        id = k * (vgs - vth - vds / 2) * vds
    else:
        id = k / 2 * (vgs - vth) ** 2 * (1 + lam * vds)

    return id


def calculate_id(vgs, vds):
    vth = 2
    k = 0.5
    lam = 0.1
    id_vals = []
    vds_vals = []

    for vd in range(0, 1001):
        vd = vd / 100
        if vds < vd:
            break

        if vgs <= vth:
            id = 0
        elif vds < vgs - vth:
            id = k * (vgs - vth - vds / 2) * vds
        else:
            id = k / 2 * (vgs - vth) ** 2 * (1 + lam * vds)

        id_vals.append(id * 1000)
        vds_vals.append(vd)

    return vds_vals, id_vals


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
