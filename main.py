import tkinter as tk
from functools import partial

class Shopping_Cart():

    def __init__(self):
        self.cart = []
        self.total = 0
    
    def add(self, item):
        self.cart.append(item)
        print(f"Added {item.name} to cart, see?: {self.cart}")
        self.total += item.price
        return True

    def remove(self, item):
        if item in self.cart():
            self.cart.remove(item)
            self.total -= item.price
            return True
        return False
    
class Product():

    def __init__(self, name: str, sku: int, price: float, quantity: int):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
    
def shopping_cart_item(master, item, qty, price, borderwidth=0):
    frame = tk.Frame(master=master, relief=tk.GROOVE, borderwidth=borderwidth)
    item = tk.Label(height="2", master=frame, text=item, width=30)
    qty = tk.Label(master=frame, text=qty, width=5)
    price = tk.Label(master=frame, text=price, width=5)
    item.grid(row=0, column=0)
    qty.grid(row=0, column=1)
    price.grid(row=0, column=2)
    return frame

shopping_cart = Shopping_Cart()
def add_to_cart(i):
    shopping_cart.add(i)

inventory = [Product("Apple", 1, 0.99, 5),
            Product("Banana", 2, 0.25, 10),
            Product("Strawberry", 3, 1.10, 5),
            Product("Lettuce", 4, 0.35, 10),
            Product("Potato", 5, 1.50, 5),
            Product("Celery", 6, 2.80, 10),
            Product("Carrot", 7, 0.20, 5),
            Product("Orange", 8, 0.40, 8),
            Product("Avocado", 9, 1.25, 1),
            Product("Blueberry", 10, 0.10, 3)]

def main():
    root = tk.Tk()
    root.title("PoS by Justyn Shelby")
    root.geometry("1280x720")

    information_frame = tk.Frame(relief=tk.GROOVE, borderwidth=2)
    title = tk.Label(master=information_frame, text="PoS Program", height="1", font=("Arial", 25))
    title.pack()

    shoppingcart_frame = tk.Frame(relief=tk.GROOVE, borderwidth=2)
    sctitle = tk.Label(master=shoppingcart_frame, text="Shopping Cart")
    sctitle.pack(side=tk.TOP)
    # Title
    sclabel = shopping_cart_item(shoppingcart_frame, "Item", "Qty", "Price", borderwidth=1)
    sclabel.pack()
    # Items
    shoppingcartitems_frame = tk.Canvas(master=shoppingcart_frame, background="ivory")
    shoppingcartitems_frame_sb = tk.Scrollbar(shoppingcartitems_frame, orient="vertical", command=shoppingcartitems_frame.yview)
    shoppingcartitems_frame.configure(yscrollcommand=shoppingcartitems_frame_sb.set)
    shoppingcartitems_frame.pack(side=tk.TOP)
    for i, item in enumerate(shopping_cart.cart):
        shopping_cart_item(shoppingcartitems_frame, item.name, "1", item.price).grid(column=0, row=i)
    # Total
    sctotal = tk.Frame(master=shoppingcart_frame, relief=tk.GROOVE, borderwidth=1)
    sctotal_label = tk.Label(master=sctotal, text="Total", width=30, height=2)
    sctotal_price = tk.Label(master=sctotal, text=shopping_cart.total, width=10, height=2)
    sctotal_label.grid(row=0, column=0)
    sctotal_price.grid(row=0, column=1)
    #sctotal.grid(column=0, row=2)
    sctotal.pack(side=tk.BOTTOM)

    product_select_frame = tk.Frame(relief=tk.GROOVE, borderwidth=2)
    page_select_frame = tk.Frame(master=product_select_frame, relief=tk.GROOVE, borderwidth=2)
    pagstitle = tk.Label(master=page_select_frame, text="Page Selection")
    pagstitle.pack(fill="x")
    page_select_frame.pack(fill="x")
    # Products Label
    prostitle = tk.Label(master=product_select_frame, text="Product Selection")
    prostitle.pack(fill="x")
    # Products
    product_grid_frame = tk.Frame(master=product_select_frame, width="107")
    product_grid_frame.pack()
    for i, product in enumerate(inventory):
        product_button = tk.Button(
            text=product.name,
            width="15",
            height="5",
            master=product_grid_frame,
            relief=tk.RAISED,
            borderwidth=1,
            command=partial(shopping_cart.add, product)
        )
        product_button.grid(column=i % 5, row=i // 5, padx=3, pady=3)

    information_frame.grid(row=0, column=0, columnspan=2, sticky="new", padx="3", pady="3")
    shoppingcart_frame.grid(row=1, column=0, sticky="nsw", padx="3", pady="3")
    product_select_frame.grid(row=1, column=1, sticky="nsew", padx="3", pady="3")

    root.columnconfigure(1, weight=3)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
    
if __name__ == "__main__":
    for item in inventory:
        add_to_cart(item)
    main()
