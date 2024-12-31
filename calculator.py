import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(event): 
    # Get the current value in the entry widget
    current = value_entry.get()
   
    # Get the text of the button clicked
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current)
            value_entry.delete(0, tk.END)
            value_entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            value_entry.delete(0, tk.END)

    elif button_text == "AC":
        value_entry.delete(0, tk.END)

    elif button_text == "DEL":
        value_entry.delete(len(current) - 1, tk.END)

    else:
        value_entry.insert(tk.END, button_text)

# Function to create the calculator
def calculator(button_click, root):
    
    # Create a frame for buttons
    buttons = [
    'AC', '/', '%', 'DEL',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '00', '='
]

    button_frame = tk.Frame(root, bg="grey")
    button_frame.pack()
    row = 1
    col = 0
    # Create buttons
    for button_text in buttons:
        
        if col == 3 or row == 1:
            button = tk.Button(button_frame, text=button_text, font=("Times New Roman", 15, "bold"), width=6, height=3, bg="black", fg="white")
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Button-1>", button_click)
            col += 1
        else:
            button = tk.Button(button_frame, text=button_text, font=("Times New Roman", 15, "bold"), width=6, height=3)
            button.bind("<Button-1>", button_click)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
        if col > 3:
            col = 0
            row += 1
    # Changing the color according to the button 
    for button in button_frame.winfo_children():
        if button.cget("text") == "AC":
            button.configure(bg="dodgerblue1")

        elif button.cget("text") == "DEL":
            button.configure(bg="#DCDCDC", fg="black")

        elif button.cget("text") == "=":
            button.configure(bg="darkorange1")
           
root = tk.Tk()
root.geometry("380x565")
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")
root.configure(bg="grey")

# Create an entry widget
entry_frame = tk.Frame(root, bg="grey")
entry_frame.pack(fill="x")

value_entry = tk.Entry(entry_frame, font=("Times New Roman", 35), borderwidth=2, relief="solid")
value_entry.pack(fill="x", ipadx=8, padx=10, pady=10)

# Call the calculator function
calculator(button_click, root)

root.mainloop()