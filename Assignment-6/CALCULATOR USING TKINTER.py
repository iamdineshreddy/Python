import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Button click function
def button_click(value):
    entry.insert(tk.END, value)

# Clear function
def clear_entry():
    entry.delete(0, tk.END)

# Calculate result with error handling
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed")
        clear_entry()
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear_entry()

# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    if button == "=":
        tk.Button(frame, text=button, width=8, height=2,
                  font=("Arial", 14), command=calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
        col += 1
    else:
        tk.Button(frame, text=button, width=5, height=2,
                  font=("Arial", 14),
                  command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", width=28, height=2,
          font=("Arial", 14), command=clear_entry).pack(pady=10)

# Run application
root.mainloop()
