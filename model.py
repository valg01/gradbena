from datetime import date

class Hisa:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
        self.prostori = []
    
    def dodaj_prostor(self, prostor):
        self.prostori.append(prostor)

    def stroski(self):
        strosek = 0
        for prostor in self.prostori:
            for delo in prostor.dela:
                strosek += delo.cena
        return strosek
    
    def ostanek_denarja(self):
        return self.proracun - self.stroski()

    def stevilo_opravljenih(self):
        opravljeni = 0
        for prostor in self.prostori:
            for delo in prostor.dela:
                if delo.opravljeno:
                    opravljeni += 1
        return opravljeni

    def delez_opravljenih(self):
        opravljeni = self.stevilo_opravljenih()
        vsa_dela = 0
        for prostor in self.prostori:
            vsa_dela += len(prostor.dela)
        return round(opravljeni / vsa_dela, 2)
    
    def delez_neopravljenih(self):
        return 1 - self.delez_opravljenih()

    def skupno_stevilo_zamujenih(self):
        st = 0
        for prostor in self.prostori:
            st += prostor.stevilo_zamujenih()
        return st

class Prostor:
    def __init__(self, ime):
        self.ime = ime
        self.dela = []
    
    def dodaj_delo(self, delo):
        self.dela.append(delo)
    
    def stevilo_zamujenih(self):
        stevilo = 0
        for delo in self.dela:
            if delo.zamuja():
                stevilo += 1
        return stevilo

    def strosek_prostora(self):
        skupna_cena = 0
        for delo in self.dela:
            skupna_cena += delo.cena
        return skupna_cena 
    
class Delo:
    def __init__(self, ime, opis, tezavnost, cena, material = None, rok = None):
        self.ime = ime
        self.opis = opis
        self.material = material
        self.tezavnost = tezavnost
        self.cena = cena
        self.rok = rok
        self.opravljeno = False

    def opravi(self):
        self.opravljeno = True
    
    def povecaj_ceno(self, k):
        self.cena += k
    
    def zmanjsaj_ceno(self, k):
        self.cena -= k
    
    def zamuja(self):
        danes = date.today()
        if not self.rok:
            return False
        else:
            if self.rok > danes:
                return False
            return True


