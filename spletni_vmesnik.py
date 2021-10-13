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

@bottle.post("/dodaj/")
def dodaj_delo():
    ime = bottle.request.forms.getunicode("ime")
    opis = bottle.request.forms.getunicode("opis")
    tezavnost = bottle.request.forms.getunicode("tezavnost")
    cena = bottle.request.forms.getunicode("cena")
    material = bottle.request.forms.getunicode("material")
    rok = date.fromisoformat(bottle.request.forms["rok"]) if bottle.request.forms["rok"] else None
    delo = Delo(ime, opis, tezavnost, cena, material, rok)
    moj_model.dodaj_delo(delo)
    moj_model.shrani_v_dat(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.post("/opravi/")
def opravi_delo():
    indeks = bottle.request.forms.getunicode("indeks")
    delo = moj_model.aktualni_prostor.dela[int(indeks)]
    delo.spremeni_opravljeno()
    moj_model.shrani_v_dat(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.error(404)
def error_404(error):
    return "Ta stran žal ne obstaja!"

bottle.run(reloder=True, debug=True)
