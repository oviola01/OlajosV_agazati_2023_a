import sorozat

def fajlba_kiir():
    fajlom = open("eredmeny.txt","w",encoding="UTF-8")
    szoveg = "II/F:\n\tA páratlanok száma: " + str(sorozat.paratlanok_szama())
    fajlom.write(szoveg)
    fajlom.close
    fajlom = open("eredmeny.txt","r",encoding="UTF-8")
    tartalom = fajlom.read()
    print(f"eredmeny.txt tartalma:\n{tartalom}")
    fajlom.close
