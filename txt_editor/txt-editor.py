#import the tkinter module
from tkinter import *
from tkinter import filedialog

#Create the class for the text editor
class TextEditor:
    #init the editor
    def __init__(self, root):
        self.menubar = Menu(root, font=('arial', 12))
        root.config(menu = self.menubar)
        self.filemenu = Menu(root, tearoff=0, font=('arial', 8))

        #Create the file menu
        self.filemenu.add_command(label="New", command=self.new)
        self.filemenu.add_command(label="Open", command=self.new_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)
    
        #Add the file menu to the menu bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        #Create the edit menu
        self.editmenu = Menu(root, tearoff=0, font=('arial', 8))
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)

        #Add the edit menu to the menu bar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.thememenu = Menu(root, tearoff=0, font=('arial', 8))
        self.thememenu.add_command(label="Dark", command=lambda: self.theme_Change(1))
        self.thememenu.add_command(label="Light", command=lambda: self.theme_Change(2))
        self.menubar.add_cascade(label="Theme", menu = self.thememenu)

        self.text_area = Text(root, bg="white", fg="black", font=("arial", 12), wrap=NONE)

        #add the scroll bar to the text area
        self.horizontal_scroll_bar = Scrollbar(root, orient=HORIZONTAL, bg="#3687ce", activebackground="#0056a1", command=self.text_area.xview)
        self.text_area.configure(xscrollcommand=self.horizontal_scroll_bar.set)
        self.horizontal_scroll_bar.pack(side=BOTTOM, fill=X)

        #add the scroll bar to the text area
        self.vertical_scroll_bar = Scrollbar(root, orient=VERTICAL, bg="#3687ce", activebackground="#0056a1", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.vertical_scroll_bar.set)
        self.vertical_scroll_bar.pack(side=RIGHT, fill=Y)

        #fill to full root  
        self.text_area.pack(expand=True, fill=BOTH)

    #cut, copy, past text
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def new(self):
        self.text_area.delete(1.0, END)

    #create a new file
    def new_file(self):
        self.filename = filedialog.askopenfilename(parent=root,title="Select a file",filetypes=(("Python file","*.py"),("All files","*.*")))
        #check if the new file is selected
        if self.filename != NONE:
            f = open(self.filename, "r")
            contents = f.read()
            #insert the content to the text area
            self.text_area.insert(1.0, contents)
            #close the file
            f.close()

    #safe a new created file
    def save_file(self):
        self.filename = filedialog.asksaveasfilename(parent = root, defaultextension = ".txt")
        #check if the file is already created
        if self.filename != NONE:
            #get the content of the text area
            contents = self.text_area.get(1.0, END)
            #open the file
            f = open(self.filename, "w")
            #write the content to the file
            f.write(contents)
            #close the file
            f.close()
        #if the file is not created
        else:
            self.new_file()

    #change the theme of the text editor
    def theme_Change(self, value):
        if(value==1):
            self.text_area["bg"]="black"
            self.text_area["fg"]="white"
        if(value==2):
            self.text_area["bg"]="white"
            self.text_area["fg"]="black"

#Create the root window
root = Tk()
#Set the title of the root window
root.title("m3ndax txt editor")
#Set the size of the root window
root.geometry("800x600")
#Create the text editor object
text_editor_obj = TextEditor(root)
#Start the main loop
root.mainloop()





