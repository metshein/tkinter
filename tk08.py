import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps
import os



def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
        kausta_sisu = os.listdir(directory)
        for fail in kausta_sisu:
            file_name, file_extension = os.path.splitext(fail)
            if file_extension == ".jpg" or file_extension == ".jpeg":
                inputtxt.insert(tk.END, fail+"\n")
        
    else:
        dir_label.config(text="Kausta ei valitud.")

def save_images():
    pass
   
aken = tk.Tk()
aken.title("Pildi suuruse muutmine")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font="Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height = 10, width = 50)
inputtxt.pack(pady=10)

open_button = tk.Button(aken, text="Vali failid", command=open_directory)
open_button.pack(pady=10)

save_button = tk.Button(aken, text="Salvesta pildid", command=save_images)
save_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()