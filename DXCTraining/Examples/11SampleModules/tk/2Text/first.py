# !/usr/bin/python3
from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello Python")
text.pack()
root.mainloop()