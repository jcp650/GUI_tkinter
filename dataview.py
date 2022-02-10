from tkinter import *
from tkinter.ttk import *

from plotdata import *
from stats import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.winfo_toplevel().title("Data View")
        self.l1 = Label(self.master, text="File Name")
        self.l2 = Label(self.master, text="X label")
        self.l3 = Label(self.master, text="Y Label")

        self.l1.grid(row=0)
        self.l2.grid(row=1)
        self.l3.grid(row=2)


root = Tk()
app = Application(master = root)
app.mainloop()