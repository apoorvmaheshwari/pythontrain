# !/usr/bin/python3
from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello Python \n")
text.insert(INSERT, "Hello World \n")
text.insert(INSERT, "Hello NEC \n")
text.pack()
root.mainloop()