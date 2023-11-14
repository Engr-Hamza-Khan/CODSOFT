import tkinter as tk

def click_button(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get()
        result = str(eval(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Create numeric keypad buttons
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: click_button(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Create operation buttons
operations = ['+', '-', '*', '/']

row_val = 1
col_val = 3

for operation in operations:
    tk.Button(root, text=operation, width=5, height=2, command=lambda o=operation: click_button(o)).grid(row=row_val, column=col_val, padx=5, pady=5)
    row_val += 1

# Clear and calculate buttons
tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=4, column=1, columnspan=5, padx=0, pady=8)

# Start the main loop
root.mainloop()
