from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')

# r = IntVar()
# r.set("2")

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

my_button = Button(root, text='SUBMIT', command=lambda: clicked(pizza.get()))
my_button.pack()


root.mainloop()
