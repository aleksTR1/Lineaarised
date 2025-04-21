from random import randint


andmed={}
andmed = {"nimi": "Mari", "vanus": 25, "keel": "eesti"}
andmed = dict(nimi="Mari", vanus=25, keel="eesti")
print(andmed)
print(andmed["nimi"])
print(andmed.get("nimi"))
print(andmed.get("nimi_","Ei ole sõnastikus"))
print(andmed.keys())
print(andmed.values())
for k,v in andmed.items():
    print(k, v)
andmed["email"]="alekstagirov5c@gmail.com"
print(andmed)
andmed["prillid"]=True
print(andmed)
andmed.update({"nimi":"kati"})
read = ["mis on python?-programmerimiskeel", "eesti pealinn?-Tallinn"]
kus_vas =  {}
for rida in read:
    kysimus, vastus = rida.split("-")
    kus_vas[kysimus.strip()] = vastus.strip()
    print(kus_vas)

kysimused = list(kus_vas.keys())

n=randint(0, len(read)-1)
valitud_kysimus = kysimused[n]
print(valitud_kysimus)
vastus= input("sisesta vastus: ")
if kus_vas[valitud_kysimus].lower()==vastus.lower():
    print("õige vastus")
else:
    print("vale vastus")









# import random

# # Algne sõnastik
# sonastik = {
#     'koer': 'собака',
#     'kass': 'кошка',
#     'maja': 'дом',
#     'auto': 'машина',
#     'päike': 'солнце'
# }

# # Funktsioon: tõlgi eesti -> vene
# def tolgi_est_rus(sona):
#     if sona in sonastik:
#         print(f"Tõlge vene keelde: {sonastik[sona]}")
#     else:
#         print("Sõna ei leitud sõnastikust.")

# # Funktsioon: tõlgi vene -> eesti
# def tolgi_rus_est(sona):
#     for est, rus in sonastik.items():
#         if rus == sona:
#             print(f"Tõlge eesti keelde: {est}")
#             return
#     print("Sõna ei leitud sõnastikust.")

# # Funktsioon: lisa uus sõna
# def lisa_sona():
#     est = input("Sisesta uus sõna eesti keeles: ")
#     rus = input("Sisesta selle sõna vene tõlge: ")
#     if est in sonastik:
#         print("See sõna on juba sõnastikus.")
#     else:
#         sonastik[est] = rus
#         print("Sõna lisatud!")

# # Funktsioon: paranda sõna
# def paranda_sona():
#     est = input("Sisesta sõna eesti keeles, mida soovid parandada: ")
#     if est in sonastik:
#         uus_rus = input(f"Sisesta uus vene tõlge sõnale '{est}': ")
#         sonastik[est] = uus_rus
#         print("Tõlge parandatud!")
#     else:
#         print("Sõna ei leitud sõnastikust.")

# # Funktsioon: testi teadmisi
# def testi_teadmisi():
#     if not sonastik:
#         print("Sõnastik on tühi. Testimine pole võimalik.")
#         return

#     print("Testi teadmisi alustatakse!")
#     oiged = 0
#     kogus = 0

#     # Loome sõnade loendi ja segame selle
#     sonad = list(sonastik.items())
#     random.shuffle(sonad)

#     for est, rus in sonad:
#         suund = random.choice(['est', 'rus'])
#         if suund == 'est':
#             vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")
#             if vastus.strip().lower() == rus.lower():
#                 print("Õige!")
#                 oiged += 1
#             else:
#                 print(f"Vale! Õige vastus on: {rus}")
#         else:
#             vastus = input(f"Sisesta eesti tõlge sõnale '{rus}': ")
#             if vastus.strip().lower() == est.lower():
#                 print("Õige!")
#                 oiged += 1
#             else:
#                 print(f"Vale! Õige vastus on: {est}")
#         kogus += 1

#     protsent = round((oiged / kogus) * 100, 2)
#     print(f"Test lõppenud! Sinu tulemus: {protsent}%")

# # Põhimenüü tsükkel
# def pea_menus():
#     print("Tere tulemast eesti-vene sõnastikku!")

#     while True:
#         print("\nValikud:")
#         print("1 - Tõlgi eesti -> vene")
#         print("2 - Tõlgi vene -> eesti")
#         print("3 - Lisa uus sõna")
#         print("4 - Paranda sõna")
#         print("5 - Testi teadmisi")
#         print("6 - Välju")
#         valik = input("Tee oma valik: ")

#         if valik == "1":
#             sona = input("Sisesta sõna eesti keeles: ")
#             tolgi_est_rus(sona)
#         elif valik == "2":
#             sona = input("Sisesta sõna vene keeles: ")
#             tolgi_rus_est(sona)
#         elif valik == "3":
#             lisa_sona()
#         elif valik == "4":
#             paranda_sona()
#         elif valik == "5":
#             testi_teadmisi()
#         elif valik == "6":
#             print("Head aega!")
#             break
#         else:
#             print("Tundmatu valik. Palun proovi uuesti.")

# # Käivitame programmi
# pea_menus()

