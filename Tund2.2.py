# try:
#     arv=input("sisesta arv")
#     if arv.isnumeric():
#         arv=int(arv)
#         if arv>0:
#             if arv%2==0:
#                 print("paaris arv")
#             else:
#                 print("paaritu")
#         else:
#             print("Negatiivne arv")
# except:
#     print("Kirjuta numbreid")


# #2
# try:
#     nurk1=float(input("esimene nurk"))
#     nurk2=float(input("teine nurk"))
#     nurk3=float(input("kolmas nurk"))
#     if nurk1>0 and nurk2>0 and nurk3>0:
#         print("Nurgad on positiivsed")
#         if nurk1+nurk2+nurk3==180:
#             print("See on kolmnurk")
#             if nurk1==nurk2 and nurk2==nurk3:
#                 print("võrgkülgne kolmnurk")
#             elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
#                 print("võrdvaarne kolmnurk")
#             else:
#                 print("Erikülgne kolmnurk")
#         else:
#             print("See ei ole kolmnurk")
# except:
#     print("sisesta ujukomaarv")


# #3
# try:
#     soov=input("Kas tahad dekodeerida?").lower()
#     if soov=="jah":
#         try:
#             nr=int(input("päeva number: "))
#             if nr in range (1,8):
#                 if nr==1:
#                     print("Esmaspäev")
#                 elif nr==2:
#                     print("teisipäev")
#             else:
#                  print("ainult 1-7")
#         except:
#             print("numbrid vahemikust 1-7")
# except:
#     print("mul on vaja vastus jah või ei")


# #4
# päev=int(input("kirjuta oma sünnipäev: "))
# kuu=int(input("kirjuta oma sünnikuu: "))
# if (1<=päev<=31) and (1<=kuu<=12):
#     if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
#         tähemärk="Jäär"
#     elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
#         tähemärk="Sõnn"
#     elif (kuu==5 and päev>=21) or (kuu==6 and päev<=20):
#         tähemärk="Kaksikud"
#     elif (kuu==6 and päev>=21) or (kuu==7 and päev<=22):
#         tähemärk="Vähk"
#     elif (kuu==7 and päev>=23) or (kuu==8 and päev<=22):
#         tähemärk="Lõvi"
#     elif (kuu==8 and päev>=23) or (kuu==9 and päev<=22):
#         tähemärk="Neitsi"
#     elif (kuu==9 and päev>=23) or (kuu==10 and päev<=22):
#         tähemärk="Kaalud"
#     elif (kuu==10 and päev>=23) or (kuu==11 and päev<=21):
#         tähemärk="Skorpion"
#     elif (kuu==11 and päev>=22) or (kuu==12 and päev<=21):
#         tähemärk ="Ambur"
#     elif (kuu==12 and päev>=22) or (kuu==1 and päev<=19):
#         tähemärk ="Kaljukits"
#     elif (kuu==1 and päev>=20) or (kuu==2 and päev<=18):
#         tähemärk="Veevalaja"
#     else:
#         tähemärk = "Kalad"
#     print(f"sinu tähemärk on: {tähemärk}")
# else:
#     print("vale andmed palun vaata")

# #ü 5

# user_input=input("kirjuta number: ")

# if user_input():
#     num=int(user_input)
#     print(f"täis arv. 50% arvest: {num * 0.5}")
   
# elif user_input('.', '', 1) and user_input('.') == 1:
#     num = float(user_input)
#     print(f"Дробное arv. 70% arvest: {num * 0.7}")
   
# elif user_input():
#     print(f" {user_input}")

# else:
#     print("vale andmet") 

