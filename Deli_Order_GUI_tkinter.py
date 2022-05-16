"""
Deli Order GUI
By Lucas Landis

This program displays a GUI interface for ordering lunchmeat and cheese.
The program displays a form for entering meat and cheese with their width and weight.
The program also asks for the users name.
The program will then display the price of the order to the user.
The program shows a submit, quit, and check price button.

"""
# Imports tkinter as tk and Callback.py
import tkinter as tk
from tkinter import ttk
# Windows for the program and their titles
Window = tk.Tk()
Window.title("Deli Order")
# Fucntion of calling new window
def newWindow():
    endWindow = tk.Tk()
    frame_end = tk.Frame()
    frame_end.pack()
    endLabel = tk.Label(master=frame_end, text="Thank you!")
    endLabel.grid(row=0, column=1)
    endWindow.title("Thank You!")

# Callback function for validation of width and weight
def Callback(input):
    if input is float:
        print(input)
        return True
                        
    elif input == "":
        print(input)
        return True

    else:
        print(input)
        return False

"""
Creates a new frame frame_form to contain the Labels
and Entry widgets for entering the Meat and Cheese order.
"""
# Defines the frames and packs them
# frame_form is given a sunken look to distuingish it against the rest of the UI
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_form.pack(side=tk.LEFT)
"""
Creates a new frame frame_buttons to contain the
Submit button. This frame fills the 
window in the horizontal direction and has
5 pixels of horizontal and vertical padding.
"""
frame_buttons = tk.Frame()
frame_buttons.pack(side=tk.BOTTOM, fill=tk.X, ipadx=5, ipady=5)

# Dictionary for prices
Prices = {
        # Meat
        "Ham":9.99,
        "Turkey":9.99,
        "Chicken":8.99,
        "Pastrami":11.99,
        "Salami":8.99,
        # Cheese
        "White American":7.99,
        "Yellow American":7.99,
        "Sharp":7.99,
        "Cobly":7.99,
        "Smoked:":8.99
}
 
# options for meat OptionMenu
meatOptions = [
        "Ham",
        "Turkey",
        "Chicken",
        "Pastrami",
        "Salami"
]
# options for cheese OptionMenu
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

"""
Creates the class for the UI labels, entries, and buttons.
Also contains the function for checking for price and the callback for input validation.
"""
class GUI_form:

        # Function creates the lables and entry or other choice propmts
        def List():
    
                # Creates the Label and OptionMenu for Meat
                labelMeat = tk.Label(master=frame_form, text="Meat:")
                entryMeat = tk.OptionMenu(frame_form, clickedMeat, *meatOptions)
                # Places the Label and OptionMenu in the first row
                labelMeat.grid(row=0, column=0, sticky="e")
                entryMeat.grid(row=0, column=1)
    
                # Creates the Label and Entry for Meat Width
                label_meat_width = tk.Label(master=frame_form, text="Meat Width (in):")
                entry_meat_width = tk.Entry(master=frame_form, width=50)
                # Places the Label and Entry in the second row
                label_meat_width.grid(row=1, column=0, sticky="e")
                entry_meat_width.grid(row=1, column=1)

                # Creates the Label and Entry for Meat Weight
                label_meat_weight = tk.Label(master=frame_form, text="Meat Weight (lbs):")
                entry_meat_weight = tk.Entry(master=frame_form, width=50) # ways to make this field effect Price?
                # Places the Label and Entry in the third row
                label_meat_weight.grid(row=2, column=0, sticky="e")
                entry_meat_weight.grid(row=2, column=1)

                # Creates the Label and OptionMenu for Cheese
                labelCheese = tk.Label(master=frame_form, text="Cheese:")
                entryCheese = tk.OptionMenu(frame_form, clickedCheese, *cheeseOptions)
                # Places the Label and OptionMenu in the fourth row
                labelCheese.grid(row=3, column=0, sticky="e")
                entryCheese.grid(row=3, column=1)

                # Creates the Label and Entry for Cheese Width
                label_cheese_width = tk.Label(master=frame_form, text="Cheese Width (in):")
                entry_cheese_width = tk.Entry(master=frame_form, width=50)
                # Places the Label and Entry in the fifth row
                label_cheese_width.grid(row=4, column=0, sticky="e")
                entry_cheese_width.grid(row=4, column=1)

                # Creates the Label and Entry for Cheese Weight
                label_cheese_weight = tk.Label(master=frame_form, text="Cheese Weight:")
                entry_cheese_weight = tk.Entry(master=frame_form, width=50)
                # Places the Label and Entry in the sixth row
                label_cheese_weight.grid(row=5, column=0, sticky="e")
                entry_cheese_weight.grid(row=5, column=1)

                # Creates the Label and Entry for Name for Order
                label_order_name = tk.Label(master=frame_form, text="Name for Order:")
                entry_order_name = tk.Entry(master=frame_form, width=50)
                # Places the Label and Entry in the seventh row
                label_order_name.grid(row=6, column=0, sticky="e")
                entry_order_name.grid(row=6, column=1)

                # Creates the Label for Price
                labelPrice = tk.Label(master=frame_form, text="Price: $0.00")
                # Places the Label in the eigth row
                labelPrice.grid(row=7, column=0, sticky="e")
                
                # Validations for width and weight entries
                # callback validations
                Register=Window.register(Callback)
                entry_cheese_weight.config(validate ="key", validatecommand =(Register, '% P'))
        
        # function for creating buttons
        def Buttons():
                # Creates the Quit button and packs it to the right of frame_buttons
                buttonQuit = tk.Button(master=frame_buttons, text="Quit", command=Window.destroy)
                buttonQuit.pack(side=tk.RIGHT, padx=10, ipadx=10)

                # Creates the Submit button and packs it to the right side of frame_buttons
                buttonSubmit = tk.Button(master=frame_buttons, text="Submit", command=lambda: newWindow())
                buttonSubmit.pack(side=tk.RIGHT, padx=10, ipadx=10)

                # Creates the Price Check button and packs it
                buttonCheck = tk.Button(master=frame_buttons, text="Check Price", command=())
                buttonCheck.pack(side=tk.RIGHT, padx=10, ipadx=10)

        # Fucntion for finding price
        ##def Price():
                ##for word in entryMeat:
                        ##if word in Prices:
                                ##tk.alertmessagebox( Prices[word] ) 
                        ##else:
                                ##pass
        
        # calls the List function
        List()
        # Calls the Buttons function
        Buttons()
        # calls the Price function
        ##Price()

# Calls the GUI_form Class
GUI_form()

# Start the application
if __name__ == "__main__":
        Window.mainloop()
