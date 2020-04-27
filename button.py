from tkinter import *

# need to write this statement before any other statement for a window...
root = Tk()


def my_click():
    my_label = Label(root, text='hye there')
    my_label.pack()


# creating a button
# my_button = Button(root, text='SUBMIT', padx=40, state=DISABLED).pack()

# handling click of a button...
my_button = Button(root, text='SUBMIT', command=my_click, fg='white', bg='#abca08')
my_button.pack()

root.mainloop()
