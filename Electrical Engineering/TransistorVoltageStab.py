import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Create a class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.r1_label = QLabel('R1 (ohms):')
        self.r1_edit = QLineEdit()
        self.vcc_label = QLabel('Vcc (volts):')
        self.vcc_edit = QLineEdit()
        self.plot_canvas = FigureCanvas(Figure())
        self.plot_axes = self.plot_canvas.figure.subplots()
        self.plot_axes.set_title('Stabilization Curve')
        self.plot_axes.set_xlabel('IC (mA)')
        self.plot_axes.set_ylabel('VCE (volts)')

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.r1_label)
        layout.addWidget(self.r1_edit)
        layout.addWidget(self.vcc_label)
        layout.addWidget(self.vcc_edit)
        layout.addWidget(self.plot_canvas)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the signal/slots
        self.r1_edit.textChanged.connect(self.update_stabilization_curve)
        self.vcc_edit.textChanged.connect(self.update_stabilization_curve)

    # Set the window properties
    def update_stabilization_curve(self):
        # Get the values of R1 and Vcc from the text boxes
        try:
            R1 = float(self.r1_edit.text())
            Vcc = float(self.vcc_edit.text())
        except ValueError:
            return

        # Calculate the stabilization curve
        stabilization_data = []
        vbe = 0.7  # Base-emitter voltage of the transistor
        beta = 100  # DC current gain of the transistor

        for vce in range(0, int(Vcc * 10) + 1, 1):
            vce /= 10.0
            ic = (Vcc - vce) / R1
            vce_saturation = Vcc - ic * R1
            vce_clamped = max(vce, vce_saturation)
            ic_saturation = (Vcc - vbe) / (beta * R1)
            ic_clamped = max(ic, ic_saturation)
            stabilization_data.append((ic_clamped * 1000, vce_clamped))

        # Update the plot
        self.plot_axes.clear()
        self.plot_axes.plot([x[0] for x in stabilization_data], [x[1] for x in stabilization_data])
        self.plot_canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
