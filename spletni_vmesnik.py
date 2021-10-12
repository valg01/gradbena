import bottle
from model import Hisa, Prostor, Delo
from datetime import date
IME_DATOTEKE = "stanje.json"
try:
    moj_model = Hisa.preberi_iz_dat(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Hisa("")

@bottle.get("/")
def osnovna_stran():
    return bottle.template(
        "osnovna_stran.tpl",
        neopravljena=moj_model.skupno_stevilo_neopravljenih(),
        zamujena=moj_model.skupno_stevilo_zamujenih(),
        kretenizem=moj_model.aktualni_prostor.dela,
        )

@bottle.get("/dodaj/")
def dodaj_delo():
    ime = bottle.request.query.getunicode("ime")
    opis = bottle.request.query.getunicode("opis")
    tezavnost = bottle.request.query.getunicode("tezavnost")
    cena = bottle.request.query.getunicode("cena")
    material = bottle.request.query.getunicode("material")
    rok = date.fromisoformat(bottle.request.query["rok"]) if bottle.request.query["rok"] else None
    delo = Delo(ime, opis, tezavnost, cena, material, rok)
    moj_model.dodaj_delo(delo)
    moj_model.shrani_v_dat(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.get("/opravi/")
def opravi_delo():
    indeks = bottle.request.query.getunicode("indeks")
    delo = moj_model.aktualni_prostor.dela[int(indeks)]
    delo.spremeni_opravljeno()
    moj_model.shrani_v_dat(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.error(404)
def error_404(error):
    return "Ta stran žal ne obstaja!"

bottle.run(reloder=True, debug=True)
