import tkinter as tk

aken = tk.Tk()
aken.title("Raadionuppude näide")
aken.geometry("300x400")


def show_selection():
    # print("Hind:", selected_color.get())
    # print(var1.get(), float(var2.get()), var3.get())
    # print(selected_option.get())
    if selected_option.get()=="Kuller":
        trans = 3
    else:
        trans = 0
    summa = selected_color.get() + var1.get() + float(var2.get()) + var3.get() + trans
    print(summa)

# StringVar, mis hoiab valitud värvi nime
selected_color = tk.IntVar(value=5)

tk.Label(aken, text="Kasutaja ID", font="Arial 16").pack(pady=(10, 0))
tk.Entry(aken).pack()

tk.Label(aken, text="Vali suurus", font="Arial 16").pack(pady=(10, 0))
# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.IntVar(value=0)
var2 = tk.StringVar(value=0)
var3 = tk.IntVar(value=0)
tk.Label(aken, text="Vali lisandid", font="Arial 16").pack(pady=(10, 0))
# Checkboxes
checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue="1.5", offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

tk.Label(aken, text="Vali kättetoimetamine", font="Arial 16").pack(pady=(10, 0))

# dropdown
valikud = ["Kuller", "Kohapeal"]
selected_option = tk.StringVar()
selected_option.set("Vali üksus")

dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()



btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

aken.mainloop()