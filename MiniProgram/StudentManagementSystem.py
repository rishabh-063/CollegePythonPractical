import tkinter as tk
from tkinter import messagebox
import sqlite3

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("500x500")
        
        # Initialize Database
        self.init_db()
        
        # UI Components
        tk.Label(root, text="Student ID:").grid(row=0, column=0, pady=10, padx=10)
        self.id_var = tk.StringVar()
        tk.Entry(root, textvariable=self.id_var).grid(row=0, column=1)

        tk.Label(root, text="Student Name:").grid(row=1, column=0, pady=10, padx=10)
        self.name_var = tk.StringVar()
        tk.Entry(root, textvariable=self.name_var).grid(row=1, column=1)

        tk.Label(root, text="Marks:").grid(row=2, column=0, pady=10, padx=10)
        self.marks_var = tk.StringVar()
        tk.Entry(root, textvariable=self.marks_var).grid(row=2, column=1)
        
        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="Add", command=self.add_record).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update", command=self.update_record).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_record).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Search", command=self.search_record).pack(side=tk.LEFT, padx=5)

        # Output Text Area
        self.output = tk.Text(root, height=12, width=50)
        self.output.grid(row=4, column=0, columnspan=2, padx=10)
        self.view_all()

    def init_db(self):
        self.conn = sqlite3.connect("sms.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students (id TEXT PRIMARY KEY, name TEXT, marks INTEGER)")
        self.conn.commit()

    def clear_inputs(self):
        self.id_var.set("")
        self.name_var.set("")
        self.marks_var.set("")

    def view_all(self):
        self.output.delete(1.0, tk.END)
        self.cursor.execute("SELECT * FROM students")
        for row in self.cursor.fetchall():
            self.output.insert(tk.END, f"ID: {row[0]} | Name: {row[1]} | Marks: {row[2]}\n")

    def add_record(self):
        try:
            self.cursor.execute("INSERT INTO students VALUES (?, ?, ?)", 
                                (self.id_var.get(), self.name_var.get(), int(self.marks_var.get())))
            self.conn.commit()
            self.view_all()
            self.clear_inputs()
            messagebox.showinfo("Success", "Record Added")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Student ID already exists!")

    def update_record(self):
        self.cursor.execute("UPDATE students SET name=?, marks=? WHERE id=?", 
                            (self.name_var.get(), int(self.marks_var.get()), self.id_var.get()))
        self.conn.commit()
        self.view_all()
        messagebox.showinfo("Success", "Record Updated")

    def delete_record(self):
        self.cursor.execute("DELETE FROM students WHERE id=?", (self.id_var.get(),))
        self.conn.commit()
        self.view_all()
        self.clear_inputs()
        messagebox.showinfo("Success", "Record Deleted")

    def search_record(self):
        self.cursor.execute("SELECT * FROM students WHERE id=?", (self.id_var.get(),))
        row = self.cursor.fetchone()
        if row:
            self.name_var.set(row[1])
            self.marks_var.set(row[2])
            messagebox.showinfo("Found", "Record Loaded into fields")
        else:
            messagebox.showwarning("Not Found", "No student matches this ID")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()