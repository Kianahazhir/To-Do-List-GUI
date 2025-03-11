import tkinter as tk
import json
from tkinter import messagebox
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
        save_tasks(tasks)
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")
save_tasks(tasks)
def clear_list():
    listbox.delete(0, tk.END)
    save_tasks(tasks)
tasks = load_tasks()

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
