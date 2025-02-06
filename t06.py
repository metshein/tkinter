import tkinter as tk

aken = tk.Tk()
aken.geometry("400x400")
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="Nupp 0,0", font=font)
nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

# sildid
label = tk.Label(text="Palun sisestage oma andmed:")
label.grid(row=0, column=2,  columnspan=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Nimi:")
nimi.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Silmade värv:")
nimi.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Pikkus:")
nimi.grid(row=3, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Kaal:")
nimi.grid(row=4, column=2, padx=padx, pady=pady, sticky="nsew")

nupp_13 = tk.Button(aken, text="Salvesta", font=font)
nupp_13.grid(row=5, column=2, padx=padx, pady=pady, sticky="nsew")

# sisestused
sis1 = tk.Entry(aken)
sis1.grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")

sis2 = tk.Entry(aken)
sis2.grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")

sis3 = tk.Entry(aken)
sis3.grid(row=3, column=3, padx=padx, pady=pady, sticky="nsew")

sis4 = tk.Entry(aken)
sis4.grid(row=4, column=3, padx=padx, pady=pady, sticky="nsew")

aken.mainloop()