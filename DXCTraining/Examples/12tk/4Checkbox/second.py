from tkinter import *

master = Tk()

var = StringVar(value="")
c = Checkbutton(
        master, text="Color image", 
		variable=var,
        onvalue="RGB", offvalue="BW"
        )
c.pack()

mainloop()