from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import lagged_fib_gen


def click_button():
    params_filename = params_entry.get()
    seq_length = length_entry.get()
    fib_num = fib_num_entry.get()

    params_file = None
    r = None
    s = None

    try:
        if not (".txt" in params_filename):
            raise ValueError("Неверное имя файла")

        try:
            params_file = open(params_filename, "r")
        except:
            raise FileExistsError("Не удалось открыть файл")

        try:
            data = list(map(int, params_file.read().split()))
            r, s = data[0], data[1]
        except:
            raise ValueError("Некорректное содержимое файла с параметрами")

        try:
            int(seq_length)
            if int(seq_length) <= 0:
                raise ValueError
        except:
            raise ValueError(
                "Некорректные данные в поле длины последовательности")

        try:
            int(fib_num)
            if int(fib_num) <= 0:
                raise ValueError
        except:
            raise ValueError(
                "Некорректные данные в поле с числом Фибоначчи")

    except Exception as E:
        # print(E)
        showerror("Ошибка", str(E))
        return

    params_file.close()

    seq_length = int(seq_length)
    fib_num = int(fib_num)
    r = int(r)
    s = int(s)

    lagged_fib_gen.launch(seq_length, fib_num, r, s)


root = Tk()
root.title("lagged Fibonacci generator")
root.geometry("400x400+200+150")

root.resizable(False, False)

params_label = ttk.Label(
    text="Файл с параметрами генератора", font=("Arial", 14))
params_label.pack(ipady=10)

params_entry = ttk.Entry(justify=CENTER)
params_entry.pack()

length_label = ttk.Label(
    text="Длина последовательности", font=("Arial", 14))
length_label.pack(ipady=10)

length_entry = ttk.Entry(justify=CENTER)
length_entry.pack()

fib_num_label = ttk.Label(
    text="Порядковый номер числа Фибоначчи", font=("Arial", 14))
fib_num_label.pack(ipady=10)

fib_num_entry = ttk.Entry(justify=CENTER)
fib_num_entry.pack()

btn = ttk.Button(text="Пуск", command=click_button)
btn.pack(pady=10)

root.mainloop()
