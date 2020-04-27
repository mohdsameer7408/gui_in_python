from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=10)
e.pack()
# for placing  a default text...
e.insert(0, "Enter your name : ")


def my_click():
    my_label = Label(root, text=e.get())
    my_label.pack()


my_button = Button(root, text='SUBMIT', command=my_click, fg='white', bg='#abca08')
my_button.pack()

root.mainloop()

