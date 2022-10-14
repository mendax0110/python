# import the modules
import sys
from tkinter import *
import time


def times():
    CURRENT_TIME = time.strftime("%H:%M:%S")
    CLOCK.config(text=CURRENT_TIME)
    CLOCK.after(200, times)


root = Tk()
root.geometry("500x250")
CLOCK = Label(root, font=("times", 50, 'bold'), bg='green')
CLOCK.grid(row=2, column=2, pady=25, padx=100)
times()

digi = Label(root, text="Digital Clock", font=("times", 24, 'bold'))
digi.grid(row=0, column=2)

nota = Label(root, text="hours   minutes   seconds   ", font="times 15 bold")
nota.grid(row=3, column=2)
root.mainloop()
