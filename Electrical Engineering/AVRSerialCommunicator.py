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
port_options = [port.device for port in list_ports.comports()]
if not port_options:
    port_options = ['No available ports']
port_field = tk.OptionMenu(window, port_var, *port_options)

# Create the send button
def send_data():
    # Read the data from the input field and write it to the serial port
    data = input_field.get()
    if ser and ser.is_open:
        ser.write(data.encode())
        input_field.delete(0, tk.END)
    else:
        output_field.insert(tk.END, 'Error: Not connected to a serial port\n')

send_button = tk.Button(window, text="Send", command=send_data)

# Create the receive button
def receive_data():
    # Read data from the serial port and display it in the output field
    if ser and ser.is_open:
        data = ser.readline()
        output_field.insert(tk.END, data.decode())
    else:
        output_field.insert(tk.END, 'Error: Not connected to a serial port\n')

receive_button = tk.Button(window, text="Receive", command=receive_data)

# Create the connect button
def connect():
    # Set up the serial port using the values entered by the user
    global ser
    try:
        ser = serial.Serial(
            port=port_var.get(),
            baudrate=int(baud_field.get()),
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
    except serial.serialutil.SerialException:
        output_field.insert(tk.END, 'Error: Unable to connect to specified port\n')

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
