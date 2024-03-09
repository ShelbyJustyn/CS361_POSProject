import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from time import sleep
from datetime import datetime
import json
from class_definitions import Shopping_Cart, Shopping_Cart_Item, Product, startup_popup, help_popup

def main():

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
    root = tk.Tk()
    root.title("Point of Sale by Justyn Shelby")
    root.geometry("1280x720")
    shopping_cart = Shopping_Cart()  

    def shopping_cart_item_frame(item, master, borderwidth=0):

        def edit_quantity(item, event):
            new_qty = tk.StringVar()
            entry = tk.Entry(master=root, width=2, textvariable=new_qty)
            entry.bind("<Return>", lambda x:destroy(item))
            entry.place(x=root.winfo_pointerx()- 20, y=root.winfo_pointery() - 85)

            def destroy(item):
                new_qty_int = int(new_qty.get())
                if new_qty_int < 0:
                    pass
                else:
                    if new_qty_int == 0: 
                        warning = tk.Toplevel(root)
                        warning.geometry(f"128x36+{root.winfo_pointerx()- 20}+{root.winfo_pointery() - 85}")
                        tk.Label(warning, text=f"{item.name} deleted!").pack()
                        warning.after(750, lambda:warning.destroy())
                    difference = new_qty_int - item.qty
                    item.qty = new_qty_int
                    shopping_cart.update(item.price * difference)
                    shopping_cart_app.reload()
                entry.destroy()

        frame = tk.Frame(master=master, relief=tk.GROOVE, borderwidth=borderwidth)
        tk.Label(height="2", master=frame, text=item.name, width=25).grid(row=0, column=0)
        quantity = tk.Label(master=frame, text=item.qty, width=5)
        quantity.bind("<Button-1>", partial(edit_quantity, item))
        quantity.grid(row=0, column=1)
        total_price = f"{item.price*item.qty:.2f}" if type(item.qty) == int else item.price
        tk.Label(master=frame, text=total_price, width=10).grid(row=0, column=2)
        return frame
    class Shopping_Cart_App():

        def __init__(self, master, shopping_cart):
            self.master = master
            self.shopping_cart = shopping_cart
            self.page = 0
            self._reload()

        def _reload(self):
            frame = tk.Frame(master=self.master, relief=tk.GROOVE, borderwidth=2)
            tk.Label(master=frame, text="Shopping Cart").pack()
            shopping_cart_item_frame(Shopping_Cart_Item(None, "Item", "Qty", "Price"), frame, borderwidth=1).pack()
            items_frame = tk.Frame(master=frame, background="pink", height=1)
            for i, item in enumerate([x for x in self.shopping_cart.cart if x.qty > 0][14 * self.page:14 * self.page + 14]):
                print(f"{item.name=} {item.qty=}")
                shopping_cart_item_frame(item, items_frame).grid(column=0, row=i)
            page_buttons = tk.Frame(master=frame)
            tk.Button(master=page_buttons, 
                    text="<", 
                    width="2", 
                    height="1", 
                    relief=tk.RAISED, 
                    borderwidth=1, 
                    command=self.dec_page).pack(side=tk.LEFT)
            tk.Label(master=page_buttons, 
                    text=f"Page {self.page + 1}/{self.shopping_cart.size // 14 + 1}", 
                    width=5).pack(side=tk.LEFT)
            tk.Button(master=page_buttons, 
                    text=">", 
                    width="2", 
                    height="1", 
                    relief=tk.RAISED, 
                    borderwidth=1, 
                    command=self.inc_page).pack(side=tk.LEFT)
            total_frame = tk.Frame(master=frame, 
                                relief=tk.GROOVE, 
                                borderwidth=1)
            tk.Label(master=total_frame, 
                    text="Total", 
                    width=30, 
                    height=2).grid(row=0, column=0)
            tk.Label(master=total_frame, 
                    text=f"${self.shopping_cart.total:.2f}", 
                    width=10, 
                    height=2).grid(row=0, column=1)
            items_frame.pack()
            total_button = tk.Button(master=frame, 
                                    text="Finalize", 
                                    width="38", 
                                    height="2", 
                                    relief=tk.RAISED, 
                                    borderwidth=1, 
                                    command=self.log)
            total_button.pack(side=tk.BOTTOM)
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
            self._reload()

        def log(self):
            cur_date = datetime.now().date().strftime("%Y-%m-%d")
            cur_time = datetime.now().time().strftime("%H:%M:%S")
            log = {
                "transaction_date": cur_date,
                "transaction_time": cur_time,
                "transaction_total": float(f"{shopping_cart.total:.2f}"),
                "items_sold": []
                }
            for item in shopping_cart.cart:
                item_sold = {"name": item.name,
                            "sku": item.sku,
                            "price": item.price,
                            "qty_sold": item.qty}
                log["items_sold"].append(item_sold)
            with open(f"processing/log_{cur_date}_{cur_time}", "w") as file:
                json.dump(log, file, indent=1)
            self.clear()

        def clear(self):
            shopping_cart.clear()
            self.reload()
    shopping_cart_app = Shopping_Cart_App(root, shopping_cart)
    
    product_select_frame = tk.Frame(relief=tk.GROOVE, borderwidth=2)
    class ProductsFrame():

        def __init__(self):
            self.page_select_frame = tk.Frame(master=product_select_frame, relief=tk.GROOVE, borderwidth=2)
            tk.Button(master=self.page_select_frame, 
                    text="Product Select", 
                    width=45, 
                    height=2, 
                    relief=tk.RAISED, 
                    command=partial(self._switch_page, "Products")).pack(side=tk.LEFT)
            tk.Button(master=self.page_select_frame, 
                    text="Totals", 
                    width=45, 
                    height=2, 
                    relief=tk.RAISED, 
                    command=partial(self._switch_page, "Totals")).pack(side=tk.RIGHT)
            self.page_select_frame.pack(fill="x")

            self.current_page = "Products"
            self.total = None

            self.product_grid_frame = tk.Frame(master=product_select_frame, width="107")
            self.product_select()

        def _add_to_cart(self, product):
            shopping_cart.add(product)
            shopping_cart_app.reload()
            
        def product_select(self):
            self.product_grid_frame = tk.Frame(master=product_select_frame, width="107")
            self.title = tk.Label(master=product_select_frame, text="Product Selection")
            self.title.pack(fill="x")
            for i, product in enumerate(inventory):
                product_button = tk.Button(
                    text=product.name,
                    width="15",
                    height="5",
                    master=self.product_grid_frame,
                    relief=tk.RAISED,
                    borderwidth=1,
                    command=partial(self._add_to_cart, product)
                )
                product_button.grid(column=i % 5, row=i // 5, padx=3, pady=3)
            self.product_grid_frame.pack()

        def totals(self):
            self.product_grid_frame = tk.Frame(master=product_select_frame, width="107")
            self.title = tk.Label(master=product_select_frame, text="Totals")
            self.title.pack(fill="x")
            with open("totals.json", "r") as file:
                data = file.read()
                totals = json.loads(data)
            for i, product in enumerate(totals["totalAmounts"]):
                product_button = tk.Button(
                    text=f"{product['name']}\n{product['total']}",
                    width="15",
                    height="5",
                    master=self.product_grid_frame,
                    relief=tk.RAISED,
                    borderwidth=1,
                    command=partial(self._add_to_cart, product)
                )
                product_button.grid(column=i % 5, row=i // 5, padx=3, pady=3)
            self.total = tk.Label(master=product_select_frame, text=f"${totals['totalRevenue']:.2f}")
            self.total.pack(side=tk.BOTTOM)
            self.product_grid_frame.pack()

        def reload(self):
            self.__init__()

        def _switch_page(self, page):
            if self.current_page == page:
                return
            if self.total:
                self.total.destroy()
            self.title.destroy()
            self.product_grid_frame.destroy()
            if self.current_page == "Products":
                self.current_page = "Totals"
                self.totals()
            else:
                self.current_page = "Products"
                self.product_select()
 
    startup_popup(root)

    information_frame = tk.Frame(relief=tk.GROOVE, borderwidth=2)
    tk.Label(master=information_frame, text="Point of Sale Program", height="1", font=("Arial", 25)).grid(row=0, column=0)
    tk.Button(master=information_frame, 
              text="Help", 
              width=2, 
              height=2, 
              relief=tk.RAISED, 
              borderwidth = 1, command=partial(help_popup, root)).grid(row=0, column=1)
    information_frame.columnconfigure(0, weight=3)

    ProductsFrame()

    information_frame.grid(row=0, column=0, columnspan=2, sticky="new", padx="3", pady="3")
    shopping_cart_app.reload()
    product_select_frame.grid(row=1, column=1, sticky="nsew", padx="3", pady="3")

    root.columnconfigure(1, weight=3)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
    
if __name__ == "__main__":
    main()
