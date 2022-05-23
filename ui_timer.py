# импорт всей библиотеки
import time
from threading import Thread

# собираем в .exe файл
# pyinstaller --onefile ui_timer.py

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !
# from tkinter import *

# импорт всей библиотеки с присовением псевдонима
# import tkinter as tk


# импорт отдельной функции из модуля(из нашего файла)
# from .calc import calc_3


# импортируем библиотеку для работы с окнами(интерфейсом) все библиотеки: tkinter pyqt5 pyside6


# import tkinter
# import tkinter.ttk as ttk
# root = tkinter.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
from tkinter import ttk

hours = 0
minutes = 0
seconds = 0

pause = True


def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0

    seconds_label.config(text=f"{seconds}")
    minutes_label.config(text=f"{minutes}")
    hours_label.config(text=f"{hours}")


def stop_timer():
    global pause
    pause = False


def start_timer():
    global pause
    pause = True

    global hours
    # hours = 0
    global minutes
    # minutes = 0
    global seconds
    # seconds = 0

    # код до цикла
    while pause:
        # seconds = seconds + 1
        seconds += 1

        if seconds > 59:
            minutes += 1
            seconds = 0

        if minutes > 59:
            hours += 1
            minutes = 0

        if hours > 23:
            seconds = 0
            minutes = 0
            hours = 0

        time.sleep(0.00001)
        seconds_label.config(text=f"{seconds}")
        minutes_label.config(text=f"{minutes}")
        hours_label.config(text=f"{hours}")
        print(f"{hours}:{minutes}" + ":" + str(seconds))


def start_new_thread():
    Thread(
        target=start_timer
    ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
    # будет виснуть


# инициализация инстанса - создание объекта ткинтер
root = Tk()

# создание главного окна
frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")
frm.grid()
# Мы пишем таймер

# часы
hours_label = ttk.Label(frm, text="00")
hours_label.grid(column=0, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)

# минуты
minutes_label = ttk.Label(frm, text="00")
minutes_label.grid(column=2, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)

# секунды
seconds_label = ttk.Label(frm, text="00")
seconds_label.grid(column=4, row=0)

# кнопка стоп
Button(text="Stop",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=stop_timer,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
       ).grid(column=3, row=1)

# кнопка старт
Button(text="Start",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=start_new_thread,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
       ).grid(column=1, row=1)

# кнопка reset
Button(text="Reset",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=reset_timer,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
       ).grid(column=2, row=1)

# ttk.Label(frm, text="Any").grid(column=0, row=1)
# ttk.Label(frm, text="Alex").grid(column=1, row=1)
# ttk.Label(frm, text="Ivan").grid(column=2, row=1)

# 0    1    2     3    4      5
# 1   Any    :   Alex  :     Ivan


# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# print_to_console("something")

root.mainloop()
