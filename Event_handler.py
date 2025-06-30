from tkinter import *

# create window
window = Tk()
window.title("event handler")
window.geometry("500x500")

# event handler for key press

def handle_keypress(event):
    """print the charecter associated to the key pressed """
    print(event.char)

# bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# event handler for button click
def handle_click(event):
    print("\n the button was clicked")

button = Button(text = "click me!")
button.pack()

# bind click event to handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()
