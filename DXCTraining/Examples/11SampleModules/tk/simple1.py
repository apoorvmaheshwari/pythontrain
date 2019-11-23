from tkinter import Tk, Label

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label1 = Label(master, text="This is our first GUI!")
        self.label2 = Label(master, text="This is our first GUI!")
        self.label3= Label(master, text="This is our first GUI!")
        self.label4 = Label(master, text="This is our first GUI!")
        self.label5 = Label(master, text="This is our first GUI!")
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()