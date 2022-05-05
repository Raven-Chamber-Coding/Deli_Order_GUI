"""
Deli Order GUI
By Lucas Landis

This program displays a GUI interface for ordering lunchmeat and cheese.
"""
# Imports tkinter as tk
import tkinter as tk
# Window for program
Window = tk.Tk()
Window.title("Deli Order")

"""
Creates a new frame `frame_form` to contain the Labels
and Entry widgets for entering a Meat and Cheese order.
"""
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Packs the frame into the window
frame_form.pack()

# List of labels
labels = [
    "Meat:",
    "Meat Width (in):",
    "Meat Weight (lbs):",
    "Cheese:",
    "Cheese Width (in):",
    "Cheese Weight (lbs):",
    "Name for Order:",
]

# Loop over the list of labels
def listLoop():
    for idx, text in enumerate(labels):
        # Creates a Label widget with the text from the labels list
        label = tk.Label(master=frame_form, text=text)
        # Creates an Entry widget
        entry = tk.Entry(master=frame_form, width=50)
        """
        Use the grid geometry manager to place the Label and
        Entry widgets in the row whose index is idx
        """
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)
listLoop()

"""
Create a new frame `frame_buttons` to contain the
Submit button. This frame fills the
whole window in the horizontal direction and has
5 pixels of horizontal and vertical padding.
"""
frame_buttons = tk.Frame()
frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

"""
Create the "Submit" button and pack it to the
right side of `frame_buttons`
"""
button_submit = tk.Button(master=frame_buttons, text="Submit")
button_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Submit on click shows the price of the order
labels = [
    "Meat:",
    "Meat Width (in):",
    "Meat Weight (lbs):",
    "Cheese:",
    "Cheese Width (in):",
    "Cheese Weight (lbs):",
    "Name for Order:",
    "Total Price:"
]
def handle_click(event):
    listLoop()
    
button_submit.bind("<Button-1>", handle_click)

# Start the application
Window.mainloop()