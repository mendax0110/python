# import the necessary modules
import sys
import os

# print the welcome message and the menu
print("Welcome to the Ohm's Law Calculator")
print("Please enter the following values")

# ask for the values
v = complex(input("Voltage v(U): ") or 0)
r = complex(input("Resistance r(R): ") or 0)
i = complex(input("Current i(I): ") or 0)
x = complex(input("Power x(P): ") or 0) * 1j

# calculate the values
if not v:
    Z = (r ** 2 + (x / 1j) ** 2) ** 0.5
    U = Z * i
elif not i:
    Z = (r ** 2 + (x / 1j) ** 2) ** 0.5
    I = v / Z
elif not r:
    Z = v / i
    r = (Z ** 2 - (x / 1j) ** 2) ** 0.5
elif not x:
    Z = v / i
    x = (Z ** 2 - r ** 2) ** 0.5 * 1j
else:
    # tell the user which values are beeing calculated
    print("Leave one parameter blank, to calculate the others")

# display the results
print("Voltage v(U): ", v)
print("Resistance r(R): ", r)
print("Current i(I): ", i)
print("Power x(P): ", x)
print("Impedance Z: ", Z)
