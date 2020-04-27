from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')


def popup():
    # created a message box...
    response = messagebox.askyesno("This is my popup", 'Hello World!!!')
    Label(root, text=response).pack()


Button(root, text='Popup', command=popup).pack()

root.mainloop()
