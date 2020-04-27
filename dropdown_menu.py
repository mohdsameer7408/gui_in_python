from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('400x400')

options = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
clicked = StringVar()
clicked.set(options[0])


def show():
    my_label = Label(root, text=clicked.get())
    my_label.pack()


# drop down box
drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text='Show Selection', command=show)
my_button.pack()

root.mainloop()
