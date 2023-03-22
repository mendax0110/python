import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QTextEdit
import serial
import glob


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize serial port
        self.serial_port = None

        # Set up UI
        self.setWindowTitle('Serial Terminal')
        self.resize(400, 300)

        self.port_label = QLabel('Port:', self)
        self.port_label.move(20, 20)

        self.port_combo = QComboBox(self)
        self.port_combo.move(60, 20)

        self.connect_button = QPushButton('Connect', self)
        self.connect_button.move(280, 20)
        self.connect_button.clicked.connect(self.connect)

        self.send_label = QLabel('Send:', self)
        self.send_label.move(20, 60)

        self.send_edit = QTextEdit(self)
        self.send_edit.move(60, 60)
        self.send_edit.setFixedHeight(80)
        self.send_edit.setFixedWidth(200)

        self.send_button = QPushButton('Send', self)
        self.send_button.move(280, 60)
        self.send_button.clicked.connect(self.send)

        self.recv_label = QLabel('Receive:', self)
        self.recv_label.move(20, 160)

        self.recv_edit = QTextEdit(self)
        self.recv_edit.move(60, 160)
        self.recv_edit.setFixedHeight(80)
        self.recv_edit.setFixedWidth(200)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.move(280, 160)
        self.clear_button.clicked.connect(self.clear)

        # Populate serial ports combo box
        ports = self.get_serial_ports()
        for port in ports:
            self.port_combo.addItem(port)

    def get_serial_ports(self):
        """Returns a list of available serial ports."""
        ports = glob.glob('/dev/tty[A-Za-z]*')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def connect(self):
        # Disconnect from any previously open port
        if self.serial_port is not None and self.serial_port.is_open:
            self.serial_port.close()

        # Connect to the selected port
        port_name = self.port_combo.currentText()
        self.serial_port = serial.Serial(port_name, 9600, timeout=0.1)

    def send(self):
        if self.serial_port is not None and self.serial_port.is_open:
            data = self.send_edit.toPlainText()
            self.serial_port.write(data.encode())

    def clear(self):
        self.recv_edit.clear()

    def read_serial(self):
        while self.serial_port is not None and self.serial_port.is_open:
            data = self.serial_port.readline().decode()
            if data:
                self.recv_edit.insertPlainText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


