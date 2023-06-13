import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from schemdraw import Drawing
from schemdraw.elements import Resistor, Capacitor, Inductor, Ground, SourceV


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Schaltungsgenerator")
        self.setGeometry(100, 100, 800, 600)

        # Schaltungsparameter-Eingabe
        self.resistor_value_input = QLineEdit()
        self.capacitor_value_input = QLineEdit()
        self.inductor_value_input = QLineEdit()

        # Schaltungsart-Auswahl
        self.series_radio_button = QRadioButton("Seriell")
        self.parallel_radio_button = QRadioButton("Parallel")
        self.parallel_radio_button.setChecked(True)  # Standardmäßig parallel

        # Schaltung generieren Button
        self.generate_button = QPushButton("Schaltung generieren")
        self.generate_button.clicked.connect(self.generate_circuit)

        # Matplotlib-FigureCanvas für Schaltungsbild
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Layout für das Hauptfenster
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Widerstand (in Ohm):"))
        layout.addWidget(self.resistor_value_input)
        layout.addWidget(QLabel("Kondensator (in Farad):"))
        layout.addWidget(self.capacitor_value_input)
        layout.addWidget(QLabel("Spule (in Henry):"))
        layout.addWidget(self.inductor_value_input)
        layout.addWidget(QLabel("Schaltungsart:"))
        layout.addWidget(self.series_radio_button)
        layout.addWidget(self.parallel_radio_button)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def generate_circuit(self):
        # Schaltungswerte aus den Eingabefeldern abrufen
        try:
            resistor_value = float(self.resistor_value_input.text())
            capacitor_value = float(self.capacitor_value_input.text())
            inductor_value = float(self.inductor_value_input.text())
        except ValueError:
            QMessageBox.critical(self, "Fehler", "Ungültige Eingabewerte")
            return

        # Schematische Zeichnung der Schaltung erstellen
        d = Drawing()

        if self.parallel_radio_button.isChecked():
            # Parallele Schaltung
            d.add(Resistor(label=f"{resistor_value} Ohm"))
            d.add(Capacitor(label=f"{capacitor_value} F"))
            d.add(Inductor(label=f"{inductor_value} H"))
        else:
            # Serielle Schaltung
            d.add(Resistor(label=f"{resistor_value} Ohm"))
            d.add(Capacitor(label=f"{capacitor_value} F"))
            d.add(Inductor(label=f"{inductor_value} H"))
            d.add(Resistor(label=f"{resistor_value} Ohm"))
            d.add(Capacitor(label=f"{capacitor_value} F"))
            d.add(Inductor(label=f"{inductor_value} H"))

        d.add(Ground())
        d.add(SourceV())

        # Schaltungsbild anzeigen
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.axis("off")
        d.draw(ax)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())










