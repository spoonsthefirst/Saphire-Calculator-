import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry field
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        button = tk.Button(window, text=buttons[row][col], padx=40, pady=20,
                           command=lambda number=buttons[row][col]: button_click(number))
        button.grid(row=row+1, column=col)

# Create the clear button
clear_button = tk.Button(window, text='C', padx=40, pady=20, command=button_clear)
clear_button.grid(row=len(buttons) + 1, column=0)

# Create the equal button
equal_button = tk.Button(window, text='=', padx=88, pady=20, command=button_equal)
equal_button.grid(row=len(buttons) + 1, column=1, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
