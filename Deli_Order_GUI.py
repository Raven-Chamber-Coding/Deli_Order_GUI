"""
Deli Order GUI
By Lucas Landis

This program displays a GUI interface for ordering lunchmeat and cheese.
"""

# Imports breezypythongui for template
from breezypythongui import EasyFrame
class deliGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Meat", row = 0, column = 0)
        self.addLabel(text = "Meat Thickness(in)", row = 1, column = 0)
        self.widthMeat = self.addFloatField(value = 0.00, row = 1, column = 1, precision = 2)
        self.addLabel(text = "Weight of Meat(lbs)", row = 2, column = 0)
        self.addLabel(text = "Cheese", row = 3, column = 0)
        self.addLabel(text = "Cheese Thickness(in)", row = 4, column = 0)
        self.addLabel(text = "Weight of Cheese(lbs)", row = 5, column = 0)
        self.addLabel(text = "Your Name", row = 6, column = 0)
        self.Order = self.addButton(text = "Order", row = 7, column = 0, command = self.Order)
