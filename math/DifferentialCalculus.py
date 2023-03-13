import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Differentiated Data")
        self.setGeometry(100, 100, 800, 600)

        # Add input label and text box
        input_label = QLabel("Input data (comma separated):", self)
        input_label.setGeometry(10, 10, 200, 20)
        self.input_textbox = QLineEdit(self)
        self.input_textbox.setGeometry(10, 30, 200, 20)

        # Add differentiate button
        differentiate_button = QPushButton("Differentiate", self)
        differentiate_button.setGeometry(10, 60, 200, 30)
        differentiate_button.clicked.connect(self.differentiate_data)

        # Add plot canvas
        self.figure = Figure(figsize=(6, 5), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(220, 10, 570, 580)

    def differentiate_data(self):
        try:
            # Parse data from the text box
            data_str = self.input_textbox.text()
            data = [float(x) for x in data_str.split(",")]

            # Convert data to numpy array
            data = np.array(data)
            n = len(data)

            # Differentiate the data using central difference formula
            differentiated_data = np.zeros(n - 2)
            for i in range(1, n - 1):
                differentiated_data[i - 1] = (data[i + 1] - data[i - 1]) / 2

            # Display the differentiated data on the plot
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(differentiated_data)
            ax.set_title("Differentiated Data")
            self.canvas.draw()

        except Exception as ex:
            print(f"Error: {ex}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#####SampleDataDifferential#####

# 0,0,1,1,2,4,3,9,4,16,5,25

# -1,1,0,0.5,1,2,2,4,3,6,4,8,5,10

# -10,100,-9,81,-8,64,-7,49,-6,36,-5,25,-4,16,-3,9,-2,4,-1,1,0,0,1,-1,2,-4,3,-9,4,-16,5,-25
