from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')

my_img = ImageTk.PhotoImage(Image.open('images/pic4.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit', command=root.quit)
button_quit.pack()

root.mainloop()
