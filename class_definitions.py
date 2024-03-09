import tkinter as tk
from functools import partial

class Shopping_Cart_Item():

    def __init__(self, sku, name, qty, price):
        self.sku = sku
        self.name = name
        self.qty = qty
        self.price = price

class Product():

    def __init__(self, name: str, sku: int, price: float, qty: int):
        self.name = name
        self.sku = sku
        self.price = price
        self.qty = qty

class Shopping_Cart():

    def __init__(self):
        self.cart = []
        self.total = 0
        self.size = 0
    
    def add(self, item):
        if item.sku not in (x.sku for x in self.cart):
            self.cart.append(Shopping_Cart_Item(item.sku, item.name, 1, item.price))
            self.total += item.price
            self.size += 1
        else:
            shopping_cart_item = self.cart[[x.sku for x in self.cart].index(item.sku)]
            shopping_cart_item.qty += 1
            self.total += shopping_cart_item.price
        self.cart.sort(key = lambda x: x.price * x.qty, reverse=True)

    def remove(self, item):
        if item in self.cart():
            self.cart.remove(item)
            self.total -= item.price
            self.size -= 1

    def update(self, difference):
        self.total += difference
        self.cart.sort(key = lambda x: x.price * x.qty, reverse=True)

    def clear(self):
        self.__init__()

def startup_popup(root):
    popup = tk.Toplevel(root)
    popup.geometry("1280x360")
    popup.title = ("Welcome!")
    tk.Label(popup, text="Welcome to a simple point of sale program by Justyn Shelby\n\n \
            This program allows you to select available items,\n total them up, and complete and log a sale!", 
            font=("Arial", 36)).pack()
    tk.Label(popup, text="\n\nCurrent features include product selection and automated shopping cart",
             font=("Arial", 18)).pack()
    
def help_popup(root):
    popup = tk.Toplevel(root)
    popup.geometry("720x360")
    popup.title = ("Help")
    tk.Label(popup, text="Help Guide", font=("Arial", 36)).pack()
    tk.Label(popup, text="\nTo use the product selection section:\nSelect a product to add it to the cart").pack()
    tk.Label(popup, text="\nTo use the shopping cart section:\nSelect the quantity of an item to edit it\nChange the quantity to 0 to remove it from the cart\nThe total and shopping cart order is automatically updated").pack()
    tk.Label(popup, text="\nStep by Step guide to complete a transaction:\nSelect all requested items from the product selection panel\nEnsure all items and quantities are correct\nSelect the complete sale button to finalize the transaction (to be implemented)").pack()
    