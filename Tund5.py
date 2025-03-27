#1
from random import randint
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Kui sisend ei ole järjendis[+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisenud ujukomaarvu tüübina
    :param float arv2: Sisenud ujukomaarvu tüübina
    :param str tehe: Sisenud listist [+,-,/,*]
    :rtype: varMääramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
    :param int aasta: Sisenud kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3
def square(külg:float)->any:
    """Kirjutage funksioon
    Tagastab True, kui külg on liigaasta ja False kui külg on tavaline
    :param float külg: Sisenud kasutajalt
    :rtype: any tõeväärsuses formaadis tulemus
    """
    S=külg**2
    P=4*külg
    D=(2)**(1/2)*külg
    return S,P,D

#4
def season(parameter:int)->str:
    """Kirjutage funksioon
    Tagastab True, kui parameter on liigaasta ja False kui parameter on tavaline
    :param int parameter: in range(1,13)
    :rtype: str hooajanimetus
    """
    if parameter [1,2,12]:
        H="Talv"
    elif parameter in [3,4,5]:
        H="Kevad"
    elif parameter in [6,7,8]:
        H="Suvi"
    else:
        H="Sugis"
    return H

#5
def bank(summa:float, aastad:int)->float:
    """Bank Funksioonid
    Tagastab True,
    :param float summa: Sisenud kasutajalt
    :param int aastad: Sisenud kasutajalt
    :rtype: varMääramata tüüp (float või int)
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa

#6
def is_prime(a=randint(1,10000))->bool:
    """
    liigaasta leidmine
    tagastab true, kui aasta on liigasta ja false kui aasta on tavaline aasta
    :param int aasta:sisenud kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    print(a)
    v=True
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v

#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    """
    if päev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu in [4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v

