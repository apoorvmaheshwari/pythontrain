# !/usr/bin/python3
from tkinter import *

import tkinter


def sel():
    data = ["Music", "video"]
    res = ""
    i = 0
    for l in li:
        if l.get():
            res += data[i]
        i += 1
    print(res)


top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
li = [IntVar(), IntVar()]

C1 = Checkbutton(top, text="Music", variable=li[0],
                 onvalue=1, offvalue=0, height=5,
                 width=20, command=sel)
C2 = Checkbutton(top, text="Video", variable=li[1],
                 onvalue=1, offvalue=0, height=5,
                 width=20, command=sel)

C1.pack()
C2.pack()
label = Label(top)
label.pack()
top.mainloop()
