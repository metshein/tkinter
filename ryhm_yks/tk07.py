import tkinter as tk

def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        #38011064711
        if int(text[0])%2==0:
            sugu = "naine"
        else:
            sugu = "mees"
        sp = f"{text[5]}{text[6]}.{text[3]}{text[4]}.{text[1]}{text[2]}"
        #print(sp)
        validation_label.config(text=f"Sugu: {sugu}\nSünnipäev {sp}", fg="green")

    else:
        validation_label.config(text="Sisesta vähemalt 11 märki!", fg="red")

aken = tk.Tk()
aken.title("Validaator")
aken.geometry("400x300")

label = tk.Label(aken, text="Isikukood", font="Arial 16").pack(pady=(10, 0))

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Sisesta vähemalt 11 märki!", fg="red")
validation_label.pack()

aken.mainloop()