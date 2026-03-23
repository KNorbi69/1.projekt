#ADATKEZELÉS
class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
termekek = []
try:
    f = open("raktar.txt", "r", encoding="utf-8")
    szoveg = f.readlines()
    f.close()
    for i in range(len(szoveg)):
        adatok = szoveg[i].strip().split(",")
        termekek.append(Termek(adatok[0], int(adatok[1]), int(adatok[2])))
except: 
    pass



def tablazat():
    print("---AKTUÁLIS KÉSZLET---")
    print(f"{'Név':<15}{'Ár(Ft)':>10}{'Mennyiség (db)':>20}")
    print("-" * 45)

    for termek in termekek:
        print(f"{termek.nev:<15}{termek.ar:>10}{termek.keszletmennyiseg:>20}")

    print("-" * 45)
    print(f"Összesen {len(termekek)} féle termék van raktáron.")

    
def felvetel():
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
    termekek.append(Termek(termeknev, int(egysegar), int(kezdokeszlet)))
    mentes()

def mentes():
    f = open("raktar.txt","w",encoding="utf-8")
    for termek in termekek:
        f.write(f"{termek.nev},{termek.ar},{termek.keszletmennyiseg}\n")


# LOGIKAI


def eladas():
    nev = input("Melyik terméket szeretnéd megvásárolni? ")

    talalat = None
    for t in termekek:
        if t.nev == nev:
            talalat = t
            break

    if talalat is None:
        print("Nincs ilyen termék!")
        return

    mennyiseg = input("Hány darabot szeretnél? ")
    while not mennyiseg.isdigit() or int(mennyiseg) < 1:
        mennyiseg = input("Nem megfelelő érték! Add meg újra: ")

    mennyiseg = int(mennyiseg)

    if mennyiseg <= talalat.keszletmennyiseg:
        talalat.keszletmennyiseg -= mennyiseg
        osszeg = talalat.ar * mennyiseg
        print(f"Eladva: {mennyiseg} db {talalat.nev}. Fizetendő: {osszeg} Ft")
        mentes()
    else:
        print("Nincs elég készlet!")



def kereses():
    keres = input("Keresett kifejezés: ").lower()
    talalat = False

    for ter in termekek:
        if keres in ter.nev.lower():
            print(f"[TALÁLAT] {ter.nev} - Ár: {ter.ar} Ft, Készlet: {ter.keszletmennyiseg} db\n")
            talalat = True

    if not talalat:
        print("Nincs ilyen termék.")

megy = True
while megy:
    print("\n1. Készlet listázása\n2. Új termék felvétele\n3. Eladás\n4. Termék keresése\n5. Mentés és Kilépés")
    csinal =input("\nVálasszon műveletet (1-5): ")
    while not csinal.isdigit() or int(csinal) <1 or int(csinal) > 5:
        csinal = input("Adj meg számot 1-től 5-ig! ")
    csinal = int(csinal)
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
mentes()