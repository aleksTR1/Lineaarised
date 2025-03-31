#Töö 4.4

#1
from string import digits, punctuation
vokaali=["a","e","u","o","i","ä","ö","ü","õ"]
konsonanti="qwrtpsdfghklzxcvbnmj"
numbrid=digits
rkid=punctuation
v = 0
k = 0
n = 0
m = 0
t = 0
tekst=input("sisend (sõna või lause):").lower()
tekst_list=list(tekst)
for s in tekst_list:
    if s in vokaali:
        v+=1
    elif s in konsonanti:
        k+=1
    elif s in numbrid:
        n+=1
    elif s in rkid:
         m+=1
    elif s=="":
         t+=1
print(f"Vokaale: {v}")
print(f"Konsonante: {k}")
print(f"Numbreid: {n}")
print(f"Marke: {m}")
print(f"Tühikute arv: {t}")

#3
numbrid=[15,17,32,44,60]
for number in numbrid:
    print('*'*number)

#4
postiindeks=input("Sisestage Eesti postiindeks (5 numbrit): ")
if len(postiindeks)==5 and postiindeks.isdigit():
    esimene_number=int(postiindeks[0])
    if esimene_number==1: maakond="Tallinna"
    elif esimene_number==2: maakond="Narva, Narva-Jõesuu"
    elif esimene_number==3: maakond="Kohtla-Järve"
    elif esimene_number==4: maakond="Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif esimene_number==5: maakond="Tartu linn"
    elif esimene_number==6: maakond="Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif esimene_number==7: maakond="Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif esimene_number==8: maakond="Pärnumaa"
    elif esimene_number==9: maakond="Läänemaa, Hiiumaa, Saaremaa"
    if esimene_number in [1,2,3]: print("Osta jööge kodus!")
    else: print("Kandke maski!")
    print(f"Postiindeks kuulub piirkonda: {maakond}")
else: print("Vigane postiindeks, palun sisestage 5 numbrit.")


#5
loend=[1,2,3,4,5]
vahetamise_arv=int(input("Sisesta, mitu esimest ja viimast elementi vahetada:"))
for i in range(vahetamise_arv):
    loend[i],loend[-(i+1)]=loend[-(i+1)],loend[i]
print("Muudetud loend:",loend)

#6
numbrid=[5,8,13,7,20]
max_number=max(numbrid)
uus_number=max_number/len(numbrid)
numbrid[numbrid.index(max_number)]=uus_number
print("Muudetud loend:",numbrid)

#7
numbrid=[7,-4,9,-2,5]
numbrid.sort(key=abs)
print("Sorteeritud nimekiri absoluutväärtuse järgi:",numbrid)
#-----------------------------------------------------------------

#3
numbrid = [15, 17, 32, 44, 60]  # Список чисел, определяющих количество звёздочек в строке
for number in numbrid:  # Цикл for перебирает каждый элемент списка
    print('*' * number)  # Оператор * умножает строку на число, создавая строку из звёздочек

#4 Проверка почтового индекса и региона
postiindeks=input("Sisestage Eesti postiindeks (5 numbrit): ") # Ввод индекса
if len(postiindeks)==5 and postiindeks.isdigit(): # Проверка длины и цифр
    esimene_number=int(postiindeks[0]) # Первая цифра индекса
    if esimene_number==1: maakond="Tallinn"
    elif esimene_number==2: maakond="Narva, Narva-Jõesuu"
    elif esimene_number==3: maakond="Kohtla-Järve"
    elif esimene_number==4: maakond="Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif esimene_number==5: maakond="Tartu"
    elif esimene_number==6: maakond="Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif esimene_number==7: maakond="Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif esimene_number==8: maakond="Pärnumaa"
    elif esimene_number==9: maakond="Läänemaa, Hiiumaa, Saaremaa"
    print("Osta jööge kodus!" if esimene_number in [1,2,3] else "Kandke maski!")
    print(f"Postiindeks kuulub piirkonda: {maakond}")
else: print("Vigane postiindeks, palun sisestage 5 numbrit.")

#5 Обмен первых и последних элементов
loend=[1,2,3,4,5] # Исходный список
vahetamise_arv=int(input("Sisesta, mitu esimest ja viimast elementi vahetada:")) # Ввод количества замен
for i in range(vahetamise_arv): loend[i],loend[-(i+1)]=loend[-(i+1)],loend[i] # Меняем местами элементы
print("Muudetud loend:",loend)

#6 Замена максимального элемента его частным от длины списка
numbrid=[5,8,13,7,20] # Исходный список
max_number=max(numbrid) # Максимальное число
numbrid[numbrid.index(max_number)]=max_number/len(numbrid) # Замена числа
print("Muudetud loend:",numbrid)

#7 Сортировка списка по абсолютному значению
numbrid=[7,-4,9,-2,5] # Исходный список
numbrid.sort(key=abs) # Сортировка по модулю
print("Sorteeritud nimekiri absoluutväärtuse järgi:",numbrid)

#list – это изменяемая упорядоченная коллекция элементов, которая поддерживает индексацию, срезы и различные методы для работы с данными, такие как append, insert, pop, remove, sort, reverse и другие.
#append(value) – добавляет элемент в конец списка.
#insert(index, value) – вставляет элемент в список по указанному индексу.
#pop(index) – удаляет и возвращает элемент по индексу (по умолчанию последний).
#remove(value) – удаляет первое вхождение указанного элемента.
#clear() – полностью очищает список.
#copy() – создаёт копию списка.
#reverse() – переворачивает список в обратном порядке.
#sort() – сортирует список по возрастанию (или убыванию, если указать reverse=True).
#max(iterable) – возвращает наибольшее значение в последовательности.
#index(value) – возвращает индекс первого вхождения элемента в списке.
#input(prompt) – получает ввод от пользователя.
#len(obj) – возвращает длину объекта (списка, строки и т. д.).
#isdigit() – проверяет, состоит ли строка только из цифр.
#f"{variable}" – форматированные строки для вставки переменных.
#int(value) – преобразует строку в целое число.
#abs(value) – возвращает модуль числа.
#if-elif-else – условный оператор для ветвления кода.
#for item in iterable: – цикл, перебирающий элементы списка.
#range(start, stop, step) – создаёт последовательность чисел.

õpilased=[]  
for i in range(7):
    nimi=input(f"Sisestage{i+1}.õpilase nimi: ")  
    õpilased.append(nimi)  

print("Õpilaste nimekiri:", õpilased)

for i in range(5):
    rnimi=input("what nimi to remove?")
    if rnimi in õpilased:
       õpilased.remove(rnimi)
print(õpilased)






