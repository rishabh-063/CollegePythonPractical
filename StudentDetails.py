import tkinter as tk

def submit_details():
    # Retrieve data from input widgets
    student_name = entry_name.get()
    student_id = entry_id.get()
    gender = gender_var.get()
    
    # Clear the text area and insert the captured information
    display_area.delete(1.0, tk.END)
    display_text = f"--- Student Information ---\nID: {student_id}\nName: {student_name}\nGender: {gender}"
    display_area.insert(tk.END, display_text)

# Main Window Setup
root = tk.Tk()
root.title("Student Data Entry")

# Input Fields (Labels and Entries)
tk.Label(root, text="Student ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Student Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# Radio Buttons for Gender
gender_var = tk.StringVar(value="Male")
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=60, sticky="w")

# Submit Button
tk.Button(root, text="Submit", command=submit_details).grid(row=3, column=0, columnspan=2, pady=10)

# Display Area
display_area = tk.Text(root, height=6, width=35)
display_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()