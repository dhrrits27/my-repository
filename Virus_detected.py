# import necessary libraries
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

# function to display warning msg
# it will be called only once the button is clicked


# messagebox.showwarning("window name", "text to be displayed")

def msg():
    messagebox.showwarning("alert", "stop! virus found")

# add button widget to window
button = Button(root, text = "scan for virus", command = msg)
button.place(x = 40, y = 80)

# entering main loop event
root.mainloop()
