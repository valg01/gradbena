from typing import ValuesView
from model import Hisa, Prostor, Delo

DODAJ_PROSTOR = 1
POBRISI_PROSTOR = 2
ZAMENJAJ_PROSTOR = 3
DODAJ_PRORACUN = 4
DODAJ_STROSEK = 5
DODAJ_DELO = 6
POBRISI_DELO = 7
OPRAVI_DELO = 8
IZHOD = 9

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vaš vnos ni število. Poskusite ponovno.")

def izberi_moznost(moznosti):
    for i, (moznosti, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _ = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}")

def prikaz_prostora(prostor):
    dela = prostor.stevilo_del()
    zamujena_dela = prostor.stevilo_zamujenih()
    neopravljena_dela = prostor.stevilo_neopravljenih()
    strosek = prostor.strosek_prostora()
    if zamujena_dela:
        return f"Za {prostor.ime} ste porabili {strosek}. Vseh del je {dela}, od tega jih je {neopravljena_dela} neopravljenih, {zamujena_dela} pa jih zamuja."
    elif not zamujena_dela and neopravljena_dela:
        return f"Za {prostor.ime} ste porabili {strosek}. Vseh del je {dela}, od tega jih je {neopravljena_dela} neopravljenih"
    else:
        return f"Za {prostor.ime} ste porabili {strosek}. Super! Opravili ste že vseh {dela} del."

def prikaz_del(delo):
    if delo.zamuja() and not delo.opravljeno:
        return f"{delo.tezavnost} delo: {delo} je neopravljeno in zamuja!!!!"
    elif not delo.opravljeno:
        return f"{delo.tezavnost} delo: {delo} je neopravljeno"
    else:
        return f"{delo.tezavnost} delo: {delo} je opravljeno"

    


