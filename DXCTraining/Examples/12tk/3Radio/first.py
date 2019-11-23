# !/usr/bin/python3
from tkinter import *

def sel():
	d={1:"Hello",2:"Good Morning",3:"AC"}
	selection = d[var.get()]
	label.config(text = selection)

root = Tk()
var = IntVar()#The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
R1 = Radiobutton(root, text = "Option 1",
				variable = var, 
				value = 1,
                  command = sel)


R2 = Radiobutton(root, text = "Option 2", 
				variable = var, 
				value = 2,
                  command = sel)


R3 = Radiobutton(root, text = "Option 3", 
		variable = var, 
		value = 3,
                  command = sel)


label = Label(root)
R1.pack()
R2.pack()
R3.pack()
label.pack()
root.mainloop()