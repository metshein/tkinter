import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


aken = ttk.Window(themename="darkly")
# aken = tk.Tk()
aken.title("Pitsapood")
aken.geometry("300x400")


def show_selection():
    # print("Pitsa suurus:", selected_size.get())
    # print(var1.get(), var2.get(), var3.get())
    valikud = ["Kuller (+3€)", "Tulen ise järgi (0€)"]
    hinnad = [3,0]
    nr = valikud.index(selected_option.get())
    # print("Valitud üksus:", hinnad[nr])
    suurus = selected_size.get()
    lisad = var1.get() + var2.get() + var3.get()
    trans = hinnad[nr]
    kokku = suurus+lisad+trans
    print(kokku)
    messagebox.showinfo("Pitsa hind", f"Tasumisele kuulub {kokku:.2f}€")
    
tk.Label(aken, text=f"Kasutaja ID:", font="Arial 14").pack()
tk.Entry(aken).pack()

# Suuruse hind
selected_size = tk.IntVar(value=5)
tk.Label(aken, text=f"Vali pitsa suurus:", font="Arial 14").pack()
# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", font="Arial 12", variable=selected_size, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", font="Arial 12", variable=selected_size, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", font="Arial 12", variable=selected_size, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.IntVar(value=0)
var2 = tk.DoubleVar(value=0)
var3 = tk.IntVar(value=0)
tk.Label(aken, text=f"Vali lisandid:", font="Arial 14").pack()
# Loome märkeruudud
checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

# Dropdown valikud
tk.Label(aken, text=f"Vali transport:", font="Arial 14").pack()
valikud = ["Kuller (+3€)", "Tulen ise järgi (0€)"]
selected_option = tk.StringVar()
selected_option.set("Kuller (+3€)")

# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

btn_confirm = ttk.Button(aken, text="Kinnita valik", command=show_selection, bootstyle="danger")
btn_confirm.pack(pady=20)

aken.mainloop()