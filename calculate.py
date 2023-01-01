"""I want to do calculate with graphic design by tkinter"""

from tkinter import *

# делаем функцию с командой для наших кнопок
def add_digit(digit):
    value = e.get() + str(digit) # делаем так, чтобы новое число добавлялось справа
    if value [0] == '0': # если первый символ равен нулю
        value = value [1:] # мы оставляем все, кроме первого символа
    e.delete(0, END) # очищаем поле ввода
    e.insert(0, value) # вставляем в поле ввода наше значение на 1 символ

# делаем функцию с командой для наших кнопок-операций
def add_operation(operation):
    value = e.get()
    if value [-1] in '/*-+': # мы должны сделать так, чтобы операции заменялись при нажатии
        value = value [:1] # при помощи среза заменяем последний символ
    e.delete(0, END)
    e.insert(0, value + operation)

# для компактности делаем функцию, которая берет все параметры кнопки
def make_button (digit):
    return Button(text=digit, bd=5, font=('Arial', 15, 'normal'), command=lambda: add_digit (digit))

# функция для кнопок с операциями
def make_operation (operation):
    return Button(text=operation, bd=5, font=('Arial', 15, 'normal'), command=lambda: add_operation (operation))


root = Tk()
root.geometry('238x270+200+200')
root.config(bg='grey')
root.title('Calculate')

e = Entry(root, bd=5, justify=RIGHT, width = 15, font = ('Arial', 15, 'normal'))
e.insert (0, '0') # делаем так, чтобы в поле ввода изначально был 0
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

make_operation ('/').grid(row=1, column=3, stick='wens', padx=3, pady=1)
make_operation ('*').grid(row=2, column=3, stick='wens', padx=3, pady=1)
make_operation ('-').grid(row=3, column=3, stick='wens', padx=3, pady=1)
make_operation ('+').grid(row=4, column=3, stick='wens', padx=3, pady=1)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_columnconfigure(4, minsize=60)

root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(3, minsize=50)
root.grid_rowconfigure(4, minsize=50)
root.grid_rowconfigure(5, minsize=50)

root.mainloop()
