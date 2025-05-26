import tkinter as tk
from tkinter import ttk

def save_task():
    event = entry_event.get().strip()
    priority = priority_var.get()
    if event:  # Only save if event is not empty
        tasks.append((event, priority))
        update_task_list()
        entry_event.delete(0, tk.END)  # Clear entry
        priority_var.set("Low")  # Reset priority dropdown

def update_task_list():
    # Clear the listbox
    listbox_tasks.delete(0, tk.END)
    # Insert all tasks
    for idx, (event, priority) in enumerate(tasks, start=1):
        listbox_tasks.insert(tk.END, f"{idx}. {event} [{priority}]")

tasks = []

root = tk.Tk()
root.title("TODO List")

# Event label and entry
tk.Label(root, text="Event:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_event = tk.Entry(root, width=40)
entry_event.grid(row=0, column=1, padx=5, pady=5)

# Priority label and dropdown
tk.Label(root, bg="blue",text="Priority:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
priority_var = tk.StringVar(value="Medium")
priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"], state="readonly", width=37)
priority_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Save button
btn_save = tk.Button(root, text="Save",bg="red", command=save_task)
btn_save.grid(row=2, column=0, columnspan=2, pady=10)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=60, height=10)
listbox_tasks.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

