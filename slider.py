from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('400x400')


def slide():
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))


# vertical slider...
vertical = Scale(root, from_=0, to=200)
vertical.pack()

# horizontal slider...
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

Button(root, text='Click Me!!!', command=slide).pack()

root.mainloop()
