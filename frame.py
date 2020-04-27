from tkinter import *

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')

frame = LabelFrame(root, text='This is my frame', padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text='Don\'t click here')
b.pack()

root.mainloop()
