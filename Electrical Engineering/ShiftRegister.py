import tkinter as tk

class ShiftRegister:
    def __init__(self, root, num_bits):
        self.num_bits = num_bits
        self.bits = [0] * num_bits
        self.labels = []
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.grid(row=0, column=num_bits)
        self.oval_id = None
        for i in range(num_bits):
            label = tk.Label(root, text="0", font=("Helvetica", 16))
            label.grid(row=0, column=i)
            self.labels.append(label)
        self.updated = False
        self.auto_shift = False

    def shift_left(self):
        self.bits = [0] + self.bits[:-1]
        self.updated = True

    def shift_right(self):
        self.bits = self.bits[1:] + [0]
        self.updated = True

    def set_value(self, value):
        for i in range(self.num_bits):
            self.bits[i] = (value >> i) & 1
        self.updated = True

    def update_display(self):
        if self.oval_id is not None:
            self.canvas.delete(self.oval_id)
        self.oval_id = self.canvas.create_oval(50, 50, 150, 150, fill="red")
        for i in range(self.num_bits):
            self.labels[i].config(text=str(self.bits[i]))
        if self.updated:
            self.canvas.after(250, self.clear_oval)
        self.updated = False

    def clear_oval(self):
        self.canvas.delete(self.oval_id)
        self.oval_id = None

def update_shift_register():
    if shift_register.auto_shift:
        shift_register.shift_left()
        shift_register.update_display()
    root.after(500, update_shift_register)

def toggle_auto_shift():
    shift_register.auto_shift = not shift_register.auto_shift

root = tk.Tk()
root.title("Shift Register Simulator")

shift_register = ShiftRegister(root, 8)

left_button = tk.Button(root, text="Shift Left", command=lambda: shift_register.shift_left())
left_button.grid(row=1, column=0)

right_button = tk.Button(root, text="Shift Right", command=lambda: shift_register.shift_right())
right_button.grid(row=1, column=1)

entry = tk.Entry(root)
entry.grid(row=1, column=2)

def set_value_from_entry():
    shift_register.set_value(int(entry.get()))
    shift_register.update_display()

set_button = tk.Button(root, text="Set Value", command=set_value_from_entry)
set_button.grid(row=1, column=3)

auto_shift_button = tk.Button(root, text="Auto Shift", command=toggle_auto_shift)
auto_shift_button.grid(row=1, column=4)

root.after(500, update_shift_register)
root.mainloop()
