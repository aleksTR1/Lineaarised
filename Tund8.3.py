import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Funktsioon ruutvõrrandi lahendamiseks
def lahenda_võrrand():
    # Taastame kõik sisendväljad, et need oleksid normaalsed
    for entry in [sisend_a, sisend_b, sisend_c]:
        entry.config(bg="white")

    # Üritame lugeda sisestatud väärtusi
    try:
        a = float(sisend_a.get())
        b = float(sisend_b.get())
        c = float(sisend_c.get())
    except ValueError:
        # Kui mingi väärtus on vale või tühi, siis värvime välja punaseks
        for entry in [sisend_a, sisend_b, sisend_c]:
            if not entry.get().strip():
                entry.config(bg="misty rose")
        tulemus.config(text="Palun sisesta kõik väljad õigesti!")
        return

    # Kontrollime, et a ei oleks 0
    if a == 0:
        tulemus.config(text="See ei ole ruutvõrrand, sest a ei saa olla 0.")
        return

    # Arvutame diskriminandi
    D = b**2 - 4*a*c
    tekst = f"Võrrand: {a}x² + {b}x + {c} = 0\n"
    tekst += f"Diskriminant (D) = {D}\n"

    # Lahendused, sõltuvalt diskriminandi väärtusest
    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2 * a)
        x2 = (-b - np.sqrt(D)) / (2 * a)
        tekst += f"Kaks lahendit: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
    elif D == 0:
        x = -b / (2 * a)
        tekst += f"Üks lahend: x = {x:.2f}"
    else:
        tekst += "Reaalseid lahendeid ei ole, D on negatiivne."

    # Kuvame tulemuse
    tulemus.config(text=tekst)

# Funktsioon graafiku kuvamiseks
def joonista_graafik():
    try:
        a = float(sisend_a.get())
        b = float(sisend_b.get())
        c = float(sisend_c.get())
    except ValueError:
        messagebox.showerror("Viga", "Palun sisesta õiged väärtused, et graafikut joonistada.")
        return

    # Määrame x-telje vahemiku
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    # Joonistame graafiku
    plt.figure()
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title("Ruutfunktsiooni graafik")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Loome akna
aken = tk.Tk()
aken.title("Ruutvõrrandi lahendaja")

# Tekstiväljad ja nupud kasutajaliideses
tk.Label(aken, text="Sisesta ruutvõrrandi kordajad").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(aken, text="a:").grid(row=1, column=0, sticky="e")
sisend_a = tk.Entry(aken)
sisend_a.grid(row=1, column=1)

tk.Label(aken, text="b:").grid(row=2, column=0, sticky="e")
sisend_b = tk.Entry(aken)
sisend_b.grid(row=2, column=1)

tk.Label(aken, text="c:").grid(row=3, column=0, sticky="e")
sisend_c = tk.Entry(aken)
sisend_c.grid(row=3, column=1)

# Lahendamise nupp
tk.Button(aken, text="Lahenda", command=lahenda_võrrand).grid(row=4, column=0, columnspan=2, pady=10)

# Graafiku nupp
tk.Button(aken, text="Graafik", command=joonista_graafik).grid(row=5, column=0, columnspan=2)

# Tulemuste kuvamine
tulemus = tk.Label(aken, text="", justify="left", fg="blue", wraplength=400)
tulemus.grid(row=6, column=0, columnspan=2, pady=10)

aken.mainloop()
