import bottle
from model import Hisa, Prostor, Delo

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
        #dela=moj_model.aktualni_prostor.dela,
        )

@bottle.get("/seznam-opravil/")
def seznam_opravil():
    return "Super, vse si naredil!"

bottle.run(reloder=True, debug=True)
