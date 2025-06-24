from tkinter import *
from datetime import date

# create window
root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')

# add widgets
# add label
lbl = Label(text = "hey there!", fg = "white", bg = "#072F5F", height = 1, width = 300)

# add label for getting name as input user
# use entry widget to create a text box for user to enter details
name_lbl = Label(text = "full name", bg = "#3895D3")
name_entry = Entry()

# function to display a message
def display():

    #read input given by user
    name = name_entry.get()

    # declaring a global variable to make it accesible anywhere
    global Message
    Message = "Welcome to the application! \n Today's date is: "
    greet = "Hello" +name+ "\n"

    # diaplay details in a text box
    # specify where to add the details in the text box
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

# add a text widget to display info/mgs
text_box = Text(height = 3)

# add button and give value of command as name of the function
# press button, display function will be called automatically
btn = Button(text = "begin", command = display, height = 1, bg = "#1261A0", fg = 'white')

# organize all the widgets in windows
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
