# import the libraries
import mraa
import time
import sys

# set the serial port
port = "/dev/ttyMFD1"

# set value to send
data = 'IMPUT YOUR DATA HERE'

# initialize the serial port
uart = mraa.Uart(port)

# send the data to the serial port
uart.write(bytearray(data, 'utf-8'))
