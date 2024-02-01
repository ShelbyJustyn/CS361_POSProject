import tkinter as tk
from functools import partial

class Shopping_Cart():

    def __init__(self):
        self.cart = []
    
    def add(self, item):
        self.cart.append(item)
        print(f"Added {item} to cart, see?: {self.cart}")
        return True

    def remove(self, item):
        if item in self.cart():
            self.cart.remove(item)
            return True
        return False
    
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
    print(i, shopping_cart.cart)

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
    shoppingcartitems_frame = tk.Frame(master=shoppingcart_frame, background="ivory")
    shoppingcartitems_frame.pack(side=tk.TOP)
    for i in range(10):
        shopping_cart_item(shoppingcartitems_frame, f"Item {i + 1}", "1", "5.00").grid(column=0, row=i)
    # Total
    sctotal = tk.Frame(master=shoppingcart_frame, relief=tk.GROOVE, borderwidth=1)
    sctotal_label = tk.Label(master=sctotal, text="Total", width=30, height=2)
    sctotal_price = tk.Label(master=sctotal, text="$COST", width=10, height=2)
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
    for i in range(10):
        product = tk.Button(
            text=f"Product {i + 1}",
            width="15",
            height="5",
            master=product_grid_frame,
            relief=tk.RAISED,
            borderwidth=1,
            command=partial(shopping_cart.add, i + 1)
        )
        product.grid(column=i % 5, row=i // 5, padx=3, pady=3)

    information_frame.grid(row=0, column=0, columnspan=2, sticky="new", padx="3", pady="3")
    shoppingcart_frame.grid(row=1, column=0, sticky="nsw", padx="3", pady="3")
    product_select_frame.grid(row=1, column=1, sticky="nsew", padx="3", pady="3")

    root.columnconfigure(1, weight=3)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
    
if __name__ == "__main__":
    main()
