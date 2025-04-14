#1
def kool():
    opilased = []  # Список для учеников
    puudumised = []  # Список для количества пропусков

    # Ввод данных
    n = int(input("Kui palju õpilasi on? "))  # Сколько учеников
    for _ in range(n):
        name = input("Sisesta õpilase nimi: ")  # Вводим имя ученика
        absences = int(input(f"Kui palju puudumisi on {name}l? "))  # Вводим количество пропусков
        opilased.append(name)  # Добавляем имя ученика
        puudumised.append(absences)  # Добавляем количество пропусков

    # Меню с действиями
    while True:
        print("\n1. Parimad õpilased\n2. Sorteeri puudumiste järgi\n3. Välja arvatud õpilased\n4. Välju")
        choice = int(input("Vali tegevus: "))  # Выбор действия
        if choice == 1:
            n = int(input("Kui palju parimaid õpilasi soovite? "))  # Сколько лучших учеников
            sorted_students = sorted(zip(puudumised, opilased))  # Сортируем по количеству пропусков
            for i in range(n):
                print(f"{sorted_students[i][1]} - {sorted_students[i][0]} puudumisi")  # Выводим лучших
        elif choice == 2:
            sorted_students = sorted(zip(puudumised, opilased))  # Сортируем по количеству пропусков
            for absences, name in sorted_students:
                print(f"{name} - {absences} puudumisi")  # Выводим список учеников с пропусками
        elif choice == 3:
            opilased = [name for name, absences in zip(opilased, puudumised) if absences <= 100]  # Убираем учеников с более чем 100 пропусками
            puudumised = [absences for absences in puudumised if absences <= 100]  # Убираем их из списка пропусков
        elif choice == 4:
            break  # Выход из программы

kool()

#2
import random

def sport():
    sportlased = []  # Список спортсменов
    tulemused = []  # Список результатов

    # Ввод данных
    n = int(input("Kui palju sportlasi on? "))  # Сколько спортсменов
    for _ in range(n):
        name = input("Sisesta sportlase nimi: ")  # Вводим имя спортсмена
        sportlased.append(name)  # Добавляем имя спортсмена
        score = max(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))  # Генерируем случайный результат
        tulemused.append(score)  # Добавляем результат

    # Меню с действиями
    while True:
        print("\n1. Parimad tulemused\n2. Sorteeri tulemused\n3. Diskvalifitseeri sportlased\n4. Välju")
        choice = int(input("Vali tegevus: "))  # Выбор действия
        if choice == 1:
            n = int(input("Kui palju parimaid tulemusi soovite? "))  # Сколько лучших результатов
            sorted_results = sorted(zip(tulemused, sportlased), reverse=True)  # Сортируем по результатам
            for i in range(n):
                print(f"{sorted_results[i][1]} - {sorted_results[i][0]} punkti")  # Выводим лучших спортсменов
        elif choice == 2:
            sorted_results = sorted(zip(tulemused, sportlased), reverse=True)  # Сортируем по результатам
            for score, name in sorted_results:
                print(f"{name} - {score} punkti")  # Выводим все результаты
        elif choice == 3:
            sportlased = [name for name, score in zip(sportlased, tulemused) if score >= 50]  # Убираем спортсменов с результатом ниже 50
            tulemused = [score for score in tulemused if score >= 50]  # Убираем их из списка результатов
        elif choice == 4:
            break  # Выход из программы

sport()

#3
def linnad():
    linnad = []  # Список городов
    elanikud = []  # Список населения

    # Ввод данных
    n = int(input("Kui palju linnu? "))  # Сколько городов
    for _ in range(n):
        city = input("Sisesta linna nimi: ")  # Вводим название города
        population = int(input(f"Kui palju elanikke on linnas {city}? "))  # Вводим количество населения
        linnad.append(city)  # Добавляем город
        elanikud.append(population)  # Добавляем население

    # Меню с действиями
    while True:
        print("\n1. Uuri linna elanike arvu\n2. Sorteeri linnad nime järgi\n3. Välju")
        choice = int(input("Vali tegevus: "))  # Выбор действия
        if choice == 1:
            city = input("Sisesta linna nimi: ")  # Вводим название города
            if city in linnad:
                print(f"{city} - {elanikud[linnad.index(city)]} elanikud")  # Выводим население города
            else:
                print("Linna ei leitud")  # Если город не найден
        elif choice == 2:
            sorted_cities = sorted(zip(linnad, elanikud))  # Сортируем города по названию
            for city, population in sorted_cities:
                print(f"{city} - {population} elanikud")  # Выводим все города с населением
        elif choice == 3:
            break  # Выход из программы

linnad()

#4
import random

def pood():
    ostud = []  # Список покупок
    hinnad = []  # Список цен

    # Ввод данных
    n = int(input("Kui palju tooteid? "))  # Сколько товаров
    for _ in range(n):
        item = input("Sisesta toode: ")  # Вводим товар
        ostud.append(item)  # Добавляем товар в список
        hinnad.append(random.randint(10, 500))  # Генерируем случайную цену

    # Меню с действиями
    while True:
        print("\n1. Ostetud tooted\n2. Sorteeri hindade järgi\n3. Välju")
        choice = int(input("Vali tegevus: "))  # Выбор действия
        if choice == 1:
            bought = []  # Список купленных товаров
            while True:
                item = input("Sisesta ostetud toode või 'lõpp' lõpetamiseks: ")  # Вводим купленный товар
                if item == "lõpp":
                    break  # Заканчиваем ввод
                if item in ostud:
                    index = ostud.index(item)  # Находим товар в списке
                    bought.append((item, hinnad[index]))  # Добавляем товар в список купленных
                    ostud.remove(item)  # Убираем товар из списка
                    hinnad.remove(hinnad[index])  # Убираем его цену
            total = 0  # Переменная для подсчёта общей стоимости
            for item, price in bought:
                print(f"{item} - {price}€")  # Выводим все купленные товары
                total += price  # Добавляем цену в общую сумму
            print(f"Kokku: {total}€")  # Выводим итоговую сумму
        elif choice == 2:
            sorted_items = sorted(zip(hinnad, ostud))  # Сортируем товары по цене
            for price, item in sorted_items:
                print(f"{item} - {price}€")  # Выводим товары с ценами
        elif choice == 3:
            break  # Выход из программы

pood()


