import random
import string
import tkinter as tk


def generate_password():
    password_length = length_var.get()

    if password_length.isdigit() and int(password_length) > 0:
        password_length = int(password_length)
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        result_var.set("Generated Password: " + generated_password)
    else:
        result_var.set("Invalid input. Please enter a positive integer.")


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input field and label for password length
length_var = tk.StringVar()
length_label = tk.Label(root, text="Enter Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create label to display the generated password
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
