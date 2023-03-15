import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def calculateFunction(x):
    if x == -1:
        return float('nan')
    else:
        return math.sin(x) / x


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.setWindowTitle("Limits of Functions")
        self.setMinimumSize(600, 400)

        # Create the central widget
        centralWidget = QWidget()

        # Create the input widgets
        limitLabel = QLabel("Limit:")
        self.limitLineEdit = QLineEdit("0")

        # Create the plot button
        plotButton = QPushButton("Plot")
        plotButton.clicked.connect(self.plotFunction)

        # Create the plot canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Add the input widgets and plot canvas to the layout
        layout = QVBoxLayout()
        layout.addWidget(limitLabel)
        layout.addWidget(self.limitLineEdit)
        layout.addWidget(plotButton)
        layout.addWidget(self.canvas)
        centralWidget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(centralWidget)

    def plotFunction(self):
        # Get the limit value
        limitValue = float(self.limitLineEdit.text())

        # Calculate the function
        y = calculateFunction(limitValue)

        # Clear the plot
        self.figure.clear()

        # Create the plot axis
        ax = self.figure.add_subplot(111)
        ax.set_title(f"f(x) = {'undefined' if y == float('nan') else y:.2f}")

        # Add the function plot
        x_values = [limitValue - 0.1, limitValue, limitValue + 0.1]
        y_values = [calculateFunction(x) for x in x_values]
        ax.plot(x_values, y_values)

        # Draw the plot
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
