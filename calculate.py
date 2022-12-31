"""I want to do calculate with graphic design by tkinter"""

from tkinter import *

root = Tk ()
root.geometry ('250x250+200+200')
root.config (bg = 'grey')
root.title ('Calculate')

e = Entry (root, bd = 5)
e.grid (row = 0, column = 0, columnspan = 4, stick = 'wens', padx = 5, pady = 5)

Button (text = '1', bd = 5).grid (row = 1, column = 0, stick = 'wens', padx = 5, pady = 5)

root.grid_columnconfigure (0, minsize = 40)
root.grid_columnconfigure (1, minsize = 40)
root.grid_columnconfigure (2, minsize = 40)
root.grid_columnconfigure (3, minsize = 40)
root.grid_columnconfigure (4, minsize = 40)

root.grid_rowconfigure (0, minsize = 1)
root.grid_rowconfigure (1, minsize = 5)
root.grid_rowconfigure (2, minsize = 5)
root.grid_rowconfigure (3, minsize = 5)
root.grid_rowconfigure (4, minsize = 5)
root.grid_rowconfigure (5, minsize = 5)

root.mainloop ()