import tkinter as tk

def main():
    aken = tk.Tk()
    aken.title("Mario ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(True, False)  
   
    label = tk.Label(aken, text="Tere, maailm!").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()