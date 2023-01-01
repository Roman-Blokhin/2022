"""I want to do calculate with graphic design by tkinter"""

from tkinter import *


def add_digit(digit):
    value = e.get() + str(digit)
    if value [0] == '0':
        value = value [1:]
    e.delete(0, END)
    e.insert(0, value)


def make_button (digit):
    return Button(text=digit, bd=5, font=('Arial', 15, 'normal'), command=lambda: add_digit (digit))


root = Tk()
root.geometry('250x250+200+200')
root.config(bg='grey')
root.title('Calculate')

e = Entry(root, bd=5, justify=RIGHT, font = ('Arial', 15, 'normal'))
e.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

make_button (1).grid(row=1, column=0, stick='wens', padx=3, pady=1)
make_button (2).grid(row=1, column=1, stick='wens', padx=3, pady=1)
make_button (3).grid(row=1, column=2, stick='wens', padx=3, pady=1)
make_button (4).grid(row=2, column=0, stick='wens', padx=3, pady=1)
make_button (5).grid(row=2, column=1, stick='wens', padx=3, pady=1)
make_button (6).grid(row=2, column=2, stick='wens', padx=3, pady=1)
make_button (7).grid(row=3, column=0, stick='wens', padx=3, pady=1)
make_button (8).grid(row=3, column=1, stick='wens', padx=3, pady=1)
make_button (9).grid(row=3, column=2, stick='wens', padx=3, pady=1)
make_button (0).grid(row=4, column=0, stick='wens', padx=3, pady=1)

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, minsize=50)
root.grid_columnconfigure(2, minsize=50)
root.grid_columnconfigure(3, minsize=50)
root.grid_columnconfigure(4, minsize=50)

root.grid_rowconfigure(0, minsize=40)
root.grid_rowconfigure(1, minsize=40)
root.grid_rowconfigure(2, minsize=40)
root.grid_rowconfigure(3, minsize=40)
root.grid_rowconfigure(4, minsize=40)
root.grid_rowconfigure(5, minsize=40)

root.mainloop()
