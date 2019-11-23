# !/usr/bin/python3
from tkinter import *

def callback():
	print(E1.get())
	content.set("*"*len(E1.get()))
top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
content = StringVar()
E1 = Entry(top,textvariable=content, bd = 1)
E1.pack(side = LEFT)
b = Button(top, text="get", width=10, command=callback)
b.pack()
top.mainloop()