"""
Deli Order GUI
By Lucas Landis

This program displays a GUI interface for ordering lunchmeat and cheese.
"""
# Imports tkinter as tk
import tkinter as tk
# Window for program and its title
Window = tk.Tk()
Window.title("Deli Order")

"""
Creates a new frame `frame_form` to contain the Labels
and Entry widgets for entering the Meat and Cheese order.
"""
# Defines the frame
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Packs the frame into the window
frame_form.pack()

# Creates the list of labels
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
        Use the grid geometry manager to place the label and
        entry widgets in the row whose index is idx
        """
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)
listLoop()

"""
Creates a new frame `frame_buttons` to contain the
Submit button. This frame fills the 
window in the horizontal direction and has
5 pixels of horizontal and vertical padding.
"""
frame_buttons = tk.Frame()
frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

"""
Creates the "Submit" button and pack it to the
right side of `frame_buttons`
"""
button_submit = tk.Button(master=frame_buttons, text="Submit")
button_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Submit on click adds the price of the order to the list of labels
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

# Defines the event for the interaction with the submit button
def handle_click(event):
    listLoop()
# Binds the submit button to event
button_submit.bind("<Button-1>", handle_click)

# Start the application
Window.mainloop()
