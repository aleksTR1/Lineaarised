#1 Функция для добавления данных о человеке и его зарплате
def lisa_andmed(palgad, inimesed):
    nimi = input("Nimi: ")  # Запрашиваем имя
    if nimi.isalpha():  # Проверяем, что имя содержит только буквы
        try:
            palk = float(input("Palk: "))  # Запрашиваем зарплату и пытаемся преобразовать в число
            palgad.append(palk)  # Добавляем зарплату в список
            inimesed.append(nimi)  # Добавляем имя в список
            print("Lisatud:", nimi, palk)  # Подтверждение добавления
        except:
            print("Palk peab olema number!")  # Если не число — ошибка
    else:
        print("Nimi peab olema tähtedega!")  # Если имя содержит что-то кроме букв

#2
palgad = [1200, 2500, 750, 395, 1300]  # Список зарплат
inimesed = ["A", "B", "C", "D", "E"]   # Список имён

while True:
    print("\nInimesed:", inimesed)  # Показываем текущие имена
    print("Palgad:", palgad)        # Показываем текущие зарплаты
    print("1 - Lisa andmeid")       # Меню: добавление данных
    print("0 - Välju")              # Выход
    valik = input("Valik: ")        # Запрос выбора пользователя
    
    if valik == "1":
        mitu = int(input("Mitu inimest lisada? "))  # Сколько людей добавить
        for _ in range(mitu):
            lisa_andmed(palgad, inimesed)  # Добавление через функцию
    elif valik == "0":
        break  # Завершаем цикл


#3 Функция для сортировки зарплат и имён по возрастанию или убыванию
def sorteerimine(p: list, i: list) -> any:
    v = input("Vali märk: > (kasvav) või < (kahanev) ")  # Запрос на знак сравнения
    # Проходим по всем элементам
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            # Сравниваем с помощью eval — аккуратно, он выполняет строку как код!
            if eval(str(p[n]) + v + str(p[m])):  
                # Меняем местами зарплаты и имена
                p[n], p[m] = p[m], p[n]
                i[n], i[m] = i[m], i[n]
    return p, i  # Возвращаем отсортированные списки

#4 Список работников и зарплат в одной переменной (неправильный формат)
töötajad = ["A", 1200, "C", 2500, "D", 750, "E", 395, "E", 1300]

# Здесь возникнет ошибка — перебор по паре (nimi, palk) невозможен с таким списком

# Правильный вариант:
töötajad = [("A", 1200), ("C", 2500), ("D", 750), ("E", 395), ("E", 1300)]

madalaim_palk = töötajad[0]  # Считаем, что первый — с минимальной зарплатой

# Перебираем кортежи (имя, зарплата)
for nimi, palk in töötajad:
    if palk < madalaim_palk[1]:  # Сравниваем зарплаты
        madalaim_palk = (nimi, palk)  # Обновляем, если нашли ниже

print(f"Madalaim palk on {madalaim_palk[0]}: {madalaim_palk[1]}")  # Вывод результата

#5 Список работников в виде кортежей (имя, зарплата)
töötajad = [("A", 3000), ("B", 4000), ("C", 2500), ("D", 3500)]

# Сортировка по зарплате по возрастанию
töötajad_asc = sorted(töötajad, key=lambda x: x[1])

# Сортировка по убыванию
töötajad_desc = sorted(töötajad, key=lambda x: x[1], reverse=True)

# Выводим отсортированных работников по возрастанию
print("Kasvavas järjekorras:")
for nimi, palk in töötajad_asc:
    print(f"{nimi}:{palk}")

# Выводим отсортированных работников по убыванию
print("\nKahanevas järjekorras:")
for nimi, palk in töötajad_desc:
    print(f"{nimi}:{palk}")

# 6. Функция выводит имена людей, у которых одинаковая зарплата
def sama_palk(palgad, nimed):
    for palk in set(palgad):  # перебираем уникальные зарплаты
        mitu = palgad.count(palk)  # сколько раз такая зарплата встречается
        if mitu > 1:  # если больше одного — выводим
            print(f"\nPalk: {palk}")
            for i in range(len(palgad)):
                if palgad[i] == palk:
                    print(nimed[i])  # выводим имя с этой зарплатой

# 7. Функция ищет и выводит зарплату по имени (без учёта регистра)
def otsi_palk(nimi, nimed, palgad):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():  # сравнение без учёта регистра
            print(f"{nimed[i]} saab {palgad[i]}")  # выводим имя и зарплату

# 8. Фильтрация по зарплате: больше или меньше указанной суммы
def palk_filter(nimed, palgad, summa, rohkem=True):
    for i in range(len(palgad)):
        if rohkem and palgad[i] > summa:  # если ищем больше указанной суммы
            print(nimed[i], palgad[i])
        elif not rohkem and palgad[i] < summa:  # если ищем меньше
            print(nimed[i], palgad[i])

# 10. Выводит среднюю зарплату и людей, у которых она точно равна среднему значению
def keskmine(nimed, palgad):
    k = sum(palgad) / len(palgad)  # находим точное среднее значение
    print("Keskmine palk on", k)  # выводим среднюю зарплату без округления
    for i in range(len(palgad)):
        if palgad[i] == k:  # ищем тех, чья зарплата точно равна среднему
            print(nimed[i])  # выводим имя

# 14. Исправляет список имён и зарплат: делает имена с заглавной и зарплаты целыми
def paranda(nimed, palgad):
    for i in range(len(nimed)):
        nimed[i] = nimed[i].capitalize()  # первая буква заглавная, остальные строчные
        palgad[i] = int(palgad[i])  # преобразуем зарплату в целое число




# #?
# def palgaotsing(p:list,i:list):
#         """Funktsioon Teha palgaotsing isiku nime jargi.
#         :param i: inimeste nimekiri
#         :param p: palkade nimekiri
#         :rtype:none
#         """
#         nimi=input("sisesta nimi mida sa sooviks: ")
#         leitud=False
#         for j in range (len(i)):
#             if i [j]==nimi:
#                 print(f"{nimi} palk: {p[j]}")
#                 leitud=True
#         if leitud==False:
#             print(f"{nimi} kohta andmeid ei leitud.")

# #?
# def bonus_salary(p: list, i: list):
#     """Своя функция по выбору. добавляет прибавку к зарплате выбранному работнику, позволяя выбрать процент на какой зарплате увеличится"""
# for idx, (name, salary) in enumerate(zip(i,p), 1):
#         print("\nCurrent employees and salaries:")
#         print(f"{idx}. {name}: {salary}$")
# try:
#     choice = int(input("valige töötaja: ")) - 1
#     bonus =float(input("Kirjutage mittu protsentis palk tõuseb: "))
#     if 0 <=choice < len(i) and bonus > 0:
#         original_salary = p[choice]
#         bonus_to = bonus / 100
#         bonus_salary = original_salary * bonus_to + original_salary
#         print(f"New salary is: {bonus_salary}$")
#     else:
#         print("valige eksisteeriv töötaja ja valige bonus rohkem kui 0")

# except:
#     print("error!")


