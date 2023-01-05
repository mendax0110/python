import serial
import tkinter as tk
import serial.tools.list_ports

# Create the GUI window
window = tk.Tk()
window.title("atmega15a Health Check")

# Create a list of available serial ports
ports = serial.tools.list_ports.comports()
port_names = [port.device for port in ports]

# Add a label and a dropdown menu to select the serial port
tk.Label(window, text="Serial Port:").grid(row=0, column=0)
port_var = tk.StringVar(window)
port_var.set(port_names[0])
tk.OptionMenu(window, port_var, *port_names).grid(row=0, column=1)

# Add a button to check the health status
def check_health():
    # Open the serial port
    ser = serial.Serial(
        port=port_var.get(),
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1
    )

    # check which ports are aviable
    ports = list(serial.tools.list_ports.comports())
    port_names = [port.device for port in ports]

    # Send the request command to the microcontroller
    ser.write(b'HEALTH\n')

    # Read the response from the microcontroller
    response = ser.readline().decode('utf-8').strip()

    # Print the response
    print(response)

    # Close the serial port
    ser.close()

tk.Button(window, text="Check Health", command=check_health).grid(row=1, column=0, columnspan=2)

# Run the GUI
window.mainloop()
