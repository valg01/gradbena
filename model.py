from datetime import date

class Hisa:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
        self.prostori = []
        self.aktualni_prostor = None
    
    def dodaj_prostor(self, prostor):
        self.prostori.append(prostor)
        if not self.aktualni_prostor:
            self.aktualni_prostor = prostor

    def odstrani_prostor(self, prostor):
        self.prostori.remove(prostor)

    def zamenjaj_spisek(self, prostor):
        self.aktualni_prostor = prostor

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
            vsa_dela += prostor.stevilo_del()
        return round(opravljeni / vsa_dela, 2)
    
    def delez_neopravljenih(self):
        return 1 - self.delez_opravljenih()

    def skupno_stevilo_zamujenih(self):
        st = 0
        for prostor in self.prostori:
            st += prostor.stevilo_zamujenih()
        return st
    
    def skupno_stevilo_neopravljenih(self):
        st = 0
        for prostor in self.prostori:
            st += prostor.stevilo_neopravljenih()
        return st
    
    def dodaj_delo(self, delo):
        self.aktualni_prostor.dodaj_delo(delo)
    
    def odstrani_delo(self, delo):
        self.aktualni_prostor.odstrani_delo(delo)

class Prostor:
    def __init__(self, ime):
        self.ime = ime
        self.dela = []
    
    def dodaj_delo(self, delo):
        self.dela.append(delo)
    
    def odstrani_delo(self, delo):
        self.dela.remove(delo)
    
    def stevilo_zamujenih(self):
        stevilo = 0
        for delo in self.dela:
            if delo.zamuja():
                stevilo += 1
        return stevilo
    
    def stevilo_neopravljenih(self):
        stevilo = 0
        for delo in self.dela:
            if not delo.opravljeno():
                stevilo += 1
        return stevilo
    
    def stevilo_del(self):
        return len(self.dela)

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

    def spremeni_opravljeno(self):
        self.opravljeno = not self.opravljeno
    
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


