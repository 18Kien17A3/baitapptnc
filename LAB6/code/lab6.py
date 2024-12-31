import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_product(name, price):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def update_product(product_id, name, price):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

# GUI Functions
def refresh_listbox():
    products = get_products()
    product_listbox.delete(0, tk.END)
    for product in products:
        product_listbox.insert(tk.END, f"{product[0]}: {product[1]} - ${product[2]:.2f}")

def add_product_handler():
    name = name_entry.get()
    try:
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Price must be a valid number.")
        return

    if name:
        add_product(name, price)
        refresh_listbox()
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Product name cannot be empty.")

def delete_product_handler():
    selected = product_listbox.curselection()
    if selected:
        product_id = int(product_listbox.get(selected).split(":")[0])
        delete_product(product_id)
        refresh_listbox()
    else:
        messagebox.showerror("Error", "No product selected.")

def update_product_handler():
    selected = product_listbox.curselection()
    if selected:
        product_id = int(product_listbox.get(selected).split(":")[0])
        name = name_entry.get()
        try:
            price = float(price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number.")
            return

        if name:
            update_product(product_id, name, price)
            refresh_listbox()
            name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Product name cannot be empty.")
    else:
        messagebox.showerror("Error", "No product selected.")

# GUI Setup
init_db()

root = tk.Tk()
root.title("Product Manager")

# Widgets
name_label = tk.Label(root, text="Product Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=1, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Product", command=add_product_handler)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

update_button = tk.Button(root, text="Update Product", command=update_product_handler)
update_button.grid(row=3, column=0, columnspan=2, pady=5)

delete_button = tk.Button(root, text="Delete Product", command=delete_product_handler)
delete_button.grid(row=4, column=0, columnspan=2, pady=5)

product_listbox = tk.Listbox(root, width=40, height=10)
product_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

refresh_listbox()

# Main loop
root.mainloop()
