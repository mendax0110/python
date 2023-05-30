import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from sympy import symbols, Function, Eq, diff, dsolve, parse_expr


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Differential Equations Solver")

        # Create a main widget and set it as central
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a layout for the main widget
        self.layout = QVBoxLayout(self.main_widget)

        # Create equation input label and line edit
        self.equation_label = QLabel("Enter the differential equation:")
        self.equation_input = QLineEdit()

        # Create a result text edit
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # Create a solve button
        self.solve_button = QPushButton("Solve")
        self.solve_button.clicked.connect(self.solve_equation)

        # Add the widgets to the layout
        self.layout.addWidget(self.equation_label)
        self.layout.addWidget(self.equation_input)
        self.layout.addWidget(self.solve_button)
        self.layout.addWidget(self.result_text)

    def solve_equation(self):
        # Clear previous results
        self.result_text.clear()

        # Get the input equation
        equation = self.equation_input.text()

        try:
            # Parse the equation
            x = symbols('x')
            y = symbols('y', cls=Function)
            expr = Eq(y(x).diff(x), parse_expr(equation))

            # Solve the equation
            solution = dsolve(expr)

            # Display the result
            self.result_text.setFont(QFont("Courier New", 10))
            self.result_text.append("Solution:")
            self.result_text.append(str(solution))

        except Exception as e:
            # Display the error message
            self.result_text.append("Error: " + str(e))


if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
