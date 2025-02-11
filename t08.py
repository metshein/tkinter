import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os
from PIL import Image


selected_files = []

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
        kausta_sisu = os.listdir(directory)
        for file in kausta_sisu:
            # print(file)
            text_field.insert(tk.END, file + "\n")
            selected_files.append(os.path.join(directory, file))

        print(selected_files)
    else:
        dir_label.config(text="Kausta ei valitud.")

def save_images():
    save_directory = filedialog.askdirectory()
    if save_directory:
        for file in selected_files:
            img = Image.open(file)
            img = img.resize((200, 200))
            filename = os.path.basename(file)
            img.save(os.path.join(save_directory, filename))
        print("Pildid on salvestatud.")
    else:
        print("Salvestamise kausta ei valitud.")

aken = tk.Tk()
aken.title("Pildi suuruse muutmine")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font=("Arial", 14))
label.pack(pady=10)

text_field = tk.Text(aken, height=10, width=50)
text_field.pack(pady=10)

select_button = tk.Button(aken, text="Vali kataloog", command=open_directory)
select_button.pack(pady=5)

save_button = tk.Button(aken, text="Salvesta pildid", command=save_images)
save_button.pack(pady=5)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()