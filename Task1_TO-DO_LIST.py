# 📝 To-Do List using Python
# CodSoft Task 1 – Created by Tanmay Patel

import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete!")

# ✅ Function to mark a task as done
def mark_done():
    try:
        selected = listbox.curselection()
        task = listbox.get(selected)

        if task.startswith("✅ "):
            # Unmark the task
            updated_task = task.replace("✅ ", "", 1)
        else:
            # Mark as done
            updated_task = "✅ " + task

        listbox.delete(selected)
        listbox.insert(selected, updated_task)
        listbox.selection_set(selected)  # Keep it selected
    except:
        messagebox.showwarning("Mark Error", "Please select a task to mark!")


# Create main window
root = tk.Tk()
root.title("🗂️ To-Do List - Tanmay Patel")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#b4ff58")

# Heading
tk.Label(root, text="📋 My To-Do List", font=("Arial", 18, "bold"), bg="#c67a7a").pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root, bg="#7ce2b4")
frame.pack()

add_btn = tk.Button(frame, text="➕ Add Task", font=("Arial", 13), width=12, bg="#0c745f", command=add_task)
add_btn.grid(row=0, column=0, padx=10)

del_btn = tk.Button(frame, text="❌ Delete Task", font=("Arial", 13), width=12, bg="#b51313", command=delete_task)
del_btn.grid(row=0, column=1, padx=10)

done_btn = tk.Button(frame, text="✅Mark Done", font=("Arial", 13), width=26, bg="#993F7E", command=mark_done)
done_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Listbox for tasks
listbox = tk.Listbox(root, font=("Arial", 13), width=35, height=12, selectbackground="#4eb2f4")
listbox.pack(pady=20)

def on_closing():
    root.quit()     # Stop the main loop
    root.destroy()  # Close the window

root.protocol("WM_DELETE_WINDOW", on_closing)

root.protocol("WM_DELETE_WINDOW", root.quit)


# Run the app
root.mainloop()
