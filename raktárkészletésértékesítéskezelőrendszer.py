
f = open("raktar.txt", "a", encoding="utf-8")
class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
    def adatok(self):
        print(f"Név                  Ár(Ft)              Mennyiség (db)\n---------------------------------------------------------\n{self.nev}             {self.ar}           {self.keszletmennyiseg}\n{self.nev}             {self.ar}           {self.keszletmennyiseg}\n{self.nev}             {self.ar}            {self.keszészletmennyiseg}\n----------------------------------------------------------\nÖsszesen: {} féle termék a raktáron.")
        
termek = input("Melyik terméket szeretnéd megvásárolni? ")
mennyiseg = input("")