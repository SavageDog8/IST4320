

import tkinter as tk
import pyperclip  # Importing pyperclip for clipboard operations
from tkinter import messagebox
import random
from enum import Enum

# Define Enumeration class for Character Type
class CharacterType(Enum):
    """Enumeration class for character type."""
    ZERO = 0
    ONE = 1
    SPACE = 2
    SPECIAL = 3

class MatrixScreen:
    """Class to create a Matrix-like screen using tkinter."""

    def __init__(self, master, update_interval=500, line_length=189):
        """
        Initializes the MatrixScreen class with master window, update_interval and line_length parameters.
        
        Args:
            master (tk.Tk): The main application window.
            update_interval (int): The time interval for screen updates.
            line_length (int): The number of characters in each line on the screen.
        """
        self.master = master
        self.line_length = line_length
        self.update_interval = update_interval

        # Create a frame for the Matrix display
        self.matrix_frame = tk.Frame(self.master, bg="black")
        self.matrix_frame.place(relwidth=1, relheight=1)

        # Create the Matrix display
        self.matrix_display = tk.Text(
            self.matrix_frame,
            bg="black",
            fg="gold",
            font=("Lucida Fax", 12),
            wrap=tk.WORD,
            padx=10,
            pady=10,
            bd=0,
            highlightthickness=0
        )
        self.matrix_display.pack(expand=True, fill=tk.BOTH)

        # Set the update interval
        self.special_characters = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]
        self.update_matrix()

    def random_char(self):
        """Returns a random character: '0', '1', ' ' or a special character."""
        choice = CharacterType(random.randint(0, 3))
        if choice == CharacterType.ZERO:
            return '0'
        elif choice == CharacterType.ONE:
            return '1'
        elif choice == CharacterType.SPACE:
            return ' '
        else:
            return random.choice(self.special_characters)

    def update_matrix(self):
        """Updates the Matrix display and schedules the next update."""
        # Generate new line
        new_line = ''.join([self.random_char() for _ in range(self.line_length)])
        self.matrix_display.insert(tk.END, new_line + '\n')
        self.matrix_display.see(tk.END)

        # Schedule the next update
        self.master.after(self.update_interval, self.update_matrix)

# Function to print keys by their values (indices)
def print_keys_by_value(value, alphaDict):
    keys = [key for key, indices in alphaDict.items() if value in indices]
    return keys

# Function to get combined keys based on some conditions
def value_of_s(alphaDict):
    combined_keys_string1 = ""  
    combined_keys_string2 = ""  
    combined_keys_string3 = ""
    combined_keys_string4 = ""
    combined_keys_string5 = ""
    combined_keys_string6 = ""
    combined_keys_string7 = ""
    combined_keys_string8 = ""
    combined_keys_string9 = ""
    combined_keys_string10 = ""
    combined_keys_string11 = ""
    combined_keys_string12 = ""
    
    for key, indices in alphaDict.items():
  

        if 4 in indices:
            combined_keys_string1 = ''.join(print_keys_by_value(1, alphaDict) + print_keys_by_value(2, alphaDict) + print_keys_by_value(3, alphaDict) + print_keys_by_value(4, alphaDict))
            combined_keys_string2 = ''.join(print_keys_by_value(2, alphaDict) + print_keys_by_value(1, alphaDict) + print_keys_by_value(4, alphaDict) + print_keys_by_value(3, alphaDict))
            combined_keys_string3 = ''.join(print_keys_by_value(3, alphaDict) + print_keys_by_value(4, alphaDict) + print_keys_by_value(1, alphaDict) + print_keys_by_value(2, alphaDict))
            
    whole_set = (combined_keys_string1, combined_keys_string2, combined_keys_string3, combined_keys_string4, 
                 combined_keys_string5, combined_keys_string6, combined_keys_string7, combined_keys_string8,
                 combined_keys_string9,combined_keys_string10,combined_keys_string11,combined_keys_string12)

    filtered_set = tuple(key for key in whole_set if key != "")
    capitalized_set = tuple(key.capitalize() for key in filtered_set)
        
    return capitalized_set

# Function to handle user input and display result
def submit_input(event=None):  # Allow for event parameter to handle key binding
    s = entry.get()  # Get the input from the entry widget
    if s.lower() == 'q':  # Check for the quit command
        root.quit()  # Exit the application

    # Create a dictionary to store character occurrences for each input
    alphaDict = {}
    for index, char in enumerate(s):
        if char not in alphaDict:
            alphaDict[char] = []  # Initialize the list if the character is not already a key
        alphaDict[char].append(index + 1)  # Append the 1-based index to the list

    # Call the function and save the result
    result = value_of_s(alphaDict)
    formatted_output = ', '.join(result)  # Format the output
    
    # Display the result in the label
    result_label.config(text=f'{formatted_output}')  # Update the result label

# Function to copy the result to the clipboard
def copy_result():
    result_text = result_label.cget("text")  # Get the current text from the result label
    if result_text:
        pyperclip.copy(result_text)  # Copy the text to the clipboard
        #messagebox.showinfo("Copied", "The result has been copied to the clipboard.")  # Show a message box

# Set up the main window
root = tk.Tk()
root.title("Permutation  generate")


# Calculate the center position for the window
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Centering the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create an instance of the MatrixScreen class
matrix_screen = MatrixScreen(root)

# Create and place the input entry
entry = tk.Entry(root, width=50)
entry.pack(pady=50)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_input)
submit_button.pack(pady=10)

# Create and place the copy button
copy_button = tk.Button(root, text="Copy Result", command=copy_result)
copy_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=50)

# Bind the Enter key to the submit_input function
root.bind('<Return>', submit_input)

# Start the Tkinter event loop
root.mainloop()