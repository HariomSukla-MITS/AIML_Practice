import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, f"☐ {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_index)
        
        # Toggle checkmark state
        if task_text.startswith("☐"):
            new_text = task_text.replace("☐", "☑", 1)
        else:
            new_text = task_text.replace("☑", "☐", 1)
            
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, new_text)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark.")

# Main Window Setup
root = tk.Tk()
root.title("My Python Tasks")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Heading Label
title_label = tk.Label(root, text="Daily To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

# Input Field Frame
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add Task", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox & Scrollbar Frame
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
task_listbox = tk.Listbox(list_frame, font=("Arial", 12), width=35, height=12, yscrollcommand=scrollbar.set, selectbackground="#a6a6a6")

scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Action Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

done_button = tk.Button(button_frame, text="Mark Done/Undone", font=("Arial", 10, "bold"), bg="#2196F3", fg="white", command=mark_done)
done_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 10, "bold"), bg="#f44336", fg="white", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Run the Application Loop
root.mainloop()
