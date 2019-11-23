# !/usr/bin/python3
from tkinter import *

top = Tk()
L1 = Button(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 1)
E1.pack(side = RIGHT)

top.mainloop()