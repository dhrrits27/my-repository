from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# setup root window
window = Tk()
window.title("codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

# function to open file
def open_file():
    """open a file for editing"""
    filepath = askopenfilename(
        filetypes = [("text files", "*.txt"), ("all files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, END)

    # if file is opened then display contents of the file
    with open(filepath, "r") as input_file:

        # resd contents of the input file
        text = input_file.read()

        # insert contents of the file in the editor box
        text_edit.insert(END, text)

        input_file.close()

    window.title(f"codingal's text editor - {filepath}")

# function to save file
def save_file():

    #save the current file as the new file
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("text files", "*.txt"), ("all files", "*.*")]
    )
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:

        # read the edited content and update it in the output file
        text = text_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"codingal's text editor - {filepath}")

# add widgets in the application
text_edit = Text(window)
fr_buttons = Frame(window, relief = RAISED, bd = 2)

btn_open = Button(fr_buttons, text = "open", command = open_file)
btn_save = Button(fr_buttons, text = "save as...", command = save_file)

btn_open.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
btn_save.grid(row = 1, column = 0, sticky = "ew", padx = 5)

fr_buttons.grid(row = 0, column = 0, sticky = "ns")
text_edit.grid(row = 0, column = 1, sticky = "nsew")

window.mainloop()
