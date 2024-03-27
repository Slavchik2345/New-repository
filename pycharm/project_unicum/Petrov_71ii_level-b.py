import tkinter as tk

def on_enter(event):
    label.config(text="Hello World!")

root = tk.Tk()
root.geometry("350x400")
label = tk.Label(root, text="")
label.pack()
root.bind('<Return>', on_enter)

root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry("350x400")
root.title("калькулятор")

def summa():
    s = int(entry1.get()) + int(entry2.get())
    result.config(text=str(s))

def subtraction():
    s = float(entry1.get()) - float(entry2.get())
    result.config(text=str(s))

label1 = tk.Label(root, text="x1:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="x2:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

button1 = tk.Button(root, text = "+", command=summa)
button1.grid(row=2, column=0)

button1 = tk.Button(root, text = "-", command=subtraction)
button1.grid(row=2, column=2)

result = tk.Label(root, text="Результат:")
result.grid(row=3, column=0, columnspan=2)


root.mainloop()



import tkinter as tk
import random

def circle(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-10, y-10, x+10, y+10)

root = tk.Tk()
root.title("круг по клику")

canvas = tk.Canvas()
canvas.pack()

canvas.bind("<Button>", circle)

root.mainloop()