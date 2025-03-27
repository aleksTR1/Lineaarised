#Töö 4.4

#1
from string import digits, punctuation
vokaali=["a","e","u","o","i","ä","ö","ü","õ"]
konsonanti="qwrtpsdfghklzxcvbnmj"
numbrid=digits
rkid=punctuation
v = 0
k = 0
n = 0
m = 0
t = 0
tekst=input("sisend (sõna või lause):").lower()
tekst_list=list(tekst)
for s in tekst_list:
    if s in vokaali:
        v+=1
    elif s in konsonanti:
        k+=1
    elif s in numbrid:
        n+=1
    elif s in rkid:
         m+=1
    elif s=="":
         t+=1
print(f"Vokaale: {v}")
print(f"Konsonante: {k}")
print(f"Numbreid: {n}")
print(f"Marke: {m}")
print(f"Tühikute arv: {t}")

#3
numbrid=[15,17,32,44,60]
for number in numbrid:
    print('*'*number)

#4
postiindeks=input("Sisestage Eesti postiindeks (5 numbrit): ")
if len(postiindeks)==5 and postiindeks.isdigit():
    esimene_number=int(postiindeks[0])
    if esimene_number==1: maakond="Tallinna"
    elif esimene_number==2: maakond="Narva, Narva-Jõesuu"
    elif esimene_number==3: maakond="Kohtla-Järve"
    elif esimene_number==4: maakond="Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif esimene_number==5: maakond="Tartu linn"
    elif esimene_number==6: maakond="Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif esimene_number==7: maakond="Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif esimene_number==8: maakond="Pärnumaa"
    elif esimene_number==9: maakond="Läänemaa, Hiiumaa, Saaremaa"
    if esimene_number in [1,2,3]: print("Osta jööge kodus!")
    else: print("Kandke maski!")
    print(f"Postiindeks kuulub piirkonda: {maakond}")
else: print("Vigane postiindeks, palun sisestage 5 numbrit.")


#5
loend=[1,2,3,4,5]
vahetamise_arv=int(input("Sisesta, mitu esimest ja viimast elementi vahetada:"))
for i in range(vahetamise_arv):
    loend[i],loend[-(i+1)]=loend[-(i+1)],loend[i]
print("Muudetud loend:",loend)

#6
numbrid=[5,8,13,7,20]
max_number=max(numbrid)
uus_number=max_number/len(numbrid)
numbrid[numbrid.index(max_number)]=uus_number
print("Muudetud loend:",numbrid)

#7
numbrid=[7,-4,9,-2,5]
numbrid.sort(key=abs)
print("Sorteeritud nimekiri absoluutväärtuse järgi:",numbrid)

#näidis
# #append
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element:"))
# print(elemendid)
# for e in elemendid:
#     print(e)
# #extend
# list_sõne.extend(elemendid)
# print(list_sõne)
# print(elemendid)
# #insert
# elemendid.insert(0,"A")
# print(elemendid)
# #remove
# elemendid.remove("A")
# print(elemendid)
# #pop
# elemendid.pop(0)
# elemendid.pop()
# print(elemendid)
# #index
# ind=list_sõne.index("r")
# print(f"täht r on {ind}-indeksiga")
# #count
# k=list_sõne.count("r")
# print(list_sõne)
# #reverse
# list_sõne.reverse()
# print(list_sõne)
# #copy
# list_sõne2=list_sõne.copy()
# list_sõne2=clear()
# print(list_sõne2)


