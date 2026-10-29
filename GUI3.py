# Develop a calculator using Tkinter

import tkinter as tk
def calc(op):
    try:
        a =float(e1.get())
        b=float(e2.get())
        r={"+": a + b, "-": a - b, "*": a * b, "/": a / b }[op]
        out.config(text=f"Result: {r}")
    except ZeroDivisionError:
        out.config(text="Error: Division by zero")
    except ValueError:
        out.config(text="Error: Invalid input")
root = tk.Tk()
root.geometry("300x200")
root.title("Simple Calculator")
e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()
for op in ["+", "-", "*", "/"]:
    tk.Button(root, text=op, command=lambda op=op: calc(op)).pack()
out = tk.Label(root, text="Result: ")
out.pack()
root.mainloop()