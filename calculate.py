"""I want to do calculate with graphic design by tkinter"""

from tkinter import *
from unicodedata import digit


def add_digit(digit):
    value = e.get() + str(digit)
    if value [0] == '0':
        value = value [1:]
    e.delete(0, END)
    e.insert(0, value)


root = Tk()
root.geometry('250x250+200+200')
root.config(bg='grey')
root.title('Calculate')

e = Entry(root, bd=5, justify=RIGHT, font = ('Arial', 15, 'normal'))
e.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

Button(text='1', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (1)).grid(row=1, column=0, stick='wens', padx=3, pady=1)
Button(text='2', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (2)).grid(row=1, column=1, stick='wens', padx=3, pady=1)
Button(text='3', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (3)).grid(row=1, column=2, stick='wens', padx=3, pady=1)
Button(text='4', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (4)).grid(row=2, column=0, stick='wens', padx=3, pady=1)
Button(text='5', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (5)).grid(row=2, column=1, stick='wens', padx=3, pady=1)
Button(text='6', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (6)).grid(row=2, column=2, stick='wens', padx=3, pady=1)
Button(text='7', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (7)).grid(row=3, column=0, stick='wens', padx=3, pady=1)
Button(text='8', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (8)).grid(row=3, column=1, stick='wens', padx=3, pady=1)
Button(text='9', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (9)).grid(row=3, column=2, stick='wens', padx=3, pady=1)
Button(text='0', bd=5, font = ('Arial', 15, 'normal'), command=lambda: add_digit (0)).grid(row=4, column=0, stick='wens', padx=3, pady=1)

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
