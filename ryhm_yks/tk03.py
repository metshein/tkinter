import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  # Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab teise sisestuse
        maksete_arv = int(sisestus3.get())*12  # Võtab teise sisestuse

        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär) ** -maksete_arv)
        # print(igakuine_makse)

        vastus = tk.Label(aken, text=f"Igakuine makse: {maksete_arv:.2f}")
        vastus.pack()

    # Esimene sisestusväli
    label = tk.Label(aken, text="Laenusumma (€)").pack(pady=(10, 0))
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    label = tk.Label(aken, text="Aastane intressimäär (%)").pack(pady=(10, 0))
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()

    # Teine sisestusväli
    label = tk.Label(aken, text="Laenuperiood (aastates)").pack(pady=(10, 0))
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack(pady=(10, 0))

    aken.mainloop()

if __name__ == "__main__":
    main()