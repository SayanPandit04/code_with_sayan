import tkinter as tk
from tkinter import messagebox

# Function to generate Fibonacci sequence
def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        fib_sequence = [0, 1]

        for i in range(2, n):
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)

        result_label.config(text="Fibonacci Series: " + ", ".join(map(str, fib_sequence[:n])))
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Function to clear the input and result
def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Fibonacci Series Generator")
root.geometry("500x350")
root.config(bg='#2C3E50')  # Dark background for a modern look

# Styling the widgets
label_style = {'bg': '#2C3E50', 'fg': '#ECF0F1', 'font': ('Helvetica', 14, 'bold')}
button_style = {
    'bg': '#1ABC9C', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'),
    'relief': 'flat', 'activebackground': '#16A085', 'cursor': 'hand2',
    'bd': 0, 'highlightthickness': 0
}
entry_style = {'bg': '#ECF0F1', 'fg': '#2C3E50', 'font': ('Helvetica', 12), 'bd': 2, 'relief': 'solid'}

# Create and place widgets
title_label = tk.Label(root, text="Fibonacci Series Generator", **label_style)
title_label.pack(pady=20)

entry_label = tk.Label(root, text="Enter number of terms:", **label_style)
entry_label.pack()

entry = tk.Entry(root, width=15, **entry_style)
entry.pack(pady=10)

# Use a Frame to hold buttons and allow better layout control
button_frame = tk.Frame(root, bg='#2C3E50')
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="Generate", command=generate_fibonacci, **button_style)
generate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_input, **button_style)
clear_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", bg='#2C3E50', fg='#ECF0F1', font=('Helvetica', 12, 'italic'), wraplength=450)
result_label.pack(pady=20)

# Make buttons rounded by using custom padding
generate_button.config(width=10, height=2)
clear_button.config(width=10, height=2)

# Start the main loop
root.mainloop()