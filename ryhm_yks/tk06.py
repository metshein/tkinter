import tkinter as tk

aken = tk.Tk()
aken.geometry("400x300")
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="Pilt", font=font, bg="lightgray")
nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

# sildid
label = tk.Label(aken, text="Palun sisestage oma andmed:", font=font)
label.grid(row=0, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(aken, text="Nimi:", font=font)
nimi.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

silmad = tk.Label(aken, text="Silmade värv:", font=font)
silmad.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

pikkus = tk.Label(aken, text="Pikkus:", font=font)
pikkus.grid(row=3, column=2, padx=padx, pady=pady, sticky="nsew")

kaal = tk.Label(aken, text="Kaal:", font=font)
kaal.grid(row=4, column=2, padx=padx, pady=pady, sticky="nsew")

cm = tk.Label(aken, text="cm", font=font)
cm.grid(row=3, column=4, padx=padx, pady=pady, sticky="nsew")

kg = tk.Label(aken, text="kg", font=font)
kg.grid(row=4, column=4, padx=padx, pady=pady, sticky="nsew")

#sisestused
sisestus1 = tk.Entry(aken).grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")
sisestus2 = tk.Entry(aken).grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")
sisestus3 = tk.Entry(aken).grid(row=3, column=3, padx=padx, pady=pady, sticky="nsew")
sisestus4 = tk.Entry(aken).grid(row=4, column=3, padx=padx, pady=pady, sticky="nsew")


nupp_13 = tk.Button(aken, text="Salvesta", font=font)
nupp_13.grid(row=5, column=2, padx=padx, pady=pady, sticky="nsew")

# Nuppude seadistamine
aken.grid_columnconfigure(0, weight=2)


aken.mainloop()