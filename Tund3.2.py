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

#�1
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

#�2
# summa = 0
# while True:
#     number = input("sisesta arv(vajuta enter l�oetamiseks): ")
#     if number =="": break
#     try:
#         number=float(number)
#         summa += number
#     except:
#         print("viga")
# print(f"Arvude summa: {summa}")

#�3
# for k�simuse_nr in range(10):
#     a=randint(1,50)
#     b=randint(1,50)
#     �ige_vastus=a+b
#     print(f"{a}+{b}", end="")
#     p=0
#     �=0
#     vastus=0
#     while p<5 and vastus!=�ige_vastus:
#         vastus=int(input("="))
#     if vastus==�ige_vastus:
#         print("Tubli!")
#         �+=1

#�4
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

#�5
# N = int(input("Sisesta ruudu suurus N: "))
# for i in range(N):
#     for j in range(N):
#         if i == j or i + j == N - 1:
#             print("X", end=" ")
#         else:
#             print("O", end=" ")
#     print()

