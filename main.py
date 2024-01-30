import tkinter as tk

def main():
    window = tk.Tk()

    information_frame = tk.Frame(width="150", relief=tk.GROOVE, borderwidth=2)
    title = tk.Label(text="PoS Program", width="150", master=information_frame)
    title.pack()

    shoppingcart_frame = tk.Frame(width="40", height="100", relief=tk.GROOVE, borderwidth=2)
    sctitle = tk.Label(text="Shopping Cart", master=shoppingcart_frame)
    sctitle.pack()
    sclabels = tk.Frame(master=shoppingcart_frame, relief=tk.GROOVE, borderwidth=1)
    sclabels_item = tk.Label(master=sclabels, text="Item", width=30)
    sclabels_qty = tk.Label(master=sclabels, text="Qty", width=5)
    sclabels_price = tk.Label(master=sclabels, text="Price", width=5)
    sclabels_item.pack(side=tk.LEFT)
    sclabels_qty.pack(side=tk.LEFT)
    sclabels_price.pack(side=tk.LEFT)
    sctotal = tk.Frame(master=shoppingcart_frame, relief=tk.GROOVE, borderwidth=1)
    sctotal_label = tk.Label(master=sctotal, text="Total", width=30, height=2)
    sctotal_price = tk.Label(master=sctotal, text="$COST", width=10, height=2)
    sctotal_label.pack(side=tk.LEFT)
    sctotal_price.pack(side=tk.LEFT)
    sctotal.pack(side=tk.BOTTOM)
    sclabels.pack()
    sc_fill = tk.Label(master=shoppingcart_frame, height="40", text=" ")
    sc_fill.pack(fill="both", expand=False)

    product_select_frame = tk.Frame(width="107", relief=tk.GROOVE, borderwidth=2)
    page_select_frame = tk.Frame(master=product_select_frame, relief=tk.GROOVE, borderwidth=2)
    pagstitle = tk.Label(master=page_select_frame, text="Page Selection", width="107")
    pagstitle.pack()
    page_select_frame.pack()
    prostitle = tk.Label(master=product_select_frame, text="Product Selection", width="107")
    prostitle.pack()
    product_grid_frame = tk.Frame(master=product_select_frame, width="107")
    product_grid_frame.pack()
    for i in range(10):
        product = tk.Button(
            text=f"Product {i + 1}",
            width="15",
            height="5",
            master=product_grid_frame,
            relief=tk.RAISED,
            borderwidth=1
        )
        product.grid(column=i % 5, row=i // 5, padx=5, pady=5)
    product_select_fill = tk.Label(master=product_select_frame, text=" ", height=40)
    product_select_fill.pack()

    information_frame.pack(side=tk.TOP)
    shoppingcart_frame.pack(side=tk.LEFT, fill="y", expand=False)
    product_select_frame.pack(side=tk.RIGHT)

    window.mainloop()
    


if __name__ == "__main__":
    main()
