# Develop a form with validation and event handling using Tkinter

import tkinter as tk
from tkinter import messagebox
def submit():
    name = e1.get()
    email = e2.get()
    if not name or not email:
        messagebox.showerror("Error", "All fields are required")
    else:
        messagebox.showinfo("Success", f"Submitted: {name}, {email}")
root = tk.Tk()
root.geometry("300x200")
root.title("Form with Validation")
tk.Label(root, text="Name:").pack()
e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()
tk.Button(root, text="Submit", command=submit).pack()
root.mainloop()