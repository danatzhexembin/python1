from tkinter import *
from tkinter import ttk

result = "Все работает хорошо"


def print_to_console():
    print(result)


# def start_new_thread():
#     Thread(
#         target=print_to_console
#     ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
#     # будет виснуть


# инициализация инстанса - создание объекта ткинтер
root = Tk()

# создание главного окна
frm = ttk.Frame(root, padding=100)
root.title("Заголовок окна программы")
root.geometry("400x200")
frm.grid()

# кнопка стоп
Button(text="Это кнопка",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=print_to_console,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
       ).grid(column=2, row=0)

root.mainloop()
