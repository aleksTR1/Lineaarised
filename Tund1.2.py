# # from random import *
# # from typing import Type

# #ülesanne 1
# #nimi=input("mis on sinu nimi?: ")
# #vanus=int(input("kui vana sa oled?: "))

# #print(f"Tere,maailm! Tervitan sind {nimi} Sa oled {vanus} aastat vana." )
# #print("Tere,maailm! Tervitan sind" ,nimi, "Sa oled",vanus,"aastat vana." )
# #print("Tere,maailm! Tervitan sind"+nimi+"\nSa oled"+str(vanus)+"aastat vana." )

# #ülesanne 2
# #eesnimi = "Jaak"
# #pikkus = 16.5
# #kas_käib_koolis = True
# #print(f"Muutuja {vanus} on {type(vanus)} tüübi")
# #print(f"Muutuja {eesnimi} on {type(eesnimi)} tüübi")
# #print(f"Muutuja {pikkus} on {type(pikkus)} tüübi")
# #print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)} tüübi")

# #ülesanne 3
# # from random import randint


# # kommidearv=randint(1,100)
# # print(f"laual on {kommidearv} kommid")
# # kommidvõtmud=int(input("mitu kommi tahad ära võtta?"))
# # onjäänud=kommidearv-kommidvõtmud
# # print(f"Laual on jäänud {onjäänud} komme")

# #ülesanne 4
# # Kasutaja sisend
# circumference = float(input("Sisesta puu ümbermõõt (m): "))

# # Puu läbimõõdu arvutamine (d = C / π)
# import math
# diameter = circumference / math.pi

# print(f"Puu läbimõõt on: {diameter:.2f} meetrit")

# #ülesanne 5
# # Kasutaja sisend
# N = float(input("Sisesta ristküliku pikkus (Nm): "))
# M = float(input("Sisesta ristküliku laius (Mm): "))

# # Diagonaali arvutamine Pythagorase teoreemi abil (d = √(N² + M²))
# import math
# diagonal = math.sqrt(N**2 + M**2)

# print(f"Ristküliku diagonaal on: {diagonal:.2f} meetrit")
# #ülesanne 6 
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg  # Õige valem

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# #ülesanne 7
# # Kasutaja sisend 5 täisarvu jaoks
# numbers = []
# for i in range(5):
#     number = int(input(f"Sisesta täisarv {i+1}: "))
#     numbers.append(number)

# # Arvutame aritmeetilise keskmise
# average = sum(numbers) / len(numbers)

# # Summa ja täisarvuline osa
# summa = sum(numbers)
# user_number = int(input("Sisesta arv, mille järgi teha jagamine: "))
# quotient = summa // user_number  # Täisarvuline osa
# remainder = summa % user_number  # Jääk

# print(f"Aritmeetiline keskmine: {average}")
# print(f"Summa: {summa}")
# print(f"Jagatis (täisarvuline osa): {quotient}, Jääk: {remainder}")

# #ülesanne 8
# # Konn
# print("   @..@")
# print("  (----)")
# print(" ( \\__/ )")
# print("^^ \"\" ^^")

# #ülesanne 9
# # Kolmnurga küljed
# a = int(input("Sisesta kolmnurga külg a: "))
# b = int(input("Sisesta kolmnurga külg b: "))
# c = int(input("Sisesta kolmnurga külg c: "))

# # Ümbermõõdu arvutamine
# perimeter = a + b + c

# print(f"Kolmnurga ümbermõõt on: {perimeter}")

#ülesanne 10
# Algandmed
# pizza_price = 12.90  # Pitsa hind
# tip_percentage = 0.10  # Teenindustasu protsent

# # Kasutaja sisend
# people = int(input("Mitu inimest on grupis? "))

# # Teenindustasu arvutamine
# tip = pizza_price * tip_percentage

# # Kokku makstava summa arvutamine
# total_amount = pizza_price + tip

# # Iga inimese osa arvutamine
# amount_per_person = total_amount / people

# print(f"Igaüks peab maksma: {amount_per_person:.2f} €")





