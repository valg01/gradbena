import bottle
import os
from model import Hisa, Prostor, Delo
from datetime import date


def nalozi_uporabnikovo_stanje():
    uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        return Hisa.preberi_iz_dat(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")

def shrani_uporabnika(hisa):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    hisa.shrani_v_dat(uporabnisko_ime)

@bottle.get("/")
def osnovna_stran():
    moj_model = nalozi_uporabnikovo_stanje()
    return bottle.template(
        "osnovna_stran.html",
        hisa=moj_model,
        prostori=moj_model.prostori,
        neopravljena=moj_model.skupno_stevilo_neopravljenih(),
        zamujena=moj_model.skupno_stevilo_zamujenih(),
        kretenizem=moj_model.aktualni_prostor.dela if moj_model.aktualni_prostor else [],
        aktualni=moj_model.aktualni_prostor,
        uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime")
        )

@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napake={}, polja={}, uporabnisko_ime=None )

@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    ime_objekta = bottle.request.forms.getunicode("ime_objekta")
    proracun = bottle.request.forms.getunicode("proracun")
    if os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime že obstaja."}
        return bottle.template("registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        Hisa(ime_objekta, proracun).shrani_v_dat(uporabnisko_ime)
        bottle.redirect("/")

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if not os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        bottle.redirect("/")

@bottle.post("/odjava/")
def odjava():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    print("piškotek uspešno pobrisan")
    bottle.redirect("/")

@bottle.get("/dodaj-prostor/")
def dodaj_prostor_get():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    moj_model=nalozi_uporabnikovo_stanje()
    return bottle.template(
        "dodaj_prostor.html",
        napake={},
        polja={},
        uporabnisko_ime=uporabnisko_ime,
        hisa=moj_model,
    )

@bottle.post("/dodaj-prostor/")
def dodaj_prostor_post():
    ime = bottle.request.forms.getunicode("ime")
    napake = {}
    polja = {"ime":ime}
    moj_model = nalozi_uporabnikovo_stanje()
    if not ime:
        napake["ime"] = "Ime mora biti neprazno."
    for prostor in moj_model.prostori:
        if prostor.ime == ime:
            napake["ime"] = "To ime je že zasedeno"
    if napake:
        return bottle.template(
            "dodaj_prostor.html",
            napake = napake,
            polja = polja
        )
    else:
        nov_prostor = Prostor(ime)
        moj_model.dodaj_prostor(nov_prostor)
        shrani_uporabnika(moj_model)
        bottle.redirect("/")

@bottle.post("/odstrani-prostor/")
def odstrani_prostor():
    moj_model=nalozi_uporabnikovo_stanje()
    indeks = bottle.request.forms.getunicode("indeks1") 
    prostor = moj_model.prostori[int(indeks)] if indeks else moj_model.prostori[0]
    moj_model.odstrani_prostor(prostor)
    shrani_uporabnika(moj_model)
    bottle.redirect("/")

@bottle.post("/dodaj/")
def dodaj_delo():
    ime = bottle.request.forms.getunicode("ime")
    opis = bottle.request.forms.getunicode("opis")
    tezavnost = bottle.request.forms.getunicode("tezavnost")
    cena = bottle.request.forms.getunicode("cena")
    material = bottle.request.forms.getunicode("material")
    rok = date.fromisoformat(bottle.request.forms["rok"]) if bottle.request.forms["rok"] else None
    delo = Delo(ime, opis, tezavnost, cena, material, rok)
    moj_model=nalozi_uporabnikovo_stanje()
    moj_model.dodaj_delo(delo)
    shrani_uporabnika(moj_model)
    bottle.redirect("/")

@bottle.post("/opravi/")
def spremeni_opravljeno():
    indeks = bottle.request.forms.getunicode("indeks")
    moj_model=nalozi_uporabnikovo_stanje()
    delo = moj_model.aktualni_prostor.dela[int(indeks)]
    delo.spremeni_opravljeno()
    shrani_uporabnika(moj_model)
    bottle.redirect("/")

@bottle.post("/zamenjaj-aktualni-prostor/")
def zamenjaj_aktualni_prostor_post():
    indeks = bottle.request.forms.getunicode("indeks")
    moj_model=nalozi_uporabnikovo_stanje()
    moj_model.aktualni_prostor = moj_model.prostori[int(indeks)]
    shrani_uporabnika(moj_model)
    bottle.redirect("/")

@bottle.post("/spremeni-proracun/")
def dodaj_proracun():
    sprememba = bottle.request.forms.getunicode("sprememba_proracuna")
    moj_model=nalozi_uporabnikovo_stanje()
    moj_model.dodaj_proracun(int(sprememba))
    shrani_uporabnika(moj_model)
    bottle.redirect("/")

@bottle.error(404)
def error_404(error):
    return "Ta stran žal ne obstaja!"

bottle.run(reloder=True, debug=True)
