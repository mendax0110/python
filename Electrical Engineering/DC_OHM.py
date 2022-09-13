#import the necessary modules
import sys
import os

#give the program the data
print("Write the parameter to calculate")

#ask the user for the parameter to calculate
U = float(input('Input U : ') or 0)
R = float(input('Input R : ') or 0)
I = float(input('Input I : ') or 0)

#calculate the parameters
if not U:
    U = R * I
elif not R:
    R = U / I
elif not I:
    I = U / R
else:
    print("Leave one parameter blank, to calculate the other two")

#print the results
print("U = " + str(U) + " V")
print("R = " + str(R) + " Ohm")
print("I = " + str(I) + " A")
