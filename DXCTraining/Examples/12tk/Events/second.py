
'''
<Button-1>, <ButtonPress-1>, and <1> are all synonyms for click
<B1-Motion> The mouse is moved
<ButtonRelease-1> Button 1 was released
<Double-Button-1> Button 1 was double clicked.
<Enter> The mouse pointer entered the widget
<Leave> The mouse pointer left the widget.
<FocusIn> Keyboard focus was moved to this 
<FocusOut> Keyboard focus was moved from this widget
<Key> The user pressed any key.
<Return> The user pressed the Enter key.

 Cancel (the Break key), BackSpace, Tab, Return(the Enter key), 
 Shift_L (any Shift key), Control_L (any Control key), 
 Alt_L (any Alt key),
 Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), 
 End, Home, Left,
 Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, 
 F6, F7, F8, F9, 
 F10, F11, F12, Num_Lock, and Scroll_Lock.
'''	
from tkinter import *
root = Tk()

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()