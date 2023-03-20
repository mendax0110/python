import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt


def plotFrequency(frequency):
    # Plot the frequency on a graph
    plt.plot([0, 1], [frequency, frequency])
    plt.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label for the input frequency
        input_frequency_label = QLabel("Input Frequency:")

        # Create a line edit for the input frequency
        self.input_frequency_edit = QLineEdit()

        # Create a button to amplify the frequency
        amplify_frequency_button = QPushButton("Amplify Frequency")
        amplify_frequency_button.clicked.connect(self.amplifyFrequency)

        # Create a label for the amplified frequency
        self.amplified_frequency_label = QLabel("Amplified Frequency:")

        # Create a layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(input_frequency_label)
        layout.addWidget(self.input_frequency_edit)
        layout.addWidget(amplify_frequency_button)
        layout.addWidget(self.amplified_frequency_label)

        # Create a widget to contain the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

    def amplifyFrequency(self):
        # Get the input frequency from the user
        input_frequency = float(self.input_frequency_edit.text())

        # Amplify the frequency
        amplified_frequency = input_frequency * 10

        # Plot the amplified frequency on a graph
        plotFrequency(amplified_frequency)

        # Show the amplified frequency
        self.amplified_frequency_label.setText("Amplified Frequency: " + str(amplified_frequency))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
