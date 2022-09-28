#import the sys module
import sys

#Define the function
def OHM(U = 0, I = 0, R = 0):
    
    #Check if the user has entered 2 values
    if(U == 0):
        U = I * R
        print("U = " + str(U) + "V")
    elif(I == 0):
        I = U / R
        print("I = " + str(I) + "A")
    elif(R == 0):
        R = U / I
        print("R = " + str(R) + "Ohm")
    else:
        print("Error: Too many variables")

    return 0
