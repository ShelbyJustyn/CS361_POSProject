import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

class Shopping_Cart():
    def __init__(self):
        self.cart = []
        self.total = 0
        self.size = 0
    
    def add(self, item):
        if item not in (x[0] for x in self.cart):
            self.cart.append([item, 1])
            self.size += 1
        else:
            self.cart[[x[0] for x in self.cart].index(item)][1] += 1
        self.total += item.price
        self.cart.sort(key = lambda x: x[0].price * x[1], reverse=True)
        return True

    def remove(self, item):
        if item in self.cart():
            self.cart.remove(item)
            self.total -= item.price
            self.size -= 1
            return True
        return False
    
class Product():

    def __init__(self, name: str, sku: int, price: float, quantity: int):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity

class Shopping_Cart_App():
    def __init__(self, master, shopping_cart):
        self.master = master
        self.shopping_cart = shopping_cart
        self.page = 0
        self._reload(self.master, self.shopping_cart)

    def _reload(self, master, shopping_cart):
        frame = tk.Frame(master=master, relief=tk.GROOVE, borderwidth=2)
        title = tk.Label(master=frame, text="Shopping Cart").pack()
        header = shopping_cart_item(frame, "Item", "Qty", "Price", borderwidth=1).pack()
        items_frame = tk.Frame(master=frame, background="pink", height=1)
        for i, item in enumerate(shopping_cart.cart[14 * self.page:14 * self.page + 14]):
            shopping_cart_item(items_frame, item[0].name, item[1], f"{item[0].price*item[1]:.2f}").grid(column=0, row=i)
        page_buttons = tk.Frame(master=frame)
        left_button = tk.Button(master=page_buttons, text="<", width="2", height="1", relief=tk.RAISED, borderwidth=1, command=self.dec_page).pack(side=tk.LEFT)
        button_label = tk.Label(master=page_buttons, text=f"Page {self.page + 1}/{shopping_cart.size // 14 + 1}", width=5).pack(side=tk.LEFT)
        right_button = tk.Button(master=page_buttons, text=">", width="2", height="1", relief=tk.RAISED, borderwidth=1, command=self.inc_page).pack(side=tk.LEFT)
        total_frame = tk.Frame(master=frame, relief=tk.GROOVE, borderwidth=1)
        total_label = tk.Label(master=total_frame, text="Total", width=30, height=2).grid(row=0, column=0)
        total = tk.Label(master=total_frame, text=f"${round(shopping_cart.total, 2)}", width=10, height=2).grid(row=0, column=1)
        items_frame.pack()
        total_frame.pack(side=tk.BOTTOM)
        page_buttons.pack(side=tk.BOTTOM)
        self.frame = frame
        self.frame.grid(row=1, column=0, sticky="nsw", padx="3", pady="3")

    def inc_page(self):
        if self.page < shopping_cart.size // 14:
            self.page += 1
            self.reload()

    def dec_page(self):
        if self.page - 1 >= 0:
            self.page -= 1
            self.reload()

    def reload(self):
        self.frame.destroy()
        self._reload(self.master, self.shopping_cart)
    
def shopping_cart_item(master_frame, item, qty, price, borderwidth=0):
    frame = tk.Frame(master=master_frame, relief=tk.GROOVE, borderwidth=borderwidth)
    item = tk.Label(height="2", master=frame, text=item, width=25)
    qty = tk.Label(master=frame, text=qty, width=5)
    price = tk.Label(master=frame, text=price, width=10)
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

    shopping_cart_app = Shopping_Cart_App(root, shopping_cart)

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
    def add_to_cart(i):
        shopping_cart.add(i)
        shopping_cart_app.reload()
    for i, product in enumerate(inventory):
        product_button = tk.Button(
            text=product.name,
            width="15",
            height="5",
            master=product_grid_frame,
            relief=tk.RAISED,
            borderwidth=1,
            command=partial(add_to_cart, product)
        )
        product_button.grid(column=i % 5, row=i // 5, padx=3, pady=3)

    information_frame.grid(row=0, column=0, columnspan=2, sticky="new", padx="3", pady="3")
    shopping_cart_app.frame.grid(row=1, column=0, sticky="nsw", padx="3", pady="3")
    product_select_frame.grid(row=1, column=1, sticky="nsew", padx="3", pady="3")

    root.columnconfigure(1, weight=3)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
    
if __name__ == "__main__":
    for item in inventory:
        for i in range(1):
            add_to_cart(item)
    main()
