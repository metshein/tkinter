import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        tekst1 = sisestus1.get()  # Võtab esimese sisestuse
        tekst2 = sisestus2.get()  # Võtab teise sisestuse
        # vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}")
        vastus = tk.Label(aken, text=f"Igakuine makse: {tekst1}")
        vastus.pack()

    # Esimene sisestusväli
    label = tk.Label(aken, text="Laenusumma (€)").pack()
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    label = tk.Label(aken, text="Aastane intressimäär (%)").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()

    # Kolmas sisestusväli
    label = tk.Label(aken, text="Laenuperiood (aastad)").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()



    aken.mainloop()

if __name__ == "__main__":
    main()