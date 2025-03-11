import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_list():
    listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create and configure widgets
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear List", command=clear_list)
listbox = tk.Listbox(root)

# Place widgets in the layout
entry.pack(pady=5)
add_button.pack()
remove_button.pack()
clear_button.pack()
listbox.pack(fill=tk.BOTH, expand=True, pady=5)

# Start the main event loop
root.mainloop()
