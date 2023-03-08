import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the radio buttons for NPN/PNP selection
        self.npn_radio = QRadioButton('NPN')
        self.pnp_radio = QRadioButton('PNP')
        self.npn_radio.setChecked(True)

        # Create the button for generating the sine wave
        self.button = QPushButton('Generate Sine Wave')
        self.button.clicked.connect(self.plot_sine_wave)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.npn_radio)
        layout.addWidget(self.pnp_radio)
        layout.addWidget(self.button)

        # Set the layout
        self.setLayout(layout)
        self.setWindowTitle('Transistor Circuit Sine Wave')
        self.show()

    def plot_sine_wave(self):
        # Get the selected transistor type from the radio buttons
        if self.npn_radio.isChecked():
            transistor_type = "NPN"
        else:
            transistor_type = "PNP"

        # Generate the input and output sine waves
        num_points = 1000
        frequency = 1000
        amplitude = 1
        phase_shift = math.pi / 2
        input_dc_offset = 0.5
        output_dc_offset = 0.5
        input_min = input_dc_offset - amplitude
        input_max = input_dc_offset + amplitude
        output_min = output_dc_offset - amplitude
        output_max = output_dc_offset + amplitude
        t = np.linspace(0, 1, num_points)
        input_waveform = input_dc_offset + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        output_waveform = np.zeros(num_points)
        for i in range(num_points):
            input_value = input_waveform[i]
            if transistor_type == "NPN":
                if input_value < 0.7:
                    output_waveform[i] = 0
                else:
                    output_waveform[i] = input_value - 0.7
            elif transistor_type == "PNP":
                if input_value > 0.3:
                    output_waveform[i] = 0
                else:
                    output_waveform[i] = 0.3 - input_value

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(input_waveform, np.zeros(num_points), 'o', label='Input')
        ax.plot(input_waveform, output_waveform, '.', label='Output')
        ax.set_xlim(input_min, input_max)
        ax.set_ylim(output_min, output_max)
        ax.set_xlabel('Input')
        ax.set_ylabel('Output')
        ax.set_title('Transistor Circuit Sine Wave ({})'.format(transistor_type))
        ax.legend()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
