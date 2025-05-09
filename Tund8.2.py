import numpy as np
import matplotlib.pyplot as plt

# Loeme andmed failist
maed_nimed = []
maed_korgused = []

with open('maed.txt', 'r', encoding='utf-8') as f:
    for line in f:
        nimi, korgus = line.rsplit(' ', 1)
        maed_nimed.append(nimi)
        maed_korgused.append(int(korgus.strip()))

# Numpy massiiv
korgused_np = np.array(maed_korgused)

# Statistika
keskmine = np.mean(korgused_np)
max_korgus = np.max(korgused_np)
min_korgus = np.min(korgused_np)
summa = np.sum(korgused_np)

# Kõrgeim ja madalaim mägi
korgeim_magi = maed_nimed[np.argmax(korgused_np)]
madalaim_magi = maed_nimed[np.argmin(korgused_np)]

# Kuvame tulemused
print(f"Keskmine kõrgus: {keskmine:.2f} m")
print(f"Kõrgeim mägi: {korgeim_magi} ({max_korgus} m)")
print(f"Madalaim mägi: {madalaim_magi} ({min_korgus} m)")
print(f"Kogukõrgus: {summa} m")

# Sorteerime andmed kahanevalt
sorted_indices = np.argsort(korgused_np)[::-1]
sorted_names = [maed_nimed[i] for i in sorted_indices]
sorted_heights = korgused_np[sorted_indices]

# Joonistame graafiku
plt.figure(figsize=(10, 6))
plt.bar(sorted_names, sorted_heights, color='skyblue')
plt.xlabel('Mäed')
plt.ylabel('Kõrgus (m)')
plt.title('Maailma kõrgeimad mäed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('maed_graafik.png')
plt.show()

