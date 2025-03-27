# #Ainult positiived arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#     print(f"Korrutis võrdub: {a*b}")

# #Kas a on paaris või paaritu arv?
# if a%2==0 and a!=0:
#     print(f"Arv {a} on paaris")
# elif a==0:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"Arv {a} on paaritu")

# Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("Mis hinne sai täna koolis?"))
#     if hinne in range(1,6):
#         print("Hinne")
#         if hinne==5:
#             print("VH")
#         elif hinne==4:
#             print("H")
#         elif hinne==3:
#             print("R")
#         else:
#             print("MR")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga:", e)

# nimi="PYTHON"
# print(nimi.isupper())
# if nimi.isupper():
#     print("Suured tähed")
# else:
#     print("Ei ole kõik suured tähed")
# Ülesanne 1----------------------------------
# 1 Juku

# nimi=input("Mis on sinu nimi?")
# if nimi=="JUKU":
#     print("Lähme kinno")
#     vanus=int(input("Kui vana sa oled?"))
#     if vanus in range(1,65):
#         print("Vanus")
#         if vanus==6:
#             print("Tasuta")
#         elif vanus==14:
#             print("lastepilet")
#         elif vanus==65:
#             print("sooduspilet")
       
# else:
#     print("Ma olen hõivatud! Mine kinno ise")

# #Ülesanne 1----------------------------------
# nimed=["Serhii","Aleks","Denis"]
# nimi1=input()
# nimi2=input()
# nimi3=input()
# if (nimi in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
#     print("Pinginaabrid")
# else:
#     print("Ei ole pringinaabrid")

# ÜL3 Remont
# a=float(input("Pikkus: "))
# b=float(input("Laius: "))
# S=a*b
# soov=input("Kas tahad remonti teha?")
# if soov.lower()=="jah":
#     print("Remont")
#     #--------------
#     hind=float(input("Hind: ")) #kontroll
#     #--------------
#     koguhind=S*hind
#     print(f"Sul on vaja {koguhind} Eur
   
   
#     ")
# else:
#     print("Head aega!")
# ----------------------------------

# ÜL 4
# täishind = float(input("Введите первоначальную цену: "))

# if täishind > 700:
#     soodushind = täishind * 0.7
#     print(f"Цена со скидкой: {soodushind}")
# else:
#     print("Цена должна быть больше 700")

# ----------------------------------

# ÜL 5

# temperatuur = float(input("Sisesta temperatuuri kraadides: "))
# if temperatuur > 18:
#     sõnum = "Temperatuur on üle 18 kraadi, see on mugav temperatuur."
# else:
#     sõnum = "Temperatuur on 18 kraadi või madalam, võib-olla on vaja soojustada."
# print(sõnum)
# -----------------------------------

# ÜL 6-7

# #Küsimine kasvu ja soo kohta
# height = float(input("Sisesta oma pikkus sentimeetrites: "))
# gender = input("Sisesta oma sugu (mees/naine): ").lower()

# # Kasvu määramine
# if height < 160:
#     height_category = "madal"
# elif 160 <= height <= 180:
#     height_category = "keskmine"
# else:
#     height_category = "kõrge"

# # Tulemuse kuvamine
# print(f"Sinu pikkus on {height_category}.")
# #------------------------------------

