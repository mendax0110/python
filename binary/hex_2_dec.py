#import the sys module
import sys

l = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

dec = int(input("Enter the decimal number: "))

c = " "

while dec > 0:

    a = dec % 16

    if a <= 15 and a > 9:
        c = l[a] + c
    else:
        c = str(a) + c
    dec = dec // 16

    #print the result
    print("The hexadecimal number is: ", c[::-1])

    #exit the program
    sys.exit()

