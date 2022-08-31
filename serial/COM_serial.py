#import the libraries for the serial communication
import serial
import serial.tools.list_ports as port_list

#list the available ports
ports = list(port_list.comports())
#print the available ports
print(ports[0].device)
port = ports[0].device
#set the baud rate to 9600
baudrate = 9600
serialPort = serial.Serial(port=port, baudrate=baudrate,
                            bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
serialString = "DATA"
#send the string to the serial port
serialPort.write(bytes.fromhex("A555FA"))

#read the data from the serial port
while True:
    try:
        serialPort.reset_input_buffer()
        serialPort.reset_output_buffer()
        serialString = serialPort.read(10).hex()
        serialString = serialPort.read()
        print(serialString)
    except KeyboardInterrupt:
        break

serialPort.close()
