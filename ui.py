# импортируем библиотеку для работы с окнами (интерфейсом)
# tkinter -> pyqt5 -> pyside6 (библиотеки по уровню сложности)

# импорт всей библиотеки
# import time
# использование одного метода из всей библиотеки
# time.sleep(secs=0.00001)

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имен !
# from tkinter import *

# вызов всех функций из файла
# from . import calc
# calc.calc()

# вызов только одной функции из файла
#from .calc import calc

# Задали Элиас (псевдоним) библиотеке
# import tkinter as tk
# tk.Entry()

# Пример
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

