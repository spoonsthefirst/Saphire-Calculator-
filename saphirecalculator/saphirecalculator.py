
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# Button click event to update the entry field with the clicked number
def button_click(number):
    current = entry.get()  # Get the current content of the entry field
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + str(number))  # Insert the clicked number into the entry field

# Button click event to clear the entry field
def button_clear():
    entry.delete(0, tk.END)  # Clear the entry field

# Button click event to delete the last character in the entry field (backspace functionality)
def button_backspace():
    entry.delete(len(entry.get()) - 1)  # Delete the last character from the entry field

# Button click event to evaluate the expression in the entry field and display the result
def button_equal():
    try:
        result = eval(entry.get())  # Evaluate the expression in the entry field
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Insert the result into the entry field
    except Exception:
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, "Error")  # Display "Error" in the entry field if an exception occurs

# Button click event to prompt the user before exiting the calculator
def exit_calculator():
    result = messagebox.askquestion("Exit Calculator", "Are you sure you want to exit?")
    if result == "yes":
        window.quit()  # Quit the main window if the user chooses "yes"



# Create the main calculator window
window = tk.Tk()
window.title("Sapphire Calculator")
window.configure(bg="#2c3e50")
window.resizable(False, False)

# Create a function to open the help/information window
def open_help_window():
    help_window = tk.Toplevel(window)
    help_window.title("Help / Information")
    help_window.configure(bg="#2c3e50")
    help_window.resizable(False, False)
    
    # Add content to the help window
    help_label = tk.Label(help_window, text="Welcome to Sapphire Calculator!\n\nThis calculator supports basic arithmetic operations.\n\nYou can use the number buttons to enter values and the operators (+, -, *, /) for calculations.\n\nPress '=' to get the result and 'C' to clear the input.\n\nYou can also use the '⌫' button for backspace functionality.")
    help_label.pack(padx=10, pady=10)




# Create a label above the calculation area
calc_label = tk.Label(window, text="Sapphire Calculator", font=("Verdana", 14), bg="#2c3e50", fg="#FFFFFF")
calc_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# Create a label above the calculation area
calc_label = tk.Label(window, text="SDEV 140 final project", font=("Verdana", 8), bg="#2c3e50", fg="#FFFFFF")
calc_label.grid(row=1, column=0, columnspan=4, pady=10, sticky="nsew")


# Load the image
image_filename = "sapphire.png"
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, image_filename)

try:
    image = Image.open(image_path)
    image = image.resize((30, 30))  # Resize the image to your desired size
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=photo)
    image_label.image = photo  # Keep a reference to the image to avoid garbage collection
    image_label.grid(row=0, column=3, columnspan=4, pady=0, sticky="nsew")
except Exception as e:
    print("Error loading image:", e)
    messagebox.showerror("Image Error", "Unable to load the image. Continuing without it.")
    

# Set custom fonts
large_font = ("Verdana", 18)
button_font = ("Verdana", 12)

# Create an entry field
entry = tk.Entry(window, width=16, borderwidth=5, font=large_font, justify=tk.RIGHT)
entry.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


# Create number buttons
buttons = [
    ['7', '8', '9', '⌫'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '+', '/']
]

number_button_color = "#98ADE6"  # Set the desired color for number buttons
button_width = 6  # Adjust the button width
button_height = 2  # Adjust the button height

# Create the number buttons and configure their appearance and functionality
for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        button_text = buttons[row][col]

        # Replace the "*" button with the multiplication symbol (×)
        if button_text == '*':
            button_text = '×'

        # Create the number button with the appropriate text and command (button_click)
        button = tk.Button(window, text=button_text, padx=10, pady=10,
                           width=button_width, height=button_height,  # Set the button width and height
                           font=button_font,  # Set button font
                           fg="#2c3e50", bg=number_button_color,  # Set foreground and background colors
                           activeforeground="#2c3e50", activebackground="#95a5a6",  # Set active colors
                           relief=tk.RAISED, bd=4,  # Set relief style and border width
                           command=lambda number=buttons[row][col]: button_click(number))  # Attach the button_click event
        button.grid(row=row+3, column=col, padx=2, pady=2, sticky="nsew")

        # Replace the "/" button with the division symbol (÷)
        if button_text == '/':
            button.configure(text="÷", command=button_click('/'))

        # Replace the "⌫" button with the backspace functionality (button_backspace)
        if button_text == '⌫':
            button.configure( command=button_backspace)
           

# Create the clear button and configure its appearance and functionality (button_clear)
clear_button = tk.Button(window, text='C', padx=10, pady=10,
                         font=button_font,  # Set button font
                         fg="#2c3e50", bg="#FF9184",  # Set foreground and background colors
                         activeforeground="#2c3e50", activebackground="#c0392b",  # Set active colors
                         relief=tk.RAISED, bd=4,  # Set relief style and border width
                         command=button_clear)  # Attach the button_clear event
clear_button.grid(row=len(buttons) + 3, column=0, padx=2, pady=2, sticky="nsew")

# Create the equal button and configure its appearance and functionality (button_equal)
equal_button = tk.Button(window, text='=', padx=10, pady=10,
                         font=button_font,  # Set button font
                         fg="#2c3e50", bg="#64E64A",  # Set foreground and background colors
                         activeforeground="#2c3e50", activebackground="#229954",  # Set active colors
                         relief=tk.RAISED, bd=4,  # Set relief style and border width
                         command=button_equal)  # Attach the button_equal event
equal_button.grid(row=len(buttons) + 3, column=1, columnspan=2, padx=2, pady=2, sticky="nsew")

# Add a help button to the main calculator window
help_button = tk.Button(window, text='Help', padx=10, pady=10,
                        font=("Verdana", 12),
                        fg="#2c3e50", bg="#FFD700",
                        activeforeground="#2c3e50", activebackground="#FFD700",
                        relief=tk.RAISED, bd=4,
                        command=open_help_window)
help_button.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

# Create the exit button and configure its appearance and functionality (exit_calculator)
exit_button = tk.Button(window, text='Exit', padx=10, pady=10,
                        font=button_font,  # Set button font
                        fg="#2c3e50", bg="#FF0000",  # Set foreground and background colors
                        activeforeground="#2c3e50", activebackground="#c0392b",  # Set active colors
                        relief=tk.RAISED, bd=4,  # Set relief style and border width
                        command=exit_calculator)  # Attach the exit_calculator event
exit_button.grid(row=len(buttons) + 3, column=3, padx=2, pady=2, sticky="nsew")

# Configure row and column weights for resizing
for i in range(len(buttons) + 2):
    window.rowconfigure(i, weight=1)
for i in range(4):
    window.columnconfigure(i, weight=1)

# Set the buttons' relief style to flat
for widget in window.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(relief=tk.FLAT)


# Start the Tkinter event loop
window.mainloop()
