#1
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

