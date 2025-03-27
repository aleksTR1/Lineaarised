from Tund5 import *

a=float(input("Arv1: "))
b=float(input("Arv2: "))
t=input("Tehe: ")
vastus=arithmetic(a,b,t)
print(vastus)

vastus=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Tehe: "))
print(vastus)

#is_year_leap funksiooni kasutamine
aasta=int(input("Mis aasta tahad kontrollida"))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on Liigaasta")
    else:
        print(f"{aasta} ei ole Liigaasta")

# square() kasutamine
#Kontroll while True ja try except...
a=float(input("Ruudu külg= "))

S,P,D=square(a)

#Season() parameter
a=float(input("Parameter now= "))

H=season(a)

