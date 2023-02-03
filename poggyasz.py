"""
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a csomag.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a pogyászok számát a mintának megfelelően a konzolra! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok átlag súlya gramban. (1kg = 1000g) (4p)
D.	Írassa ki konzolra a mintának megfelelően a legmagasabb pogyász  méreteit és súlyát (ha több is van, akkor az első legmagasabb adatait).(4p)
"""

from Csomagok import Csomagok
poggyasz = []
sorok = ""

def beolvasas():
    fajl = open("csomag.txt","r",encoding="UTF-8")
    fejlec = fajl.readline()
    sorok = fajl.readlines()
    fajl.close 
    i = 0
    while i < len(sorok):
        csomi = sorok[i].strip().split("#")
        poggyasz.append(Csomagok(csomi))
        i += 1
    #proba: print(poggyasz[3].suly)
    return sorok

def poggyaszok_szama():
    darabszam = len(beolvasas())
    print(f"III/A, B:\n\tA pogyászok száma: {darabszam}")

def atlag_suly():
    cm51_db = 0
    cm51_g = 0
    i = 0
    while i < len(beolvasas()):
        if poggyasz[i].szelesseg == 51:
            cm51_db += 1
            cm51_g += (poggyasz[i].suly)*1000
        i += 1
    eredmeny = int(cm51_g / cm51_db)
    print(f"III/C:\n\tAz 51 cm-es pogyászok átlag súlyértéke: {eredmeny} g")

def legmagasabb():
    melyik = 0
    i = 0
    while i < len(beolvasas()):
        if poggyasz[i].magassag > poggyasz[melyik].magassag:
            melyik = i
        i += 1
    print(f"III/D:\n\tA legmagasabb pogyász méretei: {poggyasz[melyik].szelesseg}X{poggyasz[melyik].magassag}X{poggyasz[melyik].melyseg}, súlya: {poggyasz[melyik].suly} kg")
