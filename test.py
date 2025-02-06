import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

# Andmebaasiühendus
def connect_db():
    conn = sqlite3.connect("mpilv.db")
    cur = conn.cursor()
    conn.commit()
    return conn

conn = connect_db()



# Andmete pärimine
def fetch_data(page, per_page):
    offset = (page - 1) * per_page
    cur = conn.cursor()
    cur.execute("SELECT * FROM mpilv LIMIT ? OFFSET ?", (per_page, offset))
    rows = cur.fetchall()
    print("Fetched rows:", rows)  # Debugging: Print fetched rows
    return rows

# Andmete kuvamine tabelis
def display_data():
    for row in tree.get_children():
        tree.delete(row)
    rows = fetch_data(page, per_page)
    for row in rows:
        tree.insert('', tk.END, values=row)
    print("Displayed rows:", rows)  # Debugging: Print displayed rows

# Andmete lisamine
def add_data():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    car_make = entry_car_make.get()
    car_model = entry_car_model.get()
    car_year = entry_car_year.get()
    car_price = entry_car_price.get()
    if first_name and last_name and email and car_make and car_model and car_year and car_price:
        cur = conn.cursor()
        cur.execute("INSERT INTO mpilv (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (first_name, last_name, email, car_make, car_model, int(car_year), float(car_price)))
        conn.commit()
        display_data()
        clear_entries()
    else:
        messagebox.showwarning("Sisendviga", "Kõik väljad peavad olema täidetud")

# Sisendväljade tühjendamine
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_car_make.delete(0, tk.END)
    entry_car_model.delete(0, tk.END)
    entry_car_year.delete(0, tk.END)
    entry_car_price.delete(0, tk.END)

# Andmete kustutamine
def delete_data():
    selected_item = tree.selection()[0]
    item_id = tree.item(selected_item)['values'][0]
    cur = conn.cursor()
    cur.execute("DELETE FROM mpilv WHERE id=?", (item_id,))
    conn.commit()
    display_data()

# Andmete otsimine
def search_data():
    search_term = entry_search.get()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mpilv WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR car_make LIKE ? OR car_model LIKE ?",
                ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
    rows = cur.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert('', tk.END, values=row)
    print("Search results:", rows)  # Debugging: Print search results

# Andmete uuendamine
def update_data():
    selected_item = tree.selection()[0]
    item_id = tree.item(selected_item)['values'][0]
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    car_make = entry_car_make.get()
    car_model = entry_car_model.get()
    car_year = entry_car_year.get()
    car_price = entry_car_price.get()
    if first_name and last_name and email and car_make and car_model and car_year and car_price:
        cur = conn.cursor()
        cur.execute("UPDATE mpilv SET first_name=?, last_name=?, email=?, car_make=?, car_model=?, car_year=?, car_price=? WHERE id=?",
                    (first_name, last_name, email, car_make, car_model, int(car_year), float(car_price), item_id))
        conn.commit()
        display_data()
        clear_entries()
    else:
        messagebox.showwarning("Sisendviga", "Kõik väljad peavad olema täidetud")

# Lehekülgede vahetamine
def next_page():
    global page
    page += 1
    display_data()

def prev_page():
    global page
    if page > 1:
        page -= 1
        display_data()

# Tkinteri aken ja ttkbootstrap dark_theme seadistus
root = ttkb.Window(themename="darkly")
root.title("Andmebaasi rakendus")
root.geometry("1000x750")

# Tabeli vaade
columns = ("ID", "Eesnimi", "Perekonnanimi", "Email", "Autotootja", "Automudel", "Aasta", "Hind")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(expand=True, fill='both')

# Sisendväljad
frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=20)

ttk.Label(frame_inputs, text="Eesnimi").grid(row=0, column=0, padx=5, pady=5)
entry_first_name = ttk.Entry(frame_inputs)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Perekonnanimi").grid(row=1, column=0, padx=5, pady=5)
entry_last_name = ttk.Entry(frame_inputs)
entry_last_name.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = ttk.Entry(frame_inputs)
entry_email.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Autotootja").grid(row=3, column=0, padx=5, pady=5)
entry_car_make = ttk.Entry(frame_inputs)
entry_car_make.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Automudel").grid(row=4, column=0, padx=5, pady=5)
entry_car_model = ttk.Entry(frame_inputs)
entry_car_model.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Aasta").grid(row=5, column=0, padx=5, pady=5)
entry_car_year = ttk.Entry(frame_inputs)
entry_car_year.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Hind").grid(row=6, column=0, padx=5, pady=5)
entry_car_price = ttk.Entry(frame_inputs)
entry_car_price.grid(row=6, column=1, padx=5, pady=5)

# Nupud
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=20)

ttk.Button(frame_buttons, text="Lisa", command=add_data).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_buttons, text="Kustuta", command=delete_data).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_buttons, text="Uuenda", command=update_data).grid(row=0, column=2, padx=5, pady=5)

# Lehekülgede navigeerimine
frame_nav = ttk.Frame(root)
frame_nav.pack(pady=20)

ttk.Button(frame_nav, text="Eelmine", command=prev_page).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_nav, text="Järgmine", command=next_page).grid(row=0, column=1, padx=5, pady=5)

# Otsing
frame_search = ttk.Frame(root)
frame_search.pack(pady=20)

ttk.Label(frame_search, text="Otsi").grid(row=0, column=0, padx=5, pady=5)
entry_search = ttk.Entry(frame_search)
entry_search.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_search, text="Otsi", command=search_data).grid(row=0, column=2, padx=5, pady=5)

# Lehekülgede ja reade arvu seadistamine
page = 1
per_page = 10

display_data()
root.mainloop()