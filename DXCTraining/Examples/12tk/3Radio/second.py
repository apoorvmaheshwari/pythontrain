# !/usr/bin/python3
from tkinter import *
def sel():
   selection = var.get()
   label.config(text = selection)
root = Tk()
var = StringVar()#The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
R1 = Radiobutton(root, text = "Bangalore", variable = var,
						value = "Bangalore",
                  command = sel)
R2 = Radiobutton(root, text = "Hyderabad", variable = var, 
					value = "Hyderabad",
                  command = sel)
R3 = Radiobutton(root, text = "Pune", variable = var, 
					value = "Pune",
                  command = sel)
label = Label(root)
R1.pack()
R2.pack()
R3.pack()
label.pack()
root.mainloop()