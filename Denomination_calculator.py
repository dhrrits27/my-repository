from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# setting up main window
root = Tk()
root.title("denomination counter")
root.configure(bg = 'light blue')
root.geometry("650x400")

# adding image and labels in the main window
upload = Image.open("app_img.jpg")

# resizing the image
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image = image, bg = 'light blue')
label.place(x = 180, y = 20)

label1 = Label(root, text = "hey user! welcome to denomination counter application", bg = 'light blue')
label1.place(relx = 0.5, rely = 340, anchor = CENTER)

# funtion to display msg box and proceed if its okk
def msg():
    Msgbox = messagebox.showinfo("alert", "do u want to calculate the denomination count?") 

    if Msgbox == 'ok':
        topwin()

# adding buttons to the main window
button1 = Button(root, text = "lets get started", command = msg, bg = 'brown', fg = 'white')
button1.place(x = 260, y = 360)

# function for opening new window
def topwin():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg = "light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text = "enter total amt", bg = 'light grey')
    entry = Entry(top)
    lbl = Label(top, text = "here are the no of notes for each denomination", bg = 'light grey')

    lbl1 = Label(top, text = "2000", bg = 'light grey')
    lbl2 = Label(top, text = "500", bg = 'light grey')
    lbl3 = Label(top, text = "100", bg = 'light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("error", "please enter a valid number")

    btn = Button(top, text = "calculate", command = calculator, bg = 'brown', fg = 'white')

    # centering widgets in the window
    label.place(x=230, y=50 )
    entry.place(x=200, y=80 )
    btn.place(x=240, y=120 )
    lbl.place(x=140, y=170 )

    lbl1.place(x=180, y=200)
    lbl2.place(x=180, y=230)
    lbl3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()