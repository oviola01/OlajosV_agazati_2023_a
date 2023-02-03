"""
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
étel neve, étel rendelőjének neve és értékelés!  (2p)
B.	A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,5], zárt intervallum értendő):
Amennyiben negatív számot adott meg:
“Az értékelés nem lehet negatív!”,
Amennyiben 5 feletti egész számot adott meg:
“5 pont feletti értékelés nem elfogadható!”
Helyes pont-adat esetén:
“Köszönjük az értékelést!” 
Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.	A mintának megfelelően írassa ki az eredményt! (1p)
"""
def vizsgal(problema):
    print(problema)
    ertekeles = int(input("Értékelés (1-5): "))

def ertekel():
    etel = input("Étel neve: ")
    rendelo = input("Étel rendelőjének neve: ")
    ertekeles = int(input("Értékelés (1-5): "))
    while ertekeles < 1 or ertekeles > 5:
        if ertekeles < 0:
            vizsgal("Az értékelés nem lehet negatív!")
        elif ertekeles > 5:
            vizsgal("5 pont feletti értékelés nem elfogadható!")
        elif ertekeles == 0:
            vizsgal("Az értékelés nem lehet nulla!")
    print(f"I/A, B:\n\tÉtel neve: {etel}\n\tÉtel rendelőjének neve: {rendelo}\n\tÉrtékelés (1-5): {ertekeles}")
    print(f"I/C:\n\tKöszönjük az értékelést!")
    

            
    