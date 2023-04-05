import math
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal Generator')
        self.resize(800, 450)
        self.signal_type = 'Sawtooth'
        self.frequency = 10
        self.amplitude = 1
        self.canvas = None
        self.polyline = None
        self.init_ui()

    def init_ui(self):
        # User input controls
        signal_label = QLabel('Signal type:')
        self.signal_selector = QComboBox()
        self.signal_selector.addItem('Sawtooth')
        self.signal_selector.addItem('Rectangle')
        self.signal_selector.addItem('Sine')
        self.signal_selector.currentTextChanged.connect(self.set_signal_type)

        freq_label = QLabel('Frequency (Hz):')
        self.freq_input = QLineEdit('10')
        self.freq_input.textChanged.connect(self.set_frequency)

        amp_label = QLabel('Amplitude:')
        self.amp_input = QLineEdit('1')
        self.amp_input.textChanged.connect(self.set_amplitude)

        draw_button = QPushButton('Draw signal')
        draw_button.clicked.connect(self.draw_signal)

        input_layout = QHBoxLayout()
        input_layout.addWidget(signal_label)
        input_layout.addWidget(self.signal_selector)
        input_layout.addWidget(freq_label)
        input_layout.addWidget(self.freq_input)
        input_layout.addWidget(amp_label)
        input_layout.addWidget(self.amp_input)
        input_layout.addWidget(draw_button)

        # Signal display canvas
        self.canvas = plt.figure(figsize=(6, 4)).canvas
        canvas_layout = QVBoxLayout()
        canvas_layout.addWidget(self.canvas)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(canvas_layout)
        self.setLayout(main_layout)

    def set_signal_type(self, text):
        self.signal_type = text

    def set_frequency(self, text):
        try:
            self.frequency = float(text)
        except ValueError:
            pass

    def set_amplitude(self, text):
        try:
            self.amplitude = float(text)
        except ValueError:
            pass

    def draw_signal(self):
        # Clear any existing signal from the canvas
        if self.polyline is not None:
            self.polyline.remove()

        # Define variables for drawing the signal
        width = self.canvas.get_width_height()[0]
        height = self.canvas.get_width_height()[1]
        x_values = [i / width for i in range(width)]
        y_values = []

        try:
            # Draw the selected signal
            if self.signal_type == 'Sawtooth':
                y_values = [2 * self.amplitude * (x - int(x + 0.5)) / self.frequency for x in x_values]

            elif self.signal_type == 'Rectangle':
                y_values = [self.amplitude * (1 if math.sin(2 * math.pi * self.frequency * x) > 0 else -1) for x in
                            x_values]

            elif self.signal_type == 'Sine':
                y_values = [self.amplitude * math.sin(2 * math.pi * self.frequency * x) for x in x_values]

            # Add the polyline to the canvas
            self.polyline, = plt.plot(x_values, y_values, color='black', linewidth=2)
            self.canvas.draw()

        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
