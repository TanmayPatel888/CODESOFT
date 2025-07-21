import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6 :
            messagebox.showwarning("Invalid Length", "Password length must be at least 6 characters.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Copy password to clipboard
def copy_to_clipboard():
    password = result_var.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
window = tk.Tk()
window.title("Password Generator - by Tanmay")
window.geometry("600x400")
window.config(bg="#ea9204")

# Title
title = tk.Label(window, text="🔐 Secure Password Generator", font=("Arial", 19, "bold"), bg="#fef461")
title.pack(pady=15)

# Password length input
length_label = tk.Label(window, text="Enter password length (min 6):", font=("Arial", 17), bg="#945dc1")
length_label.pack()
length_entry = tk.Entry(window, width=10, font=("Arial", 15))
length_entry.pack(pady=7)

# Generate button
generate_button = tk.Button(window, text="Generate Password", font=("Arial", 17), command=generate_password)
generate_button.pack(pady=11)

# Output password
result_var = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_var, font=("Arial", 17), width=35, justify="center", bd=2)
result_entry.pack(pady=12)

# Copy button
copy_button = tk.Button(window, text="📋 Copy to Clipboard", font=("Arial", 15), command=copy_to_clipboard)
copy_button.pack(pady=5)

# Footer
footer = tk.Label(window, text="Built with Python & Tkinter", font=("Arial", 13), fg="gray", bg="#0b3954")

def on_closing():
    window.quit()     
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.protocol("WM_DELETE_WINDOW", window.quit)


# Start GUI loop
window.mainloop()
