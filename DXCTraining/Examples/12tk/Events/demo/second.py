# !/usr/bin/python3
from tkinter import *

def callback():
	print(E1.get())
top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 1)
E1.pack(side = RIGHT)
b = Button(top, text="get", width=10, command=callback)
b.pack()
top.mainloop()