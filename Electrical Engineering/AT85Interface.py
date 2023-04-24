import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QGridLayout, QInputDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DigiOS Control Panel")
        self.setGeometry(100, 100, 400, 300)

        # Create the central widget and grid layout
        self.central_widget = QWidget()
        self.grid_layout = QGridLayout(self.central_widget)

        # Create the GUI elements
        self.lbl_temp = QLabel("Temperature: ")
        self.lbl_vcc = QLabel("VCC: ")
        self.btn_on = QPushButton("On")
        self.btn_off = QPushButton("Off")
        self.btn_help = QPushButton("Help")
        self.btn_clear = QPushButton("Clear")
        self.btn_ls = QPushButton("List Files")
        self.btn_reboot = QPushButton("Reboot")
        self.btn_logout = QPushButton("Logout")
        self.btn_exit = QPushButton("Exit")

        # Add the GUI elements to the grid layout
        self.grid_layout.addWidget(self.lbl_temp, 0, 0)
        self.grid_layout.addWidget(self.lbl_vcc, 1, 0)
        self.grid_layout.addWidget(self.btn_on, 2, 0)
        self.grid_layout.addWidget(self.btn_off, 3, 0)
        self.grid_layout.addWidget(self.btn_help, 4, 0)
        self.grid_layout.addWidget(self.btn_clear, 5, 0)
        self.grid_layout.addWidget(self.btn_ls, 6, 0)
        self.grid_layout.addWidget(self.btn_reboot, 7, 0)
        self.grid_layout.addWidget(self.btn_logout, 8, 0)
        self.grid_layout.addWidget(self.btn_exit, 9, 0)

        # Connect the buttons to their respective functions
        self.btn_on.clicked.connect(self.send_on_command)
        self.btn_off.clicked.connect(self.send_off_command)
        self.btn_help.clicked.connect(self.send_help_command)
        self.btn_clear.clicked.connect(self.send_clear_command)
        self.btn_ls.clicked.connect(self.send_ls_command)
        self.btn_reboot.clicked.connect(self.send_reboot_command)
        self.btn_logout.clicked.connect(self.send_logout_command)
        self.btn_exit.clicked.connect(self.send_exit_command)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

        # Get a list of available serial ports
        available_ports = list(serial.tools.list_ports.comports())

        # Create a list of available port names
        port_names = []
        for port in available_ports:
            port_names.append(port.device)

        # Display available ports to user
        selected_port, ok = QInputDialog.getItem(self, "Select a serial port", "Ports", port_names, 0, False)

        # Open the selected serial port
        if ok and selected_port:
            self.serial_port = serial.Serial(port=selected_port, baudrate=9600)

    def send_serial_command(self, command):
        self.serial_port.write(command.encode())
        response = self.serial_port.readline().decode().strip()
        return response

    def send_on_command(self):
        response = self.send_serial_command("p0on")
        print(response)

    def send_off_command(self):
        response = self.send_serial_command("p0off")
        print(response)

    def send_help_command(self):
        response = self.send_serial_command("help")
        print(response)

    def send_clear_command(self):
        response = self.send_serial_command("clear")
        print(response)

    def send_ls_command(self):
        response = self.send_serial_command("ls")
        print(response)

    def send_reboot_command(self):
        response = self.send_serial_command("reboot")
        print(response)

    def send_logout_command(self):
        response = self.send_serial_command("logout")
        print(response)

    def send_exit_command(self):
        response = self.send_serial_command("exit")
        print(response)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
