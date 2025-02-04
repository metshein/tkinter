import tkinter as tk
import ctypes
from PIL import Image, ImageTk

def main():
    aken = tk.Tk()
    aken.title("tkinter ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(False, True)

    # Pildi avamine ja Tkinteri jaoks ettevalmistamine
    pilt = Image.open("norris.jpg")
    p = 50
    pilt = pilt.crop((0+p, 0+p, 200+p, 200+p))
    foto = ImageTk.PhotoImage(pilt)

    # Sildi kuvamine
    label = tk.Label(aken, text="Jäck Nurris", font=("Arial", 16, "bold"), fg="blue").pack()

    # Pildi kuvamine Label abil
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

    # Tekstkast

    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()