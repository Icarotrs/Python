import tkinter as tk
from math import sin, cos, tan, log, exp, pi

def calculate():
    expression = input_field.get()
    try:
        result = eval(expression)
        output_field.config(state='normal')
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, result)
        output_field.config(state='disabled')
    except:
        output_field.config(state='normal')
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, "Error")
        output_field.config(state='disabled')

root = tk.Tk()
root.title("Calculadora Científica")

input_field = tk.Entry(root)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=70)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    '7', '8', '9', '*', 'sin',
    '4', '5', '6', '/', 'cos',
    '1', '2', '3', '-', 'tan',
    '.', '0', '=', '+', 'log',
    'pi', 'exp', '^2', '^3', '^'
]

r = 0
c = 0
for button_text in button_list:
    button = tk.Button(button_frame, text=button_text, width=5, height=2, command=lambda text=button_text: input_field.insert(tk.END, text))
    button.grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

output_field = tk.Text(root, height=2, width=20)
output_field.grid(row=2, column=0, columnspan=4)
output_field.config(state='disabled')

root.mainloop()
