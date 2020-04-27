from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('400x400')


def show():
    my_label = Label(root, text=var.get())
    my_label.pack()


var = StringVar()

c = Checkbutton(root, text='Check this box', variable=var, onvalue='On', offvalue='Off')
c.deselect()
c.pack()

my_button = Button(root, text='Show selection', command=show)
my_button.pack()

root.mainloop()
