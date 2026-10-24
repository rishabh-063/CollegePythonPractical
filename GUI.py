import tkinter as tk
from tkinter import messagebox
def show_message():
    name = name_entry.get().strip()
    if name:
        messagebox.showinfo("Message", f"Hello, {name}!")
    else:
        messagebox.showwarning("Warning", "Please enter your name.")
root = tk.Tk()
root.title("Student Form")
root.geometry("300x150")

tk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=15)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=15)
tk.Button(root, text="Submit", command=show_message).grid(row=1, column=1, pady=10)
root.mainloop()