#Töö 4.4

# 3
# for arv in [18,19,32,45,60,12]: print('*'*arv)

# # 5
# loend=[1,2,3,4,5,6]
# n=int(input("Mitu elementi vahetada?"))
# for i in range(n):loend[i], loend[-(i+1)] = loend[-(i+1)],loend[i]
# print(loend)

# # 6
# numbrid=[10,25,8,50,13]
# numbrid[numbrid.index(max(numbrid))] /= len(numbrid)
# print(numbrid)

# # 7
# print(sorted([-5,10,-3,8,-2],key=abs))

# # 8
# sonad=['kass','koer','jänes']
# print([s.ljust(max(map(len,sonad)),'_') for s in sonad])

# # 11
# import string
# print([c*(i+1) for i,c in enumerate(string.ascii_lowercase[:int(input("Sisesta arv: "))])])

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

#1
# from string import digits, punctuation
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="qwrtpsdfghklzxcvbnmj"
# numbrid=digits
# märkid=punctuation
# tekst=input("sisend (sõna või lause): "). lower()
# tekst_list=list(tekst)
# for s in tekst_list:
#     if s in vokaali:
#         v+=1
#     elif s in konsonanti:
#         k+=1
#     elif s in numbrid:
#         n+=1
#     elif s in märkid:
#          m+=1
#     elif s==" ":
#          t+=1
