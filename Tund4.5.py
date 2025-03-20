ikoodid = [] 
arvud = []    
while True:
    kood = input("Sisesta isikukood (või 'exit' lõpetamiseks): ")
    if kood == "exit":
        break
    if len(kood) != 11:
        print("Vale kood! Isikukood peab olema 11 numbrit.")
        arvud.append(kood)
        continue
    if kood[0] not in '123456':
        print("Vale esimene number! Isikukood algab numbriga 1–6.")
        arvud.append(kood)
        continue
    try:
        day = int(kood[5:7])  
        month = int(kood[3:5])  
        year = int(kood[1:3])  
        if not (1 <= day <= 31 and 1 <= month <= 12):  
            print("Vale kuupäev!")
            arvud.append(kood)
            continue
    except ValueError:
        print("Vale kuupäev!")
        arvud.append(kood)
        continue
    weight_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    sum_1 = sum(int(kood[i]) * weight_1[i] for i in range(10))  
    control_number = sum_1 % 11  
    if control_number == 10:
        weight_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        sum_2 = sum(int(kood[i]) * weight_2[i] for i in range(10))  
        control_number = sum_2 % 11
        if control_number == 10:
            control_number = 0  
    if int(kood[10]) != control_number:
        print("Vale kontrollnumber!")
        arvud.append(kood)
        continue
    if kood[0] in '135':
        sex = "Mees"
    else:
        sex = "Naine"
    birth_date = f"{kood[5:7]}.{kood[3:5]}.19{kood[1:3]}"
    birth_hospitals = {
        (1, 10): "Kuressaare Haigla",
        (11, 19): "Tartu Ülikooli Naistekliinik",
        (21, 220): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja",
        (221, 270): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
        (271, 370): "Maarjamõisa Kliinikum (Tartu)",
        (371, 420): "Narva Haigla",
        (421, 470): "Pärnu Haigla",
        (471, 490): "Pelgulinna Sünnitusmaja (Tallinn)",
        (491, 520): "Järvamaa Haigla (Paide)",
        (521, 570): "Rakvere, Tapa haigla",
        (571, 600): "Valga Haigla",
        (601, 650): "Viljandi Haigla",
        (651, 700): "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    }
    hospital_code = int(kood[7:10])
    hospital = next((name for (start, end), name in birth_hospitals.items() if start <= hospital_code <= end), "Tundmatu haigla")
    print(f"See on {sex}, tema sünnikuupäev on {birth_date} ja sünnitushaigla on {hospital}.")
    ikoodid.append(kood)
ikoodid_naised = [k for k in ikoodid if k[0] in '246']
ikoodid_mehed = [k for k in ikoodid if k[0] in '135']
ikoodid_sorted = ikoodid_naised + ikoodid_mehed 
arvud.sort()
print("\nÕiged isikukoodid (naised, mehed):")
for k in ikoodid_sorted:
    print(k)
print("\nVale isikukoodide nimekiri:")
for k in arvud:
    print(k)
