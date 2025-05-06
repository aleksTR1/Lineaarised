import numpy as np
import matplotlib.pyplot as plt

data = []
with open("maed.txt") as f:
    for line in f:
        name, height = line.split()
        data.append((name, int(height)))

maed, korgused = zip(*data)

print(np.mean(korgused), np.max(korgused), np.min(korgused), np.sum(korgused))

plt.bar(maed, korgused)
plt.xticks(rotation=45)
plt.show()

sorted_indices = np.argsort(korgused)[::-1]
plt.bar(np.array(maed)[sorted_indices], np.array(korgused)[sorted_indices])
plt.xticks(rotation=45)
plt.show()

