import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMainWindow
from sympy import integrate, sympify, Symbol, SympifyError
from sympy.plotting import plot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Integral Calculator")

        # Create UI elements
        self.input_textbox = QLineEdit()
        self.output_textbox = QLineEdit()
        self.output_textbox.setReadOnly(True)
        self.integral_type_combobox = QComboBox()
        self.integral_type_combobox.addItems(["Definite Integral", "Indefinite Integral"])
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_integral)
        self.plot_button = QPushButton("Plot Curve")
        self.plot_button.clicked.connect(self.plot_curve)
        self.setGeometry(100, 100, 400, 250)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Input"))
        layout.addWidget(self.input_textbox)
        layout.addWidget(QLabel("Output"))
        layout.addWidget(self.output_textbox)
        layout.addWidget(QLabel("Integral Type"))
        layout.addWidget(self.integral_type_combobox)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.plot_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calculate_integral(self):
        # Get the input expression from the textbox
        input_expression = self.input_textbox.text()

        # Select definite or indefinite integration
        integral_type = self.integral_type_combobox.currentText()

        try:
            x = Symbol('x')
            expr = sympify(input_expression)
            result = ""

            if integral_type == "Definite Integral":
                # Perform definite integration
                a = Symbol('a')
                b = Symbol('b')
                integral_value = integrate(expr, (x, a, b))
                if integral_value.is_polynomial():
                    integral_value = integral_value.as_poly()
                    result = str(integral_value)
                else:
                    result = str(integral_value)

            elif integral_type == "Indefinite Integral":
                # Perform indefinite integration
                integral_expr = integrate(expr, x)
                result = str(integral_expr) + " + C"

            # Display the result in the output textbox
            self.output_textbox.setText(result)

        except SympifyError:
            # Error handling for invalid mathematical expressions
            self.output_textbox.setText("Invalid mathematical expression.")

        except Exception as e:
            # General error handling
            self.output_textbox.setText("Error: " + str(e))

    def plot_curve(self):
        # Get the input expression from the textbox
        input_expression = self.input_textbox.text()

        try:
            x = Symbol('x')
            expr = sympify(input_expression)

            # Plot the characteristic curve of the integral
            p = plot(expr, show=False)
            p.title = 'Characteristic Curve'
            p.xlabel = 'x'
            p.ylabel = 'y'
            p.show()

        except SympifyError:
            # Error handling for invalid mathematical expressions
            self.output_textbox.setText("Invalid mathematical expression.")

        except Exception as e:
            # General error handling
            self.output_textbox.setText("Error: " + str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
