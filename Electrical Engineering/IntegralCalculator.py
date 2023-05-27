import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from sympy import integrate, symbols, sympify, Symbol
from sympy.core.sympify import SympifyError


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Integral Calculator")

        # Erstelle die UI-Elemente
        self.input_textbox = QLineEdit()
        self.output_textbox = QLineEdit()
        self.output_textbox.setReadOnly(True)
        self.integral_type_combobox = QComboBox()
        self.integral_type_combobox.addItems(["Bestimmtes Integral", "Unbestimmtes Integral"])
        self.calculate_button = QPushButton("Berechnen")
        self.calculate_button.clicked.connect(self.calculate_integral)

        # Erstelle das Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Eingabe"))
        layout.addWidget(self.input_textbox)
        layout.addWidget(QLabel("Ausgabe"))
        layout.addWidget(self.output_textbox)
        layout.addWidget(QLabel("Integraltyp"))
        layout.addWidget(self.integral_type_combobox)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate_integral(self):
        # Hole die Eingabe aus der TextBox
        input_expression = self.input_textbox.text()

        # Bestimmte oder unbestimmte Integration auswählen
        integral_type = self.integral_type_combobox.currentText()

        try:
            x = Symbol('x')
            expr = sympify(input_expression)
            result = ""

            if integral_type == "Bestimmtes Integral":
                # Führe bestimmte Integration durch
                a = Symbol('a')
                b = Symbol('b')
                integral_value = integrate(expr, (x, a, b))
                if integral_value.is_polynomial():
                    integral_value = integral_value.as_poly()
                    result = str(integral_value)
                else:
                    result = str(integral_value)

            elif integral_type == "Unbestimmtes Integral":
                # Führe unbestimmte Integration durch
                integral_expr = integrate(expr, x)
                result = str(integral_expr) + " + C"

            # Zeige das Ergebnis in der Ausgabe-TextBox an
            self.output_textbox.setText(result)

        except SympifyError:
            # Fehlerbehandlung für ungültige mathematische Ausdrücke
            self.output_textbox.setText("Ungültiger mathematischer Ausdruck.")

        except Exception as e:
            # Allgemeine Fehlerbehandlung
            self.output_textbox.setText("Fehler: " + str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


