# import the libraries
import serial
import time
import out

# config the serial port
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

# check if the serial port is open
ser.isOpen()

# write down the data to be sent
print('Sending data.....\nInsert "exit" to leave the program.')

data = 1

while (1):
    # get the input from the user
    data = input(">> ")

    if (input == 'exit'):
        ser.close()
        exit()

    else:
        # send the data to the serial port from the device
        out = ''
        time.sleep(1)

        while (ser.inWaiting() > 0):
            out += ser.read(1)

        if (out != ''):
            print((">>" + out))

        else:
            print("No data received")
