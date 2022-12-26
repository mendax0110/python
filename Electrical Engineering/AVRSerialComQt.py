# Import the libraries
import serial
from serial.tools import list_ports
from PyQt5 import QtCore, QtWidgets

# Main 
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('AVR Serial')

        # Create the layout and widgets
        layout = QtWidgets.QVBoxLayout()
        self.com_port_list = QtWidgets.QComboBox()
        baud_rate_label = QtWidgets.QLabel('Baud rate:')
        self.baud_rate_spinbox = QtWidgets.QSpinBox()
        command_label = QtWidgets.QLabel('Command:')
        self.command_line_edit = QtWidgets.QLineEdit()
        send_button = QtWidgets.QPushButton('Send')
        response_label = QtWidgets.QLabel('Response:')
        self.response_text_edit = QtWidgets.QTextEdit()

        # Populate the serial port dropdown list
        for port in list_ports.comports():
            self.com_port_list.addItem(port.device, port.description)

        # Set the default baud rate
        self.baud_rate_spinbox.setValue(9600)

        # Set the range and single step of the baud rate spinbox
        self.baud_rate_spinbox.setRange(1200, 200000)
        self.baud_rate_spinbox.setSingleStep(1200)

        # Connect the send button to the send_command function
        send_button.clicked.connect(self.send_command)

        # Add the widgets to the layout
        layout.addWidget(self.com_port_list)
        layout.addWidget(baud_rate_label)
        layout.addWidget(self.baud_rate_spinbox)
        layout.addWidget(command_label)
        layout.addWidget(self.command_line_edit)
        layout.addWidget(send_button)
        layout.addWidget(response_label)
        layout.addWidget(self.response_text_edit)

        # Set the layout and show the window
        self.setLayout(layout)
        self.show()

    # Send Command
    def send_command(self):
        # Get the selected serial port and baud rate
        com_port = self.com_port_list.currentText()
        baud_rate = self.baud_rate_spinbox.value()

        # Open the serial port
        ser = serial.Serial(com_port, baud_rate)

        # Get the command from the line edit
        command = self.command_line_edit.text().encode()

        # Send the command to the microcontroller
        ser.write(command)

        # Read the response from the microcontroller
        response = ser.read()

        # Display the response in the text edit
        self.response_text_edit.setText(response.decode())

        # Close the serial port
        ser.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()
