from typing import ValuesView
from model import Hisa, Prostor, Delo
import json

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Hisa.preberi_iz_dat(IME_DATOTEKE)
except:
    moj_model = Hisa("")

PREIMENUJ_HISO = 1
DODAJ_PROSTOR = 2
POBRISI_PROSTOR = 3
ZAMENJAJ_PROSTOR = 4
DODAJ_PRORACUN = 5
DODAJ_STROSEK = 6
DODAJ_DELO = 7
POBRISI_DELO = 8
OPRAVI_DELO = 9
IZHOD = 10

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vaš vnos ni število. Poskusite ponovno.")

def izberi_moznost(moznosti):
    for i, (moznost, opis) in enumerate(moznosti, 1):
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
        return f"Za {prostor.ime} ste porabili {strosek}. Vseh del je {dela}, od tega jih je {neopravljena_dela} neopravljenih, {zamujena_dela} pa jih zamuja. Za prostor potrebujete {prostor.mnozica_materialov()}."
    elif not zamujena_dela and neopravljena_dela:
        return f"Za {prostor.ime} ste porabili {strosek}. Vseh del je {dela}, od tega jih je {neopravljena_dela} neopravljenih. Za prostor potrebujete {prostor.mnozica_materialov()}."
    else:
        return f"Za {prostor.ime} ste porabili {strosek}. Super! Opravili ste že vseh {dela} del."

def prikaz_dela(delo):
    if delo.zamuja() and not delo.opravljeno:
        return f"{delo.tezavnost} delo: {delo} je neopravljeno in zamuja!!!! Za delo potrebujete {delo.material}, ocenjen strošek je {delo.cena} EUR."
    elif not delo.opravljeno and delo.rok != None:
        return f"{delo.tezavnost} delo: {delo} je neopravljeno, rok ima {delo.rok}! Za delo potrebujete {delo.material}, ocenjen strošek je {delo.cena} EUR."
    elif not delo.opravljeno and not delo.rok:
        return f"{delo.tezavnost} delo: {delo} je neopravljeno! Za delo potrebujete {delo.material}, ocenjen strošek je {delo.cena} EUR."
    else:
        return f"{delo.tezavnost} delo: {delo} je opravljeno. Porabili ste {delo.cena} EUR"

def izberi_prostor(model):
    return izberi_moznost([(prostor, prikaz_prostora(prostor)) for prostor in model.prostori])

def izberi_delo(model):
    return izberi_moznost(
        [
            (delo, prikaz_dela(delo))
            for delo in model.aktualni_spisek.dela
        ]
    )

def tekstovni_vmesnik():
    pozdrav()
    while True:
        if not moj_model.proracun:
            zacetni_proracun()
        elif int(moj_model.proracun) <= 0:
            zmanjka_proracun()
        prikazi_aktualna_dela()
        ukaz = izberi_moznost(
            [
                (PREIMENUJ_HISO, "preimenuj hišo"),
                (DODAJ_PROSTOR, "dodaj nov prostor"),
                (POBRISI_PROSTOR, "pobriši prostor"),
                (ZAMENJAJ_PROSTOR, "prikaži drug prostor"),
                (DODAJ_PRORACUN, "povečaj proračun"),
                (DODAJ_STROSEK, "vpiši stroške"),
                (DODAJ_DELO, "dodaj novo delo"),
                (POBRISI_DELO, "pobriši delo"),
                (OPRAVI_DELO, "opravi delo"),
                (IZHOD, "zapri program")
            ]
        )
        if ukaz == 1:
            preimenuj_hiso()
        elif ukaz == 2:
            dodaj_prostor()
        elif ukaz == 3:
            pobrisi_prostor()
        elif ukaz == 4:
            zamenjaj_prostor()
        elif ukaz == 5:
            dodaj_proracun()
        elif ukaz == 6:
            dodaj_strosek()
        elif ukaz == 7:
            dodaj_delo()
        elif ukaz == 8:
            pobrisi_delo()
        elif ukaz == 9:
            opravi_delo()
        elif ukaz == 10:
            moj_model.shrani_v_dat(IME_DATOTEKE)
            print("Nasvidenje! Uspešen dan ;)")

def pozdrav():
    print("Dobrodošli v urejevalniku gradbenih del.")

def zacetni_proracun():
    print("Niste še vnesli proračuna, zato to postorite sedaj.")
    znesek = input("Proračun> ")
    moj_model.proracun = znesek

def zmanjka_proracun():
    print("Zmanjkalo Vam je denarja, zato ga najprej dodajte.")
    znesek = input("Proračun> ")
    moj_model.proracun = znesek

def prikazi_aktualna_dela():
    if moj_model.aktualni_prostor:
        for delo in moj_model.aktualni_prostor.dela:
            print(f"- {prikaz_dela(delo)}")
    else:
        print("Nimate še nobenega prostora, zato ga najprej dodajte")
        dodaj_prostor()

def preimenuj_hiso():
    novo_ime = input("Novo ime> ")
    moj_model.preimenuj(novo_ime)

def dodaj_prostor():
    print("Vnesi podatke novega prostora.")
    ime = input("Ime> ")
    nov_prostor = Prostor(ime)
    moj_model.dodaj_prostor(nov_prostor)

def pobrisi_prostor():
    prostor = izberi_prostor(moj_model)
    moj_model.odstrani_prostor(prostor)

def zamenjaj_prostor():
    print("Izberite želeni prostor")
    zeljeni = izberi_prostor(moj_model)
    moj_model.zamenjaj_prostor(zeljeni)

def dodaj_proracun():
    znesek = input("Vnesite znesek, ki ga želite dodati proračunu> ")
    moj_model.dodaj_proracun(znesek)

def dodaj_strosek():
    znesek = input("Vnesite strošek> ")
    moj_model.zmanjsaj_proracun(znesek)

def dodaj_delo():
    print("Vnesi podatke novega dela.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    tezavnost = input("Vnesite zahtevno, srednje ali lahko> ")
    cena = input("Cena> ")
    material = input("Material> ")
    rok = input("Rok> ")
    novo_delo = Delo(ime ,opis, tezavnost, cena, material, rok)
    moj_model.dodaj_delo(novo_delo)

def pobrisi_delo():
    delo = izberi_delo(moj_model)
    moj_model.odstrani_delo(delo)

def opravi_delo():
    delo = izberi_delo(moj_model)
    delo.spremeni_opravljeno()

