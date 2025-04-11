#1
def lisa_andmed(palgad, inimesed):
    nimi = input("Nimi: ")
    if nimi.isalpha():
        try:
            palk = float(input("Palk: "))
            palgad.append(palk)
            inimesed.append(nimi)
            print("Lisatud:", nimi, palk)
        except:
            print("Palk peab olema number!")
    else:
        print("Nimi peab olema tähtedega!")

#2
palgad = [1200, 2500, 750, 395, 1300]
inimesed = ["A", "B", "C", "D", "E"]

while True:
    print("\nInimesed:", inimesed)
    print("Palgad:", palgad)
    print("1 - Lisa andmeid")
    print("0 - Välju")
    valik = input("Valik: ")

    if valik == "1":
        mitu = int(input("Mitu inimest lisada? "))
        for _ in range(mitu):
            lisa_andmed(palgad, inimesed)
    elif valik == "0":
        break

#3
def sorteerimine(p: list, i: list) -> any:
    v = input("Vali märk: > (kasvav) või < (kahanev) ")
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            if eval(str(p[n]) + v + str(p[m])):
                p[n], p[m] = p[m], p[n]
                i[n], i[m] = i[m], i[n]
    return p, i

#4
töötajad = [("A", 1200), ("C", 2500), ("D", 750), ("E", 395), ("E", 1300)]

madalaim_palk = töötajad[0]
for nimi, palk in töötajad:
    if palk < madalaim_palk[1]:
        madalaim_palk = (nimi, palk)

print(f"Madalaim palk on {madalaim_palk[0]}: {madalaim_palk[1]}")

#5
töötajad = [("A", 3000), ("B", 4000), ("C", 2500), ("D", 3500)]

töötajad_asc = sorted(töötajad, key=lambda x: x[1])
töötajad_desc = sorted(töötajad, key=lambda x: x[1], reverse=True)

print("Kasvavas järjekorras:")
for nimi, palk in töötajad_asc:
    print(f"{nimi}:{palk}")

print("\nKahanevas järjekorras:")
for nimi, palk in töötajad_desc:
    print(f"{nimi}:{palk}")

#6
def sama_palk(palgad, nimed):
    for palk in set(palgad):
        mitu = palgad.count(palk)
        if mitu > 1:
            print(f"\nPalk: {palk}")
            for i in range(len(palgad)):
                if palgad[i] == palk:
                    print(nimed[i])

#7
def otsi_palk(nimi, nimed, palgad):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            print(f"{nimed[i]} saab {palgad[i]}")

#8
def palk_filter(nimed, palgad, summa, rohkem=True):
    for i in range(len(palgad)):
        if rohkem and palgad[i] > summa:
            print(nimed[i], palgad[i])
        elif not rohkem and palgad[i] < summa:
            print(nimed[i], palgad[i])

#10
def keskmine(nimed, palgad):
    k = sum(palgad) / len(palgad)
    print("Keskmine palk on", k)
    for i in range(len(palgad)):
        if palgad[i] == k:
            print(nimed[i])

#14
def paranda(nimed, palgad):
    for i in range(len(nimed)):
        nimed[i] = nimed[i].capitalize()
        palgad[i] = int(palgad[i])