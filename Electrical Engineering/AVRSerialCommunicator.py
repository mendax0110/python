import tkinter as tk
import serial
from serial.tools import list_ports

# Create the GUI window
window = tk.Tk()
window.title("Serial Communication")

# Create the input and output fields
input_field = tk.Entry(window)
output_field = tk.Text(window)

# Create the baud rate field
baud_field = tk.Entry(window)

# Create the port selection field
port_var = tk.StringVar(window)
port_field = tk.OptionMenu(window, port_var, *[port.device for port in list_ports.comports()])

# Create the send button
def send_data():
    # Read the data from the input field and write it to the serial port
    data = input_field.get()
    ser.write(data.encode())
    input_field.delete(0, tk.END)

send_button = tk.Button(window, text="Send", command=send_data)

# Create the receive button
def receive_data():
    # Read data from the serial port and display it in the output field
    data = ser.readline()
    output_field.insert(tk.END, data.decode())

receive_button = tk.Button(window, text="Receive", command=receive_data)

# Create the connect button
def connect():
    # Set up the serial port using the values entered by the user
    global ser
    ser = serial.Serial(
        port=port_var.get(),
        baudrate=int(baud_field.get()),
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

connect_button = tk.Button(window, text="Connect", command=connect)

# Lay out the widgets in the GUI
input_field.pack()
send_button.pack()
output_field.pack()
receive_button.pack()
port_field.pack()
baud_field.pack()
connect_button.pack()

# Start the GUI event loop
window.mainloop()
