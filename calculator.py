import tkinter as tk
from tkinter import messagebox


def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")


entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)  
]


for (text, row, column) in button_layout:
    if text == '=':
        button = tk.Button(root, text=text, padx=30, pady=20, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=30, pady=20, command=clear)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=column)


root.mainloop()
