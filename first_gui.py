from tkinter import *

# need to write this statement before any other statement for a window...
root = Tk()

# creating a label widget
my_label1 = Label(root, text='Hello World!!!')
my_label2 = Label(root, text='welcome to gui')

# showing on the screen
# my_label1.pack()

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)

root.mainloop()
