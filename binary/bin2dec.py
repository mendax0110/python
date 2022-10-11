#import the necessary modules
import sys
import os
import math

#function to select from the menu
def select_from_menu():
    
    if(num == 1):
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        return(decimal)

    elif(num == 2):
        decimal = input("Enter a decimal number: ")
        binary = decimal_to_binary(decimal)
        return(binary)

#function to convert binary to decimal
def binary_to_decimal(num):
   
    b = list(num)
    n = len(list(num))
    decimal = 0
    hold    = 0
    i       = 0
    exp     = n - 1

    while(i < n):
        x    = int(b[i])
        qout = 2**exp
        hold = x * qout
        i    += 1
        exp  -= 1
        decimal += hold

    return(decimal)

#function to convert decimal to binary
def decimal_to_binary(num):

    qout    = int(num)
    base    = 0
    counter = 0
    binary  = []

    while(qout > 0):
        rem     = qout % 2
        binary.append(str(rem))
        qout    = qout // 2
        counter += 1

    binary.reverse()
    return(int(''.join(binary)))

#print the user menu
print("Binary to Decimal Converter")
print("1. Binary to Decimal")
print("2. Decimal to Binary")
num = int(input("Enter your choice: "))
print(select_from_menu())
