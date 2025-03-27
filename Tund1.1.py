# #ülesanne 1
#  datetime import *

# # Tervitus ja tänase kuupäeva kuvamine
# tana = date.today()
# print(f"Täna on {tana}")

# # Erinevad kuupäeva formaadid
# tana_str = tana.strftime("%d/%m/%Y")
# print(f"Kuupäev formaadis dd/mm/yyyy: {tana_str}")

# tana_str = tana.strftime("%B %d, %Y")
# print(f"Kuupäev formaadis kuu nimetus, dd, yyyy: {tana_str}")

# tana_str = tana.strftime("%m/%d/%y")
# print(f"Kuupäev formaadis mm/dd/yy: {tana_str}")

# tana_str = tana.strftime("%b-%d-%Y")
# print(f"Kuupäev formaadis lühendatud kuu nimetus-dd-yyyy: {tana_str}")

# # Päeva, kuu ja aasta leidmine
# day = tana.day
# month = tana.month
# year = tana.year

# print(f"Päev: {day}, Kuu: {month}, Aasta: {year}")

# # Jäänud päevade arv kuu lõpuni
# import calendar
# last_day_of_month = calendar.monthrange(year, month)[1]
# days_left_in_month = last_day_of_month - day
# print(f"Jäänud päevi kuu lõpuni: {days_left_in_month}")

# # Jäänud päevade arv aasta lõpuni
# days_left_in_year = (date(year, 12, 31) - tana).days
# print(f"Jäänud päevi aasta lõpuni: {days_left_in_year}")

# # Vanuse arvutamine
# birth_date = date(1990, 5, 15)  # Asenda oma sünnikuupäevaga
# age_in_days = (tana - birth_date).days
# age_in_years = age_in_days // 365
# age_in_months = (age_in_days % 365) // 30
# age_in_remaining_days = (age_in_days % 365) % 30

# print(f"Vanus: {age_in_years} aastat, {age_in_months} kuud, {age_in_remaining_days} päeva")

# #Ülesanne 2
# # Tehted ja seletused
# result1 = 3 + 8 / (4 - 2) * 4
# result2 = 3 + (8 / (4 - 2)) * 4
# result3 = (3 + 8) / (4 - 2) * 4

# print(f"Ilma sulgudeta: 3 + 8 / (4 - 2) * 4 = {result1}")
# print(f"Sulgudega: 3 + (8 / (4 - 2)) * 4 = {result2}")
# print(f"Teine sulgude variant: (3 + 8) / (4 - 2) * 4 = {result3}")

# #Ülesanne 3
# import math

# # Ringi raadius
# R = 5  # Asenda sobiva väärtusega

# # Ruudu pindala ja ümbermõõt
# square_area = (2 * R) ** 2
# square_perimeter = 4 * (2 * R)

# # Ringi pindala ja ümbermõõt
# circle_area = math.pi * R ** 2
# circle_circumference = 2 * math.pi * R

# print(f"Ruudu pindala: {square_area}")
# print(f"Ruudu ümbermõõt: {square_perimeter}")
# print(f"Ringi pindala: {circle_area}")
# print(f"Ringi ümbermõõt: {circle_circumference}")


# #Ülesanne 4
# #Algandmed
# earth_radius = 6378  # Maa raadius kilomeetrites
# coin_diameter = 2  # Mündi läbimõõt millimeetrites

# # Arvutame Maa ümbermõõdu
# earth_circumference = 2 * math.pi * earth_radius  # Kilomeetrites

# # Arvutame, mitu münti läheb ümber Maa
# coins_needed = earth_circumference * 1000 / coin_diameter  # Läbimõõt on millimeetrites, seetõttu korrutame 1000-ga

# print(f"Ümber Maa peab panema {int(coins_needed)} 2-euroseid münte")

# #Ülesanne 5
# # Muutujad
# word1 = "kill-koll"
# word2 = "killadi-koll"

# # Väljundi kuvamine
# print(f"{word1.upper()} {word2.upper()} {word1.upper()} {word2.upper()} {word1.upper()} {word1.upper()} {word2.upper()} {word1.upper()}")

# #Ülesanne 6 
# #Laulusõnad
# t="""
# Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.
# """

# # Kuvamine suurte tähtedega
# print(t.upper())

# #Ülesanne 7
# # Kasutaja sisend
# length = float(input("Sisesta ristküliku pikkus: "))
# width = float(input("Sisesta ristküliku laius: "))

# # Ümbermõõt ja pindala
# perimeter = 2 * (length + width)
# area = length * width

# print(f"Ristküliku ümbermõõt: {perimeter}")
# print(f"Ristküliku pindala: {area}")

# #Ülesanne 8
# # Kasutaja sisend
# fuel = float(input("Sisesta tangitud kütuse liitrid: "))
# distance = float(input("Sisesta läbitud kilomeetrid: "))

# # Kütusekulu arvutamine
# fuel_consumption = (fuel / distance) * 100

# print(f"Kütusekulu 100 km kohta: {fuel_consumption:.2f} liitrit")

# #Ülesanne 9
# # Rulluisutaja kiirus
# speed = 29.9  # km/h

# # Kasutaja sisend
# minutes = float(input("Sisesta minutid: "))

# # Jõudlus ajas
# distance = (speed * minutes) / 60  # Arvutame, kui kaugele jõuab

# print(f"Rulluisutaja jõuab {distance:.2f} km {minutes} minutiga.")

#Ülesanne 10
# Kasutaja sisend
# time_in_minutes = int(input("Sisesta aeg minutites: "))

# # Ajateisendus
# hours = time_in_minutes // 60
# minutes = time_in_minutes % 60

# print(f"Aeg: {hours} tundi ja {minutes} minutit")






