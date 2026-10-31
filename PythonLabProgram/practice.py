import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My First Python GUI")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

def update_greeting():
    """Updates the label text with the user's input."""
    user_name = name_entry.get()
    if user_name.strip():
        greeting_label.config(text=f"Hello, {user_name}! 👋", fg="#1a73e8")
    else:
        messagebox.showwarning("Input Error", "Please enter a name first!")

title_label = tk.Label(root, text="Welcome to the App", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter your name:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(input_frame, font=("Arial", 10))
name_entry.grid(row=0, column=1, padx=5)

greet_button = tk.Button(root, text="Greet Me", command=update_greeting, bg="#1a73e8", fg="white", font=("Arial", 10, "bold"))
greet_button.pack(pady=5)

greeting_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f0f0f0")
greeting_label.pack(pady=15)

root.mainloop()