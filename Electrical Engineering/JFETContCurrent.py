import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
import schemdraw as schem
import schemdraw.elements as elm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Electronic Circuit Visualization")
        self.setGeometry(100, 100, 800, 600)

        # Create the circuit diagram
        self.circuit_widget = QWidget(self)
        self.circuit_layout = QVBoxLayout()
        self.circuit_widget.setLayout(self.circuit_layout)
        self.draw_circuit()
        self.setCentralWidget(self.circuit_widget)

        # Create the graph
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.graph_widget = QWidget(self)
        self.graph_layout = QVBoxLayout()
        self.graph_layout.addWidget(self.canvas)
        self.graph_widget.setLayout(self.graph_layout)
        self.graph_widget.setMaximumHeight(200)
        self.circuit_layout.addWidget(self.graph_widget)

        # Create the layout for input elements and buttons
        self.input_layout = QVBoxLayout()

        # Create the input labels and text boxes
        self.UgsOffLabel = QLabel("UGSoff:")
        self.UgsOffTextBox = QLineEdit()
        self.input_layout.addWidget(self.UgsOffLabel)
        self.input_layout.addWidget(self.UgsOffTextBox)

        self.IdssLabel = QLabel("IDSS:")
        self.IdssTextBox = QLineEdit()
        self.input_layout.addWidget(self.IdssLabel)
        self.input_layout.addWidget(self.IdssTextBox)

        self.IlastLabel = QLabel("ILast:")
        self.IlastTextBox = QLineEdit()
        self.input_layout.addWidget(self.IlastLabel)
        self.input_layout.addWidget(self.IlastTextBox)

        self.RlastLabel = QLabel("RLast:")
        self.RlastTextBox = QLineEdit()
        self.input_layout.addWidget(self.RlastLabel)
        self.input_layout.addWidget(self.RlastTextBox)

        self.UsourceLabel = QLabel("USource:")
        self.UsourceTextBox = QLineEdit()
        self.input_layout.addWidget(self.UsourceLabel)
        self.input_layout.addWidget(self.UsourceTextBox)

        self.calculateButton = QPushButton("Calculate")
        self.drawButton = QPushButton("Draw")
        self.input_layout.addWidget(self.calculateButton)
        self.input_layout.addWidget(self.drawButton)

        # Create the main layout and add input elements and circuit diagram
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.circuit_widget)

        # Set the main layout for the main window
        self.main_widget = QWidget(self)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Connect the button signals to their respective slots
        self.calculateButton.clicked.connect(self.calculate_and_plot)
        self.drawButton.clicked.connect(self.draw_circuit)

    def draw_circuit(self):
        # Use SchemDraw to draw the circuit diagram
        d = schem.Drawing()
        d.add(elm.Resistor().label("Rs"))
        d.add(elm.SourceV().up().label("Usource"))
        d.add(elm.Resistor().down().label("RL"))
        d.add(elm.Ground())
        d.draw()

        # Display the circuit diagram in a QLabel or other suitable widget
        # For simplicity, we'll use a FigureCanvas from Matplotlib
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')
        self.ax.imshow(d.image)
        self.canvas.draw()

    def calculate_and_plot(self):
        try:
            UGSoff = float(self.UgsOffTextBox.text())
            IDSS = float(self.IdssTextBox.text())
            IL = float(self.IlastTextBox.text())
            Rs = list(map(float, self.RlastTextBox.text().split(',')))
            Usource = float(self.UsourceTextBox.text())

            # Calculate the characteristic curve
            characteristic_curve = self.calculate_characteristic_curve(Rs, Usource, UGSoff, IDSS, IL)

            # Plot the characteristic curve
            self.figure.clear()
            self.ax = self.figure.add_subplot(111)
            self.ax.plot(Rs, characteristic_curve, marker='o')
            self.ax.set_xlabel('Rs')
            self.ax.set_ylabel('IL')
            self.canvas.draw()
        except Exception as e:
            print("Error:", str(e))

    def calculate_characteristic_curve(self, Rs, Usource, UGSoff, IDSS, IL):
        if IL <= 0:
            raise ValueError("IL must be greater than 0.")

        characteristic_curve = []

        for R in Rs:
            UGS = UGSoff * (1 - math.sqrt(IL / IDSS))
            characteristic_curve.append(IL)

        return characteristic_curve


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
