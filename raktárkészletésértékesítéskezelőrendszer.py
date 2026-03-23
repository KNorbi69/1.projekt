
f = open("raktar.txt", "a", encoding="utf-8")
class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
<<<<<<< HEAD
    

def eladas():
    termek = input("Melyik terméket szeretnéd megvásárolni? ")
    while termek not in termekek:
        termek = input("Melyik terméket szeretnéd megvásárolni? ")
    mennyiseg = input("Hány darabot szeretnél? ")
    while not mennyiseg.isdigit() or int(mennyiseg) < 1:
        mennyiseg = input("Nem megfelelő érték! Add meg újra: ")
    if mennyiseg < termek.keszletmennyiseg:
        ujkeszlet = termek.keszletmennyiseg - mennyiseg
        osszeg = termek.ar * mennyiseg
        print(f"Eladva: {mennyiseg} db {termek}. Fizetendő: {osszeg}\n(Új készlet: {ujkeszlet} db)")   


=======
    def adatok(self):
        print(f"Név                  Ár(Ft)              Mennyiség (db)\n---------------------------------------------------------\n{self.nev}             {self.ar}           {self.keszletmennyiseg}\n{self.nev}             {self.ar}           {self.keszletmennyiseg}\n{self.nev}             {self.ar}            {self.keszészletmennyiseg}\n----------------------------------------------------------\nÖsszesen: {} féle termék a raktáron.")
        
termek = input("Melyik terméket szeretnéd megvásárolni? ")
mennyiseg = input("")
>>>>>>> 0b2f5e9638d54bce7f2d5d7c7e1e1cfeef5dea9d
