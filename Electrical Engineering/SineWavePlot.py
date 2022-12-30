import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QGraphicsView, \
    QGraphicsScene
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to display the sine value
        self.sine_label = QLabel("Sine: 0")

        # Create a line edit for the user to enter a number
        self.input_field = QLineEdit()

        # Create a button to calculate the sine value
        self.calculate_button = QPushButton("Calculate Sine")
        self.calculate_button.clicked.connect(self.calculate_sine)

        # Set up the layout of the main window
        layout = QVBoxLayout()
        layout.addWidget(self.sine_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.calculate_button)

        # Create a graphics view widget to display the graph
        self.graphics_view = QGraphicsView(self)
        layout.addWidget(self.graphics_view)

        self.setLayout(layout)

        # Set up the matplotlib figure and canvas
        self.figure, self.canvas = plt.subplots()

        # Convert the AxesSubplot object to a QWidget object
        canvas_widget = FigureCanvasQTAgg(self.figure)

        # Add the QWidget object to the QGraphicsScene
        graphics_scene = QGraphicsScene(self.graphics_view)
        graphics_scene.addWidget(canvas_widget)
        self.graphics_view.setScene(graphics_scene)

    def calculate_sine(self):
        # Get the number entered in the input field
        try:
            number = float(self.input_field.text())
        except ValueError:
            # Display an error message if the input is not a valid number
            self.sine_label.setText("Error: Invalid input")
            return

        # Calculate the sine value and update the label
        sine = math.sin(number)
        self.sine_label.setText(f"Sine: {sine:.2f}")

        # Clear the previous
        self.canvas.clear()

        # Plot the sine function
        x = [i / 100 for i in range(0, 628)]
        y = [math.sin(i) for i in x]
        self.canvas.plot(x, y)

        # Plot the tangent line
        x = [number, number]
        y = [0, math.sin(number)]
        self.canvas.plot(x, y)

        # Draw the graph
        self.canvas.figure.canvas.draw()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
