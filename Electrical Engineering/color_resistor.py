# import the necessary modules
from sys import setprofile

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

# Define the colors of the resistors
resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]


# create the GUI window
class Application_Resistor(Frame):
    def __init__(self, master):

        # initialize the frame
        Frame.__init__(self, master)
        self.grid()

        # set the colors
        self.current_colors = ["orange", "orange", "brown", "gold"]

        # create the elements
        self.create_elements()

    # create the elements
    def create_elements(self):

        # Create the canvas
        self.resistor = Canvas(self, width=300, height=100)
        self.resistor.config(bg="white")
        self.resistor.create_rectangle((10, 10, 290, 90), fill="#F3C967")
        self.resistor.grid(row=0, column=0, columnspan=3)

        # create the first band
        Label(self, text="First Color:").grid(row=1, column=0)
        self.band1 = Canvas(self, width=200, height=50)
        self.draw_colors(self.band1)
        self.band1.grid(row=1, column=1, columnspan=2)
        self.band1.bind("<Button-1>", self.b1)

        # create the second band
        Label(self, text="Second Color:").grid(row=2, column=0)
        self.band2 = Canvas(self, width=200, height=50)
        self.draw_colors(self.band2)
        self.band2.grid(row=2, column=1, columnspan=2)
        self.band2.bind("<Button-1>", self.b2)

        # create the third band
        Label(self, text="Third Color:").grid(row=3, column=0)
        self.band3 = Canvas(self, width=200, height=50)
        self.draw_colors(self.band3)
        self.band3.grid(row=3, column=1, columnspan=2)
        self.band3.bind("<Button-1>", self.b3)

        # create the fourth band
        Label(self, text="Fourth Color:").grid(row=4, column=0)
        self.band4 = Canvas(self, width=200, height=50)
        self.band4.create_rectangle((0, 0, 100, 50), fill="gold", outline="gold")
        self.band4.create_rectangle((100, 0, 200, 50), fill="gray", outline="gray")
        self.band4.create_text((50, 25), text="+/- 5 %")
        self.band4.create_text((150, 25), text="+/- 10 %")
        self.band4.grid(row=4, column=1, columnspan=2)
        self.band4.bind("<Button-1>", self.b4)

        self.result = Text(self, width=35, height=1)
        self.result.grid(row=5, column=0, columnspan=2)

        self.update()

    # calculate the resistor value
    def calcualte(self):
        val = str(resistor_color.index(self.current_colors[0])) + str(resistor_color.index(self.current_colors[1]))

        for i in range(resistor_color.index(self.current_colors[2])):
            val = val + "0"

        return val

    # draw the colors
    def draw_colors(self, canv):
        for i in range(10):
            canv.create_rectangle((20 * i, 1, 20 + 20 * i, 50), fill=resistor_color[i], outline=resistor_color[i])

    # update the resistor
    def update(self):

        for i in range(4):
            self.resistor.create_rectangle((60 * i + 40, 10, 60 * i + 70, 90), fill=self.current_colors[i])
            self.result.delete(0.0, END)
            self.result.insert(END, "The Resistor Value is: " + self.calcualte() + "ohm")

    # change the color
    def change(self, band, color):
        self.current_colors[band - 1] = color
        self.update()

    def b1(self, event):
        self.change(1, self.xToc(event.x))

    def b2(self, event):
        self.change(2, self.xToc(event.x))

    def b3(self, event):
        self.change(3, self.xToc(event.x))

    def b4(self, event):
        if event.x <= 100:
            self.change(4, "gold")
        else:
            self.change(4, "gray")

    def xToc(self, x):

        return resistor_color[int(x / 20)]


# run the program
root = Tk()
root.title("Resistor Color Code")
app = Application_Resistor(root)
root.mainloop()
