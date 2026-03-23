
f = open("raktar.txt", "a", encoding="utf-8")
szoveg = f.readlines()
f.close()

class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
termekek = []
for i in range(1,len(szoveg)):
    termekek.append(Termek(szoveg[i].split(",")[0], szoveg[i].split(",")[1],szoveg[i].split(",")[2]))
def tablazat(self):
    print("---AKTUÁLIS KÉSZLET---\nNév                  Ár(Ft)              Mennyiség (db)\n---------------------------------------------------------")
    for termek in termekek:
        print(f"{termek.nev}             {termek.ar}           {termek.keszletmennyiseg}")
    print(f"---------------------------------------------------------\nÖsszesen {len(termekek)} féle termék van raktáron.")

def felvetel(self):
    print("---ÚJ TERMÉKEK FELVÉTELE---")
    termeknev = input("Termék neve: ")
    while termeknev.isdigit():
        termeknev = input("Helytelen név! Termék neve: ")
    egysegar = input("Egységár: ")
    while not egysegar.isdigit():
        egysegar = input("Helytelen ár! Egységár: ")
    kezdokeszlet = input("Kezdőkészlet: ")
    while not kezdokeszlet.isdigit():
        kezdokeszlet = input("Helytelen adat! Kezdőkészlet: ")
    termekek.append(Termek(termeknev,egysegar,kezdokeszlet))


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
    print("1. Készlet listázása\n2. Új termék felvétele\n3. Eladás\n4. Termék keresése\n5. Mentés és Kilépés")
    csinal =input("\nVálasszon műveletet (1-5): ")
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