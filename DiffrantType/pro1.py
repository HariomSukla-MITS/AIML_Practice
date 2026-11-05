import tkinter as tk

def press_key(char):
    current = display_var.get()
    if current == "Error":
        display_var.set(char)
    else:
        display_var.set(current + str(char))

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        # Format floating points nicely
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Error")
    except Exception:
        display_var.set("Error")

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.configure(bg="#22252D")
root.resizable(False, False)

display_var = tk.StringVar()

# Display Screen
screen = tk.Entry(
    root, 
    textvariable=display_var, 
    font=("Arial", 24), 
    bg="#292D36", 
    fg="#FFFFFF", 
    bd=0, 
    justify="right", 
    insertbackground="white"
)
screen.pack(fill=tk.BOTH, ipadx=8, ipady=25, padx=15, pady=15)

# Button Layout Matrix
buttons = [
    ('C', 1, 0, '#FF5757'), ('/', 1, 3, '#FF9F0A'),
    ('7', 2, 0, '#292D36'), ('8', 2, 1, '#292D36'), ('9', 2, 2, '#292D36'), ('*', 2, 3, '#FF9F0A'),
    ('4', 3, 0, '#292D36'), ('5', 3, 1, '#292D36'), ('6', 3, 2, '#292D36'), ('-', 3, 3, '#FF9F0A'),
    ('1', 4, 0, '#292D36'), ('2', 4, 1, '#292D36'), ('3', 4, 2, '#292D36'), ('+', 4, 3, '#FF9F0A'),
    ('0', 5, 0, '#292D36'), ('.', 5, 2, '#292D36'), ('=', 5, 3, '#4CAF50')
]

# Button Grid Container
btn_frame = tk.Frame(root, bg="#22252D")
btn_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Configure grid weights for responsive button resizing
for i in range(6):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

# Render Buttons
for (text, row, col, bg_color) in buttons:
    fg_color = "#FFFFFF"
    
    # Assign specific actions
    if text == 'C':
        cmd = clear_display
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda x=text: press_key(x)
        
    # Handle the '0' spanning multiple columns
    colspan = 2 if text == '0' else 1
    
    btn = tk.Button(
        btn_frame, text=text, font=("Arial", 16, "bold"),
        bg=bg_color, fg=fg_color, bd=0, activebackground="#444",
        activeforeground="white", command=cmd
    )
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)

root.mainloop()
