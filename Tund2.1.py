# #näidis
# #Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if b>0 and b>0:
#         print(f"Korrutis võrdub: {a*b}")
# else:
#         print("Korrutamine on võimalik ainult positiivsete arvudega.")

# #kas a on paaris või paaritu arv?
# if a%2==0 and a!=0:
#         print(f"Arv{a} on paaris")
# elif a==0:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"arv {a} on paaritu")
# #Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("mis hinne sai täna koolis?"))
#     if hinne in range(1,6):
#         print("Hinne")
#         if hinne==5:
#             print("vh")
#         elif hinne==4:
#             print("H")
#         elif hinne==3:
#             print("R")
#         else:
#             print("MR")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("viga", e)

# #1 
# nimi=input("mis on sinu nimi?")
# if nimi=="JUKU":
#     print("Lähme kinno!")
#     vanus=int(input("kui vana sa oled?"))

#     if vanus<=6:
#         print("tasuta")
#     if vanus==6-14:
#         print("lastepilet")
#     if vanus==15-65:
#         print("täispilet")
#     if vanus<=65:
#         print("sooduspilet")
#     else:
#         print("Ma olen hõivatud! Mine kinno ise!")

# #2 Pinginaabrid
# #Serhii Aleks Denis, Aleks Serhii Denis
# nimed=["Serhii", "Aleks", "Denis"]
# nimi1=input()
# nimi2=input()
# nimi3=input()
# if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi3 and nimi2!=nimi3 and nimi1!=nimi3:
#     print("Ta on minu pinginaaber")
# else:
#     print("Ei ole minu pinginaaber")

# #3 Remont
# a=float(input("Pikkus:"))
# b=float(input("Laius: "))
# S=a*b
# soov=input("Kas tahad remoni teha?")
# if soov.lower()=="jah":
#    print("remont")
#    hind=float(input("hind: ")) #kontroll
#    koguhind=S*hind
#    print(f"sul on vaja {koguhind} Eur")
# else:
#     print("head aega!")

# #4 
# def hindkoosallahindlusega(täishind):
#     if täishind > 700:
#         soodushind = täishind * 0.7
#         return soodushind
#     else:
#         return "Цена должна быть больше 700"

# # Пример использования
# täishind=float(input("Введите первоначальную цену: "))
# soodushind=hindkoosallahindlusega(täishind)

# print(f"Цена со скидкой: {soodushind}")

# #5
# def kontrolli_temperatuur(temperatuur):
#     if temperatuur > 18:
#         return "Temperatuur on üle 18 kraadi, see on mugav temperatuur."
#     else:
#         return "Temperatuur on 18 kraadi või madalam, võib-olla on vaja soojustada."

# # Kasutamine
# temperatuur = float(input("Sisesta temperatuur kraadides: "))
# sõnum = kontrolli_temperatuur(temperatuur)

# print(sõnum)

# #ÜL 6-7
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




