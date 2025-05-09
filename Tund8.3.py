import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Lahenduse funktsioon
def lahenda():
    # Taasta taust
    for entry in [sisend_a, sisend_b, sisend_c]:
        entry.config(bg="white")

    try:
        a = float(sisend_a.get())
        b = float(sisend_b.get())
        c = float(sisend_c.get())
    except ValueError:
        for entry in [sisend_a, sisend_b, sisend_c]:
            if not entry.get().strip():
                entry.config(bg="misty rose")
        tulemus.config(text="Palun täida kõik väljad õigesti.")
        return

    if a == 0:
        tulemus.config(text="See ei ole ruutvõrrand (a ei saa olla 0).")
        return

    D = b**2 - 4*a*c
    tekst = f"Võrrand: {a}x² + {b}x + {c} = 0\n"
    tekst += f"D = {b}² - 4×{a}×{c} = {D}\n"

    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        tekst += f"Kaks lahendit:\nx₁ = {x1:.2f}, x₂ = {x2:.2f}"
    elif D == 0:
        x = -b / (2 * a)
        tekst += f"Üks lahend: x = {x:.2f}"
    else:
        tekst += "Reaalseid lahendeid ei ole."

    tulemus.config(text=tekst)

# Graafiku funktsioon
def joonista_graafik():
    try:
        a = float(sisend_a.get())
        b = float(sisend_b.get())
        c = float(sisend_c.get())
    except ValueError:
        messagebox.showerror("Viga", "Palun sisesta õiged väärtused.")
        return

    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

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

# Aken
aken = tk.Tk()
aken.title("Ruutvõrrandi lahendaja")

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

tk.Button(aken, text="Lahenda", command=lahenda).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(aken, text="Graafik", command=joonista_graafik).grid(row=5, column=0, columnspan=2)

tulemus = tk.Label(aken, text="", justify="left", fg="blue", wraplength=400)
tulemus.grid(row=6, column=0, columnspan=2, pady=10)

aken.mainloop()
