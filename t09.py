import tkinter as tk

aken = tk.Tk()
aken.title("Pitsapood")

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
    

# Suuruse hind
selected_size = tk.IntVar(value=5)

# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_size, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_size, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_size, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.IntVar(value=0)
var2 = tk.DoubleVar(value=0)
var3 = tk.IntVar(value=0)

# Loome märkeruudud
checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

# Dropdown valikud
valikud = ["Kuller (+3€)", "Tulen ise järgi (0€)"]
selected_option = tk.StringVar()
selected_option.set("Kuller (+3€)")

# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

aken.mainloop()