import sys
import threading
import serial
from datetime import datetime
from PyQt5.QtCore import QTimer
from serial import tools
from serial.tools.list_ports import comports
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QWidget


# main window class, inherits from QMainWindow
class SerialMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI setup
        self.setWindowTitle("Serial Monitor")
        self.setGeometry(100, 100, 600, 400)

        # Create the widgets
        self.port_list = QComboBox()
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.refresh_ports)
        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.connect_port)
        self.disconnect_btn = QPushButton("Disconnect")
        self.disconnect_btn.clicked.connect(self.disconnect_port)
        self.text_box = QTextEdit()
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_data)

        # Create the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.port_list)
        vbox.addWidget(self.refresh_btn)
        vbox.addWidget(self.connect_btn)
        vbox.addWidget(self.disconnect_btn)
        vbox.addWidget(self.text_box)
        vbox.addWidget(self.save_btn)

        # Create the central widget and set the layout
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        # Serial port setup
        self.ser = None
        self.baud_rate = 9600

        # Populate available serial ports
        self.refresh_ports()

        # Start the timer to read data from the serial port
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(100)

    # read_data() is called every time the timer times out
    def read_data(self):
        # Read data from the serial port and display it in the text box
        if self.ser and self.ser.isOpen():
            data = self.ser.readline().decode().rstrip()
            self.text_box.append(data)

    # refresh_ports() is called when the refresh button is clicked
    def refresh_ports(self):
        # Clear the combo box
        self.port_list.clear()

        # Populate the combo box with available ports
        ports = [port.device for port in serial.tools.list_ports.comports()]

        self.port_list.addItems(ports)

    # connect_port() is called when the connect button is clicked
    def connect_port(self):
        # Disconnect any existing connections
        self.disconnect_port()

        # Connect to the selected port
        port_name = self.port_list.currentText()
        self.ser = serial.Serial(port_name, self.baud_rate)
        self.text_box.append("Connected to port " + port_name)

    # disconnect_port() is called when the disconnect button is clicked
    def disconnect_port(self):
        # Close the serial connection if it exists
        if self.ser and self.ser.isOpen():
            self.ser.close()
            self.text_box.append("Disconnected from port " + self.ser.name)

    # save_data() is called when the save button is clicked
    def save_data(self):
        # Save the current data in the text box to a file
        file_name = "SerialData_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        with open(file_name, "w") as f:
            f.write(self.text_box.toPlainText())


# main function, called when the script is run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = SerialMonitor()
    monitor.show()

    # Start a new thread to continuously read data from the serial port
    read_thread = threading.Thread(target=monitor.read_data)
    read_thread.start()

    sys.exit(app.exec_())
