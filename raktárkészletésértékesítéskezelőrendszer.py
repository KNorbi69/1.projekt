
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



def kereses():
    keres = input("Keresett kifejezés: ")
    if keres not in termekek:
        print("Nincs ilyen termék.")
    else:
        for ter in termekek:
            if keres in ter:
                print(f"[TALÁLAT] {ter.nev} - Ár: {ter.ar} Ft, Készlet: {ter.keszletmennyiseg} db")

            