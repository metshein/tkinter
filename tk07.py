import tkinter as tk

def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        sugunr = int(text[0])
        if sugunr%2==0:
            sugu = "naine"
        else:
            sugu = "mees"
        validation_label.config(text=sugu, fg="green")
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


.container>div.suva*4