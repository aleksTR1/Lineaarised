#Töö 4.4

#1
from string import digits, punctuation
vokaali=["a","e","u","o","i","�","�","�","�"]
konsonanti="qwrtpsdfghklzxcvbnmj"
numbrid=digits
rkid=punctuation
v = 0
k = 0
n = 0
m = 0
t = 0
tekst=input("sisend (sõna või lause): "). lower()
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
    elif s==" ":
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
    elif esimene_number==2: maakond="Narva, Narva-J�esuu"
    elif esimene_number==3: maakond="Kohtla-J�rve"
    elif esimene_number==4: maakond="Ida-Virumaa, L��ne-Virumaa, J�gevamaa"
    elif esimene_number==5: maakond="Tartu linn"
    elif esimene_number==6: maakond="Tartumaa, P�lvamaa, V�rumaa, Valgamaa"
    elif esimene_number==7: maakond="Viljandimaa, J�rvamaa, Harjumaa, Raplamaa"
    elif esimene_number==8: maakond="P�rnumaa"
    elif esimene_number==9: maakond="L��nemaa, Hiiumaa, Saaremaa"
    if esimene_number in [1,2,3]: print("Osta j��ge kodus!")
    else: print("Kandke maski!")
    print(f"Postiindeks kuulub piirkonda: {maakond}")
else: print("Vigane postiindeks, palun sisestage 5 numbrit.")


#5
loend=[1,2,3,4,5]
vahetamise_arv=int(input("Sisesta, mitu esimest ja viimast elementi vahetada: "))
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

#n�idis
# #append
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element:"))
# print(elemendid)
# for e in elemendid:
#     print(e)
# #extend
# list_s�ne.extend(elemendid)
# print(list_s�ne)
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
# ind=list_s�ne.index("r")
# print(f"t�ht r on {ind}-indeksiga")
# #count
# k=list_s�ne.count("r")
# print(list_s�ne)
# #reverse
# list_s�ne.reverse()
# print(list_s�ne)
# #copy
# list_s�ne2=list_s�ne.copy()
# list_s�ne2=clear()
# print(list_s�ne2)

