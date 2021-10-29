from datetime import date
import json

class Hisa:
    def __init__(self, ime, proracun = None):
        self.ime = ime
        self.proracun = proracun
        self.prostori = []
        self.shramba = []
        self.aktualni_prostor = None
    
    def preimenuj(self, novo_ime):
        self.ime = novo_ime
    
    def dodaj_prostor(self, prostor):
        self.prostori.append(prostor)
        if not self.aktualni_prostor:
            self.aktualni_prostor = prostor

    def odstrani_prostor(self, prostor):
        self.prostori.remove(prostor)

    def zamenjaj_prostor(self, prostor):
        self.aktualni_prostor = prostor

    def stroski(self):
        strosek = 0
        for prostor in self.prostori:
            for delo in prostor.dela:
                strosek += delo.cena
        return strosek
    
    def zacetni_proracun(self):
        return self.proracun + self.stroski()
    
    def dodaj_proracun(self, k):
        if not self.proracun:
            self.proracun = k
        else:
            self.proracun += k
    
    def zmanjsaj_proracun(self, k):
        if not self.dodaj_proracun:
            self.proracun = -1 * int(k)
        else:
            self.proracun = int(self.proracun) - k
    
    def potrebni_materiali(self):
        sez = []
        for prostor in self.prostori:
            for delo in prostor.dela:
                if delo.material:
                    sez.append(delo.material)

    def dodaj_material(self, material):
        self.shramba.append(material)

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
        if vsa_dela == 0:
            return 0
        return round(opravljeni / vsa_dela, 2)
    
    def delez_neopravljenih(self):
        return 1 - self.delez_opravljenih()

    def skupno_stevilo_zamujenih(self):
        st = 0
        for prostor in self.prostori:
            st += prostor.stevilo_zamujenih()
        return st
    
    def skupno_stevilo_neopravljenih(self):
        print(sum([prostor.stevilo_neopravljenih() for prostor in self.prostori]))
        return sum([prostor.stevilo_neopravljenih() for prostor in self.prostori])
    
    def dodaj_delo(self, delo):
        self.aktualni_prostor.dodaj_delo(delo)
        nov_proracun = int(self.proracun) - int(delo.cena)
        self.proracun = nov_proracun
    
    def odstrani_delo(self, delo):
        self.aktualni_prostor.odstrani_delo(delo)
        nov_proracun = int(self.proracun) + int(delo.cena)
        self.proracun = nov_proracun
        
    def v_slovar(self):
        return {
        "ime" : self.ime,
        "proracun" : self.proracun,
        "prostori": [prostor.v_slovar() for prostor in self.prostori],
        "shramba": self.shramba,
        "aktualni_prostor": self.prostori.index(self.aktualni_prostor) if self.aktualni_prostor else None,
        }
    

    @staticmethod
    def iz_slovarja(slovar):
        proracun = slovar["proracun"] if slovar["proracun"] else 0
        hisa = Hisa(slovar["ime"], int(proracun))
        hisa.prostori = [
            Prostor.iz_slovarja(prostor) for prostor in slovar["prostori"]
        ]
        hisa.shramba = slovar["shramba"]
        if slovar["aktualni_prostor"] is not None:
            hisa.aktualni_prostor = hisa.prostori[slovar["aktualni_prostor"]]
        return hisa
    
    def shrani_v_dat(self, dat):
        with open(dat, "w", encoding="utf-8") as f:
            slovar = self.v_slovar()
            json.dump(slovar, f)
    
    @staticmethod
    def preberi_iz_dat(dat):
        with open(dat, "r", encoding="utf-8") as f:
            slovar = json.load(f)
            return Hisa.iz_slovarja(slovar)

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
            if not delo.opravljeno:
                stevilo += 1
        return stevilo
    
    def stevilo_del(self):
        return len(self.dela)

    def strosek_prostora(self):
        skupna_cena = 0
        for delo in self.dela:
            skupna_cena += int(delo.cena)
        return skupna_cena 

    def v_slovar(self):
        return {
            "ime" : self.ime,
            "dela" : [delo.v_slovar() for delo in self.dela],
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        prostor = Prostor(slovar["ime"])
        prostor.dela = [
            Delo.iz_slovarja(sl_delo) for sl_delo in slovar["dela"]
        ]
        return prostor
    
class Delo:
    def __init__(self, ime, opis, tezavnost, cena = 0, material = None, rok = None, opravljeno = False):
        self.ime = ime
        self.opis = opis
        self.material = material
        self.tezavnost = tezavnost
        self.cena = cena
        self.rok = rok
        self.opravljeno = opravljeno

    def spremeni_opravljeno(self):
        self.opravljeno = not self.opravljeno
    
    def povecaj_ceno(self, k):
        self.cena += k
    
    def zmanjsaj_ceno(self, k):
        self.cena -= k
    
    def zamuja(self):
        danes = date.today()
        if self.opravljeno:
            return False
        if not self.rok:
            return False
        else:
            if self.rok > danes:
                return False
            return True

    def v_slovar(self):
        return {
            "ime" : self.ime,
            "opis" : self.opis,
            "tezavnost" : self.tezavnost,
            "cena" : self.cena,
            "material" : self.material,
            "rok" : date.isoformat(self.rok) if self.rok else None,
            "opravljeno" : self.opravljeno,
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Delo(
            slovar["ime"],
            slovar["opis"],
            slovar["tezavnost"],
            int(slovar["cena"]),
            slovar["material"],
            date.fromisoformat(slovar["rok"]) if slovar["rok"] else None,
            slovar["opravljeno"]
        )