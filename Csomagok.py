
class Csomagok:        
    def __init__(self,csomi):
        self.szelesseg = int(csomi[0])
        self.magassag = int(csomi[1])
        self.melyseg = int(csomi[2])
        self.suly = int(csomi[3])
        
    def __str__(self):
        return(f"{self.szelesseg},{self.magassag},{self.melyseg},{self.suly}")