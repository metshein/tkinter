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

    # Loo raamid
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="x")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5, fill="x")
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5, fill="x")
    

    # Esimene sisestusväli
    label = tk.Label(frame, text="Laenusumma (€)").pack(side='left')
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(side='left', fill="x", expand="true")
   
    # Teine sisestusväli
    label2 = tk.Label(frame2, text="Aastane intressimäär (%)").pack(side='left')
    sisestus2 = tk.Entry(frame2)
    sisestus2.pack(side='left', fill="x", expand="true")

    # Kolmas sisestusväli
    label3 = tk.Label(frame3, text="Laenuperiood (aastad)").pack(side='left')
    sisestus3 = tk.Entry(frame3)
    sisestus3.pack(side='left', fill="x", expand="true")
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()



    aken.mainloop()

if __name__ == "__main__":
    main()