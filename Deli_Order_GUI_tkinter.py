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
# Defines the frames and packs them
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_form.pack(side=tk.LEFT)
frame_entry = tk.Frame(relief=tk. RAISED, borderwidth=1)
frame_entry.pack(side=tk.TOP)
"""
Creates a new frame `frame_buttons` to contain the
Submit button. This frame fills the 
window in the horizontal direction and has
5 pixels of horizontal and vertical padding.
"""
frame_buttons = tk.Frame()
frame_buttons.pack(side=tk.BOTTOM, fill=tk.X, ipadx=5, ipady=5)
# options for meatOptionMenu
meatOptions = [
        "Ham",
        "Turkey",
        "Chicken",
        "Pastrami",
        "Salami"
]
cheeseOptions = [
        "White American",
        "Yellow American",
        "Sharp",
        "Cobly",
        "Smoked"
]
# datatype of menu text
clickedMeat = tk.StringVar()
  
# initial menu text
clickedMeat.set( "Ham" )

# datatype of menu text
clickedCheese = tk.StringVar()
  
# initial menu text
clickedCheese.set( "White American" )

def List():
    
    # Create the Label and Entry for Meat
    labelMeat = tk.Label(master=frame_form, text="Meat:")
    entryMeat = tk.OptionMenu(frame_form, clickedMeat, *meatOptions)
    # Places the Label and Entry in the first row
    labelMeat.grid(row=0, column=0, sticky="e")
    entryMeat.grid(row=0, column=1)
    

    # Create the Label and Entry for Meat Width
    label_meat_width = tk.Label(master=frame_form, text="Meat Width (in):")
    entry_meat_width = tk.Entry(master=frame_form, width=50)
    # Place the Label and Enrey in the second row
    label_meat_width.grid(row=1, column=0, sticky="e")
    entry_meat_width.grid(row=1, column=1)

    # Create the Label and Entry for Meat Weight
    label_meat_weight = tk.Label(master=frame_form, text="Meat Weight (lbs):")
    entry_meat_weight = tk.Entry(master=frame_form, width=50)
    # Place the Label and Entry in the third row
    label_meat_weight.grid(row=2, column=0, sticky="e")
    entry_meat_weight.grid(row=2, column=1)

    # Create the Label and Entry for Cheese
    labelCheese = tk.Label(master=frame_form, text="Cheese:")
    entryCheese = tk.OptionMenu(frame_form, clickedCheese, *cheeseOptions)
    # Place the Label and Entry in the fourth row
    labelCheese.grid(row=3, column=0, sticky=tk.E)
    entryCheese.grid(row=3, column=1)

    # Create the Label and Entry for Cheese Width
    label_cheese_width = tk.Label(master=frame_form, text="Cheese Width (in):")
    entry_cheese_width = tk.Entry(master=frame_form, width=50)
    # Place the Label and Entry in the fifth row
    label_cheese_width.grid(row=4, column=0, sticky=tk.E)
    entry_cheese_width.grid(row=4, column=1)

    # Create the Label and Entry for Cheese Weight
    label_cheese_weight = tk.Label(master=frame_form, text="Cheese Weight:")
    entry_cheese_weight = tk.Entry(master=frame_form, width=50)
    # Place the Label and Entry in the sixth row
    label_cheese_weight.grid(row=5, column=0, sticky=tk.E)
    entry_cheese_weight.grid(row=5, column=1)

    # Create the Label and Entry for Name for Order
    label_order_name = tk.Label(master=frame_form, text="Name for Order:")
    entry_order_name = tk.Entry(master=frame_form, width=50)
    # Place the Label and Entry in the seventh row
    label_order_name.grid(row=6, column=0, sticky=tk.E)
    entry_order_name.grid(row=6, column=1)

    # Create the Label and Entry widgets for Price
    labelPrice = tk.Label(master=frame_form, text="Price:")
    entryPrice = tk.Entry(master=frame_form, width=50)
    # Place the Label and Entry in the eigth row
    labelPrice.grid(row=7, column=0, sticky=tk.E)
    entryPrice.grid(row=7, column=1)
List()
"""
Creates the "Submit" button and pack it to the
right side of `frame_buttons`
"""
button_submit = tk.Button(master=frame_buttons, text="Submit")
button_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Defines the event for the interaction with the submit button
##def handle_click(event):
##    listLoop()
# Binds the submit button to event
##button_submit.bind("<Button-1>", handle_click)

# Start the application
Window.mainloop()
