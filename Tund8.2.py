import tkinter as tk
from tkinter import filedialog

def vali_fail():
    fail = filedialog.askopenfilename()
    manus_entry.delete(0, tk.END)
    manus_entry.insert(0, fail)

aken = tk.Tk()
aken.title("E-kirja saatmine")
aken.geometry("540x420")
aken.configure(bg="#2e8b57")

font1 = ("Arial", 11)

tk.Label(aken, text="Email:", bg="#2e8b57", fg="white", font=font1).grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(aken, text="Nimi:", bg="#2e8b57", fg="white", font=font1).grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(aken, text="Telefon:", bg="#2e8b57", fg="white", font=font1).grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(aken, text="Teema:", bg="#2e8b57", fg="white", font=font1).grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(aken, text="Lisa fail:", bg="#2e8b57", fg="white", font=font1).grid(row=4, column=0, padx=10, pady=5, sticky="e")
tk.Label(aken, text="Kiri:", bg="#2e8b57", fg="white", font=font1).grid(row=5, column=0, padx=10, pady=5, sticky="ne")

email_entry = tk.Entry(aken, width=40, font=font1)
nimi_entry = tk.Entry(aken, width=40, font=font1)
telefon_entry = tk.Entry(aken, width=40, font=font1)
teema_entry = tk.Entry(aken, width=40, font=font1)
manus_entry = tk.Entry(aken, width=30, font=font1)
kiri_text = tk.Text(aken, width=40, height=8, font=font1)

email_entry.grid(row=0, column=1, padx=5, pady=5)
nimi_entry.grid(row=1, column=1, padx=5, pady=5)
telefon_entry.grid(row=2, column=1, padx=5, pady=5)
teema_entry.grid(row=3, column=1, padx=5, pady=5)
manus_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
kiri_text.grid(row=5, column=1, padx=5, pady=5)

tk.Button(aken, text="Vali fail", command=vali_fail, font=font1, bg="white").grid(row=4, column=1, sticky="e", padx=5)

aken.mainloop()
