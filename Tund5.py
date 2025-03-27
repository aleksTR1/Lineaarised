#1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon t��tab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Kui sisend ei ole j�rjendis[+,-,/,*],siis tagastab s�ne "Tundmatu tehe"
    :param float arv1: Sisenud ujukomaarvu t��bina
    :param float arv2: Sisenud ujukomaarvu t��bina
    :param str tehe: Sisenud listist [+,-,/,*]
    :rtype: varM��ramata t��p (float v�i str)
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
    :rtype: bool t�ev��rsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3
def square(k�lg:float)->any:
    """Kirjutage funksioon
    Tagastab True, kui k�lg on liigaasta ja False kui k�lg on tavaline
    :param float k�lg: Sisenud kasutajalt
    :rtype: any t�ev��rsuses formaadis tulemus
    """
    S=k�lg**2
    P=4*k�lg
    D=(2)**(1/2)*k�lg
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
    :rtype: varM��ramata t��p (float v�i int)
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa

