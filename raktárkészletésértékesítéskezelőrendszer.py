
f = open("raktar.txt", "a", encoding="utf-8")
f.readlines()
class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
    

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


