import threading
import subprocess
import tkinter as tk

class ProgramControl(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.program_name = tk.StringVar()
        self.program_name_entry = tk.Entry(self, textvariable=self.program_name)
        self.program_name_entry.pack(side="left")
        self.start_button = tk.Button(self, text="Start", command=self.start_program)
        self.start_button.pack(side="left")
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_program)
        self.stop_button.pack(side="left")

    def start_program(self):
        self.program_thread = threading.Thread(target=self.run_program)
        self.program_thread.start()

    def run_program(self):
        self.program_process = subprocess.Popen(self.program_name.get())

    def stop_program(self):
        self.program_process.terminate()

class ProgramControlGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.program_controls = []
        self.add_button = tk.Button(self, text="Add Program", command=self.add_program_control)
        self.add_button.pack()

    def add_program_control(self):
        control = ProgramControl(self)
        control.pack()
        self.program_controls.append(control)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProgramControlGUI(root)
    gui.pack()
    root.mainloop()
