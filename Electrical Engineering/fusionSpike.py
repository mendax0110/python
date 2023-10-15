import sys
import time
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class FusionSimulator:
    def __init__(self):
        self.progress = [0, 0, 0, 0, 0]
        self.neutron_flux = 0

    def simulate_step(self, step):
        self.progress[step] = 100

    def get_progress(self):
        return self.progress

    def set_neutron_flux(self, value):
        self.neutron_flux = value

    def get_neutron_flux(self):
        return self.neutron_flux


class FusionReactorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fusion Reactor Simulator")
        self.setGeometry(100, 100, 600, 400)

        self.simulator = FusionSimulator()

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Simulation")
        self.start_button.clicked.connect(self.run_simulation)
        layout.addWidget(self.start_button)

        self.neutron_flux_label = QLabel("Neutron Flux: 0")
        layout.addWidget(self.neutron_flux_label)

        self.neutron_flux_slider = QSlider()
        self.neutron_flux_slider.setRange(0, 100)
        self.neutron_flux_slider.valueChanged.connect(self.update_neutron_flux_label)
        layout.addWidget(self.neutron_flux_slider)

        self.progress_label = QLabel("Progress:")
        layout.addWidget(self.progress_label)

        self.progress_bars = []
        for i in range(5):
            progress_bar = QLabel(f"Step {i + 1}: 0%")
            self.progress_bars.append(progress_bar)
            layout.addWidget(progress_bar)

        self.canvas = MplCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def run_simulation(self):
        self.reset_progress()
        self.simulator.set_neutron_flux(self.neutron_flux_slider.value())
        self.simulate_fusion_reactor_steps()

    def simulate_fusion_reactor_steps(self):
        for step in range(5):
            self.simulator.simulate_step(step)
            self.update_progress_bars()
            time.sleep(1)  # Simulate step duration
            self.canvas.update_figure(self.simulator.get_progress())

    def reset_progress(self):
        self.simulator = FusionSimulator()
        for bar in self.progress_bars:
            bar.setText("Step: 0%")
        self.neutron_flux_slider.setValue(0)
        self.update_neutron_flux_label()
        self.canvas.update_figure([0, 0, 0, 0, 0])

    def update_neutron_flux_label(self):
        value = self.neutron_flux_slider.value()
        self.neutron_flux_label.setText(f"Neutron Flux: {value}")

    def update_progress_bars(self):
        progress = self.simulator.get_progress()
        for i, bar in enumerate(self.progress_bars):
            bar.setText(f"Step {i + 1}: {progress[i]}%")


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.update_figure([0, 0, 0, 0, 0])

    def update_figure(self, progress):
        steps = ["High Vacuum Pump", "Test High Vacuum Pump", "Build Inner Grid", "Assemble Deuterium System",
                 "Setup Neutron Detection"]

        self.ax.clear()
        self.ax.barh(steps, progress, color='skyblue')
        self.ax.set_xlabel('Completion Percentage (%)')
        self.ax.set_title('Fusion Reactor Simulation Progress')
        self.ax.set_xlim(0, 100)
        self.ax.grid(axis='x', linestyle='--', alpha=0.6)
        self.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FusionReactorGUI()
    window.show()
    sys.exit(app.exec())
