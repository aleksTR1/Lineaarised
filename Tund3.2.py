# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# for i in range (0,10,1):
#     print(f"{i}. samm")
# print()
# for i in range (10):
#     print(f"{i+1}. samm")

#Ü1
# while True:
#     try:
#         nimi=input("sisesta oma nimi")
#         if nimi.isalpha(): break
#     except:
#         print("viga!")
# while True:
#     try:
#         k=input("Mitu korda tervitada? ") #k
#         if k>0: break
#     except: 
#         print("viga!")

#Ü2
# summa = 0
# while True:
#     number = input("sisesta arv(vajuta enter lõoetamiseks): ")
#     if number =="": break
#     try:
#         number=float(number)
#         summa += number
#     except:
#         print("viga")
# print(f"Arvude summa: {summa}")

#Ü3
# for küsimuse_nr in range(10):
#     a=randint(1,50)
#     b=randint(1,50)
#     õige_vastus=a+b
#     print(f"{a}+{b}", end="")
#     p=0
#     õ=0
#     vastus=0
#     while p<5 and vastus!=õige_vastus:
#         vastus=int(input("="))
#     if vastus==õige_vastus:
#         print("Tubli!")
#         õ+=1

#Ü4
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

#Ü5
# N = int(input("Sisesta ruudu suurus N: "))
# for i in range(N):
#     for j in range(N):
#         if i == j or i + j == N - 1:
#             print("X", end=" ")
#         else:
#             print("O", end=" ")
#     print()

