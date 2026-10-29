# Develop a GUI using Label, Entry and Button widgets in Tkinter

import tkinter as tk
root = tk.Tk()
root.geometry("300x150")
root.title("Basic GUI")
tk.Label(root, text="Enter your name:").pack()
e= tk.Entry(root)
e.pack()
def greet():
    tk.Label(root, text=f"Hello, {e.get()}!").pack()
tk.Button(root, text="Greet", command=greet).pack()
root.mainloop()