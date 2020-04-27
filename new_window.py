from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')


def new_window():
    top = Toplevel()
    Label(top, text='You are on a new window!!!').pack()
    

Button(root, text='Open new window', command=new_window).pack()


root.mainloop()
