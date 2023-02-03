"""
A.	Írasson ki a konzolra dollár jelel ($) elválasztva 12 számból álló véletlen számsorozatot [-10,1000] zárt intervallumon a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A $ jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írjon függvényt paratlanok_szama néven, amiben számolja meg, hogy hány olyan elem van, ami páratlanok. A visszatérési érték legyen egy egész szám! (3p)
E.	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a eredmeny.txt nevű fájlba, amit fajlba_kiir nevű metódusban fogalmazzon meg! (2p)
"""
import random

szamsor = []

def veletlen():
    i = 0
    while i < 12:
        ujszam = int(random.random()*1010-10)
        szamsor.append(ujszam)
        i += 1

def sorozatom():
    veletlen()
    kiir = ""
    i = 0
    while i < len(szamsor):
        kiir += str(szamsor[i])
        if i < len(szamsor)-1:
            kiir += "$"
        i +=1
    print(f"II/A, B, C:\n\t{kiir}")

def paratlanok_szama():
    mennyi = 0
    i = 0
    while i < len(szamsor):
        if szamsor[i] % 2 != 0:
            mennyi += 1
        i +=1
    return mennyi

