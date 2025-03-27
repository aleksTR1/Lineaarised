# #�lesanne 1
#  datetime import *

# # Tervitus ja t�nase kuup�eva kuvamine
# tana = date.today()
# print(f"T�na on {tana}")

# # Erinevad kuup�eva formaadid
# tana_str = tana.strftime("%d/%m/%Y")
# print(f"Kuup�ev formaadis dd/mm/yyyy: {tana_str}")

# tana_str = tana.strftime("%B %d, %Y")
# print(f"Kuup�ev formaadis kuu nimetus, dd, yyyy: {tana_str}")

# tana_str = tana.strftime("%m/%d/%y")
# print(f"Kuup�ev formaadis mm/dd/yy: {tana_str}")

# tana_str = tana.strftime("%b-%d-%Y")
# print(f"Kuup�ev formaadis l�hendatud kuu nimetus-dd-yyyy: {tana_str}")

# # P�eva, kuu ja aasta leidmine
# day = tana.day
# month = tana.month
# year = tana.year

# print(f"P�ev: {day}, Kuu: {month}, Aasta: {year}")

# # J��nud p�evade arv kuu l�puni
# import calendar
# last_day_of_month = calendar.monthrange(year, month)[1]
# days_left_in_month = last_day_of_month - day
# print(f"J��nud p�evi kuu l�puni: {days_left_in_month}")

# # J��nud p�evade arv aasta l�puni
# days_left_in_year = (date(year, 12, 31) - tana).days
# print(f"J��nud p�evi aasta l�puni: {days_left_in_year}")

# # Vanuse arvutamine
# birth_date = date(1990, 5, 15)  # Asenda oma s�nnikuup�evaga
# age_in_days = (tana - birth_date).days
# age_in_years = age_in_days // 365
# age_in_months = (age_in_days % 365) // 30
# age_in_remaining_days = (age_in_days % 365) % 30

# print(f"Vanus: {age_in_years} aastat, {age_in_months} kuud, {age_in_remaining_days} p�eva")

# #�lesanne 2
# # Tehted ja seletused
# result1 = 3 + 8 / (4 - 2) * 4
# result2 = 3 + (8 / (4 - 2)) * 4
# result3 = (3 + 8) / (4 - 2) * 4

# print(f"Ilma sulgudeta: 3 + 8 / (4 - 2) * 4 = {result1}")
# print(f"Sulgudega: 3 + (8 / (4 - 2)) * 4 = {result2}")
# print(f"Teine sulgude variant: (3 + 8) / (4 - 2) * 4 = {result3}")

# #�lesanne 3
# import math

# # Ringi raadius
# R = 5  # Asenda sobiva v��rtusega

# # Ruudu pindala ja �mberm��t
# square_area = (2 * R) ** 2
# square_perimeter = 4 * (2 * R)

# # Ringi pindala ja �mberm��t
# circle_area = math.pi * R ** 2
# circle_circumference = 2 * math.pi * R

# print(f"Ruudu pindala: {square_area}")
# print(f"Ruudu �mberm��t: {square_perimeter}")
# print(f"Ringi pindala: {circle_area}")
# print(f"Ringi �mberm��t: {circle_circumference}")


# #�lesanne 4
# #Algandmed
# earth_radius = 6378  # Maa raadius kilomeetrites
# coin_diameter = 2  # M�ndi l�bim��t millimeetrites

# # Arvutame Maa �mberm��du
# earth_circumference = 2 * math.pi * earth_radius  # Kilomeetrites

# # Arvutame, mitu m�nti l�heb �mber Maa
# coins_needed = earth_circumference * 1000 / coin_diameter  # L�bim��t on millimeetrites, seet�ttu korrutame 1000-ga

# print(f"�mber Maa peab panema {int(coins_needed)} 2-euroseid m�nte")

# #�lesanne 5
# # Muutujad
# word1 = "kill-koll"
# word2 = "killadi-koll"

# # V�ljundi kuvamine
# print(f"{word1.upper()} {word2.upper()} {word1.upper()} {word2.upper()} {word1.upper()} {word1.upper()} {word2.upper()} {word1.upper()}")

# #�lesanne 6 
# #Laulus�nad
# t="""
# Rong see s�itis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see s�itis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.
# """

# # Kuvamine suurte t�htedega
# print(t.upper())

# #�lesanne 7
# # Kasutaja sisend
# length = float(input("Sisesta ristk�liku pikkus: "))
# width = float(input("Sisesta ristk�liku laius: "))

# # �mberm��t ja pindala
# perimeter = 2 * (length + width)
# area = length * width

# print(f"Ristk�liku �mberm��t: {perimeter}")
# print(f"Ristk�liku pindala: {area}")

# #�lesanne 8
# # Kasutaja sisend
# fuel = float(input("Sisesta tangitud k�tuse liitrid: "))
# distance = float(input("Sisesta l�bitud kilomeetrid: "))

# # K�tusekulu arvutamine
# fuel_consumption = (fuel / distance) * 100

# print(f"K�tusekulu 100 km kohta: {fuel_consumption:.2f} liitrit")

# #�lesanne 9
# # Rulluisutaja kiirus
# speed = 29.9  # km/h

# # Kasutaja sisend
# minutes = float(input("Sisesta minutid: "))

# # J�udlus ajas
# distance = (speed * minutes) / 60  # Arvutame, kui kaugele j�uab

# print(f"Rulluisutaja j�uab {distance:.2f} km {minutes} minutiga.")

#�lesanne 10
# Kasutaja sisend
# time_in_minutes = int(input("Sisesta aeg minutites: "))

# # Ajateisendus
# hours = time_in_minutes // 60
# minutes = time_in_minutes % 60

# print(f"Aeg: {hours} tundi ja {minutes} minutit")






