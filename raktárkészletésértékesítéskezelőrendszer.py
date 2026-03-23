
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

megy = True
while megy:
    csinal =input("1. Készlet listázása\n2. Új termék felvétele\n3. Eladás\n4. Termék keresése\n5. Mentés és Kilépés\n\nVálasszon műveletet (1-5): ")
    while not csinal.isdigit() or int(csinal) <1 or int(csinal) > 4:
        csinal = input("Adj meg számot 1-től 5-ig! ")
    if csinal == 1:
        tablazat()
    elif csinal == 2:
        felvetel()
    elif csinal == 3:
        eladas()
    elif csinal == 4:
        kereses()
    else:
        megy = False