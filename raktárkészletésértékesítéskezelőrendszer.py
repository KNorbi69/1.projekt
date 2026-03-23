
f = open("raktar.txt", "a", encoding="utf-8")
f.readlines()
class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
    


termek = input("Melyik terméket szeretnéd megvásárolni? ")
mennyiseg = input()