from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')


root.filename = filedialog.askopenfilename(initialdir='images', title='Select a file',
                                           filetypes=(('png files', '*.png'), ('all files', '*.*')))

root.mainloop()
